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
