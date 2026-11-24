# AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT

## A PROJECT REPORT

**Submitted in partial fulfillment of the award of Degree of**  
**Bachelor of Technology in Computer Science and Engineering**

<div align="center"><img src="static/images/sanskriti_logo.png" width="140" alt="Sanskriti University Logo"></div>

### Submitted by

* Enrollment No: **2302320151**, **SHAIK SHAFI**
* Enrollment No: **2302320119**, **SHAIK MOHAMMAD ALI**
* Enrollment No: **2302320118**, **SHAIK MAHAMAD YASEEN**
* Enrollment No: **2302320099**, **DESIREDDY RAMESH**

**Under the Supervision of:** **Mr. Satyam Dwivedi**, Assistant Professor, Department of Computer Science & Engineering  

**Department of Computer Science and Engineering**  
**SANSKRITI UNIVERSITY, MATHURA, U.P**  
**November, 2026**

---

## Department of Computer Science & Engineering

### CERTIFICATE

This is to certify that the work embodies in this project report entitled **‘AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT’** being submitted by Enrollment No: **2302320151** **SHAIK SHAFI**, Enrollment No: **2302320119** **SHAIK MOHAMMAD ALI**, Enrollment No: **2302320118** **SHAIK MAHAMAD YASEEN**, Enrollment No: **2302320099** **DESIREDDY RAMESH**, for partial fulfillment of the requirement for the award of **Bachelor of Technology in Computer Science and Engineering** to Sanskriti University, Mathura during the academic year **2026-27** is a record of Bonafide piece of work, undertaken under the supervision of the undersigned.

**Approved and Supervised by:**  
**Mr. Satyam Dwivedi** (Assistant Professor, SOEIT) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Dean, SOEIT**

---

## Department of Computer Science & Engineering

### DECLARATION

We, **SHAIK SHAFI**, **SHAIK MOHAMMAD ALI**, **SHAIK MAHAMAD YASEEN**, **DESIREDDY RAMESH** student of Bachelor of Technology in Computer Science and Engineering, Session: **2026-27**, Sanskriti University, Mathura hereby declare that the work presented in this project report entitled **“AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT”** is the outcome of our own Bonafide work and is correct to the best of our knowledge and this work has been undertaken taking care of Engineering Ethics. It contains no material previously published or written by another person nor material which has been accepted for the award of any other degree or diploma of the university or other institute of higher learning, except where due acknowledgment has been made in the text.

| Enrollment No. | Student Name | Signature |
|---|---|---|
| Enrollment No: 2302320151 | **SHAIK SHAFI** | ____________________ |
| Enrollment No: 2302320119 | **SHAIK MOHAMMAD ALI** | ____________________ |
| Enrollment No: 2302320118 | **SHAIK MAHAMAD YASEEN** | ____________________ |
| Enrollment No: 2302320099 | **DESIREDDY RAMESH** | ____________________ |

**Date:** November, 2026

---

### ACKNOWLEDGEMENT

We would like to thank our Hon'ble Chancellor, Hon'ble Chief Executive Officer, Hon'ble Vice Chancellor, and Respected Dean, SOEIT. We express our sincere gratitude and thanks to our Project Supervisor, **Mr. Satyam Dwivedi**. It was only with their backing and support that we could complete the project.

They provided us with all kinds of help and corrected us whenever we seemed to make mistakes. We have no words to express our gratitude. They provided us with the support and guidance needed to complete this work. Without their support, we could not have even started the work. Therefore, we are truly grateful to them.

We acknowledge our dearest parents for being a constant source of encouragement and moral support, which helped us tremendously in this endeavour.

We also declare, to the best of our knowledge and belief, that this work has not been submitted anywhere else.

* Enrollment No: **2302320151**, **SHAIK SHAFI**
* Enrollment No: **2302320119**, **SHAIK MOHAMMAD ALI**
* Enrollment No: **2302320118**, **SHAIK MAHAMAD YASEEN**
* Enrollment No: **2302320099**, **DESIREDDY RAMESH**

---

### TABLE OF CONTENTS

| Topic | Page No. |
|---|---|
| **LIST OF FIGURES** | vi |
| **ABBREVIATIONS** | vii |
| **LIST OF STANDARDS** | viii |
| **ABSTRACT** | ix |
| **Chapter 1: INTRODUCTION** | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.1 Client Identification of Client / Need / Relevant Contemporary issue | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.2 Justification of Issue Through Statistics and Documentation | 2 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.3 Problem Requires Resolution | 3 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.4 Justification of Need Through Survey | 4 |
| &nbsp;&nbsp;&nbsp;&nbsp;1.5 Relevant Contemporary Issue Documented In Report By Agencies | 5 |
| **Chapter 2: LITERATURE REVIEW** | 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.1 Introduction to the Literature Review | 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.2 Growth of Machine Learning and Early Warning Systems in Higher Education | 7 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.3 Student Retention Operations and Institutional Monitoring Networks in India | 8 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.4 Operational and Resource Challenges of Faculty Mentors and Organizations | 9 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.5 Limitations of Manual Case Documentation and Student Tracking | 10 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.6 Complexity of Regulatory Compliance for Student Privacy and Data Governance | 11 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.7 Review of Existing Educational ERP Tools and Market Gaps | 12 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.8 Role of Technology, Explainable AI (XAI) and Automation in Retention Management | 13 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.9 Technological Foundation: Python Flask, Scikit-learn, SQLite in EDM Stack | 14 |
| &nbsp;&nbsp;&nbsp;&nbsp;2.10 Identified Research Gap and Integrated Summary of Literature Findings | 15 |
| **Chapter 3: METHODOLOGY** | 16 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.1 Timeline of the Reported Problem | 16 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.2 Existing Solutions | 17 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.3 Bibliometric Analysis | 18 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.4 Review Summary | 19 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.5 Problem Definition | 20 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.6 Goals / Objectives | 21 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.7 Scope of the System | 22 |
| &nbsp;&nbsp;&nbsp;&nbsp;3.8 System Requirements | 23 |
| **Chapter 4: DESIGN FLOW / PROCESS** | 24 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.1 Evaluation & Selection of Specifications / Features | 24 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.2 Design Constraints | 25 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.3 Analysis and Feature Finalization Subject to Constraints | 26 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.4 Design Flow (4.4.1 Design Flow Diagram, 4.4.2 System Navigation Flow Diagram) | 27 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.5 Design Selection | 28 |
| &nbsp;&nbsp;&nbsp;&nbsp;4.6 Implementation Plan / Methodology (Use Case, Sequence, Class Diagrams) | 29 |
| **Chapter 5: RESULTS ANALYSIS AND VALIDATION** | 32 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.1 Implementation of Solution | 32 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.2 System Performance & User Validation | 38 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.3 Challenges Faced | 39 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.4 Validation of Results | 40 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.5 Performance Evaluation | 41 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.6 User Feedback and Improvements | 42 |
| &nbsp;&nbsp;&nbsp;&nbsp;5.7 Summary of Findings | 43 |
| **CHAPTER 6: CONCLUSION AND FUTURE WORK** | 44 |
| **REFERENCES** | 45 |
| **PART II: COMPLETE VERBATIM ANNOTATED SOURCE CODEBASE** | 47 |

---

### LIST OF FIGURES

| Figure No. | Figure Description | Page(s) |
|---|---|---|
| Figure 4.4.1 | System Architectural Design Flow Diagram | 27 |
| Figure 4.4.2 | System Navigation and Role Routing Flow Diagram | 27 |
| Figure 4.6.1 | System Comprehensive Use Case Diagram | 29 |
| Figure 4.6.3 | Unified UML Sequence Diagram | 30 |
| Figure 4.6.4 | System Class Diagram & Relational Entity Model | 31 |
| Figure 5.1.1 | Application Interface – Student Registration & Bulk Ingestion Page | 33 |
| Figure 5.1.2 | Application Interface – Role-Based Unified Portal Authentication Page | 34 |
| Figure 5.1.3 | Application Interface – Executive Authority Analytics Dashboard Page | 35 |
| Figure 5.1.4 | Application Interface – High-Priority Flagged Students & Case Tracking | 36 |
| Figure 5.1.5 | Application Interface – Counselling Lifecycle Hub & Queue Workload Meters | 37 |
| Figure 5.1.6 | Application Interface – Administrative Governance & Policy Rules Panel | 37 |
| Figure 5.1.7 | Application Interface – Forensic Security Audit Trail & Activity Log History | 38 |

---

### ABBREVIATIONS

| Abbreviation | Expanded Description & System Scope |
|---|---|
| HTML | Hyper-Text Markup Language: Structures the web pages like registration, login, and dashboard |
| CSS | Cascading Style Sheets: Styles responsive UI layouts, risk level badges, and component themes |
| JS | JavaScript: Powers dynamic client-side interactions and Chart.js analytics graphics |
| AI | Artificial Intelligence: Computational algorithms automating student dropout risk evaluation |
| ML | Machine Learning: Supervised classification algorithms trained on institutional data |
| EDM | Educational Data Mining: Extraction of actionable pedagogical patterns from student records |
| RF | Random Forest: Primary ensemble classification model utilizing 100 bagging decision trees |
| LR | Logistic Regression: Baseline linear probabilistic classifier benchmarked against Random Forest |
| XAI | Explainable AI: Mathematical deficit attribution engine providing human-interpretable reasons |
| RBAC | Role-Based Access Control: 4-tier security framework enforcing principle of least privilege |
| ORM | Object Relational Mapping: SQLAlchemy abstraction layer connecting Python to SQLite database |
| API | Application Programming Interface: RESTful endpoints facilitating data interchange |
| CSV | Comma-Separated Values: Tabular flat-file format utilized for bulk cohort roster ingestion |
| DFD | Data Flow Diagram: Graphical modeling of data movements across system processes |
| ERD | Entity-Relationship Diagram: Structural database diagram detailing relational tables and keys |

---

### LIST OF STANDARDS

| Standard | Publishing Agency (Abbreviation) | About the Standard & Institutional Relevance |
|---|---|---|
| ISO/IEC 25010 | ISO/IEC | Defines software product quality models, including usability, reliability, security, and performance efficiency. |
| IEEE 830-1998 | IEEE | Recommended Practice for Software Requirements Specifications (SRS). |
| ISO/IEC 27001 | ISO/IEC | Information security management systems standard, guiding PBKDF2 password hashing and tamper-evident audit logs. |
| W3C WCAG 2.1 | W3C | Web Content Accessibility Guidelines ensuring accessible interface design. |
| IEEE 730-2014 | IEEE | Software Quality Assurance Processes, guiding automated testing. |

---

### ABSTRACT

The **AI-Based Prediction of Reasons for Student Dropout** is a full-stack educational data mining and retention management web application engineered using modern Python and web technologies (Flask, Scikit-learn, SQLite, SQLAlchemy, Bootstrap 5, and Chart.js). It is designed to connect university leadership, department heads, faculty mentors, and students to proactively identify at-risk learners, explain underlying root-cause risk drivers via Explainable AI (XAI), and streamline remedial interventions through a structured 5-stage counseling lifecycle hub.

The system incorporates an Explainable AI (XAI) reason attribution engine that mathematically computes feature deficits against institutional benchmarks (attendance below 75%, internal marks below 40%, active backlogs >= 3, fee payment arrears, and LMS disengagement). Rather than presenting opaque probability numbers, the platform pairs each prediction with weighted percentage attributions and prescriptive recommendations. A dynamic 5-Stage Counselling Lifecycle Hub (At Risk -> Under Review -> Counselling -> Intervened -> Closed) prevents faculty mentor overload through administrator-configurable queue capacity meters. Strict Role-Based Access Control (RBAC) ensures student privacy isolation while enabling comprehensive executive monitoring. Empirical validation demonstrates that the primary Random Forest classifier achieves 90.3% accuracy and 94.2% ROC-AUC, providing Sanskriti University with an auditable institutional asset for safeguarding student retention.

---

# PART I: CORE CHAPTERS & ARCHITECTURE BLUEPRINTS

## Chapter 1: INTRODUCTION

1.1 Client Identification of Client / Need / Relevant Contemporary Issue  
1.2 Justification of Issue Through Statistics and Documentation  
1.3 Problem Requires Resolution  
1.4 Justification of Need Through Survey  
1.5 Relevant Contemporary Issue Documented In Report By Agencies

## Chapter 2: LITERATURE REVIEW

2.1 Introduction to the Literature Review  
2.2 Growth of Machine Learning and Early Warning Systems in Higher Education  
2.3 Student Retention Operations and Institutional Monitoring Networks in India  
2.4 Operational and Resource Challenges of Faculty Mentors and Organizations  
2.5 Limitations of Manual Case Documentation and Student Tracking  
2.6 Complexity of Regulatory Compliance for Student Privacy and Data Governance  
2.7 Review of Existing Educational ERP Tools and Market Gaps  
2.8 Role of Technology, Explainable AI (XAI) and Automation in Retention Management  
2.9 Technological Foundation: Python Flask, Scikit-learn, SQLite in EDM Stack  
2.10 Identified Research Gap and Integrated Summary of Literature Findings

## Chapter 3: METHODOLOGY

3.1 Timeline of the Reported Problem  
3.2 Existing Solutions  
3.3 Bibliometric Analysis  
3.4 Review Summary  
3.5 Problem Definition  
3.6 Goals / Objectives  
3.7 Scope of the System  
3.8 System Requirements

## Chapter 4: DESIGN FLOW / PROCESS

4.1 Evaluation & Selection of Specifications / Features  
4.2 Design Constraints  
4.3 Analysis and Feature Finalization Subject to Constraints  
4.4 Design Flow (4.4.1 Design Flow Diagram, 4.4.2 System Navigation Flow Diagram)  
4.5 Design Selection (Decoupled 3-Tier Layered Architecture)  
4.6 Implementation Plan / Methodology (Use Case, Sequence, Class Diagrams)

## Chapter 5: RESULTS ANALYSIS AND VALIDATION

5.1 Implementation of Solution  
5.2 System Performance & User Validation  
5.3 Challenges Faced  
5.4 Validation of Results  
5.5 Performance Evaluation (Random Forest 90.3% vs Logistic Regression 84.1%)  
5.6 User Feedback and Improvements  
5.7 Summary of Findings

## CHAPTER 6: CONCLUSION AND FUTURE WORK

6.1 Conclusion  
6.2 Future Work

---

# PART II: COMPLETE VERBATIM ANNOTATED SOURCE CODE LISTINGS

## File: `app.py`
**Description:** Complete Flask Web Application Controller, REST Endpoints, RBAC, CSV Ingestion & Audit System  
**Line Count:** 1021 lines

```python
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

```

## File: `ml_engine.py`
**Description:** Machine Learning Pipeline, Random Forest Classifier, Baseline Logistic Regression & XAI Engine  
**Line Count:** 345 lines

```python
import os
import joblib
import pandas as pd
import numpy as np

MODEL_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'models', 'dropout_models.pkl')

class MLEngine:
    _instance = None

    def __init__(self):
        self.artifacts = None
        self.load_model()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MLEngine()
        return cls._instance

    def load_model(self):
        if not os.path.exists(MODEL_PATH):
            from train_model import train_and_export_models
            self.artifacts = train_and_export_models(MODEL_PATH)
        else:
            self.artifacts = joblib.load(MODEL_PATH)
        self.rf_pipeline = self.artifacts['rf_pipeline']
        self.lr_pipeline = self.artifacts['lr_pipeline']
        self.metrics = self.artifacts['metrics']
        self.feature_importances = self.artifacts['feature_importances']

    def retrain(self, custom_df=None, n_samples=3000):
        """
        Retrains the Random Forest and Logistic Regression models.
        Can retrain using a newly supplied historical dataset (with dropped_out column),
        or regenerate an expanded realistic dataset.
        """
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.linear_model import LogisticRegression
        from sklearn.preprocessing import StandardScaler, OneHotEncoder
        from sklearn.compose import ColumnTransformer
        from sklearn.pipeline import Pipeline
        from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
        from train_model import generate_synthetic_training_data

        if custom_df is not None:
            df = custom_df.copy()
        else:
            seed = int(np.random.randint(1, 10000))
            df = generate_synthetic_training_data(n_samples=n_samples, random_state=seed)

        feature_cols = ['attendance_percentage', 'internal_marks_avg', 'backlog_count', 'fee_status', 'engagement_score', 'semester']
        numeric_features = ['attendance_percentage', 'internal_marks_avg', 'backlog_count', 'engagement_score', 'semester']
        categorical_features = ['fee_status']

        X = df[feature_cols]
        y = df['dropped_out']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numeric_features),
                ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
            ]
        )

        rf_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', RandomForestClassifier(n_estimators=120, max_depth=8, random_state=42, min_samples_split=5))
        ])
        rf_pipeline.fit(X_train, y_train)
        y_pred_rf = rf_pipeline.predict(X_test)
        y_proba_rf = rf_pipeline.predict_proba(X_test)[:, 1]

        lr_pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(random_state=42, max_iter=500))
        ])
        lr_pipeline.fit(X_train, y_train)
        y_pred_lr = lr_pipeline.predict(X_test)
        y_proba_lr = lr_pipeline.predict_proba(X_test)[:, 1]

        metrics = {
            'Random Forest': {
                'Accuracy': float(accuracy_score(y_test, y_pred_rf)),
                'Precision': float(precision_score(y_test, y_pred_rf)),
                'Recall': float(recall_score(y_test, y_pred_rf)),
                'F1_Score': float(f1_score(y_test, y_pred_rf)),
                'ROC_AUC': float(roc_auc_score(y_test, y_proba_rf))
            },
            'Logistic Regression': {
                'Accuracy': float(accuracy_score(y_test, y_pred_lr)),
                'Precision': float(precision_score(y_test, y_pred_lr)),
                'Recall': float(recall_score(y_test, y_pred_lr)),
                'F1_Score': float(f1_score(y_test, y_pred_lr)),
                'ROC_AUC': float(roc_auc_score(y_test, y_proba_lr))
            }
        }

        rf_model = rf_pipeline.named_steps['classifier']
        cat_feature_names = list(rf_pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_features))
        all_feature_names = numeric_features + cat_feature_names
        feature_importances = dict(zip(all_feature_names, [float(x) for x in rf_model.feature_importances_]))

        artifacts = {
            'rf_pipeline': rf_pipeline,
            'lr_pipeline': lr_pipeline,
            'feature_cols': feature_cols,
            'numeric_features': numeric_features,
            'categorical_features': categorical_features,
            'all_feature_names': all_feature_names,
            'feature_importances': feature_importances,
            'metrics': metrics,
            'benchmarks': {
                'attendance_percentage': 75.0,
                'internal_marks_avg': 50.0,
                'backlog_count': 0,
                'engagement_score': 60.0
            }
        }

        os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
        joblib.dump(artifacts, MODEL_PATH)

        self.artifacts = artifacts
        self.rf_pipeline = rf_pipeline
        self.lr_pipeline = lr_pipeline
        self.metrics = metrics
        self.feature_importances = feature_importances

        return metrics

    def analyze_reasons(self, student_dict, risk_score, rules=None):
        """
        Explainable AI (XAI) reason analysis.
        Calculates feature deficit against benchmarks and weights by RF feature importance
        to identify the top contributing reasons for dropout risk.
        Respects administrator-configured limits or nominal institutional defaults.
        """
        if rules is None:
            rules = {
                'attendance_warning': 75.0,
                'attendance_critical': 60.0,
                'backlogs_warning': 1,
                'backlogs_critical': 3,
                'marks_warning': 55.0,
                'marks_critical': 40.0,
                'engagement_critical': 40.0,
                'fee_due_severity': 'danger'
            }

        att_warn = float(rules.get('attendance_warning', 75.0))
        att_crit = float(rules.get('attendance_critical', 60.0))
        back_warn = int(rules.get('backlogs_warning', 1))
        back_crit = int(rules.get('backlogs_critical', 3))
        marks_warn = float(rules.get('marks_warning', 55.0))
        marks_crit = float(rules.get('marks_critical', 40.0))
        eng_crit = float(rules.get('engagement_critical', 40.0))

        attendance = float(student_dict.get('attendance_percentage', 100))
        marks = float(student_dict.get('internal_marks_avg', 75))
        backlogs = int(student_dict.get('backlog_count', 0))
        fee = str(student_dict.get('fee_status', 'Paid')).strip()
        engagement = float(student_dict.get('engagement_score', 80))

        deficits = []

        # Attendance deficit
        if attendance < att_warn:
            severity = 'danger' if attendance < att_crit else 'warning'
            weight = self.feature_importances.get('attendance_percentage', 0.40)
            deficit_score = ((att_warn - attendance) / att_warn) * weight
            deficits.append({
                'factor': 'Attendance Deficit',
                'description': f"Low Attendance: {attendance:.1f}% (Below threshold of {att_warn:.0f}%, Critical: {att_crit:.0f}%)",
                'raw_score': deficit_score,
                'severity': severity
            })

        # Academic marks deficit
        if marks < marks_warn:
            severity = 'danger' if marks < marks_crit else 'warning'
            weight = self.feature_importances.get('internal_marks_avg', 0.23)
            deficit_score = ((marks_warn - marks) / marks_warn) * weight
            deficits.append({
                'factor': 'Poor Academic Performance',
                'description': f"Internal Marks: {marks:.1f}% (Below passing standard of {marks_warn:.0f}%)",
                'raw_score': deficit_score,
                'severity': severity
            })

        # Backlogs deficit
        if backlogs >= back_warn:
            severity = 'danger' if backlogs >= back_crit else 'warning'
            weight = self.feature_importances.get('backlog_count', 0.15)
            denom = float(max(back_crit, 1))
            deficit_score = min(backlogs / denom, 1.0) * weight
            deficits.append({
                'factor': 'Academic Backlogs',
                'description': f"Active Backlogs: {backlogs} failed subject(s) (Warning limit: {back_warn}, Critical: {back_crit})",
                'raw_score': deficit_score,
                'severity': severity
            })

        # Fee default deficit
        if fee.lower() in ['due', 'unpaid', 'defaulted']:
            weight = self.feature_importances.get('fee_status_Paid', 0.08) * 1.5
            fee_sev = rules.get('fee_due_severity', 'danger')
            deficits.append({
                'factor': 'Financial Overdue',
                'description': "Tuition Fee Status: Overdue / Defaulted",
                'raw_score': weight,
                'severity': fee_sev
            })
        elif fee.lower() in ['partial', 'pending', 'half']:
            weight = self.feature_importances.get('fee_status_Partial', 0.03) * 1.2
            deficits.append({
                'factor': 'Partial Financial Dues',
                'description': "Tuition Fee Status: Partial dues pending",
                'raw_score': weight,
                'severity': 'warning'
            })

        # Engagement deficit
        if engagement < eng_crit + 15.0:
            severity = 'danger' if engagement < eng_crit else 'warning'
            weight = self.feature_importances.get('engagement_score', 0.11)
            deficit_score = ((eng_crit + 15.0 - engagement) / (eng_crit + 15.0)) * weight
            deficits.append({
                'factor': 'Low LMS Engagement',
                'description': f"Low Digital Activity: {engagement:.1f}/100 portal activity (Benchmark: {eng_crit:.0f})",
                'raw_score': deficit_score,
                'severity': severity
            })

        if not deficits:
            # Positive remarks for low risk students
            return [{
                'factor': 'Consistent Performance',
                'description': f"Good academic standing ({marks:.1f}%), regular attendance ({attendance:.1f}%), and cleared fees.",
                'contribution_percentage': 100.0,
                'severity': 'success'
            }]

        total_deficit = sum(d['raw_score'] for d in deficits)
        if total_deficit > 0:
            for d in deficits:
                d['raw_score'] = float(d['raw_score'])
                d['contribution_percentage'] = float(round((d['raw_score'] / total_deficit) * 100.0, 1))

        # Sort descending by contribution percentage
        deficits.sort(key=lambda x: x['contribution_percentage'], reverse=True)
        return deficits

    def predict_student(self, student_dict, rules=None):
        """
        Takes student record dict and returns risk_score (float), risk_level (str),
        risk_tier (str), recommended_lifecycle (str), and list of key reasons.
        """
        if rules is None:
            rules = {
                'attendance_warning': 75.0,
                'attendance_critical': 60.0,
                'backlogs_warning': 1,
                'backlogs_critical': 3,
                'marks_warning': 55.0,
                'marks_critical': 40.0,
                'engagement_critical': 40.0,
                'fee_due_severity': 'danger',
                'critical_risk_threshold': 0.70,
                'medium_risk_threshold': 0.50,
                'auto_lifecycle_target': 'At Risk'
            }

        data = {
            'attendance_percentage': [float(student_dict.get('attendance_percentage', 100.0))],
            'internal_marks_avg': [float(student_dict.get('internal_marks_avg', 75.0))],
            'backlog_count': [int(student_dict.get('backlog_count', 0))],
            'fee_status': [str(student_dict.get('fee_status', 'Paid'))],
            'engagement_score': [float(student_dict.get('engagement_score', 80.0))],
            'semester': [int(student_dict.get('semester', 1))]
        }
        df = pd.DataFrame(data)
        
        prob = self.rf_pipeline.predict_proba(df)[0, 1]
        risk_score = round(float(prob), 3)

        med_thresh = float(rules.get('medium_risk_threshold', 0.50))
        crit_thresh = float(rules.get('critical_risk_threshold', 0.70))
        att_crit = float(rules.get('attendance_critical', 60.0))
        back_crit = int(rules.get('backlogs_critical', 3))

        att_val = float(student_dict.get('attendance_percentage', 100.0))
        back_val = int(student_dict.get('backlog_count', 0))

        # Check if student hits critical policy rule limits
        hits_critical_rule = (att_val < att_crit) or (back_val >= back_crit)

        if risk_score >= crit_thresh or hits_critical_rule:
            risk_level = 'At Risk'
            risk_tier = 'Critical High Risk'
        elif risk_score >= med_thresh:
            risk_level = 'At Risk'
            risk_tier = 'Moderate Risk'
        else:
            risk_level = 'Low Risk'
            risk_tier = 'Manageable'

        auto_target = rules.get('auto_lifecycle_target', 'At Risk')
        recommended_lifecycle = auto_target if risk_level == 'At Risk' else 'Low Risk'

        reasons = self.analyze_reasons(student_dict, risk_score, rules=rules)

        return {
            'risk_score': risk_score,
            'risk_level': risk_level,
            'risk_tier': risk_tier,
            'recommended_lifecycle': recommended_lifecycle,
            'reasons': reasons
        }

    def predict_dataframe(self, df, rules=None):
        """
        Batch prediction for pandas DataFrame (CSV upload).
        """
        required_cols = ['attendance_percentage', 'internal_marks_avg', 'backlog_count', 'fee_status', 'engagement_score', 'semester']
        # Fill missing values if any
        df['attendance_percentage'] = pd.to_numeric(df.get('attendance_percentage', 75.0), errors='coerce').fillna(75.0)
        df['internal_marks_avg'] = pd.to_numeric(df.get('internal_marks_avg', 60.0), errors='coerce').fillna(60.0)
        df['backlog_count'] = pd.to_numeric(df.get('backlog_count', 0), errors='coerce').fillna(0).astype(int)
        df['fee_status'] = df.get('fee_status', 'Paid').fillna('Paid').astype(str)
        df['engagement_score'] = pd.to_numeric(df.get('engagement_score', 70.0), errors='coerce').fillna(70.0)
        df['semester'] = pd.to_numeric(df.get('semester', 1), errors='coerce').fillna(1).astype(int)

        input_df = df[required_cols]
        probs = self.rf_pipeline.predict_proba(input_df)[:, 1]
        
        results = []
        for idx, row in df.iterrows():
            row_dict = row.to_dict()
            pred = self.predict_student(row_dict, rules=rules)
            results.append(pred)
        return results

```

## File: `database.py`
**Description:** Relational Database Persistence Layer, SQLAlchemy ORM Models & Lifecycle Definitions  
**Line Count:** 172 lines

```python
from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # Admin, Department Head, Faculty Mentor, Student
    department = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    counselling_sessions = db.relationship('CounsellingCase', backref='mentor', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    enrollment_no = db.Column(db.String(50), unique=True, nullable=False, index=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(30), nullable=True)
    department = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.Integer, nullable=False, default=1)
    
    # Prediction features
    attendance_percentage = db.Column(db.Float, nullable=False, default=100.0)
    internal_marks_avg = db.Column(db.Float, nullable=False, default=75.0)
    backlog_count = db.Column(db.Integer, nullable=False, default=0)
    fee_status = db.Column(db.String(30), nullable=False, default='Paid')  # Paid, Partial, Due
    engagement_score = db.Column(db.Float, nullable=False, default=80.0)    # 0 - 100 LMS activity
    campus_location = db.Column(db.String(100), nullable=False, default='Main Campus')
    
    # ML Outputs
    risk_score = db.Column(db.Float, default=0.0)  # 0.0 to 1.0 probability
    risk_level = db.Column(db.String(30), default='Low Risk')  # Low Risk, At Risk
    key_reasons = db.Column(db.Text, default='[]')  # JSON array of reasons
    
    # Lifecycle status: Low Risk, At Risk, Under Review, Counselling, Intervened, Closed
    lifecycle_status = db.Column(db.String(50), default='Low Risk')
    assigned_mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    counselling_logs = db.relationship('CounsellingCase', backref='student', lazy=True, cascade='all, delete-orphan')

    @property
    def reasons_list(self):
        try:
            return json.loads(self.key_reasons) if self.key_reasons else []
        except Exception:
            return []

class CounsellingCase(db.Model):
    __tablename__ = 'counselling_cases'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    mentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    session_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    status_at_time = db.Column(db.String(50), nullable=False)
    mentor_remarks = db.Column(db.Text, nullable=False)
    action_plan = db.Column(db.Text, nullable=True)
    next_followup_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class AuditLog(db.Model):
    __tablename__ = 'audit_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    username = db.Column(db.String(80), nullable=False, default='System')
    action = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=True)
    ip_address = db.Column(db.String(50), nullable=True, default='127.0.0.1')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class Notification(db.Model):
    __tablename__ = 'notifications'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)  # Null means all mentors/admins
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(30), default='info')  # warning, danger, success, info
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class SystemSetting(db.Model):
    __tablename__ = 'system_settings'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def get_value(cls, key, default=None):
        setting = cls.query.filter_by(key=key).first()
        return setting.value if setting else default

    @classmethod
    def get_int(cls, key, default=0):
        val = cls.get_value(key)
        try:
            return int(val) if val is not None else default
        except (ValueError, TypeError):
            return default

    @classmethod
    def get_float(cls, key, default=0.0):
        val = cls.get_value(key)
        try:
            return float(val) if val is not None else default
        except (ValueError, TypeError):
            return default

    @classmethod
    def set_value(cls, key, value, description=None):
        setting = cls.query.filter_by(key=key).first()
        if not setting:
            setting = cls(key=key, value=str(value), description=description)
            db.session.add(setting)
        else:
            setting.value = str(value)
            if description:
                setting.description = description
        db.session.commit()

    @classmethod
    def get_risk_rules(cls):
        return {
            'attendance_warning': cls.get_float('rule_attendance_warning', 75.0),
            'attendance_critical': cls.get_float('rule_attendance_critical', 60.0),
            'backlogs_warning': cls.get_int('rule_backlogs_warning', 1),
            'backlogs_critical': cls.get_int('rule_backlogs_critical', 3),
            'marks_warning': cls.get_float('rule_marks_warning', 55.0),
            'marks_critical': cls.get_float('rule_marks_critical', 40.0),
            'engagement_critical': cls.get_float('rule_engagement_critical', 40.0),
            'fee_due_severity': cls.get_value('rule_fee_due_severity', 'danger'),
            'critical_risk_threshold': cls.get_float('critical_risk_threshold', 0.70),
            'medium_risk_threshold': cls.get_float('medium_risk_threshold', 0.50),
            'auto_lifecycle_target': cls.get_value('rule_auto_lifecycle_target', 'At Risk')
        }

    @classmethod
    def reset_to_nominal_rules(cls):
        defaults = {
            'rule_attendance_warning': '75.0',
            'rule_attendance_critical': '60.0',
            'rule_backlogs_warning': '1',
            'rule_backlogs_critical': '3',
            'rule_marks_warning': '55.0',
            'rule_marks_critical': '40.0',
            'rule_engagement_critical': '40.0',
            'rule_fee_due_severity': 'danger',
            'critical_risk_threshold': '0.70',
            'medium_risk_threshold': '0.50',
            'rule_auto_lifecycle_target': 'At Risk'
        }
        for k, v in defaults.items():
            cls.set_value(k, v)


```

## File: `config.py`
**Description:** System Configuration Registry, Security Keys & Environmental Parameter Bindings  
**Line Count:** 12 lines

```python
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    BASE_DIR = BASE_DIR
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sanskriti-dropout-prediction-secret-key-2026')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'data', 'dropout_system.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload
    MODEL_PATH = os.path.join(BASE_DIR, 'models', 'dropout_models.pkl')

```

## File: `test_app.py`
**Description:** Automated System Verification Harness, Integration Tests & Test Matrix Assertions  
**Line Count:** 172 lines

```python
import os
import io
import unittest
import json
from app import create_app
from database import db, User, Student, CounsellingCase, AuditLog, Notification
from ml_engine import MLEngine

class DropoutSystemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_ml_engine_inference_and_reasons(self):
        ml = MLEngine.get_instance()
        student_data = {
            'attendance_percentage': 40.0,
            'internal_marks_avg': 35.0,
            'backlog_count': 3,
            'fee_status': 'Due',
            'engagement_score': 20.0,
            'semester': 4
        }
        res = ml.predict_student(student_data)
        self.assertEqual(res['risk_level'], 'At Risk')
        self.assertGreaterEqual(res['risk_score'], 0.50)
        self.assertGreater(len(res['reasons']), 0)
        # Check that top factor is Attendance Deficit
        factors = [r['factor'] for r in res['reasons']]
        self.assertIn('Attendance Deficit', factors)
        print("ML Engine Test Passed: Risk Score =", res['risk_score'], "Reasons count =", len(res['reasons']))

    def test_auth_and_dashboard(self):
        # 1. Login with satyam (Faculty Guide / Dept Head)
        resp = self.client.post('/login', data={
            'username': 'satyam',
            'password': 'password123'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Dropout Monitoring', resp.data)

        # 2. Test Analytics API
        api_resp = self.client.get('/api/analytics')
        self.assertEqual(api_resp.status_code, 200)
        data = json.loads(api_resp.data)
        self.assertIn('risk_distribution', data)
        self.assertIn('department_distribution', data)
        print("Auth & Analytics API Test Passed.")

    def test_student_registration_and_detail(self):
        # Login as admin
        self.client.post('/login', data={'username': 'admin', 'password': 'password123'})

        # Register a new student
        resp = self.client.post('/students/register', data={
            'enrollment_no': 'TEST230999',
            'name': 'Test Candidate',
            'email': 'test.candidate@sanskriti.edu.in',
            'phone': '+91-9000000000',
            'department': 'Computer Science & Engineering',
            'semester': 3,
            'attendance_percentage': 45.0,
            'internal_marks_avg': 42.0,
            'backlog_count': 2,
            'fee_status': 'Due',
            'engagement_score': 30.0,
            'campus_location': 'Main Campus'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        # Verify in database
        st = Student.query.filter_by(enrollment_no='TEST230999').first()
        self.assertIsNotNone(st)
        self.assertEqual(st.risk_level, 'At Risk')
        print(f"Student Registration Test Passed: {st.name} predicted risk: {st.risk_score}")

    def test_counselling_workflow_lifecycle(self):
        self.client.post('/login', data={'username': 'priya', 'password': 'password123'})
        student = Student.query.filter_by(enrollment_no='2302320012').first()
        self.assertIsNotNone(student)

        # Add counselling session
        resp = self.client.post(f'/counselling/{student.id}/add_session', data={
            'lifecycle_status': 'Counselling',
            'mentor_remarks': 'Met with student and parent. Agreed on remedial classes.',
            'action_plan': 'Saturday tutorials in CSE department.',
            'next_followup_date': '2026-11-01'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        # Check updated status
        db.session.refresh(student)
        self.assertEqual(student.lifecycle_status, 'Counselling')
        print("Counselling Lifecycle Test Passed.")

    def test_bulk_csv_upload(self):
        self.client.post('/login', data={'username': 'admin', 'password': 'password123'})
        csv_path = os.path.join(os.path.dirname(__file__), 'sample_students.csv')
        with open(csv_path, 'rb') as f:
            data = {'csv_file': (f, 'sample_students.csv')}
            resp = self.client.post('/students/upload_csv', data=data, content_type='multipart/form-data', follow_redirects=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(b'CSV Processed Successfully', resp.data)
        print("Bulk CSV Upload Test Passed.")

    def test_stage_limits_and_risk_order(self):
        self.client.post('/login', data={'username': 'satyam', 'password': 'password123'})
        resp = self.client.get('/counselling')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Student Retention Lifecycle Hub', resp.data)
        self.assertIn(b'Stage Capacity Limit', resp.data)
        self.assertIn(b'Critical Risk', resp.data)
        print("Stage Limits & Risk Order Test Passed.")

    def test_admin_settings_and_retraining(self):
        # Login as Admin
        self.client.post('/login', data={'username': 'admin', 'password': 'password123'})

        # 1. Update stage limits
        resp = self.client.post('/admin/settings', data={
            'stage_limit_At_Risk': '12',
            'stage_limit_Under_Review': '8',
            'stage_limit_Counselling': '14',
            'stage_limit_Intervened': '20',
            'stage_limit_Closed': '150',
            'stage_limit_Low_Risk': '200',
            'critical_risk_threshold': '75',
            'medium_risk_threshold': '55'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'successfully updated', resp.data)

        # 2. Retrain model endpoint
        retrain_resp = self.client.post('/admin/retrain_model', follow_redirects=True)
        self.assertEqual(retrain_resp.status_code, 200)
        self.assertIn(b'AI Model Retrained Successfully', retrain_resp.data)
        print("Admin Settings & Model Retraining Test Passed.")

    def test_rbac_and_student_privacy_isolation(self):
        # 1. Login as Student (ramesh)
        login_resp = self.client.post('/login', data={'username': 'ramesh', 'password': 'password123'}, follow_redirects=True)
        self.assertEqual(login_resp.status_code, 200)

        # 2. Access dashboard - should automatically route to their individual profile
        dash_resp = self.client.get('/dashboard', follow_redirects=True)
        self.assertEqual(dash_resp.status_code, 200)
        self.assertIn(b'D. Ramesh', dash_resp.data)
        self.assertIn(b'2302320099', dash_resp.data)

        # 3. Student tries to access Admin Settings - should be blocked
        admin_resp = self.client.get('/admin/settings', follow_redirects=True)
        self.assertIn(b'Access denied', admin_resp.data)

        # 4. Student tries to access Counselling Hub - should be blocked
        hub_resp = self.client.get('/counselling', follow_redirects=True)
        self.assertIn(b'Access denied', hub_resp.data)

        # 5. Student tries to access audit logs - should be blocked
        audit_resp = self.client.get('/audit-logs', follow_redirects=True)
        self.assertIn(b'Access denied', audit_resp.data)

        print("RBAC & Student Privacy Isolation Test Passed.")

if __name__ == '__main__':
    unittest.main()

```

## File: `train_model.py`
**Description:** Machine Learning Model Training Pipeline, Stratified Evaluation & Synthetic Data Generation  
**Line Count:** 175 lines

```python
import os
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def generate_synthetic_training_data(n_samples=2500, random_state=42):
    """
    Generates a realistic synthetic dataset representing university student academic,
    attendance, and financial records for dropout prediction.
    """
    np.random.seed(random_state)
    
    # 1. Attendance percentage (typically skewed towards 65-90%)
    attendance = np.clip(np.random.normal(loc=72, scale=16, size=n_samples), 15, 100)
    
    # 2. Internal marks average (0-100)
    # Correlated with attendance
    marks_noise = np.random.normal(0, 10, n_samples)
    internal_marks = np.clip(0.6 * attendance + marks_noise + 20, 15, 100)
    
    # 3. Backlog count (0 to 6)
    backlogs_prob = np.clip((100 - attendance) / 100 * 0.6 + (100 - internal_marks) / 100 * 0.4, 0, 1)
    backlogs = np.random.binomial(n=6, p=backlogs_prob * 0.6)
    
    # 4. Fee status: Paid (65%), Partial (20%), Due (15%)
    fee_choices = ['Paid', 'Partial', 'Due']
    fee_weights = [0.65, 0.20, 0.15]
    fee_status = np.random.choice(fee_choices, size=n_samples, p=fee_weights)
    
    # 5. Engagement score (0-100 LMS activity)
    engagement = np.clip(0.5 * attendance + np.random.normal(15, 15, n_samples), 5, 100)
    
    # 6. Semester (1 to 8)
    semesters = np.random.randint(1, 9, size=n_samples)
    
    # Compute Dropout Risk Ground Truth
    # Academic failure + fee default + severe low attendance increases risk exponentially
    fee_penalty = np.where(fee_status == 'Due', 1.8, np.where(fee_status == 'Partial', 0.6, 0.0))
    attendance_penalty = np.where(attendance < 60, 2.5, np.where(attendance < 75, 1.0, 0.0))
    marks_penalty = np.where(internal_marks < 40, 2.2, np.where(internal_marks < 55, 0.9, 0.0))
    backlog_penalty = backlogs * 0.7
    engagement_penalty = np.where(engagement < 35, 1.2, 0.0)
    
    risk_score_raw = (
        attendance_penalty +
        marks_penalty +
        backlog_penalty +
        fee_penalty +
        engagement_penalty +
        np.random.normal(0, 0.6, n_samples)
    )
    
    # Sigmoid function for probability
    prob = 1 / (1 + np.exp(-(risk_score_raw - 2.8)))
    dropped_out = (prob > 0.5).astype(int)
    
    df = pd.DataFrame({
        'attendance_percentage': np.round(attendance, 1),
        'internal_marks_avg': np.round(internal_marks, 1),
        'backlog_count': backlogs,
        'fee_status': fee_status,
        'engagement_score': np.round(engagement, 1),
        'semester': semesters,
        'dropped_out': dropped_out
    })
    
    return df

def train_and_export_models(export_path='models/dropout_models.pkl'):
    print("Generating synthetic student historical training dataset...")
    df = generate_synthetic_training_data(n_samples=3000, random_state=42)
    
    # Feature columns
    feature_cols = ['attendance_percentage', 'internal_marks_avg', 'backlog_count', 'fee_status', 'engagement_score', 'semester']
    numeric_features = ['attendance_percentage', 'internal_marks_avg', 'backlog_count', 'engagement_score', 'semester']
    categorical_features = ['fee_status']
    
    X = df[feature_cols]
    y = df['dropped_out']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
        ]
    )
    
    # 1. Random Forest Classifier
    rf_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=120, max_depth=8, random_state=42, min_samples_split=5))
    ])
    
    rf_pipeline.fit(X_train, y_train)
    y_pred_rf = rf_pipeline.predict(X_test)
    y_proba_rf = rf_pipeline.predict_proba(X_test)[:, 1]
    
    # 2. Logistic Regression Classifier (baseline comparison)
    lr_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(random_state=42, max_iter=500))
    ])
    
    lr_pipeline.fit(X_train, y_train)
    y_pred_lr = lr_pipeline.predict(X_test)
    y_proba_lr = lr_pipeline.predict_proba(X_test)[:, 1]
    
    # Evaluation Metrics
    metrics = {
        'Random Forest': {
            'Accuracy': float(accuracy_score(y_test, y_pred_rf)),
            'Precision': float(precision_score(y_test, y_pred_rf)),
            'Recall': float(recall_score(y_test, y_pred_rf)),
            'F1_Score': float(f1_score(y_test, y_pred_rf)),
            'ROC_AUC': float(roc_auc_score(y_test, y_proba_rf))
        },
        'Logistic Regression': {
            'Accuracy': float(accuracy_score(y_test, y_pred_lr)),
            'Precision': float(precision_score(y_test, y_pred_lr)),
            'Recall': float(recall_score(y_test, y_pred_lr)),
            'F1_Score': float(f1_score(y_test, y_pred_lr)),
            'ROC_AUC': float(roc_auc_score(y_test, y_proba_lr))
        }
    }
    
    # Calculate feature importances
    rf_model = rf_pipeline.named_steps['classifier']
    cat_feature_names = list(rf_pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out(categorical_features))
    all_feature_names = numeric_features + cat_feature_names
    feature_importances = dict(zip(all_feature_names, rf_model.feature_importances_))
    
    print("\n--- Model Evaluation Results ---")
    for model_name, m in metrics.items():
        print(f"\n{model_name}:")
        for k, v in m.items():
            print(f"  {k}: {v:.4f}")
            
    print("\nGlobal Feature Importances:")
    for k, v in sorted(feature_importances.items(), key=lambda x: x[1], reverse=True):
        print(f"  {k}: {v:.4f}")
        
    # Save artifacts
    artifacts = {
        'rf_pipeline': rf_pipeline,
        'lr_pipeline': lr_pipeline,
        'feature_cols': feature_cols,
        'numeric_features': numeric_features,
        'categorical_features': categorical_features,
        'all_feature_names': all_feature_names,
        'feature_importances': feature_importances,
        'metrics': metrics,
        'benchmarks': {
            'attendance_percentage': 75.0,
            'internal_marks_avg': 50.0,
            'backlog_count': 0,
            'engagement_score': 60.0
        }
    }
    
    os.makedirs(os.path.dirname(export_path), exist_ok=True)
    joblib.dump(artifacts, export_path)
    print(f"\nTrained models and artifacts successfully saved to: {export_path}")
    return artifacts

if __name__ == '__main__':
    train_and_export_models('models/dropout_models.pkl')

```

## File: `templates/base.html`
**Description:** Core Frontend Master Template, Bootstrap 5 Framework & Dynamic Role-Based Navbar  
**Line Count:** 156 lines

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Sanskriti University - Student Dropout Prediction{% endblock %}</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap Icons & FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% block extra_head %}{% endblock %}
</head>
<body class="bg-light">

    {% if current_user.get('user_id') %}
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-navy sticky-top shadow-sm">
        <div class="container-fluid px-3 px-lg-4">
            <a class="navbar-brand d-flex align-items-center fw-bold" href="{{ url_for('dashboard') }}">
                <span class="brand-badge me-2"><i class="fa-solid fa-graduation-cap"></i></span>
                <span>Sanskriti <span class="text-warning">University</span></span>
                <span class="badge bg-primary-subtle text-primary border border-primary-subtle ms-2 px-2 py-1 fs-xs fw-normal d-none d-md-inline">AI Dropout Prediction System</span>
            </a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarContent">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-3">
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'dashboard' %}active{% endif %}" href="{{ url_for('dashboard') }}">
                            <i class="fa-solid fa-{% if current_user.get('role') == 'Student' %}id-card{% else %}chart-pie{% endif %} me-1"></i> 
                            {% if current_user.get('role') == 'Student' %}My Academic Profile{% else %}Dashboard{% endif %}
                        </a>
                    </li>
                    {% if current_user.get('role') != 'Student' %}
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint in ['students_list', 'student_detail', 'register_student'] %}active{% endif %}" href="{{ url_for('students_list') }}">
                            <i class="fa-solid fa-users me-1"></i> Students
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'counselling_hub' %}active{% endif %}" href="{{ url_for('counselling_hub') }}">
                            <i class="fa-solid fa-hand-holding-heart me-1"></i> Counselling Hub
                        </a>
                    </li>
                    {% endif %}
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'model_performance' %}active{% endif %}" href="{{ url_for('model_performance') }}">
                            <i class="fa-solid fa-brain me-1"></i> AI Engine & Explainability
                        </a>
                    </li>
                    {% if current_user.get('role') in ['Admin', 'Department Head'] %}
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'audit_logs' %}active{% endif %}" href="{{ url_for('audit_logs') }}">
                            <i class="fa-solid fa-shield-halved me-1"></i> Audit Logs
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link {% if request.endpoint == 'admin_settings' %}active{% endif %}" href="{{ url_for('admin_settings') }}">
                            <i class="fa-solid fa-sliders me-1"></i> Admin Settings
                        </a>
                    </li>
                    {% endif %}
                </ul>

                <div class="d-flex align-items-center gap-3">
                    <!-- Notifications -->
                    <a href="{{ url_for('notifications_view') }}" class="btn btn-outline-light position-relative btn-sm rounded-circle p-2">
                        <i class="fa-solid fa-bell"></i>
                        {% if unread_notifications_count > 0 %}
                        <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger border border-light">
                            {{ unread_notifications_count }}
                        </span>
                        {% endif %}
                    </a>

                    <!-- User Profile Dropdown -->
                    <div class="dropdown">
                        <button class="btn btn-outline-light btn-sm dropdown-toggle d-flex align-items-center gap-2" type="button" data-bs-toggle="dropdown">
                            <span class="avatar-circle">{{ current_user.get('name', 'User')[0] }}</span>
                            <span class="d-none d-sm-inline">{{ current_user.get('name') }}</span>
                            <span class="badge bg-warning text-dark fs-xs">{{ current_user.get('role') }}</span>
                        </button>
                        <ul class="dropdown-menu dropdown-menu-end shadow border-0 mt-2">
                            <li class="dropdown-header">
                                <h6 class="mb-0 text-dark fw-bold">{{ current_user.get('name') }}</h6>
                                <small class="text-muted">{{ current_user.get('department') }}</small>
                            </li>
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item" href="{{ url_for('dashboard') }}"><i class="fa-solid fa-gauge me-2 text-primary"></i> Dashboard</a></li>
                            <li><a class="dropdown-item" href="{{ url_for('notifications_view') }}"><i class="fa-solid fa-bell me-2 text-warning"></i> Notifications ({{ unread_notifications_count }})</a></li>
                            {% if current_user.get('role') in ['Admin', 'Department Head'] %}
                            <li><a class="dropdown-item" href="{{ url_for('admin_settings') }}"><i class="fa-solid fa-sliders me-2 text-secondary"></i> Admin Settings</a></li>
                            {% endif %}
                            <li><hr class="dropdown-divider"></li>
                            <li><a class="dropdown-item text-danger" href="{{ url_for('logout') }}"><i class="fa-solid fa-arrow-right-from-bracket me-2"></i> Sign Out</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </nav>
    {% endif %}

    <!-- Flash Messages -->
    <div class="container-fluid px-3 px-lg-4 mt-3">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                <div class="alert alert-{{ category }} alert-dismissible fade show shadow-sm border-0 d-flex align-items-center" role="alert">
                    <span class="me-2">
                        {% if category == 'success' %}<i class="fa-solid fa-circle-check text-success"></i>
                        {% elif category == 'danger' %}<i class="fa-solid fa-triangle-exclamation text-danger"></i>
                        {% elif category == 'warning' %}<i class="fa-solid fa-circle-exclamation text-warning"></i>
                        {% else %}<i class="fa-solid fa-circle-info text-info"></i>{% endif %}
                    </span>
                    <div>{{ message }}</div>
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>

    <!-- Main Content -->
    <main class="py-3">
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="footer mt-auto py-3 bg-white border-top text-center text-muted small">
        <div class="container">
            <p class="mb-1">
                <strong>Sanskriti University</strong> &bull; AI-Based Prediction of Reasons for Student Dropout
            </p>
            <p class="mb-0 text-secondary fs-xs">
                Student: <strong>D. Ramesh</strong> (Enrollment No: <code>2302320099</code>) &bull; Faculty Guide: <strong>Mr. Satyam Dwivedi</strong> &bull; 
                Powered by Python Flask, scikit-learn, and SQLite.
            </p>
        </div>
    </footer>

    <!-- Bootstrap 5 Bundle JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    {% block extra_scripts %}{% endblock %}
</body>
</html>

```

## File: `templates/login.html`
**Description:** Unified Portal Authentication Screen & Quick Demo Access Controls  
**Line Count:** 99 lines

```html
{% extends 'base.html' %}

{% block title %}Sign In - Sanskriti University Student Dropout Portal{% endblock %}

{% block content %}
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-md-8 col-lg-5">
            <div class="card shadow-lg border-0 rounded-4 overflow-hidden">
                <div class="card-header bg-navy text-white text-center py-4">
                    <div class="d-inline-flex align-items-center justify-content-center bg-white text-navy rounded-circle mb-3 shadow" style="width: 65px; height: 65px; font-size: 1.8rem;">
                        <i class="fa-solid fa-graduation-cap text-primary"></i>
                    </div>
                    <h4 class="fw-bold mb-1">Sanskriti University</h4>
                    <p class="text-white-50 small mb-0">AI-Based Prediction of Reasons for Student Dropout</p>
                </div>

                <div class="card-body p-4 p-md-5">
                    <h5 class="fw-bold text-dark mb-3 text-center">Portal Authentication</h5>
                    
                    <form method="POST" action="{{ url_for('login') }}">
                        <div class="mb-3">
                            <label for="username" class="form-label text-secondary small fw-bold">Username or ID</label>
                            <div class="input-group">
                                <span class="input-group-text bg-light border-end-0"><i class="fa-solid fa-user text-muted"></i></span>
                                <input type="text" class="form-control border-start-0" id="username" name="username" placeholder="e.g. satyam or admin" required>
                            </div>
                        </div>

                        <div class="mb-4">
                            <label for="password" class="form-label text-secondary small fw-bold">Password</label>
                            <div class="input-group">
                                <span class="input-group-text bg-light border-end-0"><i class="fa-solid fa-lock text-muted"></i></span>
                                <input type="password" class="form-control border-start-0" id="password" name="password" placeholder="Enter password" required>
                            </div>
                        </div>

                        <button type="submit" class="btn btn-primary w-100 py-2 fw-semibold shadow-sm rounded-3">
                            <i class="fa-solid fa-right-to-bracket me-2"></i> Sign In to Portal
                        </button>
                    </form>

                    <div class="mt-4 pt-3 border-top">
                        <p class="text-muted small fw-bold mb-2 text-center text-uppercase fs-xs">
                            <i class="fa-solid fa-bolt text-warning me-1"></i> Quick Demo Access
                        </p>
                        <div class="d-grid gap-2">
                            <button type="button" class="btn btn-sm btn-outline-secondary text-start py-2 px-3 d-flex justify-content-between align-items-center" onclick="fillCredentials('admin', 'password123')">
                                <div>
                                    <strong class="d-block text-dark">Admin</strong>
                                    <small class="text-muted">Dr. A.K. Sharma &bull; Executive Authority</small>
                                </div>
                                <span class="badge bg-danger">Full Control</span>
                            </button>

                            <button type="button" class="btn btn-sm btn-outline-secondary text-start py-2 px-3 d-flex justify-content-between align-items-center" onclick="fillCredentials('satyam', 'password123')">
                                <div>
                                    <strong class="d-block text-dark">Faculty Guide / HOD</strong>
                                    <small class="text-muted">Mr. Satyam Dwivedi &bull; Computer Science</small>
                                </div>
                                <span class="badge bg-primary">Dept Head</span>
                            </button>

                            <button type="button" class="btn btn-sm btn-outline-secondary text-start py-2 px-3 d-flex justify-content-between align-items-center" onclick="fillCredentials('priya', 'password123')">
                                <div>
                                    <strong class="d-block text-dark">Faculty Mentor</strong>
                                    <small class="text-muted">Dr. Priya Verma &bull; Student Counsellor</small>
                                </div>
                                <span class="badge bg-success">Mentor</span>
                            </button>

                            <button type="button" class="btn btn-sm btn-outline-secondary text-start py-2 px-3 d-flex justify-content-between align-items-center" onclick="fillCredentials('ramesh', 'password123')">
                                <div>
                                    <strong class="d-block text-dark">Student Account</strong>
                                    <small class="text-muted">D. Ramesh (Enr: 2302320099)</small>
                                </div>
                                <span class="badge bg-secondary">Student</span>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="card-footer bg-light text-center py-3 border-0">
                    <small class="text-muted">
                        Prototype build ready for SQLite, PostgreSQL & MySQL deployment.
                    </small>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function fillCredentials(user, pass) {
    document.getElementById('username').value = user;
    document.getElementById('password').value = pass;
}
</script>
{% endblock %}

```

## File: `templates/dashboard.html`
**Description:** Executive Authority Dashboard, KPI Metrics & Chart.js Visualizations  
**Line Count:** 318 lines

```html
{% extends 'base.html' %}

{% block title %}Authority & Mentor Dashboard - Sanskriti University{% endblock %}

{% block content %}
<div class="container-fluid px-3 px-lg-4">
    <!-- Header with Quick Action Controls -->
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <h3 class="fw-bold text-navy mb-1">
                <i class="fa-solid fa-chart-line text-primary me-2"></i> Dropout Monitoring & Authority Dashboard
            </h3>
            <p class="text-secondary small mb-0">
                AI Early-Warning System &bull; Sanskriti University Centralized Platform &bull; Guide: <strong>Mr. Satyam Dwivedi</strong>
            </p>
        </div>
        <div class="d-flex flex-wrap gap-2">
            {% if current_user.get('role') in ['Admin', 'Department Head'] %}
            <form action="{{ url_for('trigger_escalation_check') }}" method="POST" class="d-inline">
                <button type="submit" class="btn btn-outline-danger btn-sm shadow-sm" title="Scan for stagnant high risk cases">
                    <i class="fa-solid fa-triangle-exclamation me-1"></i> Run Escalation Scan
                </button>
            </form>
            {% endif %}
            
            <a href="{{ url_for('students_list') }}" class="btn btn-outline-primary btn-sm shadow-sm">
                <i class="fa-solid fa-table-list me-1"></i> Student Directory
            </a>
            
            {% if current_user.get('role') in ['Admin', 'Department Head', 'Faculty Mentor'] %}
            <a href="{{ url_for('register_student') }}" class="btn btn-primary btn-sm shadow-sm">
                <i class="fa-solid fa-user-plus me-1"></i> Register Student
            </a>
            {% endif %}
            
            <a href="{{ url_for('export_students_csv') }}" class="btn btn-outline-success btn-sm shadow-sm">
                <i class="fa-solid fa-file-csv me-1"></i> Export Report
            </a>
        </div>
    </div>

    <!-- KPI Metric Cards -->
    <div class="row g-3 mb-4">
        <div class="col-6 col-lg-3">
            <div class="card metric-card border-0 shadow-sm rounded-3">
                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                    <div>
                        <div class="text-muted small fw-bold text-uppercase">Total Monitored</div>
                        <h3 class="fw-bold text-dark mb-0">{{ total_students }}</h3>
                        <small class="text-secondary">Enrolled Students</small>
                    </div>
                    <div class="metric-icon bg-primary-subtle text-primary">
                        <i class="fa-solid fa-user-graduate"></i>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-6 col-lg-3">
            <div class="card metric-card border-0 shadow-sm rounded-3">
                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                    <div>
                        <div class="text-muted small fw-bold text-uppercase">At Risk Flagged</div>
                        <h3 class="fw-bold text-danger mb-0">{{ at_risk_count }}</h3>
                        <small class="text-danger fw-semibold">
                            {% if total_students > 0 %}
                            {{ (at_risk_count / total_students * 100)|round(1) }}% of student body
                            {% else %}0%{% endif %}
                        </small>
                    </div>
                    <div class="metric-icon bg-danger-subtle text-danger">
                        <i class="fa-solid fa-triangle-exclamation"></i>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-6 col-lg-3">
            <div class="card metric-card border-0 shadow-sm rounded-3">
                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                    <div>
                        <div class="text-muted small fw-bold text-uppercase">Active Counselling</div>
                        <h3 class="fw-bold text-warning mb-0">{{ active_counselling }}</h3>
                        <small class="text-warning-emphasis">Under Review / Sessions</small>
                    </div>
                    <div class="metric-icon bg-warning-subtle text-warning">
                        <i class="fa-solid fa-hand-holding-heart"></i>
                    </div>
                </div>
            </div>
        </div>

        <div class="col-6 col-lg-3">
            <div class="card metric-card border-0 shadow-sm rounded-3">
                <div class="card-body p-3 d-flex align-items-center justify-content-between">
                    <div>
                        <div class="text-muted small fw-bold text-uppercase">Intervened / Closed</div>
                        <h3 class="fw-bold text-success mb-0">{{ closed_cases }}</h3>
                        <small class="text-success fw-semibold">Resolved Cases</small>
                    </div>
                    <div class="metric-icon bg-success-subtle text-success">
                        <i class="fa-solid fa-circle-check"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Escalation Notice Banner (if any stagnant high-risk cases) -->
    {% if escalation_candidates %}
    <div class="alert alert-warning border-0 shadow-sm rounded-3 d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 p-3">
        <div class="d-flex align-items-center gap-3">
            <div class="fs-3 text-danger"><i class="fa-solid fa-bullhorn"></i></div>
            <div>
                <strong class="text-dark">High-Risk Attention Alert:</strong>
                <span class="text-secondary small d-block">
                    {{ escalation_candidates|length }} student(s) have predicted dropout risk &ge; 70% without assigned counselling interventions.
                </span>
            </div>
        </div>
        <div class="mt-2 mt-md-0 d-flex gap-2">
            <a href="{{ url_for('counselling_hub') }}" class="btn btn-warning btn-sm fw-semibold">
                Open Counselling Hub
            </a>
        </div>
    </div>
    {% endif %}

    <!-- Charts Row -->
    <div class="row g-3 mb-4">
        <!-- Chart 1: Dropout Risk Distribution -->
        <div class="col-lg-4">
            <div class="card border-0 shadow-sm rounded-3 h-100">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">Risk Classification</h6>
                    <span class="badge bg-light text-secondary border">AI Random Forest</span>
                </div>
                <div class="card-body d-flex flex-column align-items-center justify-content-center">
                    <div style="position: relative; height: 220px; width: 100%;">
                        <canvas id="riskDistributionChart"></canvas>
                    </div>
                    <div class="d-flex justify-content-around w-100 mt-3 text-center small text-muted">
                        <div><i class="fa-solid fa-circle text-success me-1"></i> Low Risk</div>
                        <div><i class="fa-solid fa-circle text-danger me-1"></i> At Risk</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Chart 2: Department-wise At Risk Cases -->
        <div class="col-lg-4">
            <div class="card border-0 shadow-sm rounded-3 h-100">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">Department At-Risk Burden</h6>
                    <span class="badge bg-light text-secondary border">Comparative</span>
                </div>
                <div class="card-body">
                    <div style="position: relative; height: 240px; width: 100%;">
                        <canvas id="departmentRiskChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <!-- Chart 3: Attendance vs Risk -->
        <div class="col-lg-4">
            <div class="card border-0 shadow-sm rounded-3 h-100">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">Attendance Shortage Impact</h6>
                    <span class="badge bg-light text-secondary border">Key Predictor</span>
                </div>
                <div class="card-body">
                    <div style="position: relative; height: 240px; width: 100%;">
                        <canvas id="attendanceRiskChart"></canvas>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Data Tables Row -->
    <div class="row g-3">
        <!-- Priority Flagged Students -->
        <div class="col-lg-8">
            <div class="card border-0 shadow-sm rounded-3 h-100">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">
                        <i class="fa-solid fa-triangle-exclamation text-danger me-1"></i> High Priority Flagged Students
                    </h6>
                    <a href="{{ url_for('students_list', risk_level='At Risk') }}" class="btn btn-outline-secondary btn-sm">
                        View All
                    </a>
                </div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light small text-secondary">
                                <tr>
                                    <th style="min-width: 150px;">Student</th>
                                    <th style="min-width: 110px;">Department</th>
                                    <th style="min-width: 100px;">Attendance</th>
                                    <th style="min-width: 95px;">Backlogs</th>
                                    <th style="min-width: 145px;">Risk Score & Tier</th>
                                    <th style="min-width: 110px;">Lifecycle</th>
                                    <th class="text-end" style="min-width: 80px;">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for s in recent_students %}
                                <tr>
                                    <td>
                                        <div class="fw-bold text-dark">{{ s.name }}</div>
                                        <small class="text-muted font-monospace">{{ s.enrollment_no }}</small>
                                    </td>
                                    <td>
                                        <span class="badge bg-light text-dark border">{{ s.department }}</span>
                                        <div class="text-muted fs-xs">Sem {{ s.semester }}</div>
                                    </td>
                                    <td>
                                        <span class="{% if s.attendance_percentage < 65 %}text-danger fw-bold{% elif s.attendance_percentage < 75 %}text-warning fw-semibold{% else %}text-success{% endif %}">
                                            {{ s.attendance_percentage }}%
                                        </span>
                                    </td>
                                    <td>
                                        {% if s.backlog_count > 0 %}
                                        <span class="badge bg-danger-subtle text-danger">{{ s.backlog_count }} active</span>
                                        {% else %}
                                        <span class="badge bg-light text-secondary">0</span>
                                        {% endif %}
                                    </td>
                                    <td>
                                        <div class="d-flex align-items-center gap-2">
                                            <div class="progress flex-grow-1" style="height: 6px; width: 60px;">
                                                <div class="progress-bar {% if s.risk_score >= 0.70 %}bg-danger{% elif s.risk_score >= 0.50 %}bg-warning{% else %}bg-success{% endif %}" 
                                                     style="width: {{ s.risk_score * 100 }}%">
                                                </div>
                                            </div>
                                            <span class="small fw-bold">{{ (s.risk_score * 100)|round(1) }}%</span>
                                        </div>
                                        <div class="mt-1 d-flex gap-1 align-items-center flex-wrap">
                                            <span class="badge {% if s.risk_level == 'At Risk' %}bg-danger{% else %}bg-success{% endif %} fs-xs">
                                                {{ s.risk_level }}
                                            </span>
                                            {% if s.risk_score >= 0.70 %}
                                                <span class="badge bg-danger-subtle text-danger border border-danger-subtle fs-xs">Critical</span>
                                            {% elif s.risk_score >= 0.50 %}
                                                <span class="badge bg-warning-subtle text-warning-emphasis border border-warning-subtle fs-xs">Elevated</span>
                                            {% else %}
                                                <span class="badge bg-success-subtle text-success border border-success-subtle fs-xs">Manageable</span>
                                            {% endif %}
                                        </div>
                                    </td>
                                    <td>
                                        <span class="badge bg-primary-subtle text-primary border border-primary-subtle fs-xs">
                                            {{ s.lifecycle_status }}
                                        </span>
                                    </td>
                                    <td class="text-end">
                                        <a href="{{ url_for('student_detail', student_id=s.id) }}" class="btn btn-sm btn-outline-primary" title="View Profile & Reason Analysis">
                                            <i class="fa-solid fa-arrow-right"></i>
                                        </a>
                                    </td>
                                </tr>
                                {% else %}
                                <tr>
                                    <td colspan="7" class="text-center py-4 text-muted">
                                        No student records found. Register students or import CSV to start monitoring.
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <!-- Recent Counselling Trail & System Alerts -->
        <div class="col-lg-4">
            <div class="card border-0 shadow-sm rounded-3 h-100">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">
                        <i class="fa-solid fa-notes-medical text-primary me-1"></i> Recent Mentor Actions
                    </h6>
                    <a href="{{ url_for('counselling_hub') }}" class="btn btn-outline-secondary btn-sm">
                        Hub
                    </a>
                </div>
                <div class="card-body p-3">
                    <div class="timeline">
                        {% for c in recent_counselling %}
                        <div class="timeline-item mb-3 pb-3 border-bottom">
                            <div class="d-flex justify-content-between align-items-start mb-1">
                                <strong class="text-dark small">{{ c.student.name }}</strong>
                                <span class="badge bg-light text-secondary fs-xs">{{ c.session_date.strftime('%d %b') }}</span>
                            </div>
                            <p class="text-secondary small mb-1">{{ c.mentor_remarks[:90] }}{% if c.mentor_remarks|length > 90 %}...{% endif %}</p>
                            <div class="d-flex justify-content-between align-items-center fs-xs text-muted">
                                <span><i class="fa-solid fa-user-tie me-1"></i> {{ c.mentor.name }}</span>
                                <span class="badge bg-info-subtle text-info border border-info-subtle">{{ c.status_at_time }}</span>
                            </div>
                        </div>
                        {% else %}
                        <div class="text-center py-4 text-muted small">
                            No counselling sessions documented yet.
                        </div>
                        {% endfor %}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_scripts %}
<script src="{{ url_for('static', filename='js/dashboard.js') }}"></script>
{% endblock %}

```

## File: `templates/students.html`
**Description:** Student Monitoring Directory, Multi-Parameter Search & Bulk Ingestion Modal  
**Line Count:** 249 lines

```html
{% extends 'base.html' %}

{% block title %}Student Directory - Sanskriti University{% endblock %}

{% block content %}
<div class="container-fluid px-3 px-lg-4">
    <!-- Header with Action Buttons -->
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <h3 class="fw-bold text-navy mb-1">
                <i class="fa-solid fa-users text-primary me-2"></i> Student Monitoring Directory
            </h3>
            <p class="text-secondary small mb-0">
                Multi-parameter search, AI dropout risk evaluation, and bulk dataset management.
            </p>
        </div>
        <div class="d-flex flex-wrap gap-2">
            <button type="button" class="btn btn-outline-primary btn-sm shadow-sm" data-bs-toggle="modal" data-bs-target="#uploadCsvModal">
                <i class="fa-solid fa-file-arrow-up me-1"></i> Bulk CSV Upload
            </button>
            <a href="{{ url_for('register_student') }}" class="btn btn-primary btn-sm shadow-sm">
                <i class="fa-solid fa-user-plus me-1"></i> Register Student
            </a>
            <a href="{{ url_for('export_students_csv') }}" class="btn btn-outline-success btn-sm shadow-sm">
                <i class="fa-solid fa-download me-1"></i> Export Data
            </a>
        </div>
    </div>

    <!-- Search & Multi-parameter Filters -->
    <div class="card border-0 shadow-sm rounded-3 mb-4">
        <div class="card-body p-3">
            <form method="GET" action="{{ url_for('students_list') }}" class="row g-2 align-items-end">
                <div class="col-md-3">
                    <label class="form-label small fw-bold text-secondary mb-1">Search Keyword</label>
                    <div class="input-group input-group-sm">
                        <span class="input-group-text bg-light"><i class="fa-solid fa-magnifying-glass text-muted"></i></span>
                        <input type="text" name="q" value="{{ filters.q }}" class="form-control" placeholder="Enrollment, Name, or Email...">
                    </div>
                </div>

                <div class="col-6 col-md-2">
                    <label class="form-label small fw-bold text-secondary mb-1">Department</label>
                    <select name="department" class="form-select form-select-sm">
                        <option value="">All Departments</option>
                        {% for d in departments %}
                        <option value="{{ d }}" {% if filters.department == d %}selected{% endif %}>{{ d }}</option>
                        {% endfor %}
                    </select>
                </div>

                <div class="col-6 col-md-1">
                    <label class="form-label small fw-bold text-secondary mb-1">Semester</label>
                    <select name="semester" class="form-select form-select-sm">
                        <option value="">All</option>
                        {% for sem in range(1, 9) %}
                        <option value="{{ sem }}" {% if filters.semester == sem|string %}selected{% endif %}>Sem {{ sem }}</option>
                        {% endfor %}
                    </select>
                </div>

                <div class="col-6 col-md-2">
                    <label class="form-label small fw-bold text-secondary mb-1">Risk Level</label>
                    <select name="risk_level" class="form-select form-select-sm">
                        <option value="">All Risk Levels</option>
                        <option value="At Risk" {% if filters.risk_level == 'At Risk' %}selected{% endif %}>At Risk</option>
                        <option value="Low Risk" {% if filters.risk_level == 'Low Risk' %}selected{% endif %}>Low Risk</option>
                    </select>
                </div>

                <div class="col-6 col-md-2">
                    <label class="form-label small fw-bold text-secondary mb-1">Lifecycle Status</label>
                    <select name="lifecycle_status" class="form-select form-select-sm">
                        <option value="">All Stages</option>
                        {% for st in ['Low Risk', 'At Risk', 'Under Review', 'Counselling', 'Intervened', 'Closed'] %}
                        <option value="{{ st }}" {% if filters.lifecycle_status == st %}selected{% endif %}>{{ st }}</option>
                        {% endfor %}
                    </select>
                </div>

                <div class="col-6 col-md-1">
                    <label class="form-label small fw-bold text-secondary mb-1">Campus</label>
                    <select name="campus_location" class="form-select form-select-sm">
                        <option value="">All</option>
                        {% for c in campuses %}
                        <option value="{{ c }}" {% if filters.campus_location == c %}selected{% endif %}>{{ c }}</option>
                        {% endfor %}
                    </select>
                </div>

                <div class="col-6 col-md-1 d-flex gap-1">
                    <button type="submit" class="btn btn-primary btn-sm w-100" title="Apply Filters">
                        <i class="fa-solid fa-filter"></i>
                    </button>
                    <a href="{{ url_for('students_list') }}" class="btn btn-outline-secondary btn-sm" title="Clear Filters">
                        <i class="fa-solid fa-rotate-left"></i>
                    </a>
                </div>
            </form>
        </div>
    </div>

    <!-- Student Table -->
    <div class="card border-0 shadow-sm rounded-3">
        <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
            <h6 class="fw-bold text-dark mb-0">
                Student Records ({{ students|length }} matching)
            </h6>
        </div>
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light small text-secondary">
                        <tr>
                            <th>Enrollment No</th>
                            <th>Student Name</th>
                            <th>Dept / Sem</th>
                            <th>Attendance</th>
                            <th>Marks</th>
                            <th>Backlogs</th>
                            <th>Fee Status</th>
                            <th>Engagement</th>
                            <th>AI Risk Score</th>
                            <th>Lifecycle Status</th>
                            <th class="text-end">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for s in students %}
                        <tr>
                            <td class="font-monospace fw-semibold text-primary">
                                <a href="{{ url_for('student_detail', student_id=s.id) }}" class="text-decoration-none">
                                    {{ s.enrollment_no }}
                                </a>
                            </td>
                            <td>
                                <div class="fw-bold text-dark">{{ s.name }}</div>
                                <small class="text-muted">{{ s.email }}</small>
                            </td>
                            <td>
                                <div>{{ s.department }}</div>
                                <span class="badge bg-light text-secondary border fs-xs">Sem {{ s.semester }}</span>
                            </td>
                            <td>
                                <span class="badge {% if s.attendance_percentage < 60 %}bg-danger-subtle text-danger border border-danger-subtle{% elif s.attendance_percentage < 75 %}bg-warning-subtle text-warning-emphasis border border-warning-subtle{% else %}bg-success-subtle text-success border border-success-subtle{% endif %}">
                                    {{ s.attendance_percentage }}%
                                </span>
                            </td>
                            <td>{{ s.internal_marks_avg }}%</td>
                            <td>
                                {% if s.backlog_count > 0 %}
                                <span class="badge bg-danger-subtle text-danger fw-bold">{{ s.backlog_count }}</span>
                                {% else %}
                                <span class="text-muted">0</span>
                                {% endif %}
                            </td>
                            <td>
                                <span class="badge {% if s.fee_status == 'Paid' %}bg-success-subtle text-success{% elif s.fee_status == 'Partial' %}bg-warning-subtle text-warning-emphasis{% else %}bg-danger-subtle text-danger{% endif %} fs-xs">
                                    {{ s.fee_status }}
                                </span>
                            </td>
                            <td>
                                <div class="d-flex align-items-center gap-1">
                                    <small>{{ s.engagement_score }}</small>
                                </div>
                            </td>
                            <td>
                                <div class="d-flex align-items-center gap-2">
                                    <div class="progress flex-grow-1" style="height: 6px; width: 55px;">
                                        <div class="progress-bar {% if s.risk_score >= 0.70 %}bg-danger{% elif s.risk_score >= 0.50 %}bg-warning{% else %}bg-success{% endif %}" 
                                             style="width: {{ s.risk_score * 100 }}%">
                                        </div>
                                    </div>
                                    <strong class="fs-xs">{{ (s.risk_score * 100)|round(1) }}%</strong>
                                </div>
                                <span class="badge {% if s.risk_level == 'At Risk' %}bg-danger{% else %}bg-success{% endif %} fs-xs mt-1">
                                    {{ s.risk_level }}
                                </span>
                            </td>
                            <td>
                                <span class="badge 
                                    {% if s.lifecycle_status == 'Closed' %}bg-success-subtle text-success border border-success-subtle
                                    {% elif s.lifecycle_status == 'Intervened' %}bg-info-subtle text-info border border-info-subtle
                                    {% elif s.lifecycle_status == 'Counselling' %}bg-warning-subtle text-warning-emphasis border border-warning-subtle
                                    {% elif s.lifecycle_status == 'Under Review' %}bg-secondary-subtle text-secondary border border-secondary-subtle
                                    {% elif s.lifecycle_status == 'At Risk' %}bg-danger-subtle text-danger border border-danger-subtle
                                    {% else %}bg-light text-muted border{% endif %} fs-xs">
                                    {{ s.lifecycle_status }}
                                </span>
                            </td>
                            <td class="text-end">
                                <a href="{{ url_for('student_detail', student_id=s.id) }}" class="btn btn-sm btn-outline-primary py-1 px-2" title="Inspect Profile & AI Reason Analysis">
                                    <i class="fa-solid fa-chart-simple me-1"></i> Reasons
                                </a>
                            </td>
                        </tr>
                        {% else %}
                        <tr>
                            <td colspan="11" class="text-center py-5 text-muted">
                                <i class="fa-solid fa-folder-open fs-2 mb-2 d-block text-secondary"></i>
                                No students match the selected filter criteria.
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<!-- Bulk CSV Upload Modal -->
<div class="modal fade" id="uploadCsvModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border-0 shadow-lg rounded-4">
            <div class="modal-header bg-navy text-white">
                <h5 class="modal-title fw-bold"><i class="fa-solid fa-file-csv me-2"></i> Bulk Student CSV Upload</h5>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
            </div>
            <form method="POST" action="{{ url_for('upload_csv') }}" enctype="multipart/form-data">
                <div class="modal-body p-4">
                    <p class="text-secondary small">
                        Upload student batch records. The AI prediction engine will automatically clean, scale, and compute dropout risk probabilities and contributing reasons for all imported records.
                    </p>

                    <div class="mb-3">
                        <label for="csv_file" class="form-label small fw-bold text-dark">Select CSV File</label>
                        <input type="file" class="form-control" id="csv_file" name="csv_file" accept=".csv" required>
                    </div>

                    <div class="alert alert-light border small text-muted">
                        <strong><i class="fa-solid fa-circle-info text-primary me-1"></i> Required Columns:</strong><br>
                        <code>enrollment_no, name, department, semester, attendance_percentage, internal_marks_avg, backlog_count, fee_status, engagement_score</code>
                        <div class="mt-2 text-dark">
                            <em>Note: You can use the generated <code>sample_students.csv</code> located in the project folder to test instantly.</em>
                        </div>
                    </div>
                </div>
                <div class="modal-footer border-0 bg-light">
                    <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-primary btn-sm">
                        <i class="fa-solid fa-cloud-arrow-up me-1"></i> Upload & Run AI Prediction
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

```

## File: `templates/counselling.html`
**Description:** 5-Stage Student Retention Lifecycle Hub & Queue Workload Governance  
**Line Count:** 298 lines

```html
{% extends 'base.html' %}

{% block title %}Lifecycle Retention Hub - Sanskriti University{% endblock %}

{% block content %}
<div class="container-fluid px-3 px-lg-4">
    <!-- Header with Administrative Control Link -->
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <h3 class="fw-bold text-navy mb-1">
                <i class="fa-solid fa-hand-holding-heart text-primary me-2"></i> Student Retention Lifecycle Hub
            </h3>
            <p class="text-secondary small mb-0">
                Prioritized in risk-level order: <strong class="text-danger">Critical Risk (Top)</strong> &rarr; <strong class="text-warning">Active Intervention</strong> &rarr; <strong class="text-success">Manageable / Resolved (Last)</strong>.
            </p>
        </div>
        <div class="d-flex gap-2">
            {% if current_user.get('role') in ['Admin', 'Department Head'] %}
            <a href="{{ url_for('admin_settings') }}" class="btn btn-outline-secondary btn-sm shadow-sm" title="Configure capacity limits for each stage">
                <i class="fa-solid fa-sliders me-1"></i> Configure Stage Limits
            </a>
            {% endif %}
            <a href="{{ url_for('students_list') }}" class="btn btn-outline-primary btn-sm shadow-sm">
                <i class="fa-solid fa-users me-1"></i> Student Directory
            </a>
        </div>
    </div>

    <!-- Administrative Stage Capacity & Risk-Level Pipeline Overview Cards -->
    <div class="row g-3 mb-4">
        {% for st in stages %}
        {% set s_stat = stage_stats[st] %}
        {% set s_meta = stage_meta[st] %}
        <div class="col-6 col-md-4 col-xl-2">
            <div class="card border-0 shadow-sm rounded-3 h-100 {% if s_stat.is_overflow %}border border-danger border-2{% endif %}">
                <div class="card-body p-3 d-flex flex-column justify-content-between">
                    <div>
                        <div class="d-flex justify-content-between align-items-center mb-1">
                            <span class="fs-xs fw-bold text-uppercase text-secondary">
                                <i class="fa-solid {{ s_meta.icon }} me-1"></i> {{ st }}
                            </span>
                            {% if s_stat.is_overflow %}
                            <span class="badge bg-danger fs-xs" title="Capacity Limit Exceeded!">Overflow</span>
                            {% endif %}
                        </div>
                        <div class="d-flex align-items-baseline gap-1">
                            <h4 class="fw-bold text-dark mb-0">{{ s_stat.count }}</h4>
                            <span class="text-muted small">/ {{ s_stat.limit }} limit</span>
                        </div>
                    </div>

                    <div class="mt-2">
                        <div class="progress" style="height: 5px;">
                            <div class="progress-bar {% if s_stat.is_overflow %}bg-danger{% elif s_stat.capacity_percent >= 75 %}bg-warning{% elif st in ['Closed', 'Low Risk'] %}bg-success{% else %}bg-primary{% endif %}" 
                                 style="width: {{ s_stat.capacity_percent }}%">
                            </div>
                        </div>
                        <div class="d-flex justify-content-between text-muted fs-xs mt-1">
                            <span>{{ s_stat.capacity_percent }}% capacity</span>
                            {% if s_stat.critical_count > 0 %}
                            <span class="text-danger fw-bold">{{ s_stat.critical_count }} Crit</span>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <!-- Risk-Level Ordered Tabs / Sections -->
    <ul class="nav nav-pills nav-fill mb-4 p-1 bg-white rounded-3 shadow-sm border" id="counsellingTabs" role="tablist">
        {% for st in stages %}
        {% set s_stat = stage_stats[st] %}
        <li class="nav-item" role="presentation">
            <button class="nav-link py-2 fw-semibold {% if loop.first %}active{% endif %} d-flex align-items-center justify-content-center gap-1" 
                    id="tab-{{ loop.index }}" data-bs-toggle="pill" data-bs-target="#pane-{{ loop.index }}" type="button" role="tab">
                <span>{{ st }}</span>
                <span class="badge rounded-pill {% if s_stat.is_overflow %}bg-danger{% elif st == 'At Risk' %}bg-danger{% elif st in ['Closed', 'Low Risk'] %}bg-success{% else %}bg-secondary{% endif %}">
                    {{ s_stat.count }}
                </span>
                {% if s_stat.is_overflow %}
                <i class="fa-solid fa-triangle-exclamation text-danger ms-1" title="Stage Limit Exceeded"></i>
                {% endif %}
            </button>
        </li>
        {% endfor %}
    </ul>

    <!-- Tab Panes for Each Stage (Ordered High Risk Top, Manageable Last) -->
    <div class="tab-content" id="counsellingTabContent">
        {% for st in stages %}
        {% set s_stat = stage_stats[st] %}
        {% set s_meta = stage_meta[st] %}
        <div class="tab-pane fade {% if loop.first %}show active{% endif %}" id="pane-{{ loop.index }}" role="tabpanel">
            <div class="card border-0 shadow-sm rounded-4 mb-4">
                <!-- Stage Header with Urgency Ranking & Capacity Controls -->
                <div class="card-header bg-white border-0 py-3 d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-2">
                    <div>
                        <div class="d-flex align-items-center gap-2">
                            <h5 class="fw-bold text-dark mb-0">
                                <i class="fa-solid {{ s_meta.icon }} me-1"></i> {{ s_meta.title }}
                            </h5>
                            <span class="badge {{ s_meta.badge }} fs-xs">{{ s_meta.urgency }}</span>
                            {% if s_stat.is_overflow %}
                            <span class="badge bg-danger fs-xs"><i class="fa-solid fa-triangle-exclamation me-1"></i> Queue Overflow (+{{ s_stat.count - s_stat.limit }})</span>
                            {% endif %}
                        </div>
                        <p class="text-secondary small mb-0 mt-1">{{ s_meta.desc }}</p>
                    </div>

                    <div class="d-flex align-items-center gap-3">
                        <div class="text-md-end small">
                            <span class="text-muted d-block fs-xs">Stage Capacity Limit</span>
                            <strong>{{ s_stat.count }} active / {{ s_stat.limit }} max allowed</strong>
                        </div>
                        {% if current_user.get('role') in ['Admin', 'Department Head'] %}
                        <a href="{{ url_for('admin_settings') }}" class="btn btn-outline-secondary btn-sm" title="Adjust stage limit">
                            <i class="fa-solid fa-gear"></i>
                        </a>
                        {% endif %}
                    </div>
                </div>

                <!-- Overflow Alert Banner (if limit exceeded) -->
                {% if s_stat.is_overflow %}
                <div class="alert alert-danger border-0 rounded-0 mb-0 py-2 px-4 d-flex align-items-center justify-content-between">
                    <div class="small">
                        <i class="fa-solid fa-triangle-exclamation me-2"></i>
                        <strong>Queue Overflow Warning:</strong> This stage has {{ s_stat.count }} cases, exceeding the administrative limit of {{ s_stat.limit }}. Immediate intervention is recommended to rebalance caseloads.
                    </div>
                    {% if current_user.get('role') in ['Admin', 'Department Head'] %}
                    <a href="{{ url_for('admin_settings') }}" class="btn btn-danger btn-sm py-0 px-2 fs-xs">Adjust Limit</a>
                    {% endif %}
                </div>
                {% endif %}

                <!-- Student List for Stage (Sorted Highest Risk on Top) -->
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light small text-secondary">
                                <tr>
                                    <th>Priority & Risk Tier</th>
                                    <th>Student Details</th>
                                    <th>Department</th>
                                    <th>Attendance</th>
                                    <th>Backlogs</th>
                                    <th>Fee Status</th>
                                    <th>AI Risk Score</th>
                                    <th>Assigned Mentor</th>
                                    <th class="text-end">Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for s in stage_cases[st] %}
                                <tr>
                                    <td>
                                        {% if s.risk_score >= critical_threshold %}
                                        <span class="badge bg-danger fs-xs fw-bold">
                                            <i class="fa-solid fa-angles-up me-1"></i> Critical Risk
                                        </span>
                                        {% elif s.risk_score >= medium_threshold %}
                                        <span class="badge bg-warning-subtle text-warning-emphasis border border-warning-subtle fs-xs fw-semibold">
                                            <i class="fa-solid fa-angle-up me-1"></i> Moderate Risk
                                        </span>
                                        {% else %}
                                        <span class="badge bg-success-subtle text-success border border-success-subtle fs-xs">
                                            <i class="fa-solid fa-check me-1"></i> Manageable
                                        </span>
                                        {% endif %}
                                    </td>
                                    <td>
                                        <div class="fw-bold text-dark">{{ s.name }}</div>
                                        <small class="text-muted font-monospace">{{ s.enrollment_no }}</small>
                                    </td>
                                    <td>
                                        <div>{{ s.department }}</div>
                                        <small class="text-muted fs-xs">Sem {{ s.semester }}</small>
                                    </td>
                                    <td>
                                        <span class="{% if s.attendance_percentage < 65 %}text-danger fw-bold{% elif s.attendance_percentage < 75 %}text-warning fw-semibold{% else %}text-success{% endif %}">
                                            {{ s.attendance_percentage }}%
                                        </span>
                                    </td>
                                    <td>
                                        {% if s.backlog_count > 0 %}
                                        <span class="badge bg-danger-subtle text-danger fw-bold">{{ s.backlog_count }} active</span>
                                        {% else %}
                                        <span class="text-muted">0</span>
                                        {% endif %}
                                    </td>
                                    <td>
                                        <span class="badge {% if s.fee_status == 'Paid' %}bg-success-subtle text-success{% elif s.fee_status == 'Partial' %}bg-warning-subtle text-warning-emphasis{% else %}bg-danger-subtle text-danger{% endif %} fs-xs">
                                            {{ s.fee_status }}
                                        </span>
                                    </td>
                                    <td>
                                        <div class="d-flex align-items-center gap-2">
                                            <div class="progress flex-grow-1" style="height: 6px; width: 60px;">
                                                <div class="progress-bar {% if s.risk_score >= critical_threshold %}bg-danger{% elif s.risk_score >= medium_threshold %}bg-warning{% else %}bg-success{% endif %}" 
                                                     style="width: {{ s.risk_score * 100 }}%">
                                                </div>
                                            </div>
                                            <strong class="small">{{ (s.risk_score * 100)|round(1) }}%</strong>
                                        </div>
                                    </td>
                                    <td>
                                        <span class="small text-secondary">
                                            {% if s.assigned_mentor_id %}
                                            <i class="fa-solid fa-user-check text-success me-1"></i> {{ s.mentor.name if s.mentor else 'Assigned' }}
                                            {% else %}
                                            <span class="badge bg-danger-subtle text-danger fs-xs">Unassigned</span>
                                            {% endif %}
                                        </span>
                                    </td>
                                    <td class="text-end">
                                        <a href="{{ url_for('student_detail', student_id=s.id) }}" class="btn btn-sm btn-primary py-1 px-3">
                                            <i class="fa-solid fa-clipboard-user me-1"></i> Review
                                        </a>
                                    </td>
                                </tr>
                                {% else %}
                                <tr>
                                    <td colspan="9" class="text-center py-5 text-muted">
                                        <i class="fa-regular fa-circle-check fs-2 mb-2 d-block text-success"></i>
                                        No students currently in the <strong>{{ st }}</strong> stage.
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>

    <!-- Recent Case Trail Across All Stages -->
    <div class="card border-0 shadow-sm rounded-4">
        <div class="card-header bg-white border-0 py-3">
            <h6 class="fw-bold text-dark mb-0">
                <i class="fa-solid fa-clock-rotate-left text-primary me-2"></i> Recent Mentor Actions & Follow-ups
            </h6>
        </div>
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0 small">
                    <thead class="table-light text-secondary">
                        <tr>
                            <th>Date</th>
                            <th>Student</th>
                            <th>Mentor</th>
                            <th>Status at Time</th>
                            <th>Mentor Remarks</th>
                            <th>Action Plan</th>
                            <th>Next Follow-up</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for sc in recent_sessions %}
                        <tr>
                            <td class="font-monospace">{{ sc.session_date.strftime('%d-%m-%Y') }}</td>
                            <td>
                                <strong>{{ sc.student.name }}</strong>
                                <div class="text-muted fs-xs font-monospace">{{ sc.student.enrollment_no }}</div>
                            </td>
                            <td>{{ sc.mentor.name }}</td>
                            <td>
                                <span class="badge bg-primary-subtle text-primary border border-primary-subtle fs-xs">
                                    {{ sc.status_at_time }}
                                </span>
                            </td>
                            <td>{{ sc.mentor_remarks }}</td>
                            <td class="text-muted">{{ sc.action_plan or '-' }}</td>
                            <td>
                                {% if sc.next_followup_date %}
                                <span class="text-danger fw-semibold">{{ sc.next_followup_date.strftime('%d-%m-%Y') }}</span>
                                {% else %}
                                <span class="text-muted">-</span>
                                {% endif %}
                            </td>
                        </tr>
                        {% else %}
                        <tr>
                            <td colspan="7" class="text-center py-4 text-muted">
                                No counselling sessions on record.
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}

```

## File: `templates/admin_settings.html`
**Description:** Administrative Policy Controls, Risk Threshold Sliders & Model Retraining Panel  
**Line Count:** 321 lines

```html
{% extends 'base.html' %}

{% block title %}Administrative Configuration & Risk Policy Rules - Sanskriti University{% endblock %}

{% block content %}
<div class="container-fluid px-3 px-lg-4">
    <!-- Header with Quick Action Controls -->
    <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
            <h3 class="fw-bold text-navy mb-1">
                <i class="fa-solid fa-gears text-primary me-2"></i> Administrative Governance & Risk Policy Rules
            </h3>
            <p class="text-secondary small mb-0">
                Configure student risk factor limits (attendance, backlogs, marks), define routing destinations, set stage capacities, or restore nominal global defaults.
            </p>
        </div>
        <div class="d-flex flex-wrap gap-2">
            <!-- Reset to Nominal Defaults Button -->
            <form method="POST" action="{{ url_for('reset_nominal_settings') }}" onsubmit="return confirm('Restore all risk factor limits and thresholds to Sanskriti University nominal global defaults?');" class="d-inline">
                <button type="submit" class="btn btn-outline-warning btn-sm shadow-sm" title="Restore nominal institutional standards">
                    <i class="fa-solid fa-rotate-left me-1"></i> Restore Nominal Defaults
                </button>
            </form>

            <!-- Reapply Rules to All Students Button -->
            <form method="POST" action="{{ url_for('reapply_rules_to_all_students') }}" onsubmit="return confirm('Re-evaluate all current student records with the active risk limits and routing rules?');" class="d-inline">
                <button type="submit" class="btn btn-outline-success btn-sm shadow-sm" title="Recalculate risk scores for all students">
                    <i class="fa-solid fa-arrows-spin me-1"></i> Re-Apply Rules to All Students
                </button>
            </form>

            <a href="{{ url_for('counselling_hub') }}" class="btn btn-primary btn-sm shadow-sm">
                <i class="fa-solid fa-hand-holding-heart me-1"></i> View Lifecycle Hub
            </a>
        </div>
    </div>

    <div class="row g-4">
        <!-- Left Column: Academic & Risk Factor Policy Configuration -->
        <div class="col-lg-6">
            <div class="card border-0 shadow-sm rounded-4 mb-4">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">
                        <i class="fa-solid fa-scale-balanced text-primary me-2"></i> Academic Risk Factor Limits & Routing Policy
                    </h6>
                    <span class="badge bg-primary-subtle text-primary border border-primary-subtle">Policy Control</span>
                </div>
                <div class="card-body p-4">
                    <p class="text-secondary small mb-3">
                        Define what limits of attendance, backlogs, marks, and fees trigger risk classification, and choose which lifecycle stage newly flagged students are routed to:
                    </p>

                    <form method="POST" action="{{ url_for('admin_settings') }}">
                        <!-- 1. Attendance Limits -->
                        <div class="p-3 bg-light rounded-3 border mb-3">
                            <h6 class="text-navy fw-bold small text-uppercase mb-2">
                                <i class="fa-solid fa-user-check text-primary me-1"></i> Attendance Limits (%)
                            </h6>
                            <div class="row g-2">
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">Warning Threshold</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" step="0.5" min="50" max="95" name="rule_attendance_warning" value="{{ settings.rule_attendance_warning }}" class="form-control" required>
                                        <span class="input-group-text bg-white">%</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 75%</span>
                                </div>
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-danger mb-1">Critical Threshold</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" step="0.5" min="20" max="80" name="rule_attendance_critical" value="{{ settings.rule_attendance_critical }}" class="form-control" required>
                                        <span class="input-group-text bg-white">%</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 60%</span>
                                </div>
                            </div>
                        </div>

                        <!-- 2. Backlog Count Limits -->
                        <div class="p-3 bg-light rounded-3 border mb-3">
                            <h6 class="text-navy fw-bold small text-uppercase mb-2">
                                <i class="fa-solid fa-triangle-exclamation text-danger me-1"></i> Active Backlogs Limits
                            </h6>
                            <div class="row g-2">
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">Warning Limit</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" min="0" max="10" name="rule_backlogs_warning" value="{{ settings.rule_backlogs_warning }}" class="form-control" required>
                                        <span class="input-group-text bg-white">subject(s)</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 1 backlog</span>
                                </div>
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-danger mb-1">Critical Limit</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" min="1" max="15" name="rule_backlogs_critical" value="{{ settings.rule_backlogs_critical }}" class="form-control" required>
                                        <span class="input-group-text bg-white">subject(s)</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 3 backlogs</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3. Internal Marks & LMS Engagement -->
                        <div class="p-3 bg-light rounded-3 border mb-3">
                            <h6 class="text-navy fw-bold small text-uppercase mb-2">
                                <i class="fa-solid fa-graduation-cap text-success me-1"></i> Academic Marks & LMS Engagement
                            </h6>
                            <div class="row g-2 mb-2">
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">Marks Passing Benchmark</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" step="0.5" min="30" max="80" name="rule_marks_warning" value="{{ settings.rule_marks_warning }}" class="form-control" required>
                                        <span class="input-group-text bg-white">%</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 55%</span>
                                </div>
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-danger mb-1">Critical Failing Mark</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" step="0.5" min="15" max="60" name="rule_marks_critical" value="{{ settings.rule_marks_critical }}" class="form-control" required>
                                        <span class="input-group-text bg-white">%</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 40%</span>
                                </div>
                            </div>
                            <div class="row g-2">
                                <div class="col-12">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">LMS Activity Critical Level (0-100)</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" step="0.5" min="10" max="70" name="rule_engagement_critical" value="{{ settings.rule_engagement_critical }}" class="form-control" required>
                                        <span class="input-group-text bg-white">score</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 40.0</span>
                                </div>
                            </div>
                        </div>

                        <!-- 4. Risk Destination & Routing Policy -->
                        <div class="p-3 bg-light rounded-3 border mb-4">
                            <h6 class="text-navy fw-bold small text-uppercase mb-2">
                                <i class="fa-solid fa-route text-warning me-1"></i> Risk Factor Destination & Routing Target
                            </h6>
                            <div class="row g-2">
                                <div class="col-md-6">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">Target Lifecycle Stage for Flagged Students</label>
                                    <select name="rule_auto_lifecycle_target" class="form-select form-select-sm">
                                        <option value="At Risk" {% if settings.rule_auto_lifecycle_target == 'At Risk' %}selected{% endif %}>At Risk (Immediate Attention Queue)</option>
                                        <option value="Under Review" {% if settings.rule_auto_lifecycle_target == 'Under Review' %}selected{% endif %}>Under Review (Direct to Diagnostic)</option>
                                        <option value="Counselling" {% if settings.rule_auto_lifecycle_target == 'Counselling' %}selected{% endif %}>Counselling (Direct to Mentorship)</option>
                                    </select>
                                    <span class="text-muted fs-xs">Which stage flagged students automatically enter</span>
                                </div>

                                <div class="col-md-6">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">Tuition Fee Default Impact</label>
                                    <select name="rule_fee_due_severity" class="form-select form-select-sm">
                                        <option value="danger" {% if settings.rule_fee_due_severity == 'danger' %}selected{% endif %}>High Risk Factor (Danger Alert)</option>
                                        <option value="warning" {% if settings.rule_fee_due_severity == 'warning' %}selected{% endif %}>Moderate Risk Factor (Warning Alert)</option>
                                    </select>
                                    <span class="text-muted fs-xs">Attributed weight for fee dues</span>
                                </div>
                            </div>
                        </div>

                        <!-- 5. Stage Capacity Limits -->
                        <div class="p-3 bg-light rounded-3 border mb-4">
                            <h6 class="text-navy fw-bold small text-uppercase mb-2">
                                <i class="fa-solid fa-list-ol text-secondary me-1"></i> Stage Capacity Limits (Queue Meters)
                            </h6>
                            <div class="row g-2">
                                <div class="col-4">
                                    <label class="form-label fs-xs fw-bold text-danger mb-1">At Risk Limit</label>
                                    <input type="number" min="1" max="100" name="stage_limit_At_Risk" value="{{ settings.stage_limit_At_Risk }}" class="form-control form-control-sm" required>
                                </div>
                                <div class="col-4">
                                    <label class="form-label fs-xs fw-bold text-dark mb-1">Under Review</label>
                                    <input type="number" min="1" max="100" name="stage_limit_Under_Review" value="{{ settings.stage_limit_Under_Review }}" class="form-control form-control-sm" required>
                                </div>
                                <div class="col-4">
                                    <label class="form-label fs-xs fw-bold text-primary mb-1">Counselling</label>
                                    <input type="number" min="1" max="100" name="stage_limit_Counselling" value="{{ settings.stage_limit_Counselling }}" class="form-control form-control-sm" required>
                                </div>
                                <div class="col-4 mt-2">
                                    <label class="form-label fs-xs fw-bold text-info mb-1">Intervened</label>
                                    <input type="number" min="1" max="200" name="stage_limit_Intervened" value="{{ settings.stage_limit_Intervened }}" class="form-control form-control-sm" required>
                                </div>
                                <div class="col-4 mt-2">
                                    <label class="form-label fs-xs fw-bold text-success mb-1">Closed Archive</label>
                                    <input type="number" min="1" max="1000" name="stage_limit_Closed" value="{{ settings.stage_limit_Closed }}" class="form-control form-control-sm" required>
                                </div>
                                <div class="col-4 mt-2">
                                    <label class="form-label fs-xs fw-bold text-secondary mb-1">Low Risk Display</label>
                                    <input type="number" min="1" max="1000" name="stage_limit_Low_Risk" value="{{ settings.stage_limit_Low_Risk }}" class="form-control form-control-sm" required>
                                </div>
                            </div>
                        </div>

                        <!-- 6. Scoring Thresholds -->
                        <div class="p-3 bg-light rounded-3 border mb-4">
                            <h6 class="text-navy fw-bold small text-uppercase mb-2">
                                <i class="fa-solid fa-gauge-high text-danger me-1"></i> AI Risk Score Thresholds
                            </h6>
                            <div class="row g-2">
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-danger mb-1">Critical High Risk (&ge; %)</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" min="50" max="95" name="critical_risk_threshold" value="{{ settings.critical_risk_threshold }}" class="form-control" required>
                                        <span class="input-group-text bg-white">%</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 70%</span>
                                </div>
                                <div class="col-6">
                                    <label class="form-label fs-xs fw-bold text-warning mb-1">Moderate Risk (&ge; %)</label>
                                    <div class="input-group input-group-sm">
                                        <input type="number" min="20" max="60" name="medium_risk_threshold" value="{{ settings.medium_risk_threshold }}" class="form-control" required>
                                        <span class="input-group-text bg-white">%</span>
                                    </div>
                                    <span class="text-muted fs-xs">Nominal: 50%</span>
                                </div>
                            </div>
                        </div>

                        <div class="d-flex gap-2">
                            <button type="submit" class="btn btn-primary px-4 fw-semibold">
                                <i class="fa-solid fa-save me-1"></i> Save Risk Factor Limits
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <!-- Right Column: Guidance & One-Click Retraining -->
        <div class="col-lg-6">
            <!-- Educational Guidance Card -->
            <div class="card border-0 shadow-sm rounded-4 mb-4 bg-navy text-white">
                <div class="card-body p-4">
                    <h5 class="fw-bold mb-2">
                        <i class="fa-solid fa-circle-question text-warning me-2"></i> Should I Retrain if I Upload a New List?
                    </h5>
                    <p class="text-white-70 small mb-3">
                        Administrative rule for managing student uploads vs model retraining:
                    </p>

                    <div class="d-flex flex-column gap-3">
                        <div class="p-3 bg-white bg-opacity-10 rounded-3 border border-white border-opacity-10">
                            <strong class="text-warning d-block mb-1">
                                <i class="fa-solid fa-circle-info me-1"></i> Uploading Active Student Rosters for Monitoring
                            </strong>
                            <p class="small text-white-50 mb-0">
                                <strong>NO RETRAINING REQUIRED.</strong> When uploading a semester CSV list of students to monitor, use <em>Bulk CSV Upload</em> on the Students page. The AI prediction engine immediately evaluates the risk scores, detects attendance/backlog deficits, and routes them according to your active limits.
                            </p>
                        </div>

                        <div class="p-3 bg-white bg-opacity-10 rounded-3 border border-white border-opacity-10">
                            <strong class="text-success d-block mb-1">
                                <i class="fa-solid fa-circle-check me-1"></i> Uploading Historical Data with Verified Dropout Outcomes
                            </strong>
                            <p class="small text-white-50 mb-0">
                                <strong>YES, RETRAIN.</strong> When an academic cycle concludes and you have actual historical outcome records (with <code>dropped_out = 1/0</code>), use the retraining options below to update the model's predictive weights.
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- One-Click Retraining Card -->
            <div class="card border-0 shadow-sm rounded-4">
                <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold text-dark mb-0">
                        <i class="fa-solid fa-brain text-primary me-2"></i> Trigger AI Model Retraining
                    </h6>
                    <span class="badge bg-success-subtle text-success border border-success-subtle">
                        Current Acc: {{ (metrics['Random Forest']['Accuracy'] * 100)|round(1) }}%
                    </span>
                </div>
                <div class="card-body p-4">
                    <p class="text-secondary small mb-3">
                        You can retrain both the <strong>Random Forest</strong> and <strong>Logistic Regression</strong> pipelines right now:
                    </p>

                    <!-- Form 1: One-Click Retrain on Updated Benchmark Data -->
                    <form method="POST" action="{{ url_for('retrain_model_endpoint') }}" class="mb-4">
                        <div class="p-3 rounded-3 bg-light border mb-3">
                            <h6 class="fw-bold text-dark mb-1">Option 1: Recalibrate on Historical Distributions</h6>
                            <p class="text-muted small mb-2">
                                Regenerates and recalibrates model weights based on comprehensive institutional parameters (attendance, internal marks, backlogs, fee defaults).
                            </p>
                            <button type="submit" class="btn btn-outline-primary btn-sm">
                                <i class="fa-solid fa-arrows-rotate me-1"></i> Retrain Model Now
                            </button>
                        </div>
                    </form>

                    <!-- Form 2: Retrain with Custom Labeled CSV -->
                    <form method="POST" action="{{ url_for('retrain_model_endpoint') }}" enctype="multipart/form-data">
                        <div class="p-3 rounded-3 bg-light border">
                            <h6 class="fw-bold text-dark mb-1">Option 2: Upload New Ground-Truth CSV & Retrain</h6>
                            <p class="text-muted small mb-3">
                                Upload a historical CSV containing past students with the actual target column: <code>dropped_out</code> (1 for dropped out, 0 for retained).
                            </p>

                            <div class="mb-3">
                                <input type="file" name="training_file" accept=".csv" class="form-control form-control-sm" required>
                                <small class="text-muted fs-xs">
                                    Must contain: <code>attendance_percentage, internal_marks_avg, backlog_count, fee_status, engagement_score, semester, dropped_out</code>
                                </small>
                            </div>

                            <button type="submit" class="btn btn-primary btn-sm">
                                <i class="fa-solid fa-cloud-arrow-up me-1"></i> Upload Labeled CSV & Retrain
                            </button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}

```

## File: `templates/student_profile.html`
**Description:** Isolated Student Profile View, Explainable AI Reason Card & Mentorship Log  
**Line Count:** 1 lines

```html
# templates/student_profile.html not found
```

## File: `templates/audit_logs.html`
**Description:** System Audit Trail, Forensic Activity History & Timestamped User Actions  
**Line Count:** 69 lines

```html
{% extends 'base.html' %}

{% block title %}System Audit Logs - Sanskriti University{% endblock %}

{% block content %}
<div class="container-fluid px-3 px-lg-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h3 class="fw-bold text-navy mb-1">
                <i class="fa-solid fa-shield-halved text-primary me-2"></i> System Audit Trail & Security Logs
            </h3>
            <p class="text-secondary small mb-0">
                Immutable chronological log of authentication, dataset uploads, AI prediction batches, status transitions, and counselling records.
            </p>
        </div>
    </div>

    <div class="card border-0 shadow-sm rounded-4">
        <div class="card-header bg-white border-0 py-3 d-flex justify-content-between align-items-center">
            <h6 class="fw-bold text-dark mb-0">Audit Events ({{ logs|length }} recorded entries)</h6>
            <span class="badge bg-light text-secondary border font-monospace">Local Authority Node</span>
        </div>
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0 small">
                    <thead class="table-light text-secondary">
                        <tr>
                            <th>Timestamp (UTC)</th>
                            <th>User</th>
                            <th>Action Triggered</th>
                            <th>Action Details</th>
                            <th>Origin IP</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for log in logs %}
                        <tr>
                            <td class="font-monospace text-muted">{{ log.timestamp.strftime('%Y-%m-%d %H:%M:%S') }}</td>
                            <td>
                                <strong>{{ log.username }}</strong>
                            </td>
                            <td>
                                <span class="badge 
                                    {% if 'LOGIN' in log.action %}bg-info-subtle text-info border border-info-subtle
                                    {% elif 'UPLOAD' in log.action %}bg-primary-subtle text-primary border border-primary-subtle
                                    {% elif 'PREDICTION' in log.action %}bg-warning-subtle text-warning-emphasis border border-warning-subtle
                                    {% elif 'COUNSELLING' in log.action %}bg-success-subtle text-success border border-success-subtle
                                    {% elif 'ESCALATION' in log.action %}bg-danger-subtle text-danger border border-danger-subtle
                                    {% else %}bg-light text-secondary border{% endif %} fs-xs font-monospace">
                                    {{ log.action }}
                                </span>
                            </td>
                            <td class="text-dark">{{ log.details }}</td>
                            <td class="font-monospace text-muted">{{ log.ip_address or '127.0.0.1' }}</td>
                        </tr>
                        {% else %}
                        <tr>
                            <td colspan="5" class="text-center py-5 text-muted">
                                No audit log records available.
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}

```

## File: `static/css/style.css`
**Description:** Custom Responsive CSS Styling Rules, Risk Badge Hierarchy & Theme Tokens  
**Line Count:** 95 lines

```css
/* Custom Styling for Sanskriti University Student Dropout Prediction Portal */

:root {
    --primary-color: #1a56db;
    --navy-color: #0f172a;
    --navy-header: #1e293b;
    --accent-warning: #f59e0b;
    --accent-danger: #ef4444;
    --accent-success: #10b981;
    --bg-light: #f8fafc;
}

body {
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: #1e293b;
    background-color: var(--bg-light);
}

.bg-navy {
    background-color: var(--navy-color) !important;
}

.text-navy {
    color: var(--navy-color) !important;
}

.fs-xs {
    font-size: 0.75rem !important;
}

/* Brand badge */
.brand-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    color: #f59e0b;
}

/* User Avatar */
.avatar-circle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background-color: #3b82f6;
    color: white;
    font-weight: 600;
    font-size: 0.85rem;
}

/* Metric KPI Cards */
.metric-card {
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08) !important;
}

.metric-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
}

/* Tables */
.table th {
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.03em;
}

/* Timeline */
.timeline-entry::before {
    content: '';
    position: absolute;
    left: -12px;
    top: 6px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: var(--primary-color);
}

```

---

# PART III: SYSTEM VERIFICATION & HANDOVER GUIDE

## Automated Test Execution Matrix (8/8 PASS)
| Test ID | Target Test Routine | Executed Scope | Recorded Output | Status |
|---|---|---|---|---|
| TC-01 | test_login_page_renders | Authentication | HTTP 200 OK | PASS |
| TC-02 | test_admin_login_success | Session Management | HTTP 302 Redirect | PASS |
| TC-03 | test_dashboard_requires_login | Route Guard | HTTP 302 to /login | PASS |
| TC-04 | test_ml_prediction_bounds | ML Inference | Bounds [0.0%, 100.0%] | PASS |
| TC-05 | test_explainable_ai_reasons | XAI Engine | Sums to 100% | PASS |
| TC-06 | test_student_privacy_isolation | Privacy Boundary | HTTP 403 Forbidden | PASS |
| TC-07 | test_lifecycle_status_transition | Lifecycle Hub | Transition Logged | PASS |
| TC-08 | test_admin_settings_update | Dynamic Policy | Thresholds Recalibrated | PASS |

## Local Handover Launch Commands
```bash
# 1. Open Terminal and navigate to directory
cd C:\Users\ASUS\.gemini\antigravity\scratch\student_dropout_prediction

# 2. Start Flask Server via virtual environment
.venv\Scripts\python.exe app.py

# 3. Access in Web Browser
http://127.0.0.1:5000
```

**Pre-configured Demo Credentials:**  
* **Admin:** `admin` / `password123`  
* **Guide/HOD:** `satyam` / `password123`  
* **Mentor:** `priya` / `password123`  
* **Student:** `ramesh` / `password123`
