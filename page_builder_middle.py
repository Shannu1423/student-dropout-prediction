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
        "Student retention and academic attrition have been subjects of sustained empirical inquiry across educational psychology and computer science for over four decades. As higher education has expanded globally, early identification of students at risk of academic failure or voluntary withdrawal has transitioned from an informal counseling duty to an essential domain of data-driven institutional management.",
        body_indent
    ))
    p.append(Paragraph(
        "This chapter surveys the evolutionary trajectory of retention systems, evaluates the comparative efficacy of machine learning algorithms applied to educational datasets, analyzes modern web frameworks supporting real-time inference, and examines the emerging role of Explainable Artificial Intelligence (XAI) in establishing trust among academic advisors.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.2 Evolution of Student Retention Systems", h2_sec))
    p.append(Paragraph(
        "The conceptual foundation of student retention research originates with Tinto’s Student Integration Model (1975), which posited that college departure is primarily driven by a student's degree of academic and social integration within the university environment. Early operational retention systems in the 1980s and 1990s relied upon physical ledgers, faculty observation notes, and periodic attendance roll calls. These manual processes suffered from severe latency, low inter-rater reliability, and complete inability to identify multi-factorial distress patterns.",
        body_indent
    ))
    p.append(Paragraph(
        "With the widespread adoption of relational Campus Management Systems (CMS) and Learning Management Systems (LMS) in the 2000s, institutions aggregated massive volumes of digital footprints. However, first-generation institutional analytics dashboards were purely descriptive, summarizing historical grade distributions and overdue fee balances without predictive capacity. Modern educational data mining leverages predictive modeling to forecast outcomes before academic standing is irrevocably compromised.",
        body_indent
    ))

    # =========================================================================
    # PAGE 17: CHAPTER 2 cont. (Numbered Page 6)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.3 Review of Machine Learning Algorithms in Higher Education", h2_sec))
    p.append(Paragraph(
        "Numerous supervised learning algorithms have been applied to educational retention forecasting. Logistic Regression provides straightforward coefficient interpretability and probabilistic outputs; however, it assumes linear separability and struggles to capture complex non-linear feature interactions, such as the compounding jeopardy of concurrent attendance loss and tuition arrears.",
        body_indent
    ))
    p.append(Paragraph(
        "Decision Trees (e.g., CART, C4.5) generate intuitive if-then decision rules that appeal to educators, but single trees suffer from high variance and severe susceptibility to overfitting on smaller institutional cohorts. Support Vector Machines (SVM) with radial basis function kernels demonstrate strong generalization in high-dimensional spaces, but their decision boundaries are opaque, obscuring specific risk drivers from faculty counselors.",
        body_indent
    ))
    p.append(Paragraph(
        "Random Forest classifiers, an ensemble of de-correlated decision trees constructed via bootstrap aggregation (bagging) and random feature subspace selection, consistently emerge as the superior architecture for tabular educational data. Random Forests inherently manage mixed data types (continuous test scores and discrete attendance bands), resist overfitting, handle moderate class imbalance effectively, and yield well-calibrated posterior probabilities. Furthermore, ensemble tree architectures support reliable Gini-impurity feature importance metrics.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.4 Review of Existing Technologies", h2_sec))
    p.append(Paragraph(
        "Developing an operational educational retention platform requires harmonious integration across backend computational engines, persistent relational data stores, and intuitive user interfaces. The following sections review the technology selections governing this implementation.",
        body_indent
    ))

    # =========================================================================
    # PAGE 18: CHAPTER 2 cont. (Numbered Page 7)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.4.1 Flask and Scikit-Learn Frameworks", h3_subsec))
    p.append(Paragraph(
        "Python has emerged as the definitive ecosystem for applied machine learning. The scikit-learn library provides robust, battle-tested implementations of preprocessing transformers, cross-validation iterators, and classification estimators. For the serving layer, Flask provides a lightweight, un-opinionated WSGI web microframework that allows direct native execution of serialized scikit-learn pipeline objects without inter-process serialization overhead.",
        body
    ))
    p.append(Paragraph("2.4.2 SQLite and SQLAlchemy ORM", h3_subsec))
    p.append(Paragraph(
        "SQLAlchemy provides enterprise-grade Object-Relational Mapping (ORM) and declarative abstractions over relational SQL databases. SQLite offers a zero-configuration, serverless, self-contained SQL database engine ideal for institutional offline reliability, zero network latency, and seamless version-controlled backup without complex database administration overhead.",
        body
    ))
    p.append(Paragraph("2.4.3 Bootstrap 5 and Chart.js UI", h3_subsec))
    p.append(Paragraph(
        "Frontend visualization requires responsive components that render reliably across administrative desktop monitors and mobile tablets. Bootstrap 5 delivers a modern CSS grid system with zero jQuery dependency. Chart.js provides canvas-rendered asynchronous statistical charts displaying cohort risk distributions and historical retention trajectories.",
        body
    ))
    p.append(Spacer(1, 4))
    t21_h = ["Technology Component", "Selected Framework", "Evaluation & Technical Rationale"]
    t21_r = [
        ["Backend Web Core", "Python 3.14 + Flask 3.1", "Native Python ML execution, low memory footprint, WSGI flexibility"],
        ["Machine Learning", "scikit-learn 1.9 + joblib", "Calibrated probability estimators, reproducible pipeline serialization"],
        ["Persistence Layer", "SQLite 3 + SQLAlchemy 2.1", "Zero-daemon deployment, atomic transactions, complete ACID compliance"],
        ["Frontend UI/UX", "Bootstrap 5.3 + FontAwesome", "Mobile-responsive layouts, accessible contrast semantics, zero jQuery"],
        ["Data Visualizer", "Chart.js 4.4 (Canvas API)", "High-performance client-side rendering of cohort distribution curves"]
    ]
    p.append(make_table(t21_h, t21_r, [usable_width*0.28, usable_width*0.28, usable_width*0.44]))
    p.append(Paragraph("Table 2.1 Technology stack selection and evaluation rationale", caption_style))

    # =========================================================================
    # PAGE 19: CHAPTER 2 cont. (Numbered Page 8)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.4.4 Token-Based Authentication and Password Security", h3_subsec))
    p.append(Paragraph(
        "User authentication security is paramount when storing sensitive student academic records. Industry standards dictate cryptographically salted password hashing using PBKDF2 (Password-Based Key Derivation Function 2) or Argon2 to prevent rainbow-table and dictionary attacks. Session management utilizes cryptographically signed client-side cookies with HTTP-only and SameSite flags, mitigating Cross-Site Scripting (XSS) and Cross-Site Request Forgery (CSRF).",
        body
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("2.5 Explainable AI (XAI) in Educational Analytics", h2_sec))
    p.append(Paragraph(
        "A critical barrier to the adoption of machine learning in academic administration is the 'black-box' dilemma. When a complex algorithmic model classifies a student as 'High Risk' with 85% probability but fails to elucidate the contributing factors, faculty counselors are left without actionable recourse. They cannot discern whether the student requires academic tutoring, financial aid counseling, or psychological support.",
        body_indent
    ))
    p.append(Paragraph(
        "While model-agnostic explanation frameworks such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) provide rigorous mathematical feature attributions, they impose substantial computational latency during batch inference and generate complex mathematical graphs that non-technical faculty struggle to interpret under time constraints.",
        body_indent
    ))
    p.append(Paragraph(
        "In contrast, this project implements a localized, rule-based feature deficit attribution algorithm. By evaluating individual student feature values against dynamically configured institutional policy thresholds (e.g., Attendance < 75%, Internal Marks < 40%, Fee Dues > 0), the engine generates human-readable 'Reason Cards' detailing the exact deficit and pairing it with a concrete remedial recommendation.",
        body_indent
    ))

    # =========================================================================
    # PAGE 20: CHAPTER 2 cont. (Numbered Page 9)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("2.6 Comparative Analysis of Existing Systems", h2_sec))
    p.append(Paragraph(
        "To establish the distinct contributions of the proposed system, a comparative analysis was performed against standard commercial Campus ERPs, standalone ML research scripts, and general academic counseling logs.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t22_h = ["System Capability", "Commercial Campus ERP", "Generic ML Research Scripts", "Proposed Dropout Prediction System"]
    t22_r = [
        ["Predictive Analytics", "None (Descriptive reports only)", "High (Jupyter notebook models)", "High (Calibrated ensemble inference)"],
        ["Explainable Diagnostics", "Not Supported", "Complex mathematical plots", "Automated human-readable XAI cards"],
        ["Counselling Workflow", "Basic static remarks field", "Not Supported", "5-Stage lifecycle queue with capacity meters"],
        ["Role-Based Privacy", "Coarse-grained departmental", "None (Single user execution)", "4-Tier RBAC with strict peer isolation"],
        ["Dynamic Policy Controls", "Hardcoded vendor database", "Requires code modification", "Live admin GUI threshold recalibration"],
        ["Offline Deployment", "Cloud SaaS dependent", "Manual local scripting", "Self-contained offline production executable"]
    ]
    p.append(make_table(t22_h, t22_r, [usable_width*0.25, usable_width*0.25, usable_width*0.25, usable_width*0.25]))
    p.append(Paragraph("Table 2.2 Comparative analysis with existing educational retention tools", caption_style))
    p.append(Paragraph("2.7 Research Gap and Identified Problems", h2_sec))
    p.append(Paragraph(
        "The literature highlights three critical gaps: (1) predictive algorithms rarely bridge into actionable counseling workflows; (2) predictions remain opaque black boxes; and (3) student peer privacy is frequently breached in open department registries. This capstone directly bridges these gaps.",
        body
    ))
    p.append(Paragraph("2.8 Summary", h2_sec))
    p.append(Paragraph(
        "The literature validates the selection of Random Forest classification combined with localized Explainable AI feature attribution, implemented over a Flask/SQLAlchemy architecture, providing an optimal foundation for institutional retention management.",
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
        "At Sanskriti University, academic monitoring has historically relied on decentralized, semi-manual procedures. Faculty maintain classroom attendance rosters in hardcopy registers or isolated spreadsheets. Examination marks are aggregated post-semester into a centralized database, and fee records reside within a dedicated accounts portal. Department Heads hold periodic review meetings to review detention lists only after semester examinations conclude.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.2 Limitations of the Existing System", h2_sec))
    p.append(Paragraph("Analysis of the existing operational workflow revealed several severe structural bottlenecks:", body))
    p.append(Paragraph("1. <b>Extreme Indicator Latency:</b> Identification occurs post-semester after failing grades are finalized, missing the critical window for remedial intervention.", body))
    p.append(Paragraph("2. <b>Siloed Departmental Data:</b> Academic performance, behavioral indicators, and fee records reside in disparate systems, preventing holistic risk synthesis.", body))
    p.append(Paragraph("3. <b>Subjective Mentor Triage:</b> Mentors must manually inspect hundreds of student records, leading to inconsistent identification driven by counselor intuition rather than standardized criteria.", body))
    p.append(Paragraph("4. <b>Lack of Structured Follow-Up:</b> Counseling notes are written on paper files or informal emails without systematic tracking of action plans or stage progression.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.3 Proposed System", h2_sec))
    p.append(Paragraph(
        "The proposed AI-Based Student Dropout Prediction System replaces fragmented manual monitoring with a unified, automated, proactive intelligence platform. The system continuously synthesizes academic, behavioral, and socio-financial indicators, generates real-time calibrated risk scores, articulates specific deficit reasons, and manages cases through a 5-stage counseling hub.",
        body_indent
    ))

    # =========================================================================
    # PAGE 22: CHAPTER 3 cont. (Numbered Page 11)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.4 Advantages of the Proposed System", h2_sec))
    p.append(Paragraph("The proposed architecture introduces key operational advantages:", body))
    p.append(Paragraph("• <b>Proactive Early Identification:</b> Risk scores are computed dynamically upon data upload, enabling mid-semester counseling weeks before exams.", body))
    p.append(Paragraph("• <b>Actionable Explainability:</b> Automated diagnostic cards highlight the primary root cause, empowering counselors with tailored remediation plans.", body))
    p.append(Paragraph("• <b>Queue Workload Balancing:</b> Visual capacity meters prevent mentor burnout and highlight institutional counselling backlogs.", body))
    p.append(Paragraph("• <b>Data Privacy by Design:</b> Strict RBAC isolation ensures students only access their individual profiles, preventing stigma.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.5 Functional Requirements", h2_sec))
    p.append(Paragraph(
        "Functional requirements define the core operational capabilities the system must deliver across user roles. Table 3.1 details the functional requirements matrix.",
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
        "Non-functional requirements specify the architectural qualities, operational constraints, and performance parameters required for production deployment.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t32_h = ["Quality Attribute", "Specification and Verification Criteria"]
    t32_r = [
        ["Inference Latency", "Model inference and XAI attribution must execute under 50ms per single student."],
        ["Bulk Throughput", "Ingestion and risk calculation for 500 student records must complete under 3 seconds."],
        ["Data Privacy", "Zero peer data leakage; students strictly restricted to own record via session binding."],
        ["System Availability", "Zero external cloud dependencies; application functions 100% offline via local SQLite."],
        ["Cryptographic Security", "Passwords hashed using PBKDF2-SHA256 with 600,000 iterations and salt."],
        ["Browser Compatibility", "Responsive layout fully functional on Chrome 90+, Edge 90+, Firefox 88+, Safari 14+."]
    ]
    p.append(make_table(t32_h, t32_r, [usable_width*0.30, usable_width*0.70]))
    p.append(Paragraph("Table 3.2 Non-functional requirements specification matrix", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.7 Software Requirements", h2_sec))
    p.append(Paragraph(
        "Table 3.3 documents the verified software runtime environment and package dependencies.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t33_h = ["Software Component", "Verified Production Version", "Role in System Architecture"]
    t33_r = [
        ["Operating System", "Windows 10/11, Ubuntu 22.04 LTS", "Host server runtime environment"],
        ["Programming Language", "Python 3.11 / 3.12 / 3.14", "Core runtime and computational engine"],
        ["Web Microframework", "Flask 3.1.3", "WSGI application routing, HTTP request handling"],
        ["ORM / Persistence", "SQLAlchemy 2.1.5 + SQLite 3", "Database modeling, query execution, transactions"],
        ["Machine Learning", "scikit-learn 1.9.1, joblib 1.6", "Model training, inference, and serialization"],
        ["Data Manipulation", "pandas 3.0.6, numpy 2.5.4", "Tabular dataset preprocessing and vector math"],
        ["Frontend UI Toolkit", "Bootstrap 5.3.3 + FontAwesome 6", "Responsive layout, styling, and visual icons"]
    ]
    p.append(make_table(t33_h, t33_r, [usable_width*0.28, usable_width*0.28, usable_width*0.44]))
    p.append(Paragraph("Table 3.3 Software requirements and version environment", caption_style))

    # =========================================================================
    # PAGE 24: CHAPTER 3 cont. (Numbered Page 13)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.8 Hardware Requirements", h2_sec))
    p.append(Paragraph(
        "The application is engineered for maximum resource efficiency, allowing operation on standard departmental hardware without dedicated GPU acceleration.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t34_h = ["Hardware Component", "Minimum Host Server Specification", "Recommended Client Terminal Specification"]
    t34_r = [
        ["Processor (CPU)", "Intel Core i3 / AMD Ryzen 3 (Dual Core 2.0 GHz)", "Intel Celeron / Core i3 (1.5 GHz)"],
        ["System Memory (RAM)", "4 GB DDR4 (8 GB recommended for large cohorts)", "2 GB DDR3/DDR4"],
        ["Persistent Storage", "500 MB free space (Application, SQLite, Models)", "100 MB free browser cache space"],
        ["Network Interface", "Standard 10/100 Mbps Local Area Network (LAN)", "LAN / Wi-Fi connection to institutional host"],
        ["Display Resolution", "1280 x 720 (HD) minimum", "1024 x 768 minimum, 1920 x 1080 recommended"]
    ]
    p.append(make_table(t34_h, t34_r, [usable_width*0.28, usable_width*0.36, usable_width*0.36]))
    p.append(Paragraph("Table 3.4 Hardware specifications for host and client devices", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("3.9 Feasibility Study", h2_sec))
    p.append(Paragraph(
        "A formal three-factor feasibility study was conducted to evaluate project viability:",
        body_indent
    ))
    p.append(Paragraph(
        "• <b>Technical Feasibility:</b> The system utilizes stable, production-grade open-source libraries (Python, Flask, scikit-learn). Offline model execution and SQLite persistence eliminate external API latency and cloud dependencies. Technical feasibility is highly favorable.",
        body
    ))
    p.append(Paragraph(
        "• <b>Operational Feasibility:</b> The interface adheres to standard institutional UX patterns. Clear visual indicators (color-coded risk badges, queue progress bars) require minimal faculty training. Operational feasibility is confirmed.",
        body
    ))
    p.append(Paragraph(
        "• <b>Economic Feasibility:</b> All software dependencies are open-source with permissive licenses (Apache 2.0, MIT, BSD), resulting in zero software licensing expenses. The system runs on existing departmental desktop computers. Economic feasibility is exceptional.",
        body
    ))

    # =========================================================================
    # PAGE 25: CHAPTER 3 cont. (Numbered Page 14)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("3.10 Use Case Analysis", h2_sec))
    p.append(Paragraph(
        "System actors comprise four distinct operational roles with specific privileges and goals. Table 3.5 outlines the core actor-goal interaction matrix.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t35_h = ["Actor Role", "Primary Use Case / Goal", "Operational Description and System Boundaries"]
    t35_r = [
        ["Administrator", "System Management & Policy", "Configure global risk thresholds, trigger model retraining, view audit logs, adjust queue limits."],
        ["Guide / HOD", "Department Cohort Oversight", "Inspect department risk registry, monitor cohort distributions, assign faculty mentors, escalate stalled cases."],
        ["Faculty Mentor", "Student Counselling & Case Progression", "Review assigned at-risk students, inspect XAI reason cards, record counseling session notes, advance stage."],
        ["Student", "Self-Assessment & Guidance", "View personal academic attendance, CGPA, risk status, and review assigned mentor guidance securely."]
    ]
    p.append(make_table(t35_h, t35_r, [usable_width*0.22, usable_width*0.32, usable_width*0.46]))
    p.append(Paragraph("Table 3.5 Use case actor-goal interaction summary", caption_style))
    p.append(Paragraph(
        "Each user is strictly segregated by role. If an unauthorized actor attempts to access an administrative endpoint (e.g., `/admin/settings`), the security decorator intercepts the request, aborts execution with HTTP 403, and records the attempted violation in the security audit log.",
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
        "The system is architected as a decoupled, 3-tier web application structured across the Presentation Tier, Application Logic Tier, and Data Persistence Tier. This separation of concerns ensures that machine learning inference routines remain independent of web routing, enabling modular maintenance, rapid retraining, and robust unit testing.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t41_h = ["Architectural Tier", "Constituent Technologies", "Functional Responsibilities"]
    t41_r = [
        ["Presentation Tier", "Bootstrap 5.3, HTML5, Jinja2, Chart.js", "Renders role-specific dashboards, modal forms, queue meters, and charts."],
        ["Application Logic Tier", "Flask 3.1, Werkzeug, scikit-learn", "Enforces RBAC security, executes ML inference, computes XAI cards, routes APIs."],
        ["Data Persistence Tier", "SQLAlchemy ORM, SQLite 3 Engine", "Guarantees ACID transactions, manages relational constraints, stores audit logs."]
    ]
    p.append(make_table(t41_h, t41_r, [usable_width*0.25, usable_width*0.35, usable_width*0.40]))
    p.append(Paragraph("Table 4.1 Architectural tiers and decoupled system responsibilities", caption_style))
    p.append(Spacer(1, 4))
    p.append(Paragraph("4.2 Overall Architecture Overview", h2_sec))
    p.append(Paragraph(
        "Figure 4.1 illustrates the architectural relationship between client browsers, the Flask WSGI server, the machine learning inference pipeline, and the persistent SQLite database.",
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
        "This chapter details the technical implementation of the AI-Based Student Dropout Prediction System, documenting key algorithmic logic, software configurations, database schemas, and integration patterns.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.2 Development Environment", h2_sec))
    p.append(Paragraph(
        "Development was executed using Python 3.11/3.14 within an isolated virtual environment (`.venv`). Source code version control was maintained using Git with semantic branching, synchronized to GitHub (`https://github.com/Shannu1423/student-dropout-prediction.git`).",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.3 Machine Learning Model Implementation", h2_sec))
    p.append(Paragraph(
        "The classification pipeline is implemented in `ml_engine.py`. Continuous variables are scaled using `StandardScaler` and missing values imputed with median strategies.",
        body_indent
    ))
    p.append(Spacer(1, 2))
    p.append(Paragraph("<b>Listing 5.1 Pipeline Construction Excerpt (ml_engine.py)</b>", caption_style))
    ml_code = """# ml_engine.py: Model training pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(
        n_estimators=100, max_depth=6,
        class_weight='balanced', random_state=42
    ))
])
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, 'models/dropout_model.pkl')"""
    p.append(Preformatted(ml_code, code_style))

    # =========================================================================
    # PAGE 41: CHAPTER 5 cont. (Numbered Page 30)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.4 Explainable AI (XAI) Attribution Engine Implementation", h2_sec))
    p.append(Paragraph(
        "To bridge algorithmic predictions with faculty counseling, the Explainable AI attribution engine evaluates student records against institutional deficit thresholds.",
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
        "The web application utilizes the Flask Application Factory pattern, isolating configuration parameters and registering route blueprints cleanly.",
        body_indent
    ))

    # =========================================================================
    # PAGE 42: CHAPTER 5 cont. (Numbered Page 31)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("5.6 Database Implementation & Model Serialization", h2_sec))
    p.append(Paragraph(
        "SQLAlchemy declarative base classes map Python objects directly to SQLite tables. Database indexes on `enrollment_no` and `student_id` optimize retrieval.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("5.7 Authentication and Session Management", h2_sec))
    p.append(Paragraph(
        "Authentication is enforced via the `@roles_required` decorator, intercepting unauthorized access attempts and verifying session identity.",
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
        "The codebase is version-controlled on GitHub (`https://github.com/Shannu1423/student-dropout-prediction.git`). The system runs completely offline on Windows via `.venv\\Scripts\\python.exe app.py` on `http://127.0.0.1:5000`.",
        body_indent
    ))

    print(f"Middle chapters (Ch2 to Ch5) complete: {len(pages)} pages.")
