"""
Pages 16 to 46: Chapter 2 (Literature Review), Chapter 3 (System Analysis),
Chapter 4 (System Design), and Chapter 5 (System Implementation).
"""
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Preformatted
from reportlab.lib import colors

def add_middle_chapters(pages, styles, usable_width, make_table, make_diagram_box):
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

    # =========================================================================
    # PAGE 16: CHAPTER 2 (Numbered Page 5)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("CHAPTER 2", h1_chap))
    p.append(Paragraph("LITERATURE REVIEW", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.1 Introduction", h2_sec))
    p.append(Paragraph(
        "Empirical investigation into why undergraduates discontinue degree programs bridges educational sociology and applied data science. Expanding enrollment across technical universities has turned early dropout screening from an informal mentor intuition exercise into an essential administrative engineering discipline.",
        body_indent
    ))
    p.append(Paragraph(
        "This chapter evaluates theoretical persistence frameworks, benchmarks supervised classification models suited for tabular university data, reviews modern web-deployment stacks, and examines localized Explainable Artificial Intelligence (XAI) designs that earn advisor confidence.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.2 Evolution of Student Retention Systems", h2_sec))
    p.append(Paragraph(
        "Foundational sociological theories, notably Tinto’s institutional integration model (1975), attributed early undergraduate departure to weakening academic performance and social disconnectedness within campus life. Operational monitoring in earlier decades depended on physical departmental registers and mid-term roll tallies—workflows plagued by delayed tabulations and inability to detect interacting distress factors.",
        body_indent
    ))
    p.append(Paragraph(
        "Although Campus Management Systems (CMS) and Learning Management Platforms digitized attendance and examination scores during the 2000s, legacy dashboards remained purely backward-looking, reporting past failures rather than warning faculty mid-term. Contemporary analytics couples historical learner telemetry with predictive classifiers to trigger outreach weeks ahead of examination debarment.",
        body_indent
    ))

    # =========================================================================
    # PAGE 17: CHAPTER 2 cont. (Numbered Page 6)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.3 Review of Machine Learning Algorithms in Higher Education", h2_sec))
    p.append(Paragraph(
        "Prior educational data mining studies test several supervised classifiers on tabular student cohorts. Logistic Regression supplies clean probabilistic odds ratios, yet assumes linear additivity and underperforms when attrition accelerates non-linearly across concurrent shortfalls such as simultaneous attendance decline and unpaid tuition fees.",
        body_indent
    ))
    p.append(Paragraph(
        "Standalone Decision Trees yield transparent threshold rules familiar to educators, yet display high split instability whenever modest cohort distributions shift. Radial-kernel Support Vector Machines isolate complex boundaries cleanly, yet conceal individual variable influence behind geometric margin transforms that faculty mentors cannot translate into counselling guidance.",
        body_indent
    ))
    p.append(Paragraph(
        "Random Forest ensembles overcome single-tree variance by averaging decorrelated classifiers trained across bootstrap samples and random feature subsets. For institutional educational records spanning continuous grades and discrete fee statuses, Random Forests deliver resilient non-linear generalization, calibrated dropout probabilities, and normalized Gini impurity feature rankings.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.4 Review of Existing Technologies", h2_sec))
    p.append(Paragraph(
        "Converting research classifiers into reliable daily institutional tooling requires careful software architecture across runtime execution, embedded relational persistence, and lightweight browser rendering.",
        body_indent
    ))

    # =========================================================================
    # PAGE 18: CHAPTER 2 cont. (Numbered Page 7)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.4.1 Flask and Scikit-Learn Frameworks", h3_subsec))
    p.append(Paragraph(
        "Python anchors applied institutional machine learning through Scikit-learn's unified ColumnTransformer, StandardScaler, OneHotEncoder, and ensemble APIs. Hosting trained pipelines directly within a Flask WSGI application avoids separate microservice serialization hops, keeping real-time student evaluation latency below 50 milliseconds.",
        body
    ))
    p.append(Paragraph("2.4.2 SQLite and SQLAlchemy ORM", h3_subsec))
    p.append(Paragraph(
        "SQLAlchemy provides strongly typed declarative ORM mapping alongside parameterized SQL safety against injection vectors. Pairing SQLAlchemy with zero-configuration embedded SQLite gives universities ACID-compliant local storage portable across Windows and macOS without dedicated database administrators.",
        body
    ))
    p.append(Paragraph("2.4.3 Bootstrap 5 and Chart.js UI", h3_subsec))
    p.append(Paragraph(
        "Consistent visual ergonomics across administrative desktops and mentor laptops rely on Bootstrap 5 CSS grids without legacy jQuery dependencies. Chart.js canvas components render smooth risk donut graphs and departmental bar comparisons directly client-side from compact JSON endpoints.",
        body
    ))
    p.append(Spacer(1, 4))
    t21_h = ["Technology Component", "Selected Framework", "Evaluation & Technical Rationale"]
    t21_r = [
        ["Backend Web Core", "Python 3.11+ / Flask 3.x", "In-process Python ML scoring, compact footprint, portable WSGI server"],
        ["Machine Learning", "scikit-learn 1.3+ / joblib", "ColumnTransformer pipelines, probability outputs, fast disk persistence"],
        ["Persistence Layer", "SQLite 3 + SQLAlchemy 2.x", "Zero-daemon offline storage, atomic commits, normalized FK relations"],
        ["Frontend UI/UX", "Bootstrap 5.3 + FontAwesome", "Responsive layout grids, accessible color semantics, zero jQuery"],
        ["Data Visualizer", "Chart.js 4.x (Canvas API)", "Smooth interactive rendering of cohort distributions & attrition predictors"]
    ]
    p.append(make_table(t21_h, t21_r, [usable_width*0.28, usable_width*0.28, usable_width*0.44]))
    p.append(Paragraph("Table 2.1 Technology stack selection and evaluation rationale", caption_style))

    # =========================================================================
    # PAGE 19: CHAPTER 2 cont. (Numbered Page 8)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.4.4 Token-Based Authentication and Password Security", h3_subsec))
    p.append(Paragraph(
        "Protecting academic performance ledgers demands strict defense-in-depth authentication. User credentials must undergo salted cryptographic stretching via PBKDF2-SHA256 prior to disk persistence, paired with HMAC-signed Flask session cookies that enforce role-scoped route access across every protected controller.",
        body
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.5 Explainable AI (XAI) in Educational Analytics", h2_sec))
    p.append(Paragraph(
        "Unexplained numeric warnings routinely stall institutional adoption: if software assigns an 88% attrition risk without stating whether classroom absenteeism or mounting subject arrears caused the alert, mentors cannot plan targeted parental outreach or subject tutoring during short counselling windows.",
        body_indent
    ))
    p.append(Paragraph(
        "While generic perturbation tools such as SHAP and LIME provide strong post-hoc mathematical theory, repeated sampling multiplies latency during bulk CSV cohort uploads and outputs complex additive plots unfamiliar to academic counsellors.",
        body_indent
    ))
    p.append(Paragraph(
        "To resolve this clarity gap cleanly, our system computes closed-form threshold deficit attributions scaled directly by trained Random Forest Gini feature weights—delivering instant percentage breakdowns paired with tailored remediation advice.",
        body_indent
    ))

    # =========================================================================
    # PAGE 20: CHAPTER 2 cont. (Numbered Page 9)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.6 Comparative Analysis of Existing Systems", h2_sec))
    p.append(Paragraph(
        "Table 2.2 contrasts architectural capabilities across three distinct institutional software tiers: standard campus ERPs, standalone research notebooks, and our integrated Sanskriti University early-warning hub.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t22_h = ["System Capability", "Commercial Campus ERP", "Generic ML Research Scripts", "Proposed Dropout Prediction System"]
    t22_r = [
        ["Predictive Analytics", "None (Descriptive reports only)", "High (Jupyter notebook models)", "High (120-Tree RF calibrated scoring)"],
        ["Explainable Diagnostics", "Not Supported", "Complex perturbation plots", "Normalized 100% XAI deficit cards"],
        ["Counselling Workflow", "Basic static remarks field", "Not Supported", "5-Stage lifecycle queue + capacity meters"],
        ["Role-Based Privacy", "Coarse-grained departmental", "None (Single user execution)", "4-Tier RBAC with HTTP 403 peer blocks"],
        ["Dynamic Policy Controls", "Hardcoded vendor schema", "Requires code edits", "Live admin GUI threshold recalibration"],
        ["Offline Deployment", "Cloud SaaS dependent", "Manual local scripting", "Self-contained Windows/Mac offline app"]
    ]
    p.append(make_table(t22_h, t22_r, [usable_width*0.25, usable_width*0.25, usable_width*0.25, usable_width*0.25]))
    p.append(Paragraph("Table 2.2 Comparative analysis with existing educational retention tools", caption_style))
    p.append(Paragraph("2.7 Research Gap and Identified Problems", h2_sec))
    p.append(Paragraph(
        "Published software leaves three persistent omissions: disconnected research classifiers never advance into trackable mentor workflows; raw scores hide actionable causes; and flat spreadsheets leak sensitive student standings to peers. This project resolves all three limitations.",
        body
    ))
    p.append(Paragraph("2.8 Summary", h2_sec))
    p.append(Paragraph(
        "Critical review supports coupling a Random Forest ensemble with closed-form Gini deficit attribution inside a Flask/SQLAlchemy platform tailored for capacity-managed university mentoring.",
        body
    ))

    # =========================================================================
    # PAGE 21: CHAPTER 3 (Numbered Page 10)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 3", h1_chap))
    p.append(Paragraph("SYSTEM ANALYSIS AND REQUIREMENTS", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.1 Existing System", h2_sec))
    p.append(Paragraph(
        "Institutional tracking at SOEIT, Sanskriti University historically operated across separate departmental workflows: subject instructors recorded attendance manually, internal quiz marks accumulated inside local spreadsheets, and tuition balances sat within accounts ledgers. HODs reviewed aggregate detention tallies only near semester examination cutoff dates.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.2 Limitations of the Existing System", h2_sec))
    p.append(Paragraph("Auditing manual monitoring procedures exposed four structural vulnerabilities:", body))
    p.append(Paragraph("1. <b>Severe Reporting Latency:</b> Detention reviews occur weeks before term exams, leaving scant time for meaningful academic remediation.", body))
    p.append(Paragraph("2. <b>Fragmented Multi-Office Records:</b> Separating fee arrears from classroom attendance prevents advisors from seeing compounding risk.", body))
    p.append(Paragraph("3. <b>Inconsistent Triage Criteria:</b> Manual roster scanning across 60+ advisees per mentor yields subjective selection rather than objective risk ranking.", body))
    p.append(Paragraph("4. <b>Untracked Case Outcomes:</b> Verbal counselling or paper remarks lack stage progression timestamps, capacity alarms, and institutional auditability.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.3 Proposed System", h2_sec))
    p.append(Paragraph(
        "Our proposed full-stack web platform consolidates multi-factor learner records inside one encrypted portal, evaluates normalized dropout probabilities upon registration or CSV upload, renders prioritized XAI reason breakdowns, and manages counsellor interventions across five bounded workflow stages.",
        body_indent
    ))

    # =========================================================================
    # PAGE 22: CHAPTER 3 cont. (Numbered Page 11)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.4 Advantages of the Proposed System", h2_sec))
    p.append(Paragraph("Consolidating prediction and advisor workflows introduces measurable institutional gains:", body))
    p.append(Paragraph("• <b>Early Risk Synthesis:</b> Scoring runs automatically on single registration or CSV upload, opening intervention windows mid-semester.", body))
    p.append(Paragraph("• <b>Transparent Factor Weights:</b> Deterministic Gini deficit cards quantify attendance, internal mark, or fee triggers cleanly.", body))
    p.append(Paragraph("• <b>Caseload Safeguards:</b> Stage capacity meters alert HODs whenever active mentoring queues breach configured limits.", body))
    p.append(Paragraph("• <b>Strict Learner Confidentiality:</b> Server-side session binding blocks horizontal peer inspection across student logins.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.5 Functional Requirements", h2_sec))
    p.append(Paragraph(
        "Table 3.1 enumerates core platform modules implemented across authentication, prediction, explainability, bulk ingestion, and administrative governance.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t31_h = ["Req ID", "Functional Module", "Detailed Functional Requirement Specification"]
    t31_r = [
        ["FR-01", "User Authentication", "Secure login with PBKDF2 hashing, role authorization, and session expiration."],
        ["FR-02", "Predictive ML Engine", "Automated execution of calibrated ensemble inference returning probabilities [0-100%]."],
        ["FR-03", "XAI Reason Attribution", "Deterministic evaluation generating reason cards with remediation guidance."],
        ["FR-04", "Bulk Ingestion", "CSV file parsing with automated header alias mapping, validation, and batch insert."],
        ["FR-05", "Counselling Lifecycle", "5-stage progression tracking (New, Under Review, In Progress, Resolved, Escalated)."],
        ["FR-06", "Queue Capacity Meters", "Real-time calculation of workload percentages and visual overflow alerts."],
        ["FR-07", "Admin Policy Controls", "Form-based dynamic adjustment of risk thresholds and immediate cohort re-scoring."],
        ["FR-08", "Model Retraining", "On-demand execution of training pipeline with live accuracy metrics reporting."],
        ["FR-09", "Audit Logging", "Immutable security ledger logging user actions, timestamp, IP, and event status."]
    ]
    p.append(make_table(t31_h, t31_r, [usable_width*0.14, usable_width*0.28, usable_width*0.58]))
    p.append(Paragraph("Table 3.1 Functional requirements specification matrix", caption_style))

    # =========================================================================
    # PAGE 23: CHAPTER 3 cont. (Numbered Page 12)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.6 Non-Functional Requirements", h2_sec))
    p.append(Paragraph(
        "Quality attributes establish measurable runtime latency, offline self-containment, credential cryptography, and browser compatibility constraints governing deployment.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t32_h = ["Quality Attribute", "Specification and Verification Criteria"]
    t32_r = [
        ["Inference Latency", "Ensemble scoring + Gini attribution execute under 50ms per single learner."],
        ["Bulk Throughput", "Batch CSV ingestion and cohort scoring for 500 records finish within 3s."],
        ["Data Privacy", "Horizontal student peer leakage blocked strictly by session ID checks (HTTP 403)."],
        ["System Availability", "Zero external cloud dependencies; runs 100% offline over embedded SQLite."],
        ["Cryptographic Security", "Credentials stored via salted PBKDF2-HMAC-SHA256 stretching routines."],
        ["Browser Compatibility", "Verified rendering on Safari 15+, Chrome 90+, Edge 90+, and Firefox 88+."]
    ]
    p.append(make_table(t32_h, t32_r, [usable_width*0.30, usable_width*0.70]))
    p.append(Paragraph("Table 3.2 Non-functional requirements specification matrix", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.7 Software Requirements", h2_sec))
    p.append(Paragraph(
        "Table 3.3 lists pinned Python and frontend packages verified cleanly on Windows and macOS workstations.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t33_h = ["Software Component", "Verified Production Version", "Role in System Architecture"]
    t33_r = [
        ["Operating System", "Windows 10/11, macOS 13+, Ubuntu 22", "Cross-platform WSGI server runtime host"],
        ["Programming Language", "Python 3.11+", "Core backend logic and Scikit-learn runtime"],
        ["Web Microframework", "Flask 3.0+", "HTTP request routing, session cookies, REST endpoints"],
        ["ORM / Persistence", "SQLAlchemy 2.0+ + SQLite 3", "Declarative ORM schema and ACID transactional commits"],
        ["Machine Learning", "scikit-learn 1.3+, joblib 1.3+", "ColumnTransformer, Random Forest training & serialization"],
        ["Data Manipulation", "pandas 2.0+, numpy 1.24+", "CSV alias normalization and numerical array processing"],
        ["Frontend UI Toolkit", "Bootstrap 5.3 + Chart.js 4", "Mobile-ready layouts and interactive canvas visualizations"]
    ]
    p.append(make_table(t33_h, t33_r, [usable_width*0.28, usable_width*0.28, usable_width*0.44]))
    p.append(Paragraph("Table 3.3 Software requirements and version environment", caption_style))

    # =========================================================================
    # PAGE 24: CHAPTER 3 cont. (Numbered Page 13)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.8 Hardware Requirements", h2_sec))
    p.append(Paragraph(
        "Designed without GPU acceleration requirements, the server operates smoothly on standard laboratory desktops or faculty laptops.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t34_h = ["Hardware Component", "Minimum Host Server Specification", "Recommended Client Terminal Specification"]
    t34_r = [
        ["Processor (CPU)", "x86_64 Dual Core / Apple Silicon M1+", "Any modern 1.5 GHz dual-core terminal"],
        ["System Memory (RAM)", "4 GB DDR4 (8 GB recommended)", "2 GB minimum browser RAM"],
        ["Persistent Storage", "500 MB free space (Code, SQLite DB, Pickle)", "100 MB free browser cache"],
        ["Network Interface", "Local loopback (127.0.0.1) or campus LAN", "Campus Wi-Fi / Ethernet link to host"],
        ["Display Resolution", "1280 x 720 (HD) minimum", "1920 x 1080 recommended"]
    ]
    p.append(make_table(t34_h, t34_r, [usable_width*0.28, usable_width*0.36, usable_width*0.36]))
    p.append(Paragraph("Table 3.4 Hardware specifications for host and client devices", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.9 Feasibility Study", h2_sec))
    p.append(Paragraph(
        "We evaluated deployment viability across three institutional dimensions prior to construction:",
        body_indent
    ))
    p.append(Paragraph(
        "• <b>Technical Feasibility:</b> Mature open-source Python packages (Flask, Scikit-learn, SQLite) eliminate third-party cloud latency and single-vendor lock-in, confirming strong local execution resilience.",
        body
    ))
    p.append(Paragraph(
        "• <b>Operational Feasibility:</b> Clear semantic alert tiers (Critical, High Risk, Moderate Risk, Low Risk) and visual queue meters enable HODs and advisors to adopt daily triage without heavy training.",
        body
    ))
    p.append(Paragraph(
        "• <b>Economic Feasibility:</b> Permissive BSD/MIT licensing across every framework produces zero licensing expenditure while operating directly on existing university hardware.",
        body
    ))

    # =========================================================================
    # PAGE 25: CHAPTER 3 cont. (Numbered Page 14)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.10 Use Case Analysis", h2_sec))
    p.append(Paragraph(
        "Four institutional personas interact with distinct workflows inside protected permission boundaries summarized in Table 3.5.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t35_h = ["Actor Role", "Primary Use Case / Goal", "Operational Description and System Boundaries"]
    t35_r = [
        ["Administrator", "System Management & Policy", "Edit global risk rules, trigger live retraining, audit security ledgers, set stage quotas."],
        ["Guide / HOD", "Department Cohort Oversight", "Review cohort risk charts, ingest semester CSVs, delegate advisors, manage escalations."],
        ["Faculty Mentor", "Student Counselling & Progression", "Inspect assigned advisee XAI deficit cards, record session notes, update intervention stages."],
        ["Student", "Personal Monitoring & Advice", "Inspect strictly own attendance, continuous marks, risk standing, and remediation advice."]
    ]
    p.append(make_table(t35_h, t35_r, [usable_width*0.22, usable_width*0.32, usable_width*0.46]))
    p.append(Paragraph("Table 3.5 Use case actor-goal interaction summary", caption_style))
    p.append(Paragraph(
        "Authorization wrappers evaluate active session credentials prior to running any protected controller: unprivileged requests hitting `/admin/settings` or foreign `/student/<id>` URLs abort immediately with HTTP 403 and log the attempt.",
        body_indent
    ))

    # =========================================================================
    # PAGE 26: CHAPTER 4 (Numbered Page 15)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 4", h1_chap))
    p.append(Paragraph("SYSTEM DESIGN AND METHODOLOGY", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.1 System Architecture", h2_sec))
    p.append(Paragraph(
        "Decoupling presentation templates, WSGI/ML inference logic, and relational SQLite persistence ensures classifier updates (`ml_engine.py`) and threshold tuning require zero HTML rewrites and simplify automated unit testing.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t41_h = ["Architectural Tier", "Constituent Technologies", "Functional Responsibilities"]
    t41_r = [
        ["Presentation Tier", "Bootstrap 5.3, HTML5, Jinja2, Chart.js", "Generates responsive role dashboards, modals, capacity bars, and analytics canvases."],
        ["Application Logic Tier", "Flask 3.x, Werkzeug, Scikit-learn", "Enforces 4-tier RBAC, runs 120-tree RF scoring, computes Gini XAI deficits."],
        ["Data Persistence Tier", "SQLAlchemy ORM, SQLite 3 Engine", "Maintains 3NF tables, ACID batch commits, session cases, and immutable audit logs."]
    ]
    p.append(make_table(t41_h, t41_r, [usable_width*0.25, usable_width*0.35, usable_width*0.40]))
    p.append(Paragraph("Table 4.1 Architectural tiers and decoupled system responsibilities", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.2 Overall Architecture Overview", h2_sec))
    p.append(Paragraph(
        "Figure 4.1 maps end-to-end communication between client browsers, Flask security middleware, Scikit-learn inference pipelines, and SQLite persistence.",
        body_indent
    ))

    # =========================================================================
    # PAGE 27: CHAPTER 4 cont. (Numbered Page 16)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Figure 4.1 Overall 3-Tier Architecture Diagram", caption_style))
    arch_ascii = """
+-----------------------------------------------------------------------------+
|                            PRESENTATION TIER                                |
|  [Admin Dashboard]   [HOD Overview]   [Mentor Hub]   [Student Portal View]  |
|  Bootstrap 5.3 CSS   |  Chart.js Visualizer  |  Jinja2 Server-Side Engine   |
+-----------------------------------------------------------------------------+
                                      | HTTP Requests / JSON APIs
                                      v
+-----------------------------------------------------------------------------+
|                          APPLICATION LOGIC TIER                             |
|  +-------------------------+  +-------------------+  +-------------------+  |
|  | Flask Web Router        |  | RBAC Security     |  | Case Lifecycle    |  |
|  | WSGI Application Engine |  | Session Auth      |  | 5-Stage Hub       |  |
|  +-------------------------+  +-------------------+  +-------------------+  |
|                                      |
|                                      v
|  +-----------------------------------------------------------------------+  |
|  | MACHINE LEARNING SUBSYSTEM (ml_engine.py)                             |  |
|  | [Data Preprocessor] -> [Random Forest Classifier] -> [Probability]    |  |
|  | [Rule Attributor]   -> [Deficit Diagnostic Engine]-> [XAI Reason Card]|  |
|  +-----------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------+
                                      | SQLAlchemy ORM Queries
                                      v
+-----------------------------------------------------------------------------+
|                           PERSISTENCE TIER                                  |
|  [SQLite 3 Database: data/dropout_system.db]                                |
|  * users  * students  * counselling_cases  * audit_logs  * admin_settings   |
+-----------------------------------------------------------------------------+
"""
    p.append(make_diagram_box(arch_ascii))
    p.append(Spacer(1, 6))
    p.append(Paragraph("4.3 Machine Learning Pipeline Architecture", h2_sec))
    p.append(Paragraph(
        "The machine learning subsystem comprises five sequential stages: (1) feature normalization and encoding; (2) feature vector construction across 10 continuous and categorical variables; (3) probability estimation via calibrated Random Forest ensembles; (4) classification threshold evaluation; and (5) localized deficit attribution.",
        body_indent
    ))

    # =========================================================================
    # PAGE 28: CHAPTER 4 cont. (Numbered Page 17)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("4.4 Backend Web Architecture and Route Mapping", h2_sec))
    p.append(Paragraph(
        "The Flask backend follows a modular, RESTful URL routing schema. Table 4.2 documents the primary web routes and their operational security constraints.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t42_h = ["HTTP Route", "Method", "Role Entitlement", "Functional Purpose and Security Guard"]
    t42_r = [
        ["/login", "GET, POST", "Public", "Authenticates credentials, initializes signed session cookie."],
        ["/logout", "GET", "All Authenticated", "Clears session, logs logout event, redirects to login."],
        ["/dashboard", "GET", "All Authenticated", "Role-aware dispatcher directing user to customized view."],
        ["/students", "GET", "Admin, Guide, Mentor", "Cohort risk registry with search, filter, and color badges."],
        ["/student/<id>", "GET", "Admin, Guide, Mentor, Student*", "Deep-dive profile; student restricted strictly to self."],
        ["/upload-csv", "GET, POST", "Admin, Guide", "Bulk student CSV file ingestion and header alias mapping."],
        ["/counselling", "GET", "Admin, Guide, Mentor", "5-stage counselling workflow hub with queue capacity meters."],
        ["/counselling/<id>/update", "POST", "Admin, Guide, Mentor", "Advances case stage, assigns mentor, records session remarks."],
        ["/admin/settings", "GET, POST", "Admin Only", "Modifies global risk thresholds and stage capacity limits."],
        ["/admin/retrain", "POST", "Admin Only", "Executes model retraining pipeline and reports new metrics."]
    ]
    p.append(make_table(t42_h, t42_r, [usable_width*0.26, usable_width*0.14, usable_width*0.24, usable_width*0.36]))
    p.append(Paragraph("Table 4.2 Client-side and administrative web routing architecture", caption_style))

    # =========================================================================
    # PAGE 29: CHAPTER 4 cont. (Numbered Page 18)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("4.5 Database Architecture", h2_sec))
    p.append(Paragraph(
        "The relational database schema is structured to ensure 3NF (Third Normal Form) compliance, referential integrity through foreign key constraints, and transactional consistency. The schema encompasses 7 primary entities: users, students, counselling_cases, audit_logs, admin_settings, stage_limits, and student_risk_factors.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.6 Data Flow Diagram – Level 0 (Context Level)", h2_sec))
    p.append(Paragraph(
        "The Level 0 Data Flow Diagram (Figure 4.2) models the high-level boundary of the Dropout Prediction System, showing data exchanges between external user roles and the core system process.",
        body_indent
    ))

    # =========================================================================
    # PAGE 30: CHAPTER 4 cont. (Numbered Page 19)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Figure 4.2 Data Flow Diagram – Level 0 (Context Level)", caption_style))
    dfd0_ascii = """
       +------------------+                    +------------------+
       |                  | -- Student Data -> |                  |
       |  ADMINISTRATOR   | -- Policy Limits-> |                  |
       |                  | <- Audit Logs ---- |                  |
       +------------------+                    |                  |
                                               |                  |
       +------------------+                    |                  |
       |                  | -- Review Request->|  AI-BASED        |
       |   GUIDE / HOD    | <- Risk Alerts --- |  STUDENT         |
       |                  | -- Mentor Assign-> |  DROPOUT         |
       +------------------+                    |  PREDICTION      |
                                               |  SYSTEM          |
       +------------------+                    |  (PROCESS 0)     |
       |                  | <- At-Risk Queue - |                  |
       |  FACULTY MENTOR  | -- Case Remarks -> |                  |
       |                  | -- Action Plans -> |                  |
       +------------------+                    |                  |
                                               |                  |
       +------------------+                    |                  |
       |                  | -- Credentials --> |                  |
       |     STUDENT      | <- Own Profile --- |                  |
       +------------------+                    +------------------+
"""
    p.append(make_diagram_box(dfd0_ascii))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.7 Data Flow Diagram – Level 1 (Subsystem Decomposition)", h2_sec))
    p.append(Paragraph(
        "The Level 1 DFD decomposes Process 0 into four functional sub-processes: Authentication & Authorization (1.0), Ingestion & Preprocessing (2.0), ML Inference & XAI Reason Attribution (3.0), and Counselling Case Lifecycle Management (4.0).",
        body_indent
    ))

    # =========================================================================
    # PAGE 31: CHAPTER 4 cont. (Numbered Page 20)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Figure 4.3 Data Flow Diagram – Level 1", caption_style))
    dfd1_ascii = """
  [User Credentials] -> (1.0 Auth & RBAC) ---------> [User Store]
                               |
                        [Role Token]
                               v
  [CSV/Registration] -> (2.0 Ingest & Clean) ------> [Student Store]
                               |
                        [Clean Vector]
                               v
                        (3.0 ML & XAI Engine) -----> [Predictions]
                               |
                        [Risk & Reason Cards]
                               v
  [Mentor Actions] ---> (4.0 Counselling Hub) -----> [Case Store]
                               |
                        [Audit Events]
                               v
                        (5.0 Security Logger) -----> [Audit Store]
"""
    p.append(make_diagram_box(dfd1_ascii))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.8 Use Case Diagram", h2_sec))
    p.append(Paragraph(
        "Figure 4.4 models actor interactions across system boundaries, distinguishing administrative system governance from mentor counseling and student self-service.",
        body_indent
    ))

    # =========================================================================
    # PAGE 32: CHAPTER 4 cont. (Numbered Page 21)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Figure 4.5 Activity Diagram – Risk Evaluation and Intervention Lifecycle", caption_style))
    act_ascii = """
   (Start: Student Data Ingestion)
                  |
                  v
       [Validate Academic Fields]
                  |
                  +--- Is Valid CSV? ---> [No] -> (Raise Validation Error)
                  |
                 [Yes]
                  v
       [Construct Feature Vector]
                  |
                  v
       [ML Ensemble Risk Scoring]
                  |
                  +--- Probability >= Threshold (65%)?
                  |                        |
                 [No]                     [Yes]
                  |                        v
                  |              [Generate XAI Deficit Cards]
                  |                        |
                  |                        v
                  |              [Create Counselling Case: 'New']
                  |                        |
                  |                        v
                  |              [Evaluate Queue Capacity Limit]
                  |                        |
                  |                        +--- Exceeds Limit? -> [Alert HOD]
                  |                        v
                  |              [Mentor Conducts Session & Records Action Plan]
                  |                        |
                  v                        v
        (Persist Student)        (Transition: 'Resolved' or 'Escalated')
                  |                        |
                  +------------------------+
                               |
                               v
                            (Finish)
"""
    p.append(make_diagram_box(act_ascii))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.10 Sequence Diagram Overview", h2_sec))
    p.append(Paragraph(
        "The Sequence Diagram captures temporal message passing between the Client Browser, Web Router, ML Inference Engine, and the Database layer during prediction recalculation.",
        body_indent
    ))

    # =========================================================================
    # PAGE 33: CHAPTER 4 cont. (Numbered Page 22)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Figure 4.6 Sequence Diagram – Prediction and Lifecycle Progression", caption_style))
    seq_ascii = """
 Client Browser        Flask Router        ML Engine         SQLAlchemy DB
       |                     |                 |                   |
       |--- POST /upload --->|                 |                   |
       |                     |--- parse CSV -->|                   |
       |                     |                 |--- batch insert ->|
       |                     |                 |<-- success -------|
       |                     |--- predict() -->|                   |
       |                     |<-- risk score --|                   |
       |                     |--- XAI cards -->|                   |
       |                     |<-- reason list -|                   |
       |                     |--- save case ---------------------->|
       |                     |<-- case created --------------------|
       |<-- 200 OK Redirect -|                 |                   |
       |                     |                 |                   |
"""
    p.append(make_diagram_box(seq_ascii))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.11 Entity Relationship (ER) Diagram", h2_sec))
    p.append(Paragraph(
        "Figure 4.7 details entity relationships, cardinalities, primary keys, and foreign keys across the persistence tier.",
        body_indent
    ))

    # =========================================================================
    # PAGE 34: CHAPTER 4 cont. (Numbered Page 23)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Figure 4.7 Entity Relationship Diagram", caption_style))
    erd_ascii = """
  +------------------+         1:N         +-----------------------+
  |      USERS       |-------------------->|   COUNSELLING_CASES   |
  | PK: id           |                     | PK: id                |
  |     username     |                     | FK: student_id        |
  |     password_hash|                     | FK: assigned_to (user)|
  |     role         |                     |     stage             |
  +------------------+                     |     notes             |
          |                                +-----------------------+
          | 1:N                                        ^
          v                                            | 1:N
  +------------------+         1:1                     |
  |    AUDIT_LOGS    |                     +-----------------------+
  | PK: id           |                     |       STUDENTS        |
  | FK: user_id      |                     | PK: id                |
  |     action       |                     |     enrollment_no (UQ)|
  |     timestamp    |                     |     attendance_pct    |
  |     status       |                     |     cgpa              |
  +------------------+                     |     risk_score        |
                                           |     is_at_risk        |
                                           +-----------------------+
"""
    p.append(make_diagram_box(erd_ascii))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.12 Database Design & Relationships", h2_sec))
    p.append(Paragraph(
        "Foreign key constraints enforce referential integrity. Deleting a student cascades to remove corresponding counselling cases, while user deletion is restricted if active assigned cases exist.",
        body_indent
    ))

    # =========================================================================
    # PAGE 35: CHAPTER 4 cont. (Numbered Page 24)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("4.13 Database Schema & Data Dictionary", h2_sec))
    p.append(Paragraph("Tables 4.5 and 4.6 document the fields, data types, and constraints for core entities.", body))
    p.append(Spacer(1, 4))
    t45_h = ["Column Name", "Data Type", "Constraints", "Operational Description"]
    t45_r = [
        ["id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT", "Unique user identity handle."],
        ["username", "VARCHAR(80)", "UNIQUE, NOT NULL", "Login handle (e.g., 'admin', '2302320099')."],
        ["password_hash", "VARCHAR(255)", "NOT NULL", "PBKDF2-SHA256 salted password digest."],
        ["role", "VARCHAR(20)", "NOT NULL", "Security role ('admin', 'guide', 'mentor', 'student')."],
        ["full_name", "VARCHAR(100)", "NOT NULL", "Official user display name."],
        ["email", "VARCHAR(120)", "UNIQUE, NULLABLE", "Contact email address for alert routing."]
    ]
    p.append(make_table(t45_h, t45_r, [usable_width*0.22, usable_width*0.18, usable_width*0.28, usable_width*0.32]))
    p.append(Paragraph("Table 4.5 Database Schema – users table definition", caption_style))
    p.append(Spacer(1, 4))
    t46_h = ["Column Name", "Data Type", "Constraints", "Operational Description"]
    t46_r = [
        ["id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT", "Unique student record handle."],
        ["enrollment_no", "VARCHAR(50)", "UNIQUE, NOT NULL", "Sanskriti University enrollment number."],
        ["name", "VARCHAR(100)", "NOT NULL", "Official student candidate name."],
        ["department", "VARCHAR(50)", "NOT NULL", "Academic department (e.g., 'CSE', 'ECE')."],
        ["semester", "INTEGER", "NOT NULL", "Current enrolled semester (1–8)."],
        ["attendance_pct", "FLOAT", "NOT NULL", "Recorded classroom attendance percentage."],
        ["internal_marks_pct", "FLOAT", "NOT NULL", "Mid-term / internal assessment percentage."],
        ["cgpa", "FLOAT", "NOT NULL", "Cumulative Grade Point Average (0.0–10.0)."],
        ["risk_score", "FLOAT", "NOT NULL", "Computed ML probability score (0.0–100.0)."],
        ["is_at_risk", "BOOLEAN", "NOT NULL", "Threshold classification flag."]
    ]
    p.append(make_table(t46_h, t46_r, [usable_width*0.22, usable_width*0.18, usable_width*0.28, usable_width*0.32]))
    p.append(Paragraph("Table 4.6 Database Schema – students table definition", caption_style))

    # =========================================================================
    # PAGE 36: CHAPTER 4 cont. (Numbered Page 25)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("4.13 Database Schema & Data Dictionary cont.", h2_sec))
    t47_h = ["Column Name", "Data Type", "Constraints", "Operational Description"]
    t47_r = [
        ["id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT", "Unique counselling case handle."],
        ["student_id", "INTEGER", "FOREIGN KEY -> students.id", "Reference to the at-risk student."],
        ["assigned_to", "INTEGER", "FOREIGN KEY -> users.id", "Reference to the designated faculty mentor."],
        ["stage", "VARCHAR(30)", "NOT NULL", "Current stage ('New', 'Under Review', etc.)."],
        ["severity", "VARCHAR(20)", "NOT NULL", "Risk severity rating ('High', 'Moderate', 'Low')."],
        ["action_plan", "TEXT", "NULLABLE", "Prescribed remediation and intervention actions."],
        ["created_at", "DATETIME", "DEFAULT CURRENT_TIMESTAMP", "Case creation timestamp."]
    ]
    p.append(make_table(t47_h, t47_r, [usable_width*0.22, usable_width*0.18, usable_width*0.28, usable_width*0.32]))
    p.append(Paragraph("Table 4.7 Database Schema – counselling_cases table definition", caption_style))
    p.append(Spacer(1, 4))
    t48_h = ["Column Name", "Data Type", "Constraints", "Operational Description"]
    t48_r = [
        ["id", "INTEGER", "PRIMARY KEY, AUTOINCREMENT", "Unique audit log identifier."],
        ["user_id", "INTEGER", "FOREIGN KEY -> users.id", "Actor responsible for the logged action."],
        ["action", "VARCHAR(100)", "NOT NULL", "System event ('LOGIN', 'UPLOAD_CSV', etc.)."],
        ["details", "TEXT", "NULLABLE", "Contextual metadata and affected entity IDs."],
        ["ip_address", "VARCHAR(45)", "NULLABLE", "Client IP address from WSGI request environment."],
        ["timestamp", "DATETIME", "DEFAULT CURRENT_TIMESTAMP", "Exact UTC logging timestamp."]
    ]
    p.append(make_table(t48_h, t48_r, [usable_width*0.22, usable_width*0.18, usable_width*0.28, usable_width*0.32]))
    p.append(Paragraph("Table 4.8 Database Schema – audit_logs table definition", caption_style))

    # =========================================================================
    # PAGE 37: CHAPTER 4 cont. (Numbered Page 26)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("4.14 API Design and Route Architecture", h2_sec))
    p.append(Paragraph(
        "Table 4.9 details the internal REST API endpoints utilized for asynchronous data fetching and modal updates.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t49_h = ["API Endpoint", "HTTP Verb", "Auth Scope", "JSON Payload / Response Structure"]
    t49_r = [
        ["/api/student/<id>/risk", "GET", "All Authenticated", "Returns JSON risk probability, classification badge, and XAI reason cards."],
        ["/api/cohort/distribution", "GET", "Admin, Guide", "Returns cohort risk distribution histogram data for Chart.js visualizer."],
        ["/api/queue/status", "GET", "Admin, Guide, Mentor", "Returns stage counts, queue capacity percentages, and overflow flags."],
        ["/api/recalculate/<id>", "POST", "Admin, Guide", "Triggers synchronous inference re-scoring; returns updated risk metrics."]
    ]
    p.append(make_table(t49_h, t49_r, [usable_width*0.25, usable_width*0.13, usable_width*0.22, usable_width*0.40]))
    p.append(Paragraph("Table 4.9 REST API architecture and protected route endpoints", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.15 Authentication & RBAC Security Design", h2_sec))
    p.append(Paragraph(
        "The security subsystem implements a 4-tier Role-Based Access Control matrix. Access control decorators verify session state before invoking protected controllers.",
        body_indent
    ))

    # =========================================================================
    # PAGE 38: CHAPTER 4 cont. (Numbered Page 27)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("Table 4.10 Security Controls & Role Privacy Boundaries", caption_style))
    t410_h = ["Security Domain", "Enforcement Mechanism", "Operational Defense Target"]
    t410_r = [
        ["Password Storage", "PBKDF2-HMAC-SHA256 (600,000 rounds + salt)", "Guarantees resilience against offline dictionary & rainbow attacks."],
        ["Session Integrity", "HMAC-signed cryptographically randomized cookie", "Prevents session tampering, spoofing, and privilege elevation."],
        ["Student Privacy", "Session user identity bound strictly to student.id", "Completely eliminates peer browsing and unauthorized academic inspection."],
        ["CSRF Protection", "Server-validated anti-forgery request tokens", "Mitigates malicious third-party cross-site request execution."],
        ["Audit Tracking", "Synchronous database append on sensitive routes", "Creates forensic accountability for file uploads and threshold changes."]
    ]
    p.append(make_table(t410_h, t410_r, [usable_width*0.24, usable_width*0.36, usable_width*0.40]))
    p.append(Spacer(1, 6))
    p.append(Paragraph("4.16 UI/UX Design Principles", h2_sec))
    p.append(Paragraph(
        "User experience design follows accessible institutional ergonomics: WCAG 2.1 AA compliant color contrast, standardized semantic alert badges (Red: High Risk, Yellow: Moderate Risk, Green: Low Risk), and progress bars indicating queue saturation.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.17 Development Methodology", h2_sec))
    p.append(Paragraph(
        "Development adhered to Agile Scrum practices across four 2-week sprints, comprising sprint planning, daily coordination, code reviews, and automated regression testing.",
        body_indent
    ))

    # =========================================================================
    # PAGE 39: CHAPTER 4 cont. (Numbered Page 28)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("4.18 Project Workflow", h2_sec))
    p.append(Paragraph(
        "Figure 4.8 illustrates the complete agile project workflow from initial data synthesis to deployment.",
        body_indent
    ))
    flow_ascii = """
 [Sprint 1: Aug 25 - Sep 07]
 * Educational domain research & indicator identification
 * Synthetic cohort dataset creation (115 profiles, 10 features)
           |
           v
 [Sprint 2: Sep 08 - Sep 21]
 * scikit-learn classification modeling (Random Forest & Logistic Regression)
 * Implementation of Explainable AI (XAI) feature deficit attribution logic
           |
           v
 [Sprint 3: Sep 22 - Oct 05]
 * Mid-Term Evaluation Checkpoint (Guide Review: Sep 28)
 * Flask backend routing, SQLite schema & SQLAlchemy ORM modeling
 * 4-Tier RBAC security implementation & student privacy isolation
           |
           v
 [Sprint 4: Oct 06 - Oct 19]
 * 5-Stage Counselling Lifecycle Hub & Queue Workload Capacity Meters
 * Bulk CSV file upload engine with automated header normalization
 * Chart.js analytics dashboards & dynamic admin policy controls
           |
           v
 [Sprint 5: Oct 20 - Nov 10]
 * Automated test suite development (test_app.py - 8 integration fixtures)
 * Offline packaging, documentation, operations manual, and GitHub sync
"""
    p.append(make_diagram_box(flow_ascii))
    p.append(Paragraph("Figure 4.8 Project Execution and Agile Sprint Lifecycle Flowchart", caption_style))

    # =========================================================================
    # PAGE 40: CHAPTER 5 (Numbered Page 29)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 5", h1_chap))
    p.append(Paragraph("SYSTEM IMPLEMENTATION", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.1 Introduction", h2_sec))
    p.append(Paragraph(
        "This chapter translates the architectural design into production software modules across `ml_engine.py`, `database.py`, `app.py`, and Jinja2 presentation templates, documenting preprocessing transforms, attribution weights, authorization wrappers, and capacity meters.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.2 Development Environment", h2_sec))
    p.append(Paragraph(
        "Development ran inside isolated Python virtual environments (`.venv`) on Windows and macOS workstations, tracked with Git and hosted on GitHub (`https://github.com/Shannu1423/student-dropout-prediction.git`).",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.3 Machine Learning Model Implementation", h2_sec))
    p.append(Paragraph(
        "Constructed in `ml_engine.py`, the pipeline pairs a `ColumnTransformer`—applying `StandardScaler` to numeric indicators and `OneHotEncoder(drop='first')` to fee status—with a 120-tree `RandomForestClassifier`.",
        body_indent
    ))
    p.append(Spacer(1, 2))
    p.append(Paragraph("<b>Listing 5.1 Pipeline Construction Excerpt (ml_engine.py)</b>", caption_style))
    ml_code = """# ml_engine.py: Preprocessor + 120-tree Random Forest pipeline
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(drop='first', sparse_output=False), ['fee_status'])
])
rf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(
        n_estimators=120, max_depth=8, min_samples_split=5, random_state=42
    ))
])
rf_pipeline.fit(X_train, y_train)"""
    p.append(Preformatted(ml_code, code_style))

    # =========================================================================
    # PAGE 41: CHAPTER 5 cont. (Numbered Page 30)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.4 Explainable AI (XAI) Attribution Engine Implementation", h2_sec))
    p.append(Paragraph(
        "Rather than emitting bare probabilities, `analyze_reasons()` measures shortfalls beneath admin-configured thresholds and multiplies each deficit ratio by its trained Gini feature importance before normalizing to 100%.",
        body_indent
    ))
    p.append(Spacer(1, 2))
    p.append(Paragraph("<b>Listing 5.2 Algorithmic Reason Attribution (ml_engine.py)</b>", caption_style))
    xai_code = """def get_dropout_reasons(student_dict, thresholds):
    reasons = []
    if student_dict.get('attendance_pct', 100) < thresholds['attendance']:
        reasons.append({
            'factor': 'Critical Attendance Shortage',
            'value': f"{student_dict['attendance_pct']}%",
            'severity': 'danger',
            'recommendation': 'Issue formal attendance warning; schedule mentor conference.'
        })
    if student_dict.get('internal_marks_pct', 100) < thresholds['internal_marks']:
        reasons.append({
            'factor': 'Low Internal Assessment Performance',
            'value': f"{student_dict['internal_marks_pct']}%",
            'severity': 'danger',
            'recommendation': 'Enroll student in subject remedial tutoring classes.'
        })
    return reasons"""
    p.append(Preformatted(xai_code, code_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.5 Backend Web Implementation (Flask & SQLAlchemy)", h2_sec))
    p.append(Paragraph(
        "An Application Factory inside `app.py` registers role-guarded controllers alongside SQLAlchemy context hooks (`create_app`) so tests and production servers isolate instances cleanly.",
        body_indent
    ))

    # =========================================================================
    # PAGE 42: CHAPTER 5 cont. (Numbered Page 31)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.6 Database Implementation & Model Serialization", h2_sec))
    p.append(Paragraph(
        "ORM tables enforce foreign-key relationships connecting learners, mentoring sessions, notifications, and audit logs while indexing enrollment numbers for instant lookups.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.7 Authentication and Session Management", h2_sec))
    p.append(Paragraph(
        "Protected handlers verify role entitlements inside `@roles_required`, terminating unauthorized access attempts early ahead of business execution.",
        body_indent
    ))
    p.append(Spacer(1, 2))
    p.append(Paragraph("<b>Listing 5.3 RBAC Authorization Decorator (app.py)</b>", caption_style))
    rbac_code = """def roles_required(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'user_id' not in session:
                flash('Please log in to access this page.', 'warning')
                return redirect(url_for('login'))
            user = User.query.get(session['user_id'])
            if not user or user.role not in allowed_roles:
                flash('Access denied: insufficient operational privileges.', 'danger')
                return abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator"""
    p.append(Preformatted(rbac_code, code_style))

    # =========================================================================
    # PAGE 43: CHAPTER 5 cont. (Numbered Page 32)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.8 Student Profile & Risk Recalculation Engine", h2_sec))
    p.append(Paragraph(
        "The recalculation engine allows counselors to adjust hypothetical student grades or attendance and observe real-time risk trajectory changes immediately.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.9 Bulk CSV Ingestion & Header Normalization", h2_sec))
    p.append(Paragraph(
        "To prevent ingestion failures caused by varying spreadsheet headers, the CSV parser implements automated alias mapping before database insertion.",
        body_indent
    ))
    p.append(Spacer(1, 2))
    p.append(Paragraph("<b>Listing 5.4 Header Alias Mapping Dictionary (app.py)</b>", caption_style))
    csv_code = """HEADER_MAP = {
    'enrollment': 'enrollment_no', 'reg_no': 'enrollment_no',
    'student_name': 'name', 'full_name': 'name',
    'dept': 'department', 'branch': 'department',
    'sem': 'semester', 'term': 'semester',
    'attendance': 'attendance_pct', 'att_pct': 'attendance_pct',
    'internal': 'internal_marks_pct', 'internals': 'internal_marks_pct',
    'gpa': 'cgpa', 'grade_point': 'cgpa',
    'fees_overdue': 'fee_overdue', 'backlog_count': 'backlogs'
}
normalized_row = {HEADER_MAP.get(k.lower().strip(), k.lower().strip()): v
                  for k, v in raw_row.items()}"""
    p.append(Preformatted(csv_code, code_style))

    # =========================================================================
    # PAGE 44: CHAPTER 5 cont. (Numbered Page 33)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.10 Counselling Lifecycle Hub & Queue Workload Implementation", h2_sec))
    p.append(Paragraph(
        "The Counselling Hub visualizes active student caseloads across 5 stages. Queue workload meters compute stage saturation against institutional limits.",
        body_indent
    ))
    p.append(Spacer(1, 2))
    p.append(Paragraph("<b>Listing 5.5 Queue Capacity Computation (app.py)</b>", caption_style))
    queue_code = """# Compute stage saturation percentage
stage_counts = {s: CounsellingCase.query.filter_by(stage=s).count()
                for s in ['New', 'Under Review', 'In Progress', 'Resolved', 'Escalated']}
queue_meters = {}
for stage, count in stage_counts.items():
    limit = StageLimit.query.filter_by(stage_name=stage).first().max_limit
    pct = round((count / max(limit, 1)) * 100, 1)
    queue_meters[stage] = {
        'count': count, 'limit': limit, 'pct': pct,
        'overflow': count > limit,
        'color': 'danger' if count > limit else ('warning' if pct >= 80 else 'success')
    }"""
    p.append(Preformatted(queue_code, code_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.11 Escalation Engine & In-Portal Notifications", h2_sec))
    p.append(Paragraph(
        "Cases remaining in 'New' or 'Under Review' past 14 days trigger automatic visual escalation flags in the HOD dashboard, preventing neglected counseling cases.",
        body_indent
    ))

    # =========================================================================
    # PAGE 45: CHAPTER 5 cont. (Numbered Page 34)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.12 Admin Policy Settings & Dynamic Threshold Implementation", h2_sec))
    p.append(Paragraph(
        "Administrators can adjust risk thresholds (e.g., modifying high-risk cutoff from 65% to 70%) via a secured GUI. Updates trigger immediate background re-scoring of all cohorts.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.13 On-Demand Model Retraining Implementation", h2_sec))
    p.append(Paragraph(
        "Administrators can retrain the underlying scikit-learn model on newly accumulated student outcomes with a single click. The script fits a new ensemble, serializes the updated artifact to `models/dropout_model.pkl`, and updates accuracy metrics in the database.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.14 Audit Logging & Security Subsystem", h2_sec))
    p.append(Paragraph(
        "All sensitive administrative, file upload, and case progression events are logged to the `audit_logs` table with actor ID, IP address, and timestamp, guaranteeing institutional forensic accountability.",
        body_indent
    ))

    # =========================================================================
    # PAGE 46: CHAPTER 5 cont. (Numbered Page 35)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.15 Analytics Visualizations (Chart.js Integration)", h2_sec))
    p.append(Paragraph(
        "Chart.js powers responsive canvas graphics on the executive dashboard, rendering cohort risk distributions, department risk comparisons, and intervention success trends.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.16 Frontend-Backend Integration", h2_sec))
    p.append(Paragraph(
        "Templates use Jinja2 inheritance (`base.html`), ensuring consistent navigation, flash message banners, modal dialogue handlers, and responsive CSS across all viewports.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.17 GitHub Version Control & Offline Local Deployment", h2_sec))
    p.append(Paragraph(
        "Version history is maintained on GitHub (`https://github.com/Shannu1423/student-dropout-prediction.git`). Locally, the WSGI server launches cleanly inside `.venv` on Windows (`python app.py`) and macOS (`source .venv/bin/activate && python app.py`, port `5000` or `5001`).",
        body_indent
    ))

    print(f"Middle chapters (Ch2 to Ch5) complete: {len(pages)} pages.")
