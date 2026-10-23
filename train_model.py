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
