import json
import os
from datetime import datetime, timedelta
from app import create_app
from database import db, User, Student, CounsellingCase, AuditLog, Notification, SystemSetting
from ml_engine import MLEngine

def seed_database():
    app = create_app()
    with app.app_context():
        # Recreate tables cleanly
        db.create_all()

        if User.query.first():
            print("Database already has data. Skipping seed.")
            return

        print("Seeding initial users...")
        users = [
            User(username='admin', name='Dr. A. K. Sharma', email='admin@sanskriti.edu.in', role='Admin', department='Administration'),
            User(username='satyam', name='Mr. Satyam Dwivedi', email='satyam.dwivedi@sanskriti.edu.in', role='Department Head', department='Computer Science & Engineering'),
            User(username='priya', name='Dr. Priya Verma', email='priya.verma@sanskriti.edu.in', role='Faculty Mentor', department='Computer Science & Engineering'),
            User(username='rajesh', name='Prof. Rajesh Kumar', email='rajesh.kumar@sanskriti.edu.in', role='Faculty Mentor', department='Mechanical Engineering'),
            User(username='ramesh', name='D. Ramesh', email='ramesh.2302320099@sanskriti.edu.in', role='Student', department='Computer Science & Engineering')
        ]
        
        # Set default password 'password123' for all demo accounts
        for u in users:
            u.set_password('password123')
            db.session.add(u)
        db.session.commit()

        mentor_priya = User.query.filter_by(username='priya').first()
        mentor_rajesh = User.query.filter_by(username='rajesh').first()

        print("Initializing ML Engine for initial student risk scoring...")
        ml = MLEngine.get_instance()

        sample_students_data = [
            # The Student from Sanskriti University Evaluation form:
            {
                'enrollment_no': '2302320099',
                'name': 'D. Ramesh',
                'email': 'ramesh.2302320099@sanskriti.edu.in',
                'phone': '+91-9876543210',
                'department': 'Computer Science & Engineering',
                'semester': 5,
                'attendance_percentage': 82.5,
                'internal_marks_avg': 78.0,
                'backlog_count': 0,
                'fee_status': 'Paid',
                'engagement_score': 85.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Low Risk',
                'assigned_mentor_id': mentor_priya.id
            },
            # At Risk - Critical attendance & backlogs
            {
                'enrollment_no': '2302320012',
                'name': 'Aakash Verma',
                'email': 'aakash.v@sanskriti.edu.in',
                'phone': '+91-9811223344',
                'department': 'Computer Science & Engineering',
                'semester': 4,
                'attendance_percentage': 42.0,
                'internal_marks_avg': 38.5,
                'backlog_count': 3,
                'fee_status': 'Due',
                'engagement_score': 25.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'At Risk',
                'assigned_mentor_id': mentor_priya.id
            },
            # Under Review - Fee Due & borderline attendance
            {
                'enrollment_no': '2302320045',
                'name': 'Rohit Sen',
                'email': 'rohit.sen@sanskriti.edu.in',
                'phone': '+91-9822334455',
                'department': 'Mechanical Engineering',
                'semester': 3,
                'attendance_percentage': 61.5,
                'internal_marks_avg': 48.0,
                'backlog_count': 2,
                'fee_status': 'Due',
                'engagement_score': 40.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Under Review',
                'assigned_mentor_id': mentor_rajesh.id
            },
            # In Counselling - Active intervention in progress
            {
                'enrollment_no': '2302320078',
                'name': 'Sneha Kapoor',
                'email': 'sneha.k@sanskriti.edu.in',
                'phone': '+91-9833445566',
                'department': 'Computer Science & Engineering',
                'semester': 6,
                'attendance_percentage': 56.0,
                'internal_marks_avg': 52.0,
                'backlog_count': 2,
                'fee_status': 'Partial',
                'engagement_score': 45.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Counselling',
                'assigned_mentor_id': mentor_priya.id
            },
            # Intervened - Remediations assigned
            {
                'enrollment_no': '2302320104',
                'name': 'Vikas Mehra',
                'email': 'vikas.m@sanskriti.edu.in',
                'phone': '+91-9844556677',
                'department': 'Civil Engineering',
                'semester': 4,
                'attendance_percentage': 68.0,
                'internal_marks_avg': 59.0,
                'backlog_count': 1,
                'fee_status': 'Partial',
                'engagement_score': 62.0,
                'campus_location': 'South Campus',
                'lifecycle_status': 'Intervened',
                'assigned_mentor_id': mentor_priya.id
            },
            # Closed - Successfully resolved
            {
                'enrollment_no': '2302320130',
                'name': 'Ananya Sharma',
                'email': 'ananya.s@sanskriti.edu.in',
                'phone': '+91-9855667788',
                'department': 'Electrical Engineering',
                'semester': 6,
                'attendance_percentage': 88.0,
                'internal_marks_avg': 81.0,
                'backlog_count': 0,
                'fee_status': 'Paid',
                'engagement_score': 90.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Closed',
                'assigned_mentor_id': mentor_rajesh.id
            },
            # Low Risk student
            {
                'enrollment_no': '2302320155',
                'name': 'Karan Gupta',
                'email': 'karan.g@sanskriti.edu.in',
                'phone': '+91-9866778899',
                'department': 'Management',
                'semester': 2,
                'attendance_percentage': 91.0,
                'internal_marks_avg': 84.5,
                'backlog_count': 0,
                'fee_status': 'Paid',
                'engagement_score': 88.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Low Risk',
                'assigned_mentor_id': mentor_priya.id
            },
            # High Risk - Escalation candidate (pending review for long time)
            {
                'enrollment_no': '2302320188',
                'name': 'Mohit Chauhan',
                'email': 'mohit.c@sanskriti.edu.in',
                'phone': '+91-9877889900',
                'department': 'Mechanical Engineering',
                'semester': 5,
                'attendance_percentage': 38.0,
                'internal_marks_avg': 32.0,
                'backlog_count': 4,
                'fee_status': 'Due',
                'engagement_score': 18.0,
                'campus_location': 'North Campus',
                'lifecycle_status': 'At Risk',
                'assigned_mentor_id': mentor_rajesh.id
            },
            # Additional students for analytics richness
            {
                'enrollment_no': '2302320202',
                'name': 'Pooja Tiwari',
                'email': 'pooja.t@sanskriti.edu.in',
                'phone': '+91-9888990011',
                'department': 'Computer Science & Engineering',
                'semester': 3,
                'attendance_percentage': 73.0,
                'internal_marks_avg': 66.0,
                'backlog_count': 1,
                'fee_status': 'Paid',
                'engagement_score': 68.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Low Risk',
                'assigned_mentor_id': mentor_priya.id
            },
            {
                'enrollment_no': '2302320225',
                'name': 'Deepak Joshi',
                'email': 'deepak.j@sanskriti.edu.in',
                'phone': '+91-9899001122',
                'department': 'Civil Engineering',
                'semester': 5,
                'attendance_percentage': 52.0,
                'internal_marks_avg': 44.0,
                'backlog_count': 3,
                'fee_status': 'Due',
                'engagement_score': 35.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Under Review',
                'assigned_mentor_id': mentor_rajesh.id
            },
            {
                'enrollment_no': '2302320250',
                'name': 'Ritu Mishra',
                'email': 'ritu.m@sanskriti.edu.in',
                'phone': '+91-9900112233',
                'department': 'Management',
                'semester': 4,
                'attendance_percentage': 79.0,
                'internal_marks_avg': 72.0,
                'backlog_count': 0,
                'fee_status': 'Paid',
                'engagement_score': 75.0,
                'campus_location': 'South Campus',
                'lifecycle_status': 'Low Risk',
                'assigned_mentor_id': mentor_priya.id
            },
            {
                'enrollment_no': '2302320280',
                'name': 'Gaurav Yadav',
                'email': 'gaurav.y@sanskriti.edu.in',
                'phone': '+91-9911223344',
                'department': 'Computer Science & Engineering',
                'semester': 7,
                'attendance_percentage': 49.0,
                'internal_marks_avg': 46.0,
                'backlog_count': 2,
                'fee_status': 'Partial',
                'engagement_score': 41.0,
                'campus_location': 'Main Campus',
                'lifecycle_status': 'Counselling',
                'assigned_mentor_id': mentor_priya.id
            }
        ]

        print("Adding and predicting sample students...")
        created_students = []
        for sdata in sample_students_data:
            pred = ml.predict_student(sdata)
            student = Student(
                enrollment_no=sdata['enrollment_no'],
                name=sdata['name'],
                email=sdata['email'],
                phone=sdata['phone'],
                department=sdata['department'],
                semester=sdata['semester'],
                attendance_percentage=sdata['attendance_percentage'],
                internal_marks_avg=sdata['internal_marks_avg'],
                backlog_count=sdata['backlog_count'],
                fee_status=sdata['fee_status'],
                engagement_score=sdata['engagement_score'],
                campus_location=sdata['campus_location'],
                risk_score=pred['risk_score'],
                risk_level=pred['risk_level'],
                key_reasons=json.dumps(pred['reasons']),
                lifecycle_status=sdata['lifecycle_status'],
                assigned_mentor_id=sdata['assigned_mentor_id']
            )
            db.session.add(student)
            created_students.append(student)

        db.session.commit()

        # Seed counselling cases
        print("Seeding counselling logs...")
        sneha = Student.query.filter_by(enrollment_no='2302320078').first()
        if sneha:
            case1 = CounsellingCase(
                student_id=sneha.id,
                mentor_id=mentor_priya.id,
                session_date=datetime.utcnow().date() - timedelta(days=5),
                status_at_time='Under Review',
                mentor_remarks="Student reported personal family health difficulties leading to irregular attendance in past month.",
                action_plan="1. Connect with student welfare office for fee installment.\n2. Provide lecture notes for missed classes.\n3. Bi-weekly attendance check.",
                next_followup_date=datetime.utcnow().date() + timedelta(days=7)
            )
            db.session.add(case1)

        vikas = Student.query.filter_by(enrollment_no='2302320104').first()
        if vikas:
            case2 = CounsellingCase(
                student_id=vikas.id,
                mentor_id=mentor_priya.id,
                session_date=datetime.utcnow().date() - timedelta(days=12),
                status_at_time='Counselling',
                mentor_remarks="Enrolled in remedial classes for backlog mechanics subject. Submitted fee payment commitment letter.",
                action_plan="Remedial tutorials on Saturdays. Progress check at mid-semester.",
                next_followup_date=datetime.utcnow().date() + timedelta(days=10)
            )
            db.session.add(case2)

        # Seed notifications
        print("Seeding notifications...")
        notifications = [
            Notification(
                title="Critical Dropout Risk Alert",
                message="Student Aakash Verma (2302320012) flagged with 99% dropout risk (Attendance 42%, 3 Backlogs, Fee Due).",
                category="danger"
            ),
            Notification(
                title="Escalation Required",
                message="Case for Mohit Chauhan (2302320188) in Mechanical Dept has been pending review without mentor action.",
                category="warning"
            ),
            Notification(
                title="Counselling Milestones Achieved",
                message="Student Ananya Sharma (2302320130) case closed successfully after clearing backlogs and fee payment.",
                category="success"
            )
        ]
        for n in notifications:
            db.session.add(n)

        # Seed initial audit logs
        print("Seeding audit logs...")
        audit_events = [
            AuditLog(username='admin', action='SYSTEM_INITIALIZED', details='System database and AI models initialized with baseline dataset.', ip_address='127.0.0.1'),
            AuditLog(username='satyam', action='LOGIN', details='Department Head Satyam Dwivedi logged in to authority portal.', ip_address='127.0.0.1'),
            AuditLog(username='priya', action='COUNSELLING_SESSION', details='Counselling note recorded for student Sneha Kapoor (2302320078).', ip_address='127.0.0.1'),
            AuditLog(username='system', action='PREDICTION_BATCH', details='Automated dropout prediction run on 12 student records.', ip_address='127.0.0.1')
        ]
        for a in audit_events:
            db.session.add(a)

        # Seed initial system settings
        print("Seeding default stage limits and risk thresholds...")
        default_settings = [
            ('stage_limit_At_Risk', '8', 'Maximum active capacity for At Risk queue before overflow warning'),
            ('stage_limit_Under_Review', '6', 'Maximum active capacity for Under Review queue'),
            ('stage_limit_Counselling', '10', 'Maximum concurrent active counselling sessions'),
            ('stage_limit_Intervened', '15', 'Capacity for students in post-counselling intervention'),
            ('stage_limit_Closed', '100', 'Archive capacity for resolved cases'),
            ('critical_risk_threshold', '0.70', 'Risk probability threshold for Critical High Risk status (>= 70%)'),
            ('medium_risk_threshold', '0.50', 'Risk probability threshold for Moderate Risk status (50% - 69%)')
        ]
        for key, val, desc in default_settings:
            s = SystemSetting(key=key, value=val, description=desc)
            db.session.add(s)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
