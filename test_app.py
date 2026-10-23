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
