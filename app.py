import os
import io
import json
import csv
import shutil
from datetime import datetime, date, timedelta
from functools import wraps
import pandas as pd
from flask import (
    Flask, render_template, request, redirect, url_for, flash,
    session, jsonify, Response, send_file
)
from werkzeug.utils import secure_filename
from config import Config
from database import db, User, Student, CounsellingCase, AuditLog, Notification, SystemSetting
from ml_engine import MLEngine

def log_audit(action, details=None, username=None):
    try:
        user_name = username or session.get('username', 'System')
        user_id = session.get('user_id')
        ip = request.remote_addr if request else '127.0.0.1'
        log = AuditLog(
            user_id=user_id,
            username=user_name,
            action=action,
            details=details,
            ip_address=ip,
            timestamp=datetime.utcnow()
        )
        db.session.add(log)
        db.session.commit()
    except Exception as e:
        print(f"Error logging audit: {e}")

def create_notification(title, message, category='info', user_id=None):
    try:
        notif = Notification(
            title=title,
            message=message,
            category=category,
            user_id=user_id,
            created_at=datetime.utcnow()
        )
        db.session.add(notif)
        db.session.commit()
    except Exception as e:
        print(f"Error adding notification: {e}")

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this portal.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                return redirect(url_for('login'))
            user_role = session.get('role')
            if user_role not in roles:
                flash(f"Access denied. Requires one of roles: {', '.join(roles)}", 'danger')
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.join(app.config['BASE_DIR'], 'data'), exist_ok=True)
    os.makedirs(os.path.join(app.config['BASE_DIR'], 'models'), exist_ok=True)

    db.init_app(app)

    @app.context_processor
    def inject_globals():
        unread_count = 0
        if 'user_id' in session:
            unread_count = Notification.query.filter_by(is_read=False).count()
        return {
            'current_user': session,
            'unread_notifications_count': unread_count,
            'current_year': datetime.utcnow().year
        }

    # ========================== AUTH ROUTES ==========================
    @app.route('/')
    def index():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if 'user_id' in session:
            return redirect(url_for('dashboard'))

        if request.method == 'POST':
            username = request.form.get('username', '').strip()
            password = request.form.get('password', '').strip()

            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session['user_id'] = user.id
                session['username'] = user.username
                session['name'] = user.name
                session['role'] = user.role
                session['department'] = user.department or 'General'

                log_audit('USER_LOGIN', f"User {user.username} ({user.role}) logged in successfully.")
                flash(f"Welcome back, {user.name}!", 'success')
                
                next_page = request.args.get('next')
                return redirect(next_page or url_for('dashboard'))
            else:
                flash('Invalid username or password. Please try again.', 'danger')

        return render_template('login.html')

    @app.route('/logout')
    def logout():
        user_name = session.get('username', 'Unknown')
        log_audit('USER_LOGOUT', f"User {user_name} logged out.")
        session.clear()
        flash('You have been logged out securely.', 'info')
        return redirect(url_for('login'))

    # ========================== DASHBOARD & ANALYTICS ==========================
    @app.route('/dashboard')
    @login_required
    def dashboard():
        role = session.get('role')
        user_id = session.get('user_id')

        # Base student query
        base_query = Student.query

        if role == 'Student':
            student_rec = Student.query.filter(
                (Student.enrollment_no == session.get('username')) |
                (Student.name.ilike(f"%{session.get('name', '')}%"))
            ).first()
            if student_rec:
                return redirect(url_for('student_detail', student_id=student_rec.id))

        if role == 'Faculty Mentor':
            # Mentors see their assigned students, plus high risk cases in their department
            mentor_students = base_query.filter_by(assigned_mentor_id=user_id)
            total_students = mentor_students.count()
            at_risk_count = mentor_students.filter(Student.risk_level == 'At Risk').count()
            active_counselling = mentor_students.filter(Student.lifecycle_status.in_(['Under Review', 'Counselling'])).count()
            closed_cases = mentor_students.filter(Student.lifecycle_status == 'Closed').count()
            recent_students = mentor_students.order_by(Student.risk_score.desc()).limit(8).all()
        else:
            # Admin & Dept Head view college-wide data
            total_students = base_query.count()
            at_risk_count = base_query.filter(Student.risk_level == 'At Risk').count()
            active_counselling = base_query.filter(Student.lifecycle_status.in_(['Under Review', 'Counselling'])).count()
            closed_cases = base_query.filter(Student.lifecycle_status == 'Closed').count()
            recent_students = base_query.order_by(Student.risk_score.desc()).limit(8).all()

        # Critical Escalations: At Risk students not yet in Counselling or Intervened
        escalation_candidates = Student.query.filter(
            Student.risk_score >= 0.70,
            Student.lifecycle_status.in_(['At Risk', 'Low Risk'])
        ).limit(5).all()

        recent_notifications = Notification.query.order_by(Notification.created_at.desc()).limit(5).all()
        recent_counselling = CounsellingCase.query.order_by(CounsellingCase.created_at.desc()).limit(5).all()

        return render_template(
            'dashboard.html',
            total_students=total_students,
            at_risk_count=at_risk_count,
            active_counselling=active_counselling,
            closed_cases=closed_cases,
            recent_students=recent_students,
            escalation_candidates=escalation_candidates,
            recent_notifications=recent_notifications,
            recent_counselling=recent_counselling
        )

    @app.route('/api/analytics')
    @login_required
    def api_analytics():
        # 1. Risk distribution
        low_risk = Student.query.filter(Student.risk_level == 'Low Risk').count()
        at_risk = Student.query.filter(Student.risk_level == 'At Risk').count()

        # 2. Lifecycle status distribution
        status_counts = {}
        for st in ['Low Risk', 'At Risk', 'Under Review', 'Counselling', 'Intervened', 'Closed']:
            status_counts[st] = Student.query.filter_by(lifecycle_status=st).count()

        # 3. Department-wise At Risk breakdown
        departments = db.session.query(Student.department).distinct().all()
        dept_labels = [d[0] for d in departments if d[0]]
        dept_total = []
        dept_at_risk = []
        for d in dept_labels:
            tot = Student.query.filter_by(department=d).count()
            risk = Student.query.filter(Student.department == d, Student.risk_level == 'At Risk').count()
            dept_total.append(tot)
            dept_at_risk.append(risk)

        # 4. Average Attendance vs Risk distribution
        ranges = ['< 50%', '50-65%', '65-75%', '75-85%', '> 85%']
        attendance_risk_counts = [
            Student.query.filter(Student.attendance_percentage < 50, Student.risk_level == 'At Risk').count(),
            Student.query.filter(Student.attendance_percentage.between(50, 64.9), Student.risk_level == 'At Risk').count(),
            Student.query.filter(Student.attendance_percentage.between(65, 74.9), Student.risk_level == 'At Risk').count(),
            Student.query.filter(Student.attendance_percentage.between(75, 84.9), Student.risk_level == 'At Risk').count(),
            Student.query.filter(Student.attendance_percentage >= 85, Student.risk_level == 'At Risk').count()
        ]

        return jsonify({
            'risk_distribution': {
                'labels': ['Low Risk', 'At Risk'],
                'data': [low_risk, at_risk]
            },
            'lifecycle_distribution': {
                'labels': list(status_counts.keys()),
                'data': list(status_counts.values())
            },
            'department_distribution': {
                'labels': dept_labels,
                'total': dept_total,
                'at_risk': dept_at_risk
            },
            'attendance_risk': {
                'labels': ranges,
                'data': attendance_risk_counts
            }
        })

    # ========================== STUDENT DIRECTORY & CRUD ==========================
    @app.route('/students')
    @login_required
    def students_list():
        if session.get('role') == 'Student':
            student_rec = Student.query.filter(
                (Student.enrollment_no == session.get('username')) |
                (Student.name.ilike(f"%{session.get('name', '')}%"))
            ).first()
            if student_rec:
                flash("Student accounts have direct access only to their individual academic record.", "info")
                return redirect(url_for('student_detail', student_id=student_rec.id))

        # Query parameters for multi-parameter search & filtering
        q = request.args.get('q', '').strip()
        department = request.args.get('department', '').strip()
        semester = request.args.get('semester', '').strip()
        risk_level = request.args.get('risk_level', '').strip()
        lifecycle_status = request.args.get('lifecycle_status', '').strip()
        campus_location = request.args.get('campus_location', '').strip()

        query = Student.query

        if q:
            query = query.filter(
                (Student.enrollment_no.ilike(f"%{q}%")) |
                (Student.name.ilike(f"%{q}%")) |
                (Student.email.ilike(f"%{q}%"))
            )
        if department:
            query = query.filter_by(department=department)
        if semester:
            query = query.filter_by(semester=int(semester))
        if risk_level:
            query = query.filter_by(risk_level=risk_level)
        if lifecycle_status:
            query = query.filter_by(lifecycle_status=lifecycle_status)
        if campus_location:
            query = query.filter_by(campus_location=campus_location)

        students = query.order_by(Student.risk_score.desc()).all()

        # Get unique values for filter dropdowns
        all_departments = [d[0] for d in db.session.query(Student.department).distinct().all() if d[0]]
        all_campuses = [c[0] for c in db.session.query(Student.campus_location).distinct().all() if c[0]]
        mentors = User.query.filter(User.role.in_(['Faculty Mentor', 'Department Head', 'Admin'])).all()

        return render_template(
            'students.html',
            students=students,
            departments=all_departments,
            campuses=all_campuses,
            mentors=mentors,
            filters={
                'q': q,
                'department': department,
                'semester': semester,
                'risk_level': risk_level,
                'lifecycle_status': lifecycle_status,
                'campus_location': campus_location
            }
        )

    @app.route('/students/register', methods=['GET', 'POST'])
    @login_required
    @roles_required('Admin', 'Department Head', 'Faculty Mentor')
    def register_student():
        mentors = User.query.filter(User.role.in_(['Faculty Mentor', 'Department Head', 'Admin'])).all()

        if request.method == 'POST':
            enrollment_no = request.form.get('enrollment_no', '').strip()
            name = request.form.get('name', '').strip()
            email = request.form.get('email', '').strip()
            phone = request.form.get('phone', '').strip()
            department = request.form.get('department', '').strip()
            semester = int(request.form.get('semester', 1))
            attendance = float(request.form.get('attendance_percentage', 100))
            internal_marks = float(request.form.get('internal_marks_avg', 75))
            backlogs = int(request.form.get('backlog_count', 0))
            fee_status = request.form.get('fee_status', 'Paid').strip()
            engagement = float(request.form.get('engagement_score', 80))
            campus = request.form.get('campus_location', 'Main Campus').strip()
            mentor_id = request.form.get('assigned_mentor_id')
            mentor_id = int(mentor_id) if mentor_id else None

            existing = Student.query.filter_by(enrollment_no=enrollment_no).first()
            if existing:
                flash(f'Student with Enrollment No. {enrollment_no} already exists.', 'danger')
                return render_template('register_student.html', mentors=mentors)

            # Predict risk using ML Engine with admin-configured rules
            ml = MLEngine.get_instance()
            rules = SystemSetting.get_risk_rules()
            student_data = {
                'attendance_percentage': attendance,
                'internal_marks_avg': internal_marks,
                'backlog_count': backlogs,
                'fee_status': fee_status,
                'engagement_score': engagement,
                'semester': semester
            }
            pred = ml.predict_student(student_data, rules=rules)

            # Determine initial lifecycle status from admin routing policy
            initial_status = pred.get('recommended_lifecycle', 'At Risk' if pred['risk_level'] == 'At Risk' else 'Low Risk')

            student = Student(
                enrollment_no=enrollment_no,
                name=name,
                email=email,
                phone=phone,
                department=department,
                semester=semester,
                attendance_percentage=attendance,
                internal_marks_avg=internal_marks,
                backlog_count=backlogs,
                fee_status=fee_status,
                engagement_score=engagement,
                campus_location=campus,
                risk_score=pred['risk_score'],
                risk_level=pred['risk_level'],
                key_reasons=json.dumps(pred['reasons']),
                lifecycle_status=initial_status,
                assigned_mentor_id=mentor_id
            )
            db.session.add(student)
            db.session.commit()

            log_audit('STUDENT_REGISTERED', f"Student {name} ({enrollment_no}) registered. Risk: {pred['risk_level']} ({pred['risk_score'] * 100:.1f}%)")

            if pred['risk_level'] == 'At Risk':
                create_notification(
                    title="New At-Risk Student Registered",
                    message=f"Student {name} ({enrollment_no}) has been flagged as At-Risk ({pred['risk_score']*100:.1f}%).",
                    category="warning"
                )

            flash(f"Student {name} registered successfully with predicted Risk: {pred['risk_level']} ({pred['risk_score']*100:.1f}%).", 'success')
            return redirect(url_for('student_detail', student_id=student.id))

        return render_template('register_student.html', mentors=mentors)

    @app.route('/students/<int:student_id>')
    @login_required
    def student_detail(student_id):
        student = Student.query.get_or_404(student_id)

        # Student data isolation: students cannot view peers' records
        if session.get('role') == 'Student':
            student_rec = Student.query.filter(
                (Student.enrollment_no == session.get('username')) |
                (Student.name.ilike(f"%{session.get('name', '')}%"))
            ).first()
            if student_rec and student_rec.id != student.id:
                flash("Access restricted: You may only view your personal academic standing.", "warning")
                return redirect(url_for('student_detail', student_id=student_rec.id))

        mentors = User.query.filter(User.role.in_(['Faculty Mentor', 'Department Head', 'Admin'])).all()
        counselling_history = CounsellingCase.query.filter_by(student_id=student.id).order_by(CounsellingCase.session_date.desc()).all()
        
        return render_template(
            'student_detail.html',
            student=student,
            mentors=mentors,
            counselling_history=counselling_history
        )

    @app.route('/students/<int:student_id>/predict', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head', 'Faculty Mentor')
    def recalculate_prediction(student_id):
        student = Student.query.get_or_404(student_id)
        
        # Check if form has updated values
        if 'attendance_percentage' in request.form:
            student.attendance_percentage = float(request.form.get('attendance_percentage', student.attendance_percentage))
            student.internal_marks_avg = float(request.form.get('internal_marks_avg', student.internal_marks_avg))
            student.backlog_count = int(request.form.get('backlog_count', student.backlog_count))
            student.fee_status = request.form.get('fee_status', student.fee_status)
            student.engagement_score = float(request.form.get('engagement_score', student.engagement_score))
            student.semester = int(request.form.get('semester', student.semester))

        ml = MLEngine.get_instance()
        student_data = {
            'attendance_percentage': student.attendance_percentage,
            'internal_marks_avg': student.internal_marks_avg,
            'backlog_count': student.backlog_count,
            'fee_status': student.fee_status,
            'engagement_score': student.engagement_score,
            'semester': student.semester
        }
        rules = SystemSetting.get_risk_rules()
        pred = ml.predict_student(student_data, rules=rules)
        
        old_risk = student.risk_score
        student.risk_score = pred['risk_score']
        student.risk_level = pred['risk_level']
        student.key_reasons = json.dumps(pred['reasons'])
        db.session.commit()

        log_audit('PREDICTION_RERUN', f"Risk score updated for {student.name} ({student.enrollment_no}): {old_risk*100:.1f}% -> {pred['risk_score']*100:.1f}%")
        flash(f"AI prediction updated: Risk Score is {pred['risk_score']*100:.1f}% ({pred.get('risk_tier', pred['risk_level'])}).", 'info')
        return redirect(url_for('student_detail', student_id=student.id))

    # ========================== BULK CSV UPLOAD ==========================
    @app.route('/students/upload_csv', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head', 'Faculty Mentor')
    def upload_csv():
        if 'csv_file' not in request.files:
            flash('No file part in upload request.', 'danger')
            return redirect(url_for('students_list'))

        file = request.files['csv_file']
        if file.filename == '':
            flash('No CSV file selected.', 'warning')
            return redirect(url_for('students_list'))

        if not file.filename.endswith('.csv'):
            flash('Invalid file format. Please upload a valid CSV file.', 'danger')
            return redirect(url_for('students_list'))

        try:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Also save a copy directly in project root directory for easy file explorer / VS Code visibility
            try:
                root_copy = os.path.join(app.config['BASE_DIR'], filename)
                shutil.copyfile(filepath, root_copy)
            except Exception:
                pass

            df = pd.read_csv(filepath)

            # Normalize column aliases (e.g. 'enrollment' -> 'enrollment_no')
            col_map = {
                'enrollment': 'enrollment_no',
                'reg_no': 'enrollment_no',
                'roll_no': 'enrollment_no',
                'student_id': 'enrollment_no'
            }
            df.rename(columns=lambda c: col_map.get(str(c).strip().lower(), str(c).strip()), inplace=True)

            required_cols = ['enrollment_no', 'name', 'department', 'semester', 'attendance_percentage', 'internal_marks_avg', 'backlog_count', 'fee_status', 'engagement_score']
            
            missing_cols = [c for c in required_cols if c not in df.columns]
            if missing_cols:
                flash(f"CSV is missing required columns: {', '.join(missing_cols)}", 'danger')
                return redirect(url_for('students_list'))

            ml = MLEngine.get_instance()
            rules = SystemSetting.get_risk_rules()
            predictions = ml.predict_dataframe(df.copy(), rules=rules)

            imported_count = 0
            updated_count = 0

            for idx, row in df.iterrows():
                enr = str(row['enrollment_no']).strip()
                pred = predictions[idx]

                student = Student.query.filter_by(enrollment_no=enr).first()
                if not student:
                    student = Student(enrollment_no=enr)
                    imported_count += 1
                else:
                    updated_count += 1

                student.name = str(row['name']).strip()
                student.email = str(row.get('email', f"{enr}@sanskriti.edu.in")).strip()
                student.phone = str(row.get('phone', '')).strip()
                student.department = str(row['department']).strip()
                student.semester = int(row.get('semester', 1))
                student.attendance_percentage = float(row.get('attendance_percentage', 75.0))
                student.internal_marks_avg = float(row.get('internal_marks_avg', 60.0))
                student.backlog_count = int(row.get('backlog_count', 0))
                student.fee_status = str(row.get('fee_status', 'Paid')).strip()
                student.engagement_score = float(row.get('engagement_score', 70.0))
                student.campus_location = str(row.get('campus_location', 'Main Campus')).strip()
                student.risk_score = pred['risk_score']
                student.risk_level = pred['risk_level']
                student.key_reasons = json.dumps(pred['reasons'])
                
                if not student.lifecycle_status or student.lifecycle_status in ['Low Risk', 'At Risk']:
                    student.lifecycle_status = pred.get('recommended_lifecycle', 'At Risk' if pred['risk_level'] == 'At Risk' else 'Low Risk')

                db.session.add(student)

            db.session.commit()
            log_audit('CSV_BULK_UPLOAD', f"Processed CSV upload '{filename}': {imported_count} new students added, {updated_count} updated.")
            create_notification(
                title="Bulk CSV Upload Completed",
                message=f"Successfully imported {imported_count} new student records and updated {updated_count} records with AI dropout risk scores.",
                category="info"
            )
            flash(f"CSV Processed Successfully! Added: {imported_count}, Updated: {updated_count} students with AI predictions.", 'success')

        except Exception as e:
            db.session.rollback()
            flash(f"Failed to process CSV file: {str(e)}", 'danger')

        return redirect(url_for('students_list'))

    @app.route('/students/export')
    @login_required
    def export_students_csv():
        # Export current records
        students = Student.query.all()
        si = io.StringIO()
        cw = csv.writer(si)
        cw.writerow([
            'Enrollment No', 'Name', 'Email', 'Department', 'Semester',
            'Attendance (%)', 'Internal Marks', 'Backlogs', 'Fee Status',
            'Engagement Score', 'Campus Location', 'Dropout Risk Score', 'Risk Level', 'Lifecycle Status'
        ])
        for s in students:
            cw.writerow([
                s.enrollment_no, s.name, s.email, s.department, s.semester,
                s.attendance_percentage, s.internal_marks_avg, s.backlog_count,
                s.fee_status, s.engagement_score, s.campus_location,
                s.risk_score, s.risk_level, s.lifecycle_status
            ])
        output = io.BytesIO()
        output.write(si.getvalue().encode('utf-8'))
        output.seek(0)
        return send_file(
            output,
            mimetype="text/csv",
            as_attachment=True,
            download_name=f"student_dropout_report_{datetime.now().strftime('%Y%m%d')}.csv"
        )

    # ========================== COUNSELLING & INTERVENTION WORKFLOW ==========================
    @app.route('/counselling')
    @login_required
    @roles_required('Admin', 'Department Head', 'Faculty Mentor')
    def counselling_hub():
        role = session.get('role')
        user_id = session.get('user_id')

        # Lifecycle stages in strict risk-level priority (High Risk top, Manageable last)
        stages = ['At Risk', 'Under Review', 'Counselling', 'Intervened', 'Closed', 'Low Risk']

        # Configurable Stage Limits from SystemSetting
        limits = {
            'At Risk': SystemSetting.get_int('stage_limit_At_Risk', 8),
            'Under Review': SystemSetting.get_int('stage_limit_Under_Review', 6),
            'Counselling': SystemSetting.get_int('stage_limit_Counselling', 10),
            'Intervened': SystemSetting.get_int('stage_limit_Intervened', 15),
            'Closed': SystemSetting.get_int('stage_limit_Closed', 100),
            'Low Risk': SystemSetting.get_int('stage_limit_Low_Risk', 100)
        }

        critical_threshold = SystemSetting.get_float('critical_risk_threshold', 0.70)
        medium_threshold = SystemSetting.get_float('medium_risk_threshold', 0.50)

        stage_meta = {
            'At Risk': {
                'title': 'Critical At-Risk Queue',
                'badge': 'bg-danger text-white',
                'urgency': 'Critical (Immediate Action Required)',
                'desc': 'Students flagged by AI with high dropout probability needing urgent mentor assignment.',
                'icon': 'fa-triangle-exclamation text-danger'
            },
            'Under Review': {
                'title': 'Under Diagnostic Review',
                'badge': 'bg-warning-subtle text-dark border-warning',
                'urgency': 'High Priority (Pending Evaluation)',
                'desc': 'Cases escalated or assigned to mentors for preliminary diagnostics.',
                'icon': 'fa-clipboard-question text-warning'
            },
            'Counselling': {
                'title': 'Active Mentorship & Counselling',
                'badge': 'bg-primary-subtle text-primary border-primary',
                'urgency': 'Active Interventions',
                'desc': 'Active one-on-one sessions, parental consultations, and psycho-social support.',
                'icon': 'fa-comments text-primary'
            },
            'Intervened': {
                'title': 'Remedial Action Underway',
                'badge': 'bg-info-subtle text-info border-info',
                'urgency': 'Stabilizing & Monitoring',
                'desc': 'Students attending remedial classes, following fee installment plans, and recovering.',
                'icon': 'fa-chalkboard-user text-info'
            },
            'Closed': {
                'title': 'Resolved / Stable Cases',
                'badge': 'bg-success-subtle text-success border-success',
                'urgency': 'Manageable & Closed',
                'desc': 'Successfully rehabilitated students who cleared backlogs, improved attendance, and settled dues.',
                'icon': 'fa-circle-check text-success'
            },
            'Low Risk': {
                'title': 'Manageable Student Cohort',
                'badge': 'bg-light text-secondary border',
                'urgency': 'Low Risk / Manageable Baseline',
                'desc': 'Students in satisfactory academic and attendance standing.',
                'icon': 'fa-user-graduate text-success'
            }
        }

        stage_cases = {}
        stage_stats = {}

        for st in stages:
            q = Student.query.filter_by(lifecycle_status=st)
            if role == 'Faculty Mentor':
                q = q.filter((Student.assigned_mentor_id == user_id) | (Student.assigned_mentor_id == None))
            # Sort strictly by risk_score descending so high risk students are on top!
            students_in_stage = q.order_by(Student.risk_score.desc()).all()
            stage_cases[st] = students_in_stage

            count = len(students_in_stage)
            limit = limits.get(st, 10)
            capacity_pct = min(int((count / limit) * 100), 100) if limit > 0 else 0
            is_overflow = count > limit

            crit_count = sum(1 for s in students_in_stage if s.risk_score >= critical_threshold)
            med_count = sum(1 for s in students_in_stage if critical_threshold > s.risk_score >= medium_threshold)
            manageable_count = sum(1 for s in students_in_stage if s.risk_score < medium_threshold)

            stage_stats[st] = {
                'count': count,
                'limit': limit,
                'capacity_percent': capacity_pct,
                'is_overflow': is_overflow,
                'critical_count': crit_count,
                'moderate_count': med_count,
                'manageable_count': manageable_count
            }

        recent_sessions = CounsellingCase.query.order_by(CounsellingCase.created_at.desc()).limit(10).all()
        mentors = User.query.filter(User.role.in_(['Faculty Mentor', 'Department Head', 'Admin'])).all()

        return render_template(
            'counselling.html',
            stage_cases=stage_cases,
            stages=stages,
            stage_stats=stage_stats,
            stage_meta=stage_meta,
            critical_threshold=critical_threshold,
            medium_threshold=medium_threshold,
            recent_sessions=recent_sessions,
            mentors=mentors
        )

    @app.route('/counselling/<int:student_id>/add_session', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head', 'Faculty Mentor')
    def add_counselling_session(student_id):
        student = Student.query.get_or_404(student_id)
        mentor_id = session.get('user_id')
        new_status = request.form.get('lifecycle_status', student.lifecycle_status)
        remarks = request.form.get('mentor_remarks', '').strip()
        action_plan = request.form.get('action_plan', '').strip()
        followup_date_str = request.form.get('next_followup_date', '').strip()

        followup_date = None
        if followup_date_str:
            try:
                followup_date = datetime.strptime(followup_date_str, '%Y-%m-%d').date()
            except ValueError:
                pass

        if not remarks:
            flash('Mentor remarks are required to document the counselling session.', 'warning')
            return redirect(url_for('student_detail', student_id=student.id))

        # Create session record
        session_case = CounsellingCase(
            student_id=student.id,
            mentor_id=mentor_id,
            session_date=date.today(),
            status_at_time=new_status,
            mentor_remarks=remarks,
            action_plan=action_plan,
            next_followup_date=followup_date
        )
        db.session.add(session_case)

        # Update student record
        old_status = student.lifecycle_status
        student.lifecycle_status = new_status
        if not student.assigned_mentor_id:
            student.assigned_mentor_id = mentor_id

        db.session.commit()

        log_audit(
            'COUNSELLING_RECORDED',
            f"Counselling session recorded for {student.name} ({student.enrollment_no}). Status updated: '{old_status}' -> '{new_status}'."
        )

        create_notification(
            title=f"Counselling Update: {student.name}",
            message=f"Status progressed to '{new_status}' by {session.get('name')}. Plan: {action_plan[:60]}...",
            category="info"
        )

        flash(f"Counselling record saved successfully! Case status is now '{new_status}'.", 'success')
        return redirect(url_for('student_detail', student_id=student.id))

    @app.route('/students/<int:student_id>/assign_mentor', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head')
    def assign_mentor(student_id):
        student = Student.query.get_or_404(student_id)
        mentor_id = request.form.get('mentor_id')
        if mentor_id:
            mentor = User.query.get(int(mentor_id))
            if mentor:
                student.assigned_mentor_id = mentor.id
                db.session.commit()
                log_audit('MENTOR_ASSIGNED', f"Assigned mentor {mentor.name} to student {student.name}.")
                flash(f"Mentor {mentor.name} successfully assigned to {student.name}.", 'success')
        return redirect(url_for('student_detail', student_id=student.id))

    # ========================== ESCALATIONS & NOTIFICATIONS ==========================
    @app.route('/escalations/run_check', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head')
    def trigger_escalation_check():
        # Finds At-Risk students with risk score > 0.70 who have not progressed to Counselling or Intervened
        stagnant_cases = Student.query.filter(
            Student.risk_score >= 0.70,
            Student.lifecycle_status.in_(['At Risk', 'Low Risk'])
        ).all()

        escalated_count = 0
        for s in stagnant_cases:
            s.lifecycle_status = 'Under Review'
            create_notification(
                title=f"Escalation Flagged: {s.name}",
                message=f"Urgent attention required: {s.name} ({s.enrollment_no}) has {s.risk_score*100:.1f}% risk score without active intervention. Auto-escalated to 'Under Review'.",
                category="danger"
            )
            escalated_count += 1

        db.session.commit()
        log_audit('ESCALATION_CHECK_EXECUTED', f"Automated escalation scan processed {escalated_count} students to 'Under Review'.")
        flash(f"Escalation scan completed. Flagged and escalated {escalated_count} high-risk cases.", 'warning' if escalated_count > 0 else 'info')
        return redirect(url_for('dashboard'))

    @app.route('/notifications')
    @login_required
    def notifications_view():
        notifications = Notification.query.order_by(Notification.created_at.desc()).all()
        return render_template('notifications.html', notifications=notifications)

    @app.route('/notifications/<int:notif_id>/mark_read', methods=['POST'])
    @login_required
    def mark_notification_read(notif_id):
        notif = Notification.query.get_or_404(notif_id)
        notif.is_read = True
        db.session.commit()
        return redirect(url_for('notifications_view'))

    @app.route('/notifications/mark_all_read', methods=['POST'])
    @login_required
    def mark_all_notifications_read():
        Notification.query.update({Notification.is_read: True})
        db.session.commit()
        flash('All notifications marked as read.', 'info')
        return redirect(url_for('notifications_view'))

    # ========================== AUDIT LOGS ==========================
    @app.route('/audit-logs')
    @login_required
    @roles_required('Admin', 'Department Head')
    def audit_logs():
        logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(150).all()
        return render_template('audit_logs.html', logs=logs)

    # ========================== MODEL EXPLAINABILITY & PERFORMANCE ==========================
    @app.route('/model-performance')
    @login_required
    def model_performance():
        ml = MLEngine.get_instance()
        metrics = ml.metrics
        feature_importances = ml.feature_importances
        sorted_fi = sorted(feature_importances.items(), key=lambda x: x[1], reverse=True)
        
        return render_template(
            'model_performance.html',
            metrics=metrics,
            feature_importances=sorted_fi
        )

    # ========================== ADMINISTRATIVE CONTROLS & MODEL RETRAINING ==========================
    @app.route('/admin/settings', methods=['GET', 'POST'])
    @login_required
    @roles_required('Admin', 'Department Head')
    def admin_settings():
        if request.method == 'POST':
            # 1. Update stage limits
            for key in ['stage_limit_At_Risk', 'stage_limit_Under_Review', 'stage_limit_Counselling', 
                        'stage_limit_Intervened', 'stage_limit_Closed', 'stage_limit_Low_Risk']:
                if key in request.form:
                    val = request.form.get(key, '').strip()
                    if val.isdigit():
                        SystemSetting.set_value(key, int(val))

            # 2. Update Risk Factor Policy Limits (Attendance, Backlogs, Marks, LMS)
            float_rules = ['rule_attendance_warning', 'rule_attendance_critical', 
                           'rule_marks_warning', 'rule_marks_critical', 'rule_engagement_critical']
            for fr in float_rules:
                if fr in request.form:
                    try:
                        v = float(request.form.get(fr))
                        SystemSetting.set_value(fr, str(round(v, 1)))
                    except (ValueError, TypeError):
                        pass

            int_rules = ['rule_backlogs_warning', 'rule_backlogs_critical']
            for ir in int_rules:
                if ir in request.form:
                    val = request.form.get(ir, '').strip()
                    if val.isdigit():
                        SystemSetting.set_value(ir, int(val))

            if 'rule_fee_due_severity' in request.form:
                SystemSetting.set_value('rule_fee_due_severity', request.form.get('rule_fee_due_severity'))

            if 'rule_auto_lifecycle_target' in request.form:
                SystemSetting.set_value('rule_auto_lifecycle_target', request.form.get('rule_auto_lifecycle_target'))

            # 3. Update Risk Score Thresholds
            if 'critical_risk_threshold' in request.form:
                try:
                    crit = float(request.form.get('critical_risk_threshold', 70)) / 100.0
                    SystemSetting.set_value('critical_risk_threshold', str(round(crit, 2)))
                except ValueError:
                    pass

            if 'medium_risk_threshold' in request.form:
                try:
                    med = float(request.form.get('medium_risk_threshold', 50)) / 100.0
                    SystemSetting.set_value('medium_risk_threshold', str(round(med, 2)))
                except ValueError:
                    pass

            log_audit('SETTINGS_UPDATED', f"Risk factor policy rules, stage capacity limits, and thresholds updated by {session.get('name')}.")
            flash('Administrative risk limits, stage capacities, and routing policies successfully updated!', 'success')
            return redirect(url_for('admin_settings'))

        # Fetch current settings and rules
        rules = SystemSetting.get_risk_rules()
        settings = {
            'stage_limit_At_Risk': SystemSetting.get_int('stage_limit_At_Risk', 8),
            'stage_limit_Under_Review': SystemSetting.get_int('stage_limit_Under_Review', 6),
            'stage_limit_Counselling': SystemSetting.get_int('stage_limit_Counselling', 10),
            'stage_limit_Intervened': SystemSetting.get_int('stage_limit_Intervened', 15),
            'stage_limit_Closed': SystemSetting.get_int('stage_limit_Closed', 100),
            'stage_limit_Low_Risk': SystemSetting.get_int('stage_limit_Low_Risk', 100),
            'critical_risk_threshold': int(rules['critical_risk_threshold'] * 100),
            'medium_risk_threshold': int(rules['medium_risk_threshold'] * 100),
            'rule_attendance_warning': rules['attendance_warning'],
            'rule_attendance_critical': rules['attendance_critical'],
            'rule_backlogs_warning': rules['backlogs_warning'],
            'rule_backlogs_critical': rules['backlogs_critical'],
            'rule_marks_warning': rules['marks_warning'],
            'rule_marks_critical': rules['marks_critical'],
            'rule_engagement_critical': rules['engagement_critical'],
            'rule_fee_due_severity': rules['fee_due_severity'],
            'rule_auto_lifecycle_target': rules['auto_lifecycle_target']
        }

        ml = MLEngine.get_instance()
        return render_template('admin_settings.html', settings=settings, metrics=ml.metrics)

    @app.route('/admin/settings/reset_nominal', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head')
    def reset_nominal_settings():
        SystemSetting.reset_to_nominal_rules()
        log_audit('SETTINGS_RESET_NOMINAL', f"Risk limits reset to Sanskriti University nominal defaults by {session.get('name')}.")
        flash('Risk factor limits successfully reset to Sanskriti University nominal global defaults.', 'info')
        return redirect(url_for('admin_settings'))

    @app.route('/admin/reapply_rules', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head')
    def reapply_rules_to_all_students():
        ml = MLEngine.get_instance()
        rules = SystemSetting.get_risk_rules()
        students = Student.query.all()

        recalc_count = 0
        for s in students:
            student_data = {
                'attendance_percentage': s.attendance_percentage,
                'internal_marks_avg': s.internal_marks_avg,
                'backlog_count': s.backlog_count,
                'fee_status': s.fee_status,
                'engagement_score': s.engagement_score,
                'semester': s.semester
            }
            pred = ml.predict_student(student_data, rules=rules)
            s.risk_score = pred['risk_score']
            s.risk_level = pred['risk_level']
            s.key_reasons = json.dumps(pred['reasons'])
            
            # If in un-managed or initial status, route according to admin policy
            if s.lifecycle_status in ['Low Risk', 'At Risk']:
                s.lifecycle_status = pred['recommended_lifecycle']
            recalc_count += 1

        db.session.commit()
        log_audit('RULES_REAPPLIED_ALL', f"Re-evaluated {recalc_count} students against updated policy rules.")
        flash(f"Successfully re-evaluated all {recalc_count} student records against the active risk policy limits!", 'success')
        return redirect(url_for('admin_settings'))

    @app.route('/admin/retrain_model', methods=['POST'])
    @login_required
    @roles_required('Admin', 'Department Head')
    def retrain_model_endpoint():
        ml = MLEngine.get_instance()
        custom_df = None

        saved_filename = None
        if 'training_file' in request.files:
            file = request.files['training_file']
            if file and file.filename != '' and file.filename.endswith('.csv'):
                try:
                    filename = secure_filename(file.filename)
                    saved_filename = filename
                    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filepath)

                    # Also save directly to project root directory
                    try:
                        root_copy = os.path.join(app.config['BASE_DIR'], filename)
                        shutil.copyfile(filepath, root_copy)
                    except Exception:
                        pass

                    custom_df = pd.read_csv(filepath)
                    required_cols = ['attendance_percentage', 'internal_marks_avg', 'backlog_count', 'fee_status', 'engagement_score', 'semester', 'dropped_out']
                    missing = [c for c in required_cols if c not in custom_df.columns]
                    if missing:
                        flash(f"Uploaded training file is missing required columns: {', '.join(missing)}", 'danger')
                        return redirect(url_for('admin_settings'))
                except Exception as e:
                    flash(f"Error reading training CSV: {str(e)}", 'danger')
                    return redirect(url_for('admin_settings'))

        try:
            new_metrics = ml.retrain(custom_df=custom_df)
            rf_acc = new_metrics['Random Forest']['Accuracy'] * 100
            rf_auc = new_metrics['Random Forest']['ROC_AUC'] * 100
            
            log_audit(
                'MODEL_RETRAINED',
                f"Model retrained successfully. New RF Accuracy: {rf_acc:.2f}%, ROC-AUC: {rf_auc:.2f}%."
            )
            create_notification(
                title="AI Model Retrained",
                message=f"Dropout prediction classifier retrained. Updated Accuracy: {rf_acc:.2f}%, ROC-AUC: {rf_auc:.2f}%.",
                category="success"
            )
            msg = f"AI Model Retrained Successfully! New Random Forest Accuracy: {rf_acc:.2f}%, ROC-AUC: {rf_auc:.2f}%."
            if saved_filename:
                msg += f" Dataset saved to: '{saved_filename}' in project folder."
            flash(msg, 'success')
        except Exception as e:
            flash(f"Failed to retrain model: {str(e)}", 'danger')

        return redirect(url_for('model_performance'))

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
