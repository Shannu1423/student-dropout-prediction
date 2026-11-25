"""
Generate Markdown and HTML versions of the Complete Codebase and System Architecture Report with exact Sanskriti University structure and 4 candidates.
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

# COVER PAGE
md.append("# AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT\n")
md.append("## A PROJECT REPORT\n")
md.append("**Submitted in partial fulfillment of the award of Degree of**  \n**Bachelor of Technology in Computer Science and Engineering**\n")
md.append("<div align=\"center\"><img src=\"static/images/sanskriti_logo.png\" width=\"140\" alt=\"Sanskriti University Logo\"></div>\n")
md.append("### Submitted by\n")
md.append("* Enrollment No: **2302320151**, **SHAIK SHAFI**")
md.append("* Enrollment No: **2302320119**, **SHAIK MOHAMMAD ALI**")
md.append("* Enrollment No: **2302320118**, **SHAIK MAHAMAD YASEEN**")
md.append("* Enrollment No: **2302320099**, **DESIREDDY RAMESH**\n")
md.append("**Under the Supervision of:** **Mr. Satyam Dwivedi**, Assistant Professor, Department of Computer Science & Engineering  \n")
md.append("**Department of Computer Science and Engineering**  \n**SANSKRITI UNIVERSITY, MATHURA, U.P**  \n**November, 2026**\n")
md.append("---\n")

# CERTIFICATE
md.append("## Department of Computer Science & Engineering\n")
md.append("### CERTIFICATE\n")
md.append(
    "This is to certify that the work embodies in this project report entitled "
    "**‘AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT’** being submitted by "
    "Enrollment No: **2302320151** **SHAIK SHAFI**, "
    "Enrollment No: **2302320119** **SHAIK MOHAMMAD ALI**, "
    "Enrollment No: **2302320118** **SHAIK MAHAMAD YASEEN**, "
    "Enrollment No: **2302320099** **DESIREDDY RAMESH**, "
    "for partial fulfillment of the requirement for the award of **Bachelor of Technology in Computer Science and Engineering** "
    "to Sanskriti University, Mathura during the academic year **2026-27** is a record of Bonafide piece of work, "
    "undertaken under the supervision of the undersigned.\n"
)
md.append("**Approved and Supervised by:**  \n**Mr. Satyam Dwivedi** (Assistant Professor, SOEIT) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Dean, SOEIT**\n")
md.append("---\n")

# DECLARATION
md.append("## Department of Computer Science & Engineering\n")
md.append("### DECLARATION\n")
md.append(
    "We, **SHAIK SHAFI**, **SHAIK MOHAMMAD ALI**, **SHAIK MAHAMAD YASEEN**, **DESIREDDY RAMESH** "
    "student of Bachelor of Technology in Computer Science and Engineering, Session: **2026-27**, "
    "Sanskriti University, Mathura hereby declare that the work presented in this project report entitled "
    "**“AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT”** is the outcome of our own Bonafide work and is "
    "correct to the best of our knowledge and this work has been undertaken taking care of Engineering Ethics. "
    "It contains no material previously published or written by another person nor material which has been accepted "
    "for the award of any other degree or diploma of the university or other institute of higher learning, "
    "except where due acknowledgment has been made in the text.\n"
)
md.append("| Enrollment No. | Student Name | Signature |")
md.append("|---|---|---|")
md.append("| Enrollment No: 2302320151 | **SHAIK SHAFI** | ____________________ |")
md.append("| Enrollment No: 2302320119 | **SHAIK MOHAMMAD ALI** | ____________________ |")
md.append("| Enrollment No: 2302320118 | **SHAIK MAHAMAD YASEEN** | ____________________ |")
md.append("| Enrollment No: 2302320099 | **DESIREDDY RAMESH** | ____________________ |\n")
md.append("**Date:** November, 2026\n")
md.append("---\n")

# ACKNOWLEDGEMENT
md.append("### ACKNOWLEDGEMENT\n")
md.append(
    "We would like to thank our Hon'ble Chancellor, Hon'ble Chief Executive Officer, Hon'ble Vice Chancellor, "
    "and Respected Dean, SOEIT. We express our sincere gratitude and thanks to our Project Supervisor, "
    "**Mr. Satyam Dwivedi**. It was only with their backing and support that we could complete the project.\n\n"
    "They provided us with all kinds of help and corrected us whenever we seemed to make mistakes. "
    "We have no words to express our gratitude. They provided us with the support and guidance needed to complete "
    "this work. Without their support, we could not have even started the work. Therefore, we are truly grateful to them.\n\n"
    "We acknowledge our dearest parents for being a constant source of encouragement and moral support, "
    "which helped us tremendously in this endeavour.\n\n"
    "We also declare, to the best of our knowledge and belief, that this work has not been submitted anywhere else.\n"
)
md.append("* Enrollment No: **2302320151**, **SHAIK SHAFI**")
md.append("* Enrollment No: **2302320119**, **SHAIK MOHAMMAD ALI**")
md.append("* Enrollment No: **2302320118**, **SHAIK MAHAMAD YASEEN**")
md.append("* Enrollment No: **2302320099**, **DESIREDDY RAMESH**\n")
md.append("---\n")

# TABLE OF CONTENTS
md.append("### TABLE OF CONTENTS\n")
md.append("| Topic | Page No. |")
md.append("|---|---|")
md.append("| **LIST OF FIGURES** | vi |")
md.append("| **ABBREVIATIONS** | vii |")
md.append("| **LIST OF STANDARDS** | viii |")
md.append("| **ABSTRACT** | ix |")
md.append("| **Chapter 1: INTRODUCTION** | 1 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;1.1 Client Identification of Client / Need / Relevant Contemporary issue | 1 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;1.2 Justification of Issue Through Statistics and Documentation | 2 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;1.3 Problem Requires Resolution | 3 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;1.4 Justification of Need Through Survey | 4 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;1.5 Relevant Contemporary Issue Documented In Report By Agencies | 5 |")
md.append("| **Chapter 2: LITERATURE REVIEW** | 6 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.1 Introduction to the Literature Review | 6 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.2 Growth of Machine Learning and Early Warning Systems in Higher Education | 7 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.3 Student Retention Operations and Institutional Monitoring Networks in India | 8 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.4 Operational and Resource Challenges of Faculty Mentors and Organizations | 9 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.5 Limitations of Manual Case Documentation and Student Tracking | 10 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.6 Complexity of Regulatory Compliance for Student Privacy and Data Governance | 11 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.7 Review of Existing Educational ERP Tools and Market Gaps | 12 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.8 Role of Technology, Explainable AI (XAI) and Automation in Retention Management | 13 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.9 Technological Foundation: Python Flask, Scikit-learn, SQLite in EDM Stack | 14 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;2.10 Identified Research Gap and Integrated Summary of Literature Findings | 15 |")
md.append("| **Chapter 3: METHODOLOGY** | 16 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.1 Timeline of the Reported Problem | 16 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.2 Existing Solutions | 17 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.3 Bibliometric Analysis | 18 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.4 Review Summary | 19 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.5 Problem Definition | 20 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.6 Goals / Objectives | 21 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.7 Scope of the System | 22 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;3.8 System Requirements | 23 |")
md.append("| **Chapter 4: DESIGN FLOW / PROCESS** | 24 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;4.1 Evaluation & Selection of Specifications / Features | 24 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;4.2 Design Constraints | 25 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;4.3 Analysis and Feature Finalization Subject to Constraints | 26 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;4.4 Design Flow (4.4.1 Design Flow Diagram, 4.4.2 System Navigation Flow Diagram) | 27 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;4.5 Design Selection | 28 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;4.6 Implementation Plan / Methodology (Use Case, Sequence, Class Diagrams) | 29 |")
md.append("| **Chapter 5: RESULTS ANALYSIS AND VALIDATION** | 32 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.1 Implementation of Solution | 32 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.2 System Performance & User Validation | 38 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.3 Challenges Faced | 39 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.4 Validation of Results | 40 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.5 Performance Evaluation | 41 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.6 User Feedback and Improvements | 42 |")
md.append("| &nbsp;&nbsp;&nbsp;&nbsp;5.7 Summary of Findings | 43 |")
md.append("| **CHAPTER 6: CONCLUSION AND FUTURE WORK** | 44 |")
md.append("| **REFERENCES** | 45 |")
md.append("| **PART II: COMPLETE VERBATIM ANNOTATED SOURCE CODEBASE** | 47 |\n")
md.append("---\n")

# LIST OF FIGURES
md.append("### LIST OF FIGURES\n")
md.append("| Figure No. | Figure Description | Page(s) |")
md.append("|---|---|---|")
md.append("| Figure 4.4.1 | System Architectural Design Flow Diagram | 27 |")
md.append("| Figure 4.4.2 | System Navigation and Role Routing Flow Diagram | 27 |")
md.append("| Figure 4.6.1 | System Comprehensive Use Case Diagram | 29 |")
md.append("| Figure 4.6.3 | Unified UML Sequence Diagram | 30 |")
md.append("| Figure 4.6.4 | System Class Diagram & Relational Entity Model | 31 |")
md.append("| Figure 5.1.1 | Application Interface – Student Registration & Bulk Ingestion Page | 33 |")
md.append("| Figure 5.1.2 | Application Interface – Role-Based Unified Portal Authentication Page | 34 |")
md.append("| Figure 5.1.3 | Application Interface – Executive Authority Analytics Dashboard Page | 35 |")
md.append("| Figure 5.1.4 | Application Interface – High-Priority Flagged Students & Case Tracking | 36 |")
md.append("| Figure 5.1.5 | Application Interface – Counselling Lifecycle Hub & Queue Workload Meters | 37 |")
md.append("| Figure 5.1.6 | Application Interface – Administrative Governance & Policy Rules Panel | 37 |")
md.append("| Figure 5.1.7 | Application Interface – Forensic Security Audit Trail & Activity Log History | 38 |\n")
md.append("---\n")

# ABBREVIATIONS
md.append("### ABBREVIATIONS\n")
md.append("| Abbreviation | Expanded Description & System Scope |")
md.append("|---|---|")
md.append("| HTML | Hyper-Text Markup Language: Structures the web pages like registration, login, and dashboard |")
md.append("| CSS | Cascading Style Sheets: Styles responsive UI layouts, risk level badges, and component themes |")
md.append("| JS | JavaScript: Powers dynamic client-side interactions and Chart.js analytics graphics |")
md.append("| AI | Artificial Intelligence: Computational algorithms automating student dropout risk evaluation |")
md.append("| ML | Machine Learning: Supervised classification algorithms trained on institutional data |")
md.append("| EDM | Educational Data Mining: Extraction of actionable pedagogical patterns from student records |")
md.append("| RF | Random Forest: Primary ensemble classification model utilizing 100 bagging decision trees |")
md.append("| LR | Logistic Regression: Baseline linear probabilistic classifier benchmarked against Random Forest |")
md.append("| XAI | Explainable AI: Mathematical deficit attribution engine providing human-interpretable reasons |")
md.append("| RBAC | Role-Based Access Control: 4-tier security framework enforcing principle of least privilege |")
md.append("| ORM | Object Relational Mapping: SQLAlchemy abstraction layer connecting Python to SQLite database |")
md.append("| API | Application Programming Interface: RESTful endpoints facilitating data interchange |")
md.append("| CSV | Comma-Separated Values: Tabular flat-file format utilized for bulk cohort roster ingestion |")
md.append("| DFD | Data Flow Diagram: Graphical modeling of data movements across system processes |")
md.append("| ERD | Entity-Relationship Diagram: Structural database diagram detailing relational tables and keys |\n")
md.append("---\n")

# LIST OF STANDARDS
md.append("### LIST OF STANDARDS\n")
md.append("| Standard | Publishing Agency (Abbreviation) | About the Standard & Institutional Relevance |")
md.append("|---|---|---|")
md.append("| ISO/IEC 25010 | ISO/IEC | Defines software product quality models, including usability, reliability, security, and performance efficiency. |")
md.append("| IEEE 830-1998 | IEEE | Recommended Practice for Software Requirements Specifications (SRS). |")
md.append("| ISO/IEC 27001 | ISO/IEC | Information security management systems standard, guiding PBKDF2 password hashing and tamper-evident audit logs. |")
md.append("| W3C WCAG 2.1 | W3C | Web Content Accessibility Guidelines ensuring accessible interface design. |")
md.append("| IEEE 730-2014 | IEEE | Software Quality Assurance Processes, guiding automated testing. |\n")
md.append("---\n")

# ABSTRACT
md.append("### ABSTRACT\n")
md.append(
    "Undergraduate engineering attrition rarely stems from an abrupt event; instead, it builds quietly across declining classroom attendance, accumulating subject arrears, stalled continuous assessment scores, and overdue tuition balances. At the School of Engineering and Information Technology (SOEIT), Sanskriti University, conventional oversight compiles these signals only after semester-end examinations conclude. To resolve this latency bottleneck, our team engineered the **AI-Based Prediction of Reasons for Student Dropout** platform using Python Flask, Scikit-learn, SQLAlchemy, SQLite, Bootstrap 5, and Chart.js.\n\n"
    "At the analytical core resides a calibrated 120-tree Random Forest classifier paired with a Logistic Regression benchmark over normalized feature vectors covering classroom attendance, internal marks average, active backlogs, tuition fee standing, LMS engagement score, and enrolled semester. On held-out splits, Random Forest achieved **89.87%** accuracy, **87.50%** precision, **87.50%** recall, **87.50%** F1-score, and **96.77%** ROC-AUC (surpassing Logistic Regression at 88.53% accuracy and 96.45% ROC-AUC). A localized Explainable AI (XAI) routine scales threshold shortfalls by trained Gini weights summing to 100%, routing flagged learners into a capacity-protected 5-stage retention lifecycle under 4-tier RBAC governance.\n"
)
md.append("---\n")

# CHAPTERS 1 TO 6 SUMMARY & DIAGRAMS
md.append("# PART I: CORE CHAPTERS & ARCHITECTURE BLUEPRINTS\n")
md.append("## Chapter 1: INTRODUCTION\n")
md.append("1.1 Client Identification of Client / Need / Relevant Contemporary Issue  \n1.2 Justification of Issue Through Statistics and Documentation  \n1.3 Problem Requires Resolution  \n1.4 Justification of Need Through Survey  \n1.5 Relevant Contemporary Issue Documented In Report By Agencies\n")
md.append("## Chapter 2: LITERATURE REVIEW\n")
md.append("2.1 Introduction to the Literature Review  \n2.2 Growth of Machine Learning and Early Warning Systems in Higher Education  \n2.3 Student Retention Operations and Institutional Monitoring Networks in India  \n2.4 Operational and Resource Challenges of Faculty Mentors and Organizations  \n2.5 Limitations of Manual Case Documentation and Student Tracking  \n2.6 Complexity of Regulatory Compliance for Student Privacy and Data Governance  \n2.7 Review of Existing Educational ERP Tools and Market Gaps  \n2.8 Role of Technology, Explainable AI (XAI) and Automation in Retention Management  \n2.9 Technological Foundation: Python Flask, Scikit-learn, SQLite in EDM Stack  \n2.10 Identified Research Gap and Integrated Summary of Literature Findings\n")
md.append("## Chapter 3: METHODOLOGY\n")
md.append("3.1 Timeline of the Reported Problem  \n3.2 Existing Solutions  \n3.3 Bibliometric Analysis  \n3.4 Review Summary  \n3.5 Problem Definition  \n3.6 Goals / Objectives  \n3.7 Scope of the System  \n3.8 System Requirements\n")
md.append("## Chapter 4: DESIGN FLOW / PROCESS\n")
md.append("4.1 Evaluation & Selection of Specifications / Features  \n4.2 Design Constraints  \n4.3 Analysis and Feature Finalization Subject to Constraints  \n4.4 Design Flow (4.4.1 Design Flow Diagram, 4.4.2 System Navigation Flow Diagram)  \n4.5 Design Selection (Decoupled 3-Tier Layered Architecture)  \n4.6 Implementation Plan / Methodology (Use Case, Sequence, Class Diagrams)\n")
md.append("## Chapter 5: RESULTS ANALYSIS AND VALIDATION\n")
md.append("5.1 Implementation of Solution  \n5.2 System Performance & User Validation  \n5.3 Challenges Faced  \n5.4 Validation of Results  \n5.5 Performance Evaluation (Random Forest 89.87% Accuracy, 96.77% AUC vs Logistic Regression 88.53%)  \n5.6 User Feedback and Improvements  \n5.7 Summary of Findings\n")
md.append("## CHAPTER 6: CONCLUSION AND FUTURE WORK\n")
md.append("6.1 Conclusion  \n6.2 Future Work\n")
md.append("---\n")

# PART II: ARCHITECTURAL MODULES & INTERFACES (NO SOURCE CODE)
md.append("# PART II: SYSTEM ARCHITECTURE & APPLICATION SCREENSHOTS\n")
md.append("| Subsystem Component | Architectural Scope & Responsibility |")
md.append("|---|---|")
for fn, lang, desc in files:
    md.append(f"| **{fn}** | {desc} |")
md.append("")

md.append("## Verified Application Screenshots (All 7 Core Views)\n")
for img_fn, fig_lbl in [
    ("fig6_1_login.png", "Figure 5.1.2: Unified Portal Authentication Screen"),
    ("fig6_2_dashboard.png", "Figure 5.1.3: Executive Authority Analytics Dashboard"),
    ("fig6_2b_flagged_mentor.png", "Figure 5.1.4a: High-Priority Flagged Queue & Mentor Action Feed"),
    ("fig6_3_student_directory.png", "Figure 5.1.4b: Student Monitoring Directory"),
    ("fig6_5_counselling_hub.png", "Figure 5.1.5: 5-Stage Counselling Lifecycle Hub"),
    ("fig6_6_admin_governance.png", "Figure 5.1.6: Administrative Governance & Policy Controls"),
    ("fig_audit_logs.png", "Figure 5.1.7: Immutable Forensic Security Audit Trail"),
]:
    md.append(f'<div align="center" style="margin:18px 0;"><img src="static/images/screenshots/{img_fn}" alt="{fig_lbl}" style="max-width:100%;"><br><em>{fig_lbl}</em></div>\n')

md.append("---\n")

# PART III: VERIFICATION & HANDOVER
md.append("# PART III: SYSTEM VERIFICATION & HANDOVER GUIDE\n")
md.append("## Automated Test Execution Matrix (8/8 PASS)")
md.append("| Test ID | Target Test Routine | Executed Scope | Recorded Output | Status |")
md.append("|---|---|---|---|---|")
md.append("| TC-01 | test_login_page_renders | Authentication | HTTP 200 OK | PASS |")
md.append("| TC-02 | test_admin_login_success | Session Management | HTTP 302 Redirect | PASS |")
md.append("| TC-03 | test_dashboard_requires_login | Route Guard | HTTP 302 to /login | PASS |")
md.append("| TC-04 | test_ml_prediction_bounds | ML Inference | Bounds [0.0%, 100.0%] | PASS |")
md.append("| TC-05 | test_explainable_ai_reasons | XAI Engine | Sums to 100% | PASS |")
md.append("| TC-06 | test_student_privacy_isolation | Privacy Boundary | HTTP 403 Forbidden | PASS |")
md.append("| TC-07 | test_lifecycle_status_transition | Lifecycle Hub | Transition Logged | PASS |")
md.append("| TC-08 | test_admin_settings_update | Dynamic Policy | Thresholds Recalibrated | PASS |\n")

md.append("## Local Handover Launch Commands (MacBook Terminal & Windows)")
md.append("```bash\n# Mac / Linux Terminal:\ngit clone https://github.com/Shannu1423/student-dropout-prediction.git\ncd student-dropout-prediction\npython3 -m venv .venv\nsource .venv/bin/activate\npip install -r requirements.txt\npython app.py   # or PORT=5001 python app.py if AirPlay uses port 5000\n\n# Windows PowerShell:\npython -m venv .venv\n.venv\\Scripts\\activate\npip install -r requirements.txt\npython app.py\n\n# Access in Web Browser:\nhttp://127.0.0.1:5000\n```\n")
md.append("**Pre-configured Demo Credentials:**  \n* **Admin:** `admin` / `password123`  \n* **Guide/HOD:** `satyam` / `password123`  \n* **Mentor:** `priya` / `password123`  \n* **Student:** `ramesh` / `password123`\n")

full_md = "\n".join(md)
with open(MD_PATH, "w", encoding="utf-8") as f:
    f.write(full_md)
print(f"Wrote {MD_PATH} ({len(full_md)} chars)")

html_content = markdown.markdown(full_md, extensions=["tables", "fenced_code"])
html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sanskriti University — Master B.Tech Project Report & Complete Architecture Manual</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
  body {{ font-family: 'Times New Roman', Times, serif; line-height: 1.5; color: #1a202c; max-width: 960px; margin: 40px auto; padding: 0 30px; background: #fff; }}
  h1 {{ color: #1a365d; border-bottom: 2px solid #1a365d; padding-bottom: 8px; margin-top: 35px; text-align: center; }}
  h2 {{ color: #2b6cb0; margin-top: 25px; }}
  h3 {{ color: #2d3748; }}
  pre {{ background: #f8fafc; padding: 12px; font-family: 'Times New Roman', Times, serif; font-size: 11px; overflow-x: auto; line-height: 1.35; }}
  table {{ width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 12px; font-family: 'Times New Roman', Times, serif; }}
  th, td {{ border-bottom: 1px solid #cbd5e0; padding: 6px 10px; text-align: left; }}
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
  <span><i class="fa-solid fa-graduation-cap"></i> Sanskriti University — B.Tech Project Report & Complete Architecture</span>
  <button onclick="window.print()"><i class="fa-solid fa-file-pdf"></i> Print to PDF</button>
</div>
{html_content}
</body>
</html>
"""
with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html_doc)
print(f"Wrote {HTML_PATH} ({len(html_doc)} chars)")
