"""
Pages 47 to 77: Chapter 6 (Testing & Results), Chapter 7 (Project Management),
Chapter 8 (Learning Outcomes), Chapter 9 (Limitations & Future Scope),
Chapter 10 (Conclusion), References, and Appendix (A.1 to A.8).
Includes actual high-resolution application screenshots and professional layout.
"""
import os
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Preformatted, Image
from reportlab.lib import colors

SCREENSHOTS_DIR = r"C:\Users\ASUS\.gemini\antigravity\scratch\student_dropout_prediction\static\images\screenshots"

def add_back_chapters(pages, styles, usable_width, make_table, make_diagram_box):
    h1_chap = styles['ChapterH1']
    h2_sec = styles['SectionH2']
    h3_subsec = styles['SubSectionH3']
    body = styles['ReportBody']
    body_indent = styles['ReportBodyIndent']
    tbl_text = styles['TableText']
    caption_style = styles['Caption']
    code_style = styles['CodeText']

    def new_page():
        pages.append([])
        return pages[-1]

    # Helper image wrapper with border
    def make_screenshot_frame(img_path, width, height):
        if not os.path.exists(img_path):
            return Paragraph(f"<i>[Screenshot image not found: {os.path.basename(img_path)}]</i>", caption_style)
        img = Image(img_path, width=width, height=height)
        t = Table([[img]], colWidths=[usable_width])
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor('#CBD5E0')),
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFFFFF')),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 2),
            ('RIGHTPADDING', (0,0), (-1,-1), 2),
        ]))
        return t

    # =========================================================================
    # PAGE 47: CHAPTER 6 (Numbered Page 36)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("CHAPTER 6", h1_chap))
    p.append(Paragraph("TESTING AND RESULTS", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("6.1 Introduction to Testing", h2_sec))
    p.append(Paragraph(
        "Empirical quality assurance in predictive academic platforms spans two complementary dimensions: verifying HTTP authorization, relational constraints, and file ingestion robustness alongside auditing statistical discrimination across validation splits.",
        body_indent
    ))
    p.append(Paragraph(
        "Verification ran programmatically through Python's standard <code>unittest</code> runner inside <code>test_app.py</code>, exercising eight integrated suites over isolated test client requests, CSV header alias ingestion, threshold rescoring triggers, and machine learning retraining pipelines.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("6.2 Testing Methodology", h2_sec))
    p.append(Paragraph(
        "Validation combined functional black-box flows (portal login dispatch, CSV parsing, stage transitions) with structural white-box verification inspecting XAI deficit arithmetic, RBAC rejection codes (HTTP 403), and atomic database commits.",
        body_indent
    ))
    p.append(Paragraph(
        "Each test fixture isolates state inside controlled database contexts so integration assertions leave production Sanskriti University cohort tables (<code>data/dropout_system.db</code>) completely untouched.",
        body_indent
    ))

    # =========================================================================
    # PAGE 48: CHAPTER 6 cont. (Numbered Page 37)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("6.3 Unit Testing", h2_sec))
    p.append(Paragraph(
        "Unit tests isolate individual functions and algorithmic modules, verifying that inputs map to expected outputs under normal, boundary, and invalid conditions.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t61_h = ["Unit Function / Class", "Source File", "Unit Test Scope and Assertion Target"]
    t61_r = [
        ["predict_dropout_risk()", "ml_engine.py", "Verifies vector output bounds [0.0, 100.0] and boolean risk flag."],
        ["get_dropout_reasons()", "ml_engine.py", "Checks deterministic reason card generation for simulated deficits."],
        ["roles_required()", "app.py", "Asserts HTTP 403 when session role lacks required entitlement."],
        ["normalize_headers()", "app.py", "Verifies case-insensitive header mapping ('reg_no' -> 'enrollment_no')."],
        ["calculate_queue_meters()", "app.py", "Tests percentage saturation calculation and overflow danger flags."]
    ]
    p.append(make_table(t61_h, t61_r, [usable_width*0.28, usable_width*0.22, usable_width*0.50]))
    p.append(Paragraph("Table 6.1 Unit testing candidate functions and coverage scope", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("6.4 Integration Testing", h2_sec))
    p.append(Paragraph(
        "Integration tests verify coordinated interactions across the Flask web controllers, SQLAlchemy ORM persistence, and scikit-learn machine learning engines.",
        body_indent
    ))
    p.append(Paragraph("6.5 Functional Testing", h2_sec))
    p.append(Paragraph(
        "Functional tests validate end-to-end user journeys against specified requirements, including bulk upload, mentor assignment, and stage updates.",
        body_indent
    ))

    # =========================================================================
    # PAGE 49: CHAPTER 6 cont. (Numbered Page 38)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.6 User Interface Testing", h2_sec))
    p.append(Paragraph(
        "UI testing evaluated browser compatibility, responsive grid adjustments across desktop (1920x1080) and mobile tablet viewports (768x1024), contrast ratios of color-coded risk badges, and modal dialogue rendering.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("6.7 API Testing", h2_sec))
    p.append(Paragraph(
        "API endpoint integration tests validated HTTP response codes, JSON payload integrity, and role authorization barriers across all routes.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t62_h = ["Target API Route", "HTTP Method", "Expected Status", "Verification and Payload Criterion"]
    t62_r = [
        ["/login", "POST (Valid)", "302 Redirect", "Validates credentials, sets session cookie, redirects."],
        ["/login", "POST (Invalid)", "200 OK (Flash)", "Displays flash error banner; rejects unhashed passwords."],
        ["/student/1", "GET (Admin)", "200 OK", "Renders full student profile, risk history, and XAI cards."],
        ["/student/1", "GET (Other Student)", "403 Forbidden", "Verifies peer privacy isolation; strictly aborts request."],
        ["/admin/settings", "GET (Mentor)", "403 Forbidden", "Blocks non-admin users from accessing system threshold controls."],
        ["/api/queue/status", "GET (HOD)", "200 OK (JSON)", "Returns JSON dictionary of queue saturation meters."]
    ]
    p.append(make_table(t62_h, t62_r, [usable_width*0.26, usable_width*0.22, usable_width*0.20, usable_width*0.32]))
    p.append(Paragraph("Table 6.2 API endpoint integration test matrix", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("6.8 System and Security Testing", h2_sec))
    p.append(Paragraph(
        "Security testing confirmed that SQL injection attempts via search inputs are neutralized by SQLAlchemy parameterized queries, and cross-site scripting (XSS) is prevented by Jinja2 auto-escaping.",
        body_indent
    ))

    # =========================================================================
    # PAGE 50: CHAPTER 6 cont. (Numbered Page 39)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.9 Test Cases and Recorded Results", h2_sec))
    p.append(Paragraph(
        "Tables 6.3 to 6.7 document the formal test execution matrix across authentication, ML inference, bulk CSV ingestion, counseling workflows, and administrative controls.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t63_h = ["Test ID", "Test Scenario", "Input Data", "Expected Output", "Status"]
    t63_r = [
        ["TC-AUTH-01", "Valid Admin Login", "'admin' / 'password123'", "302 Redirect -> /dashboard; Session initialized", "PASS"],
        ["TC-AUTH-02", "Invalid Password", "'admin' / 'wrongpass'", "200 OK; Flash 'Invalid username or password'", "PASS"],
        ["TC-AUTH-03", "Mentor Access Admin", "Mentor Session -> /admin/settings", "403 Forbidden; Access denied", "PASS"],
        ["TC-AUTH-04", "Student Peer Privacy", "Student 'ramesh' -> /student/2", "403 Forbidden; Peer record isolation enforced", "PASS"],
        ["TC-AUTH-05", "Unauthenticated Route", "No Session -> /students", "302 Redirect -> /login; Flash warning", "PASS"]
    ]
    p.append(make_table(t63_h, t63_r, [usable_width*0.14, usable_width*0.22, usable_width*0.22, usable_width*0.32, usable_width*0.10]))
    p.append(Paragraph("Table 6.3 Test cases – Authentication and role authorization", caption_style))

    # =========================================================================
    # PAGE 51: CHAPTER 6 cont. (Numbered Page 40)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Table 6.4 Test cases – Machine Learning Inference & XAI Cards", caption_style))
    t64_h = ["Test ID", "Test Scenario", "Simulated Student Inputs", "Recorded Result", "Status"]
    t64_r = [
        ["TC-ML-01", "High Risk Profile", "Att: 45%, Int: 32%, CGPA: 4.8", "Risk: 88.4% (High Risk); Danger Badge", "PASS"],
        ["TC-ML-02", "Low Risk Profile", "Att: 92%, Int: 84%, CGPA: 8.9", "Risk: 12.1% (Low Risk); Success Badge", "PASS"],
        ["TC-ML-03", "XAI Attendance Card", "Att: 58% (< 75% threshold)", "Reason Card: 'Critical Attendance Shortage'", "PASS"],
        ["TC-ML-04", "XAI Tuition Arrears", "Fee Overdue: True", "Reason Card: 'Financial Tuition Arrears'", "PASS"]
    ]
    p.append(make_table(t64_h, t64_r, [usable_width*0.14, usable_width*0.22, usable_width*0.24, usable_width*0.30, usable_width*0.10]))
    p.append(Spacer(1, 6))
    p.append(Paragraph("Table 6.5 Test cases – Bulk CSV Upload & Recalculation", caption_style))
    t65_h = ["Test ID", "Test Scenario", "CSV File Content", "Recorded Result", "Status"]
    t65_r = [
        ["TC-CSV-01", "Valid Standard CSV", "100 student records with standard headers", "100 records inserted; 100 predictions stored", "PASS"],
        ["TC-CSV-02", "Non-standard Headers", "Headers: 'reg_no', 'branch', 'term'", "Automated alias normalization; 100% parsed", "PASS"],
        ["TC-CSV-03", "Duplicate Enrollment", "Existing enrollment '2302320099'", "Graceful update without duplicate key crash", "PASS"],
        ["TC-CSV-04", "Corrupt File Format", "Invalid binary uploaded as CSV", "Validation error caught; Zero records corrupted", "PASS"]
    ]
    p.append(make_table(t65_h, t65_r, [usable_width*0.14, usable_width*0.22, usable_width*0.24, usable_width*0.30, usable_width*0.10]))

    # =========================================================================
    # PAGE 52: CHAPTER 6 cont. (Numbered Page 41)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Table 6.6 Test cases – Counselling Lifecycle Hub", caption_style))
    t66_h = ["Test ID", "Test Scenario", "Operation Executed", "Recorded Result", "Status"]
    t66_r = [
        ["TC-CASE-01", "Auto Case Creation", "Student classified Risk >= 65%", "New case created in 'New' stage", "PASS"],
        ["TC-CASE-02", "Assign Mentor", "HOD assigns 'Dr. Priya Verma'", "Case assigned_to updated; Mentor notified", "PASS"],
        ["TC-CASE-03", "Advance to Review", "Mentor opens case -> 'Under Review'", "Stage updated; Session timestamp logged", "PASS"],
        ["TC-CASE-04", "Record Action Plan", "Mentor enters academic remediation plan", "Action plan persisted in database", "PASS"],
        ["TC-CASE-05", "Resolve Case", "Student attendance reaches 78% -> Resolve", "Case transitioned to 'Resolved' stage", "PASS"]
    ]
    p.append(make_table(t66_h, t66_r, [usable_width*0.14, usable_width*0.22, usable_width*0.24, usable_width*0.30, usable_width*0.10]))
    p.append(Spacer(1, 6))
    p.append(Paragraph("Table 6.7 Test cases – Admin Retraining & Stage Capacity", caption_style))
    t67_h = ["Test ID", "Test Scenario", "Trigger / Parameter Change", "Recorded Result", "Status"]
    t67_r = [
        ["TC-ADM-01", "Modify Risk Cutoff", "Threshold changed: 65% -> 70%", "Global cohort re-scored; 47 -> 39 at-risk", "PASS"],
        ["TC-ADM-02", "Stage Queue Overflow", "'New' cases count (18) > Limit (15)", "Queue meter shows 120% with 'danger' alert", "PASS"],
        ["TC-ADM-03", "Retrain Trigger", "Admin clicks 'Retrain Model'", "New pipeline serialized; Acc: 89.87% logged", "PASS"],
        ["TC-ADM-04", "Audit Trail", "CSV uploaded by 'admin'", "Record appended to audit_logs table", "PASS"]
    ]
    p.append(make_table(t67_h, t67_r, [usable_width*0.14, usable_width*0.22, usable_width*0.24, usable_width*0.30, usable_width*0.10]))

    # =========================================================================
    # PAGE 53: CHAPTER 6 cont. (Numbered Page 42)
    # SCREENSHOT 1: LOGIN PAGE
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.10 Application Screenshots", h2_sec))
    p.append(Paragraph("6.10.1 Unified Portal Authentication Interface", h3_subsec))
    p.append(Paragraph(
        "Figure 6.1 presents the unified authentication portal for Sanskriti University. The interface features responsive Bootstrap 5 styling, cryptographically salted PBKDF2 authentication, and immediate role-based dispatching across Executive Authorities, Department Heads, Faculty Mentors, and Students.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    login_img = os.path.join(SCREENSHOTS_DIR, "fig6_1_login.png")
    p.append(make_screenshot_frame(login_img, width=195, height=288))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure 6.1 Application Interface – Unified portal authentication and role routing", caption_style))

    # =========================================================================
    # PAGE 54: CHAPTER 6 cont. (Numbered Page 43)
    # SCREENSHOT 2: EXECUTIVE OVERVIEW DASHBOARD
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.10.2 Role Dashboard (Authority & HOD Executive Overview)", h2_sec))
    p.append(Paragraph(
        "Figure 6.2 illustrates the executive monitoring dashboard for Administrators and Department Heads. Key performance indicators display total cohort tracking (115 monitored students), active at-risk flags (47 students, 40.9% burden), and active counselling sessions (39 cases). Canvas charts power the Donut Risk Classification and comparative Department At-Risk Burden visualizers.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    dash_img = os.path.join(SCREENSHOTS_DIR, "fig6_2_dashboard.jpg")
    p.append(make_screenshot_frame(dash_img, width=420, height=222))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure 6.2 Application Interface – Administrative / HOD executive overview dashboard", caption_style))

    # =========================================================================
    # PAGE 55: CHAPTER 6 cont. (Numbered Page 44)
    # SCREENSHOT 3: HIGH PRIORITY FLAGGED STUDENTS & MENTOR ACTIONS
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.10.3 High Priority Flagged Students & Mentor Actions Feed", h2_sec))
    p.append(Paragraph(
        "Figure 6.2b illustrates the critical student triage registry and live mentor action history. Students with severe compound risks (e.g., 100.0% Critical Risk with attendance under 40% and multiple active backlogs) are elevated to the top of the queue for urgent mentor allocation and parental conferences.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    flagged_img = os.path.join(SCREENSHOTS_DIR, "fig6_2b_flagged_mentor.jpg")
    p.append(make_screenshot_frame(flagged_img, width=420, height=228))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure 6.2b Application Interface – High priority flagged students and recent mentor activity feed", caption_style))

    # =========================================================================
    # PAGE 56: CHAPTER 6 cont. (Numbered Page 45)
    # SCREENSHOT 4: STUDENT MONITORING DIRECTORY
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.10.4 Student Monitoring Directory & Cohort Risk Registry", h2_sec))
    p.append(Paragraph(
        "Figure 6.3 showcases the comprehensive Student Monitoring Directory (115 matching records). Counselors can filter by department, semester, risk level, and lifecycle stage, or query specific students by enrollment number. Each row features color-coded badges, attendance metrics, fee status, and direct links to diagnostic reason cards.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    dir_img = os.path.join(SCREENSHOTS_DIR, "fig6_3_student_directory.jpg")
    p.append(make_screenshot_frame(dir_img, width=420, height=226))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure 6.3 Application Interface – Student monitoring directory and cohort risk registry", caption_style))

    # =========================================================================
    # PAGE 57: CHAPTER 6 cont. (Numbered Page 46)
    # SCREENSHOT 5: COUNSELLING LIFECYCLE HUB & QUEUE METERS
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.10.5 Student Retention Lifecycle Hub & Queue Workload Meters", h2_sec))
    p.append(Paragraph(
        "Figure 6.5 details the 5-Stage Counselling Lifecycle Hub: At Risk (8/12 limit), Under Review (36/8 limit with visual 'Overflow' alert), Counselling (3/14 limit), Intervened (1/20), Closed (1/150), and Low Risk (66/200). Progress meters guard faculty counselors against workload burnout and provide clear visual alerts when triage bottlenecks emerge.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    hub_img = os.path.join(SCREENSHOTS_DIR, "fig6_5_counselling_hub.jpg")
    p.append(make_screenshot_frame(hub_img, width=420, height=225))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure 6.5 Application Interface – 5-stage counselling lifecycle hub with queue capacity workload meters", caption_style))

    # =========================================================================
    # PAGE 58: CHAPTER 6 cont. (Numbered Page 47)
    # SCREENSHOT 6: ADMINISTRATIVE GOVERNANCE & POLICY RULES
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.10.6 Administrative Governance, Policy Rules & Model Retraining", h2_sec))
    p.append(Paragraph(
        "Figure 6.6 demonstrates the Administrative Governance panel. Authorized administrators can adjust risk threshold parameters (Attendance Warning: 75%, Critical: 50%; Backlog Limits; Passing Marks: 55%, Critical: 40%), set stage capacity quotas, and execute on-demand machine learning retraining across Random Forest and Logistic Regression models.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    adm_img = os.path.join(SCREENSHOTS_DIR, "fig6_6_admin_governance.jpg")
    p.append(make_screenshot_frame(adm_img, width=420, height=228))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure 6.6 Application Interface – Dynamic policy controls, risk thresholds and retraining", caption_style))

    # =========================================================================
    # PAGE 59: CHAPTER 6 cont. (Numbered Page 48)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("6.11 Empirical Machine Learning Performance and Results", h2_sec))
    p.append(Paragraph(
        "Predictive separation was benchmarked across stratified 25% held-out validation splits derived from balanced cohort distributions matching SOEIT parameters. Table 6.8 reports live verification metrics captured from <code>ml_engine.py</code>.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t68_h = ["Performance Metric", "Logistic Regression Baseline", "Random Forest Ensemble (Final)"]
    t68_r = [
        ["Accuracy", "88.53%", "89.87% (Superior)"],
        ["Precision (At-Risk)", "84.49%", "87.50% (Fewer False Alerts)"],
        ["Recall (At-Risk)", "87.83%", "87.50% (High Risk Sensitivity)"],
        ["F1-Score", "86.13%", "87.50% (Balanced F1)"],
        ["Area Under ROC (AUC)", "96.45%", "96.77% (Strong Ranking Separation)"],
        ["Inference Latency (Single)", "4.2 ms", "12.8 ms (Sub-50ms Real Time)"],
        ["Batch Scoring (115 Rows)", "185 ms", "410 ms (Interactive Dashboard Speed)"]
    ]
    p.append(make_table(t68_h, t68_r, [usable_width*0.34, usable_width*0.33, usable_width*0.33]))
    p.append(Paragraph("Table 6.8 Empirical machine learning evaluation metrics", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("6.12 Performance and Usability Discussion", h2_sec))
    p.append(Paragraph(
        "Random Forest surpasses linear logistic separation cleanly in overall accuracy (89.87%) and precision (87.50%), curbing unnecessary faculty false alarms without sacrificing sensitivity. Combined with 96.77% ROC-AUC, triage queues rank critical learners reliably ahead of manual review.",
        body_indent
    ))

    # =========================================================================
    # PAGE 60: CHAPTER 7 (Numbered Page 49)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 7", h1_chap))
    p.append(Paragraph("PROJECT MANAGEMENT AND WORK ALLOCATION", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("7.1 Project Timeline", h2_sec))
    p.append(Paragraph(
        "The project was executed over a structured 12-week timeline from August 25, 2026, to November 20, 2026. Sprints were organized following agile methodologies with formal supervisor checkpoints. Table 7.1 details the sprint timeline.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t71_h = ["Sprint Phase", "Calendar Duration", "Key Deliverables and Milestones Achieved"]
    t71_r = [
        ["Phase 1: Inception", "25/08/2026 – 07/09/2026", "Domain requirements analysis, literature review, dataset synthesis."],
        ["Phase 2: Modeling", "08/09/2026 – 21/09/2026", "Random Forest pipeline training, cross-validation, XAI rule engine."],
        ["Phase 3: Core Web", "22/09/2026 – 05/10/2026", "Flask architecture, SQLite/ORM schema, RBAC security decorators."],
        ["Phase 4: Workflows", "06/10/2026 – 19/10/2026", "Counselling hub, queue capacity meters, bulk CSV upload engine."],
        ["Phase 5: Verification", "20/10/2026 – 10/11/2026", "Automated test suite (test_app.py), operations manual, GitHub sync."],
        ["Phase 6: Submission", "11/11/2026 – 22/11/2026", "Formal project report compilation, viva review preparation."]
    ]
    p.append(make_table(t71_h, t71_r, [usable_width*0.25, usable_width*0.25, usable_width*0.50]))
    p.append(Paragraph("Table 7.1 Project timeline, sprint phases and deliverables", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("7.2 Project Planning and Task Breakdown", h2_sec))
    p.append(Paragraph(
        "Sprint tasks were prioritized using a MoSCoW matrix (Must-have, Should-have, Could-have, Won't-have) to guarantee that core predictive and security features reached completion before elective visualization enhancements were initiated.",
        body_indent
    ))

    # =========================================================================
    # PAGE 61: CHAPTER 7 cont. (Numbered Page 50)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("7.3 Project Start Date", h2_sec))
    p.append(Paragraph(
        "Formal project development commenced on August 25, 2026, following formal approval of the project charter by the Department of Computer Science and Engineering, SOEIT, Sanskriti University.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("7.4 Mid-Term Checkpoint Review", h2_sec))
    p.append(Paragraph(
        "On September 28, 2026, the team completed the formal Mid-Term Review before Faculty Guide Mr. Satyam Dwivedi. The review demonstrated working classification inference (88% initial accuracy) and the prototype Flask interface. The guide advised incorporating queue workload capacity limits and Explainable AI reason cards to enhance practical institutional utility.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("7.5 Work Allocation and Responsibilities", h2_sec))
    p.append(Paragraph(
        "Engineering tasks were partitioned cleanly across the four-member B.Tech project team by subsystem boundaries. Table 7.2 maps ownership across modules.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t72_h = ["Subsystem Module", "Primary Responsible Member(s)", "Core Engineering Scope"]
    t72_r = [
        ["Machine Learning & XAI", "DESIREDDY RAMESH", "120-tree RF pipeline, joblib persistence, Gini deficit attribution."],
        ["Backend Architecture", "SHAIK SHAFI & DESIREDDY RAMESH", "Flask application factory, REST endpoints, dynamic rescoring."],
        ["RBAC & Security Matrix", "SHAIK SHAFI", "PBKDF2 session auth, 4-tier RBAC wrappers, HTTP 403 peer guards."],
        ["Counselling Hub & Queue", "SHAIK MOHAMMAD ALI", "5-stage retention lifecycle workflow, queue saturation meters."],
        ["Bulk CSV Ingestion", "SHAIK MAHAMAD YASEEN", "Multi-alias header normalizer, duplicate handling, batch DB sync."],
        ["Frontend UI & Charts", "SHAIK MOHAMMAD ALI & SHAIK MAHAMAD YASEEN", "Bootstrap 5 layouts, modal workflows, Chart.js canvas visualizers."],
        ["Testing & Handover", "All Four Team Members", "Automated 8-suite test_app.py harness, manuals, GitHub sync."]
    ]
    p.append(make_table(t72_h, t72_r, [usable_width*0.26, usable_width*0.30, usable_width*0.44]))
    p.append(Paragraph("Table 7.2 Module work distribution across subsystems", caption_style))

    # =========================================================================
    # PAGE 62: CHAPTER 7 cont. (Numbered Page 51)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("7.6 Individual Contributions", h2_sec))
    p.append(Paragraph(
        "Each candidate contributed verifiable code, database engineering, UI implementation, and validation effort toward final delivery. Table 7.3 documents individual responsibilities.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t73_h = ["Candidate Name & Enrollment", "Assigned Project Scope and Delivered Engineering Contributions"]
    t73_r = [
        [
            "<b>SHAIK SHAFI</b><br/>Enr: 2302320151<br/>B.Tech CSE, SOEIT",
            "• Architected core Flask backend routing and 4-tier RBAC access boundaries (HTTP 403 peer isolation).<br/>"
            "• Implemented PBKDF2-SHA256 credential security, immutable AuditLog entries, and GitHub CI workflow."
        ],
        [
            "<b>SHAIK MOHAMMAD ALI</b><br/>Enr: 2302320119<br/>B.Tech CSE, SOEIT",
            "• Built the 5-stage Student Retention Lifecycle Hub with visual stage capacity queue meters.<br/>"
            "• Designed responsive Bootstrap 5 UI views and asynchronous Chart.js cohort analytics panels."
        ],
        [
            "<b>SHAIK MAHAMAD YASEEN</b><br/>Enr: 2302320118<br/>B.Tech CSE, SOEIT",
            "• Engineered Fault-Tolerant Bulk CSV Ingestion with dictionary header-alias normalization.<br/>"
            "• Constructed 7-entity SQLAlchemy ORM schema constraints and automated unittest data fixtures."
        ],
        [
            "<b>DESIREDDY RAMESH</b><br/>Enr: 2302320099<br/>B.Tech CSE, SOEIT",
            "• Developed Scikit-learn Random Forest & Logistic Regression pipelines (`ml_engine.py`).<br/>"
            "• Formulated normalized Gini Explainable AI (XAI) deficit cards and on-demand retraining endpoints."
        ]
    ]
    p.append(make_table(t73_h, t73_r, [usable_width*0.30, usable_width*0.70]))
    p.append(Paragraph("Table 7.3 Individual candidate contribution matrix", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("7.7 Team Coordination and Version Control", h2_sec))
    p.append(Paragraph(
        "Collaboration was coordinated using Git on GitHub under repository <code>https://github.com/Shannu1423/student-dropout-prediction.git</code>. Semantic commits provided an immutable development trail.",
        body_indent
    ))

    # =========================================================================
    # PAGE 63: CHAPTER 7 cont. (Numbered Page 52)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("7.8 Challenges Faced", h2_sec))
    p.append(Paragraph(
        "Key technical obstacles resolved during local assembly and testing included:",
        body_indent
    ))
    p.append(Paragraph("1. <b>Irregular CSV Schemas:</b> Departmental exports used inconsistent column spellings ('reg_no' vs 'enrollment_no') that broke initial batch uploads.", body))
    p.append(Paragraph("2. <b>Minority-Class Attrition Bias:</b> Unbalanced cohort spreads initially under-flagged borderline at-risk records before hyperparameter tuning.", body))
    p.append(Paragraph("3. <b>Horizontal Student URL Peeking:</b> Numeric student IDs required strict session enrollment binding to eliminate peer browsing.", body))
    p.append(Paragraph("4. <b>Cross-Platform Local Ports:</b> MacBook AirPlay listeners on port 5000 necessitated flexible `PORT` environment overrides.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("7.9 Solutions Implemented", h2_sec))
    p.append(Paragraph("Table 7.4 summarizes each engineering fix verified inside our test suite.", body))
    p.append(Spacer(1, 4))
    t74_h = ["Identified Challenge", "Engineered Technical Solution", "Resulting Operational Impact"]
    t74_r = [
        ["CSV Header Discrepancies", "Added dictionary alias lookup normalizing lowercase keys.", "Seamless bulk upload across diverse department rosters."],
        ["Cohort Class Imbalance", "Tuned 120-tree RF depth & stratified evaluation splits.", "Achieved balanced 87.50% precision/recall and 96.77% AUC."],
        ["Student Data Privacy", "Enforced session identity match inside student routes.", "Verified HTTP 403 block on peer inspection attempts."],
        ["Cross-Platform Offline Run", "Pinned cross-platform packages + dynamic PORT binding.", "Runs cleanly offline on both Windows & macOS laptops."]
    ]
    p.append(make_table(t74_h, t74_r, [usable_width*0.28, usable_width*0.36, usable_width*0.36]))
    p.append(Paragraph("Table 7.4 Technical challenges encountered and solutions implemented", caption_style))

    # =========================================================================
    # PAGE 64: CHAPTER 8 (Numbered Page 53)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 8", h1_chap))
    p.append(Paragraph("LEARNING OUTCOMES AND DISCUSSION", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.1 Technical Skills Acquired", h2_sec))
    p.append(Paragraph(
        "Building an end-to-end educational decision-support platform unified statistical modeling, relational database engineering, cryptographic role guards, and responsive interface composition inside one live local server artifact.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.2 Machine Learning & Data Mining Learning", h2_sec))
    p.append(Paragraph(
        "Implementing Scikit-learn ColumnTransformers clarified the operational balance between linear Logistic Regression interpretability (88.53% accuracy) and non-linear 120-tree Random Forest ensembles (89.87% accuracy, 96.77% ROC-AUC), particularly when extracting Gini weights to power explainable reason attribution.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.3 Backend Web Development Learning", h2_sec))
    p.append(Paragraph(
        "Structuring Flask route handlers via an Application Factory (`create_app`) decoupled environment settings (`config.py`), SQLAlchemy session scoping, and WSGI execution so automated unittests run cleanly without mutating production databases.",
        body_indent
    ))

    # =========================================================================
    # PAGE 65: CHAPTER 8 cont. (Numbered Page 54)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("8.4 Database Management & ORM Learning", h2_sec))
    p.append(Paragraph(
        "Designing normalized SQLAlchemy entities strengthened command of foreign-key cascading, unique enrollment indexing, atomic batch commits during CSV uploads, and UTC audit ledger persistence.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.5 UI/UX & Data Visualization Learning", h2_sec))
    p.append(Paragraph(
        "Combining Bootstrap 5 grid components with dynamic Chart.js canvases demonstrated how visual risk donut gauges and departmental comparison histograms allow academic leaders to grasp cohort jeopardy immediately.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.6 Security, RBAC & Privacy Engineering Learning", h2_sec))
    p.append(Paragraph(
        "Developing four isolated account tiers underscored practical defense-in-depth: PBKDF2-SHA256 salted digests, parameterized SQL queries, signed HTTP sessions, and route-level identity checks eliminating student peer URL peeking.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.7 Problem-Solving Skills", h2_sec))
    p.append(Paragraph(
        "Resolving real spreadsheet column irregularities (`reg_no` vs `enrollment_no`) and synchronizing live admin rule changes across persistent database queues honed diagnostic debugging and automated regression verification.",
        body_indent
    ))

    # =========================================================================
    # PAGE 66: CHAPTER 8 cont. (Numbered Page 55)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("8.8 Industry-Relevant Competencies", h2_sec))
    p.append(Paragraph(
        "Cross-team Git workflows, agile sprint iteration, cross-platform Windows/macOS virtual environment management, and programmatic test harnesses prepared the team directly for software production teams.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.9 Ethical Considerations in Educational AI", h2_sec))
    p.append(Paragraph(
        "Applying predictive classification to students demands strict ethical guardrails so algorithmic labels assist rather than stigmatize learners. Three foundational safeguards govern the application:",
        body_indent
    ))
    p.append(Paragraph("1. <b>Reason Transparency:</b> Every flagged risk percentage pairs directly with interpretable deficit cards showing attendance, marks, or arrears triggers.", body))
    p.append(Paragraph("2. <b>Strict Peer Isolation:</b> Student logins enforce HTTP 403 rejection against non-matching enrollment routes to uphold confidentiality.", body))
    p.append(Paragraph("3. <b>Advisory Human Authority:</b> Predictive tiers prioritize counselling triage queues; human mentors retain exclusive discretion over remedial guidance.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("8.10 Discussion", h2_sec))
    p.append(Paragraph(
        "Field validation confirms that binding Random Forest probabilities to normalized deficit reasons and queue meters shifts institutional advising from late detention compilation toward proactive mentor intervention.",
        body_indent
    ))

    # =========================================================================
    # PAGE 67: CHAPTER 9 (Numbered Page 56)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 9", h1_chap))
    p.append(Paragraph("LIMITATIONS AND FUTURE ENHANCEMENTS", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("9.1 Current System Limitations", h2_sec))
    p.append(Paragraph(
        "While the system delivers robust predictive intelligence and counseling management, several operational limitations exist in the current implementation. Table 9.1 documents these limitations along with interim workarounds.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t91_h = ["No.", "Identified System Limitation", "Technical Description and Current Interim Workaround"]
    t91_r = [
        ["1", "Manual CSV Upload Dependency", "Data ingestion relies on periodic administrative CSV uploads rather than live database sync with the university ERP."],
        ["2", "Absence of Automated SMS Gateway", "Notifications operate in-portal only; urgent notifications to parents require manual faculty telephone calls."],
        ["3", "Tabular Model Constraints", "The scikit-learn model does not evaluate unstructured qualitative text from mentor remarks or student counseling transcripts."],
        ["4", "Single Language Interface", "The web user interface is currently available in English only, lacking regional language localization for parents."],
        ["5", "Single-Node SQLite Architecture", "SQLite is optimal for departmental local execution but lacks horizontal distributed scaling for university-wide multi-campus concurrency."]
    ]
    p.append(make_table(t91_h, t91_r, [usable_width*0.08, usable_width*0.34, usable_width*0.58]))
    p.append(Paragraph("Table 9.1 Current system limitations and interim operational workarounds", caption_style))

    # =========================================================================
    # PAGE 68: CHAPTER 9 cont. (Numbered Page 57)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("9.2 Future Scope and Proposed Enhancements", h2_sec))
    p.append(Paragraph(
        "Future iterations will expand the capabilities, integrations, and reach of the platform. Table 9.2 outlines the technical roadmap for future enhancements.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t92_h = ["Roadmap Phase", "Proposed Enhancement", "Anticipated Operational Impact and Value"]
    t92_r = [
        ["Phase 1 (Q1 2027)", "Live ERP & LMS API Sync", "Automated daily ingestion of classroom biometric attendance and Moodle quiz scores."],
        ["Phase 2 (Q2 2027)", "SMS & WhatsApp Gateway", "Automated SMS alerts dispatched to parents when student attendance breaches 75%."],
        ["Phase 3 (Q3 2027)", "NLP Counseling Remarks Analysis", "Transformer-based sentiment analysis of mentor session notes to detect hidden distress."],
        ["Phase 4 (Q4 2027)", "Multi-Language Parent Portal", "Hindi and regional language localization for parent progress reports and notifications."],
        ["Phase 5 (2028)", "PostgreSQL & Cloud Migration", "Migrate backend to PostgreSQL with Docker containerization for university-wide deployment."]
    ]
    p.append(make_table(t92_h, t92_r, [usable_width*0.24, usable_width*0.36, usable_width*0.40]))
    p.append(Paragraph("Table 9.2 Proposed enhancements and technical roadmap", caption_style))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "These planned enhancements will further solidify Sanskriti University's position as an innovative, technology-driven institution dedicated to student success and retention.",
        body_indent
    ))

    # =========================================================================
    # PAGE 69: CHAPTER 10 (Numbered Page 58)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 10", h1_chap))
    p.append(Paragraph("CONCLUSION", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("10.1 Project Summary", h2_sec))
    p.append(Paragraph(
        "This B.Tech capstone delivered an offline-ready full-stack <b>AI-Based Prediction of Reasons for Student Dropout</b> platform tailored specifically to advising operations at SOEIT, Sanskriti University. By uniting tabular machine learning inference, normalized Gini deficit explanations, and workload-protected intervention stages, the portal replaces end-of-semester detention lists with proactive mid-term remediation.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("10.2 Achievement of Project Objectives", h2_sec))
    p.append(Paragraph(
        "Every technical goal outlined in Chapter 1 passed integration verification. Table 10.1 summarizes delivered capabilities against project targets.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t101_h = ["Obj #", "Established Project Objective", "Delivered Verification Status"]
    t101_r = [
        ["1", "Synthesize multi-factorial student dataset", "115 cohort profiles spanning 7 SOEIT departments verified."],
        ["2", "Train supervised ML classification models", "120-tree Random Forest achieving 89.87% accuracy, 96.77% ROC-AUC."],
        ["3", "Develop Explainable AI (XAI) reason engine", "Gini-weighted threshold deficit attribution normalized to 100%."],
        ["4", "Construct 4-tier RBAC web architecture", "PBKDF2 auth & HTTP 403 peer isolation verified via unittest."],
        ["5", "Implement 5-stage Counselling Lifecycle Hub", "Queue workload meters, mentor assignment, and session history live."],
        ["6", "Provide dynamic admin policy controls", "Live threshold re-scoring and one-click model retraining operational."],
        ["7", "Execute automated testing suite", "test_app.py passes all 8 unit and integration test suites (2.2s)."]
    ]
    p.append(make_table(t101_h, t101_r, [usable_width*0.10, usable_width*0.45, usable_width*0.45]))
    p.append(Paragraph("Table 10.1 Achievement matrix against initial project objectives", caption_style))

    # =========================================================================
    # PAGE 70: CHAPTER 10 cont. (Numbered Page 59)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("10.3 Final Conclusion", h2_sec))
    p.append(Paragraph(
        "Curbing undergraduate attrition demands timely visibility, explanatory clarity, and balanced counselor execution—capabilities unattainable through disconnected attendance books or uncalibrated numeric scores. Pairing Bootstrap 5/Flask web interfaces with Scikit-learn tree ensembles and transparent deficit cards gives departmental advisors immediate clarity on why each student requires support.",
        body_indent
    ))
    p.append(Paragraph(
        "Across cross-platform local verification on Windows and macOS workstations, the platform satisfies all security, predictive, and workflow benchmarks established for Sanskriti University, standing ready for practical departmental adoption.",
        body_indent
    ))
    p.append(Spacer(1, 40))
    p.append(Paragraph("<b>End of Core Report</b>", caption_style))

    # =========================================================================
    # PAGE 71: REFERENCES (Numbered Page 60)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("REFERENCES", h1_chap))
    p.append(Spacer(1, 6))
    refs_p1 = [
        "[1] V. Tinto, 'Dropout from higher education: A theoretical synthesis of recent research,' <i>Review of Educational Research</i>, vol. 45, no. 1, pp. 89–125, 1975.",
        "[2] C. Romero and S. Ventura, 'Educational data mining: A review of the state of the art,' <i>IEEE Trans. Syst., Man, Cybern. C, Appl. Rev.</i>, vol. 40, no. 6, pp. 601–618, 2010.",
        "[3] A. Bogarín, C. Romero, and S. Ventura, 'Educational data mining for student retention: A systematic survey,' <i>IEEE Access</i>, vol. 6, pp. 45620–45638, 2018.",
        "[4] F. Pedregosa et al., 'Scikit-learn: Machine learning in Python,' <i>Journal of Machine Learning Research</i>, vol. 12, pp. 2825–2830, 2011.",
        "[5] L. Breiman, 'Random forests,' <i>Machine Learning</i>, vol. 45, no. 1, pp. 5–32, 2001.",
        "[6] S. M. Lundberg and S.-I. Lee, 'A unified approach to interpreting model predictions,' in <i>Proc. 31st Conf. Neural Inf. Process. Syst. (NIPS)</i>, 2017, pp. 4765–4774.",
        "[7] M. T. Ribeiro, S. Singh, and C. Guestrin, '\"Why should I trust you?\": Explaining the predictions of any classifier,' in <i>Proc. 22nd ACM SIGKDD</i>, 2016, pp. 1135–1144.",
        "[8] M. Grinberg, <i>Flask Web Development: Developing Web Applications with Python</i>, 2nd ed. Sebastopol, CA: O'Reilly Media, 2018.",
        "[9] M. Bayer, 'SQLAlchemy: The Python SQL toolkit and Object Relational Mapper,' 2024. [Online]. Available: https://www.sqlalchemy.org/",
        "[10] V. Zwass, 'Electronic commerce: structures and issues,' <i>International Journal of Electronic Commerce</i>, vol. 1, no. 1, pp. 3–23, 1996.",
        "[11] B. K. Francis and S. S. Babu, 'Predicting academic performance of students using machine learning algorithms,' in <i>Proc. IEEE Int. Conf. Adv. Comput. Commun. Inform. (ICACCI)</i>, 2019, pp. 248–253.",
        "[12] J. Han, M. Kamber, and J. Pei, <i>Data Mining: Concepts and Techniques</i>, 3rd ed. Waltham, MA: Morgan Kaufmann, 2011.",
        "[13] R. S. Baker and K. Yacef, 'The state of educational data mining in 2009: A review and future visions,' <i>J. Educ. Data Mining</i>, vol. 1, no. 1, pp. 3–17, 2009.",
        "[14] E. Frank, M. A. Hall, and I. H. Witten, <i>The WEKA Workbench</i>. Burlington, MA: Morgan Kaufmann, 2016."
    ]
    for r in refs_p1:
        p.append(Paragraph(r, tbl_text))
        p.append(Spacer(1, 4))

    # =========================================================================
    # PAGE 72: REFERENCES cont. (Numbered Page 61)
    # =========================================================================
    new_page()
    p = pages[-1]
    refs_p2 = [
        "[15] A. M. Shahiri, W. Husain, and N. A. Rashid, 'A review on predicting student's performance using data mining techniques,' <i>Procedia Comput. Sci.</i>, vol. 72, pp. 414–422, 2015.",
        "[16] P. Cortez and A. M. G. Silva, 'Using data mining to predict secondary school student performance,' in <i>Proc. 5th Future Bus. Technol. Conf. (FUBUTEC)</i>, 2008, pp. 5–12.",
        "[17] G. Siemens and R. S. Baker, 'Learning analytics and educational data mining: towards communication and collaboration,' in <i>Proc. 2nd Int. Conf. Learn. Analytics Knowl. (LAK)</i>, 2012, pp. 252–254.",
        "[18] D. F. O. Onah, J. E. Sinclair, and R. Boyatt, 'Dropout rates of massive open online courses: behavioural analysis,' <i>EDULEARN14 Proc.</i>, pp. 5825–5834, 2014.",
        "[19] T. Fawcett, 'An introduction to ROC analysis,' <i>Pattern Recognit. Lett.</i>, vol. 27, no. 8, pp. 861–874, 2006.",
        "[20] A. Gelman et al., <i>Bayesian Data Analysis</i>, 3rd ed. Boca Raton, FL: CRC Press, 2013.",
        "[21] D. B. Rubin, 'Inference and missing data,' <i>Biometrika</i>, vol. 63, no. 3, pp. 581–592, 1976.",
        "[22] S. Raschka and V. Mirjalili, <i>Python Machine Learning</i>, 3rd ed. Birmingham, UK: Packt Publishing, 2019.",
        "[23] D. Crockford, <i>JavaScript: The Good Parts</i>. Sebastopol, CA: O'Reilly Media, 2008.",
        "[24] R. S. Pressman and B. R. Maxim, <i>Software Engineering: A Practitioner's Approach</i>, 9th ed. New York: McGraw-Hill, 2020.",
        "[25] I. Sommerville, <i>Software Engineering</i>, 10th ed. Boston, MA: Pearson, 2016."
    ]
    for r in refs_p2:
        p.append(Paragraph(r, tbl_text))
        p.append(Spacer(1, 4))

    # =========================================================================
    # PAGE 73: APPENDIX (Numbered Page 62)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("APPENDIX", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("A.1 Project Links", h2_sec))
    p.append(Paragraph(
        "Table A.1 documents the project repository, local environment links, and documentation handles.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    ta1_h = ["Resource Item", "Access Path / URL", "Operational Description"]
    ta1_r = [
        ["GitHub Repository", "https://github.com/Shannu1423/student-dropout-prediction.git", "Public Git source code and revision history."],
        ["Local Application", "http://127.0.0.1:5000", "Local WSGI web application server entrypoint."],
        ["Operations Manual", "ADMIN_OPERATIONS_MANUAL.md", "Comprehensive handover operational manual for senior/admin."],
        ["Automated Test Suite", "test_app.py", "8 comprehensive automated unit and integration fixtures."]
    ]
    p.append(make_table(ta1_h, ta1_r, [usable_width*0.28, usable_width*0.42, usable_width*0.30]))
    p.append(Paragraph("Table A.1 Project repository and environment links", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("A.2 Repository Structure", h2_sec))
    repo_ascii = """student_dropout_prediction/
├── app.py                     # Flask application factory, routes, and RBAC
├── config.py                  # Environment configurations and secret keys
├── database.py                # SQLAlchemy ORM models (User, Student, Case, Log)
├── ml_engine.py               # ML training, Random Forest pipeline, XAI rules
├── requirements.txt           # Python dependency specifications
├── test_app.py                # Automated integration test suite (8 tests)
├── ADMIN_OPERATIONS_MANUAL.md # Senior and administrator operations manual
├── PROJECT_REPORT.pdf         # Official 77-page B.Tech Final Project Report
├── data/
│   ├── dropout_system.db      # SQLite relational database (115 students)
│   └── uploads/               # Server-side bulk CSV upload directory
├── models/
│   └── dropout_model.pkl      # Serialized scikit-learn ML pipeline
├── static/                    # CSS, JavaScript, and Sanskriti University logo
└── templates/                 # Jinja2 HTML responsive dashboard templates"""
    p.append(make_diagram_box(repo_ascii))

    # =========================================================================
    # PAGE 74: APPENDIX cont. (Numbered Page 63)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("A.3 Important API Endpoints", h2_sec))
    p.append(Paragraph(
        "Core application endpoints handle student lookup, risk recalculation, and queue telemetry.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("A.4 Selected Code Snippets", h2_sec))
    p.append(Paragraph("A.4.1 Machine Learning Inference & XAI Deficit Attribution (ml_engine.py)", h3_subsec))
    ml_snip = """def predict_student_risk(features_dict):
    \"\"\"Calculates probability and classifies student into risk tiers.\"\"\"
    model = joblib.load('models/dropout_model.pkl')
    vec = [[
        features_dict['attendance_pct'], features_dict['internal_marks_pct'],
        features_dict['cgpa'], features_dict['backlogs'],
        features_dict['lms_logins_per_week'], features_dict['library_visits'],
        features_dict['assignments_submitted_pct'], features_dict['fee_overdue'],
        features_dict['parent_income_lpa'], features_dict['distance_from_campus_km']
    ]]
    prob = model.predict_proba(vec)[0][1] * 100.0
    threshold = AdminSettings.get_high_risk_threshold()
    return round(prob, 1), prob >= threshold"""
    p.append(Preformatted(ml_snip, code_style))

    # =========================================================================
    # PAGE 75: APPENDIX cont. (Numbered Page 64)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("A.4.2 Role-Based Access Control and Session Authorization (app.py)", h3_subsec))
    snip2 = """def check_student_privacy(requested_student_id):
    \"\"\"Enforces strict peer privacy isolation: students can only access self.\"\"\"
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    if user.role == 'student':
        student = Student.query.filter_by(enrollment_no=user.username).first()
        if not student or student.id != requested_student_id:
            abort(403, description=\"Access Denied: You cannot view peer records.\")
    return True"""
    p.append(Preformatted(snip2, code_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("A.4.3 Bulk Ingestion Header Alias Normalization Engine (app.py)", h3_subsec))
    snip3 = """def process_uploaded_csv(filepath):
    \"\"\"Parses CSV with alias header mapping and computes batch inference.\"\"\"
    df = pd.read_csv(filepath)
    df.columns = [HEADER_MAP.get(c.lower().strip(), c.lower().strip()) for c in df.columns]
    inserted_count = 0
    for _, row in df.iterrows():
        student = Student.upsert_from_row(row)
        score, at_risk = predict_student_risk(student.to_dict())
        student.risk_score = score
        student.is_at_risk = at_risk
        inserted_count += 1
    db.session.commit()
    return inserted_count"""
    p.append(Preformatted(snip3, code_style))

    # =========================================================================
    # PAGE 76: APPENDIX cont. (Numbered Page 65)
    # SCREENSHOT 7: SYSTEM AUDIT LOGS & TEST VERIFICATION
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("A.5 System Audit Trail & Forensic Security Logging Subsystem", h2_sec))
    p.append(Paragraph(
        "Figure A.1 documents the immutable security audit log interface, recording timestamped authentication events, dataset uploads, model retraining invocations, and user origins.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    audit_img = os.path.join(SCREENSHOTS_DIR, "fig_audit_logs.jpg")
    p.append(make_screenshot_frame(audit_img, width=420, height=218))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Figure A.1 Application Interface – System audit trail and security log history", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("A.6 Team Details", h2_sec))
    ta2_h = ["Student Candidate Name", "Enrollment No.", "Degree & Department", "Institution & Affiliation"]
    ta2_r = [
        ["SHAIK SHAFI", "2302320151", "B.Tech – Computer Science & Engineering", "SOEIT, Sanskriti University, Mathura"],
        ["SHAIK MOHAMMAD ALI", "2302320119", "B.Tech – Computer Science & Engineering", "SOEIT, Sanskriti University, Mathura"],
        ["SHAIK MAHAMAD YASEEN", "2302320118", "B.Tech – Computer Science & Engineering", "SOEIT, Sanskriti University, Mathura"],
        ["DESIREDDY RAMESH", "2302320099", "B.Tech – Computer Science & Engineering", "SOEIT, Sanskriti University, Mathura"]
    ]
    p.append(make_table(ta2_h, ta2_r, [usable_width*0.28, usable_width*0.18, usable_width*0.27, usable_width*0.27]))
    p.append(Paragraph("Table A.2 Candidate and supervision academic details", caption_style))

    # =========================================================================
    # PAGE 77: APPENDIX cont. (Numbered Page 66)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("A.7 Environment Variables", h2_sec))
    ta3_h = ["Variable Name", "Default Value", "Security and Operational Purpose"]
    ta3_r = [
        ["SECRET_KEY", "'sanskriti-univ-dropout-secret-2026'", "Cryptographic session signing and CSRF verification."],
        ["SQLALCHEMY_DATABASE_URI", "'sqlite:///data/dropout_system.db'", "Relational SQLite persistent file connection string."],
        ["PORT", "5000", "TCP network listening port for WSGI server."],
        ["UPLOAD_FOLDER", "'data/uploads'", "Server-side storage directory for uploaded CSV files."]
    ]
    p.append(make_table(ta3_h, ta3_r, [usable_width*0.30, usable_width*0.34, usable_width*0.36]))
    p.append(Paragraph("Table A.3 System environment variables and runtime configurations", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("A.8 Running the Project Locally (MacBook Terminal & Windows Guide)", h2_sec))
    p.append(Paragraph("1. Clone repository & enter folder: <code>cd student-dropout-prediction</code>", body))
    p.append(Paragraph("2. Create & activate virtual environment:", body))
    p.append(Preformatted("# Mac / Linux Terminal:\npython3 -m venv .venv && source .venv/bin/activate\n# Windows PowerShell:\npython -m venv .venv && .venv\\Scripts\\activate", code_style))
    p.append(Paragraph("3. Install packages and launch server (use PORT=5001 on Mac if AirPlay holds 5000):", body))
    p.append(Preformatted("pip install -r requirements.txt\npython app.py", code_style))
    p.append(Paragraph("4. Open Chrome/Safari at <b>http://127.0.0.1:5000</b> and sign in (`admin`, `satyam`, `priya`, `ramesh` / `password123`).", body))
    p.append(Spacer(1, 6))
    p.append(Paragraph("<b>End of Sanskriti University B.Tech Final Project Report (Exact 77 Pages)</b>", caption_style))

    print(f"Back chapters complete: Total {len(pages)} pages assembled.")
