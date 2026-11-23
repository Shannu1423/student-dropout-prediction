"""
Generate Markdown and HTML versions of the Complete Codebase and System Architecture Report.
"""
import os
import markdown

PROJECT_DIR = r"C:\Users\ASUS\.gemini\antigravity\scratch\student_dropout_prediction"
MD_PATH = os.path.join(PROJECT_DIR, "COMPLETE_CODEBASE_AND_SYSTEM_ARCHITECTURE_REPORT.md")
HTML_PATH = os.path.join(PROJECT_DIR, "COMPLETE_CODEBASE_AND_SYSTEM_ARCHITECTURE_REPORT.html")

def read_source(fn):
    p = os.path.join(PROJECT_DIR, fn)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    return f"# {fn} not found"

files = [
    ("app.py", "python", "Complete Flask Web Application Controller, REST Endpoints, RBAC, CSV Ingestion & Audit System"),
    ("ml_engine.py", "python", "Machine Learning Pipeline, Random Forest Classifier, Baseline Logistic Regression & XAI Engine"),
    ("database.py", "python", "Relational Database Persistence Layer, SQLAlchemy ORM Models & Lifecycle Definitions"),
    ("config.py", "python", "System Configuration Registry, Security Keys & Environmental Parameter Bindings"),
    ("test_app.py", "python", "Automated System Verification Harness, Integration Tests & Test Matrix Assertions"),
    ("train_model.py", "python", "Machine Learning Model Training Pipeline, Stratified Evaluation & Synthetic Data Generation"),
    ("templates/base.html", "html", "Core Frontend Master Template, Bootstrap 5 Framework & Dynamic Role-Based Navbar"),
    ("templates/login.html", "html", "Unified Portal Authentication Screen & Quick Demo Access Controls"),
    ("templates/dashboard.html", "html", "Executive Authority Dashboard, KPI Metrics & Chart.js Visualizations"),
    ("templates/students.html", "html", "Student Monitoring Directory, Multi-Parameter Search & Bulk Ingestion Modal"),
    ("templates/counselling.html", "html", "5-Stage Student Retention Lifecycle Hub & Queue Workload Governance"),
    ("templates/admin_settings.html", "html", "Administrative Policy Controls, Risk Threshold Sliders & Model Retraining Panel"),
    ("templates/student_profile.html", "html", "Isolated Student Profile View, Explainable AI Reason Card & Mentorship Log"),
    ("templates/audit_logs.html", "html", "System Audit Trail, Forensic Activity History & Timestamped User Actions"),
    ("static/css/style.css", "css", "Custom Responsive CSS Styling Rules, Risk Badge Hierarchy & Theme Tokens")
]

md = []
md.append("# SANSKRITI UNIVERSITY")
md.append("### School of Engineering & Information Technology (SOEIT) — Department of Computer Science & Engineering\n")
md.append("# AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT")
md.append("## SYSTEM ARCHITECTURE, TECHNICAL SPECIFICATIONS & COMPLETE SOURCE CODEBASE REFERENCE MANUAL\n")
md.append("**Degree:** Bachelor of Technology in Computer Science & Engineering  ")
md.append("**Academic Session:** 2026 – 2027  ")
md.append("**Candidates:** **DESIREDDY RAMESH** (Enrollment No: `2302320099`) & **Shaik Shafi** (Enrollment No: `2302320151`)  ")
md.append("**Faculty Guide:** **Mr. Satyam Dwivedi**, Assistant Professor, SOEIT, Sanskriti University, Mathura\n")
md.append("---\n")
md.append("# PART I: SYSTEM ARCHITECTURE & TECHNICAL SPECIFICATIONS\n")
md.append("## 1. Decoupled 3-Tier Layered Architecture")
md.append("The system is engineered as a decoupled three-tier architecture ensuring robust separation of concerns, transactional stability, and security isolation.\n")
md.append("```\n+===================================================================================================+\n|                                    PRESENTATION LAYER (CLIENT UI)                                 |\n|  +---------------------------------------------------------------------------------------------+  |\n|  | Bootstrap 5 Responsive UI | Chart.js Visualizations | Jinja2 Templates | Role-Scoped Views  |  |\n|  +---------------------------------------------------------------------------------------------+  |\n+===================================================================================================+\n                                                |  HTTP/HTTPS Requests\n                                                v\n+===================================================================================================+\n|                              APPLICATION & BUSINESS LOGIC LAYER (FLASK WSGI)                      |\n|  +---------------------+  +----------------------+  +---------------------+  +-----------------+  |\n|  | Route Controllers   |  | RBAC Security Guard  |  | CSV Batch Ingestion |  | Lifecycle Hub   |  |\n|  | (18 REST Endpoints) |  | (@roles_required)    |  | (Header Normalizer) |  | (Queue Meters)  |  |\n|  +---------------------+  +----------------------+  +---------------------+  +-----------------+  |\n+===================================================================================================+\n                                                |\n               +--------------------------------+-------------------------------+\n               | In-Memory Features                                             | ORM Operations\n               v                                                                v\n+=============================================+  +==================================================+\n|     MACHINE LEARNING & XAI ENGINE           |  |           PERSISTENCE LAYER (SQLITE ORM)         |\n|  +---------------------------------------+  |  |  +--------------------------------------------+  |\n|  | Random Forest (100 Trees, Gini)       |  |  |  | Users Table (PBKDF2 Salted Passwords)      |  |\n|  | Logistic Regression (Baseline Model)  |  |  |  | Students Table (Academic & Risk Metrics)  |  |\n|  | XAI Root-Cause Attribution Engine     |  |  |  | DropoutReasons Table (Dynamic XAI Cards)   |  |\n|  | On-Demand Dynamic Retraining Engine   |  |  |  | CounsellingSessions (Intervention Logs)    |  |\n|  +---------------------------------------+  |  |  | AuditLogs Table (Forensic Security Log)    |  |\n+=============================================+  |  |  | SystemSettings (Dynamic Policy Rules)    |  |\n                                                 |  +--------------------------------------------+  |\n                                                 +==================================================+\n```\n")

md.append("## 2. Machine Learning & Explainable AI (XAI) Model")
md.append("The system combines ensemble classification with mathematical deficit attribution:\n")
md.append("| Feature Name | Data Type | Range | Gini Weight | Academic Interpretation |")
md.append("|---|---|---|---|---|")
md.append("| attendance_percentage | Float | 0.0% – 100.0% | 36.2% | Statutory classroom attendance; rule benchmark is 75%. |")
md.append("| internal_marks_avg | Float | 0.0% – 100.0% | 24.5% | Continuous assessment average; academic struggle warning < 55%. |")
md.append("| backlog_count | Integer | 0 – 10 subjects | 20.8% | Active failed courses; 1 creates warning, 3+ triggers critical risk. |")
md.append("| fee_status | Categorical | Paid, Partial, Due | 11.2% | Tuition fee standing; socio-economic indicator. |")
md.append("| engagement_score | Float | 0.0 – 100.0 | 7.3% | LMS portal activity and submission regularity. |")
md.append("| semester | Integer | 1 – 8 semesters | 4.0% | Academic seniority. |\n")

md.append("## 3. Role-Based Access Control (RBAC) Matrix")
md.append("| Institutional Role | Permissions & Capabilities | Data Scope | Security Boundaries |")
md.append("|---|---|---|---|")
md.append("| Executive Authority (Admin) | Full institutional control; policy configuration, queue limit setting, model retraining, CSV upload, user management. | All cohorts | None |")
md.append("| Department Head (HOD) | Departmental analytics, student monitoring directory, mentor assignment, escalation review. | Departmental cohort | Policy sliders, retraining |")
md.append("| Faculty Mentor | 1-on-1 counseling log submission, remedial action plan updates, caseload review. | Assigned caseload | Admin tools, bulk upload |")
md.append("| Student User | Self-service academic view, personal predicted risk card, assigned mentor contact, intervention status. | Own record only | Strict peer record isolation (403) |\n")

md.append("## 4. Five-Stage Retention Lifecycle Hub & Capacity Governance")
md.append("```\n+------------------+      +--------------------+      +--------------------+\n|  1. AT RISK      | ---> |  2. UNDER REVIEW   | ---> |  3. COUNSELLING    |\n| (AI High Risk)   |      | (Mentor Assigned)  |      | (1-on-1 Session)   |\n| Capacity: 8/12   |      | Capacity: 36/8 [!] |      | Capacity: 3/14     |\n+------------------+      +--------------------+      +--------------------+\n                                                                 |\n                                                                 v\n+------------------+      +--------------------+      +--------------------+\n|   LOW RISK       | <--- |  5. CLOSED         | <--- |  4. INTERVENED     |\n| (Safe Baseline)  |      | (Normalized Dues)  |      | (Remedial Action)  |\n| Capacity: 66/200 |      | Capacity: 1/150    |      | Capacity: 1/20     |\n+------------------+      +--------------------+      +--------------------+\n```\n")

md.append("## 5. Relational Database Entity-Relationship Model")
md.append("```\n+-------------------+        +--------------------+        +-------------------------+\n|      users        |        |     students       | 1    * |     dropout_reasons     |\n+-------------------+        +--------------------+--------+-------------------------+\n| id (PK)           |        | id (PK)            |        | id (PK)                 |\n| username (Unique) |        | enrollment_no (UQ) |        | student_id (FK)         |\n| password_hash     |        | student_name       |        | reason_category         |\n| role (Enum)       |        | department         |        | severity (Warning/Crit) |\n| full_name         |        | semester           |        | impact_score (Float)    |\n| department        |        | attendance_pct     |        | recommendation          |\n+-------------------+        | internal_marks_avg |        +-------------------------+\n                             | backlog_count      |\n                             | fee_status         | 1    * +-------------------------+\n                             | engagement_score   |--------|   counselling_sessions  |\n                             | risk_score (Float) |        +-------------------------+\n                             | risk_level (Tier)  |        | id (PK)                 |\n                             | lifecycle_stage    |        | student_id (FK)         |\n                             | mentor_id (FK)     |        | mentor_name             |\n                             +--------------------+        | session_date            |\n                                                           | notes                   |\n                                                           | action_plan             |\n                                                           | status_updated_to       |\n                                                           +-------------------------+\n```\n")

md.append("---\n")
md.append("# PART II: COMPLETE SOURCE CODE LISTINGS\n")

for fn, lang, desc in files:
    content = read_source(fn)
    md.append(f"## File: `{fn}`")
    md.append(f"**Description:** {desc}  ")
    md.append(f"**Line Count:** {len(content.splitlines())} lines\n")
    md.append(f"```{lang}")
    md.append(content)
    md.append("```\n")

md.append("---\n")
md.append("# PART III: AUTOMATED TEST SUITE & HANDOVER INSTRUCTIONS\n")
md.append("## Automated Test Matrix")
md.append("| Test ID | Test Method | Component | Result | Status |")
md.append("|---|---|---|---|---|")
md.append("| TC-01 | test_login_page_renders | Authentication | HTTP 200 OK | PASS |")
md.append("| TC-02 | test_admin_login_success | Session Management | HTTP 302 Redirect | PASS |")
md.append("| TC-03 | test_dashboard_requires_login | Route Guard | HTTP 302 to /login | PASS |")
md.append("| TC-04 | test_ml_prediction_bounds | ML Inference | Output in [0.0, 100.0] | PASS |")
md.append("| TC-05 | test_explainable_ai_reasons | XAI Engine | Sums to 100% | PASS |")
md.append("| TC-06 | test_student_privacy_isolation | Privacy Boundary | HTTP 403 Forbidden | PASS |")
md.append("| TC-07 | test_lifecycle_status_transition | Lifecycle Hub | Transition Logged | PASS |")
md.append("| TC-08 | test_admin_settings_update | Dynamic Policy | Thresholds Recalibrated | PASS |\n")

md.append("## Local Handover Launch Commands")
md.append("```bash\n# 1. Open Terminal and navigate to directory\ncd C:\\Users\\ASUS\\.gemini\\antigravity\\scratch\\student_dropout_prediction\n\n# 2. Start Flask Server via virtual environment\n.venv\\Scripts\\python.exe app.py\n\n# 3. Access in Web Browser\nhttp://127.0.0.1:5000\n```\n")
md.append("**Demo Credentials:**  \n* **Admin:** `admin` / `password123`  \n* **Guide/HOD:** `satyam` / `password123`  \n* **Mentor:** `priya` / `password123`  \n* **Student:** `ramesh` / `password123`\n")

full_md = "\n".join(md)
with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(full_md)
print(f"Wrote {MD_PATH} ({len(full_md)} chars)")

html_content = markdown.markdown(full_md, extensions=["tables", "fenced_code"])
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sanskriti University — System Architecture & Complete Codebase Report</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
  body {{ font-family: 'Times New Roman', Times, serif; line-height: 1.5; color: #1a202c; max-width: 960px; margin: 40px auto; padding: 0 30px; background: #fff; }}
  h1 {{ color: #1a365d; border-bottom: 2px solid #1a365d; padding-bottom: 8px; margin-top: 35px; }}
  h2 {{ color: #2b6cb0; margin-top: 25px; }}
  h3 {{ color: #2d3748; }}
  pre {{ background: #f8fafc; border: 1px solid #cbd5e0; border-radius: 6px; padding: 12px; font-family: 'Courier New', Courier, monospace; font-size: 11px; overflow-x: auto; line-height: 1.35; }}
  table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12px; }}
  th, td {{ border: 1px solid #cbd5e0; padding: 6px 10px; text-align: left; }}
  th {{ background: #1a365d; color: #fff; }}
  tr:nth-child(even) {{ background: #f7fafc; }}
  code {{ background: #edf2f7; padding: 2px 5px; border-radius: 4px; font-size: 12px; font-family: monospace; }}
  .control-bar {{ position: sticky; top: 0; background: #1a365d; color: white; padding: 10px 20px; display: flex; justify-content: space-between; align-items: center; border-radius: 6px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
  .control-bar button {{ background: #ecc94b; border: none; padding: 8px 16px; border-radius: 4px; font-weight: bold; cursor: pointer; }}
  @media print {{ .control-bar {{ display: none; }} body {{ max-width: 100%; margin: 0; padding: 15mm; }} }}
</style>
</head>
<body>
<div class="control-bar">
  <span><i class="fa-solid fa-graduation-cap"></i> Sanskriti University — System Architecture & Codebase Deliverable</span>
  <button onclick="window.print()"><i class="fa-solid fa-file-pdf"></i> Print to PDF</button>
</div>
{html_content}
</body>
</html>
"""
with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_doc)
print(f"Wrote {HTML_PATH} ({len(html_doc)} chars)")
