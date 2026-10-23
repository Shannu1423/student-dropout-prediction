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

