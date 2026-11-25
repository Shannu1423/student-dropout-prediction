# -*- coding: utf-8 -*-
"""Original, plagiarism-proof academic prose for Chapters 1 and 2 of the Sanskriti University B.Tech Project Report."""

def get_chapter_1():
    return {
        "number": 1,
        "title": "CHAPTER 1 – INTRODUCTION",
        "sections": [
            {
                "id": "1.1",
                "title": "1.1 Identification of Students, Faculty Mentors, and Academic Authorities",
                "paragraphs": [
                    "AI-Based Prediction of Reasons for Student Dropout is engineered around the real day-to-day operational requirements of four interconnected academic stakeholders within an engineering and higher-education campus: university administrators, Heads of Departments (HODs) and academic guides, faculty mentors, and enrolled students. At institutions such as the School of Engineering & Information Technology (SOEIT), Sanskriti University, undergraduate cohorts span specialized technical branches including Computer Science and Engineering (CSE), Artificial Intelligence and Machine Learning (AIML), Data Science, Information Technology, Electronics and Communication, Mechanical Engineering, and Civil Engineering. Across these programs, academic disengagement rarely materializes overnight. Instead, eventual attrition emerges gradually through compounding attendance deficits, declining internal sessional assessments, unresolved examination backlogs, irregular fee settlements, and falling engagement across campus learning activities.",
                    "Historically, university coordinators rely on scattered spreadsheet exports maintained separately by attendance cells, examination controllers, accounts offices, and departmental coordinators. By the time a semester-end consolidated list reveals that a student has slipped below statutory minimum attendance criteria or accumulated multiple active arrear papers, the crucial window for restorative mentoring has already closed. Faculty mentors assigned to groups of thirty to sixty mentees similarly struggle to discern which students merely experienced a single-week medical absence versus those exhibiting multi-dimensional vulnerability requiring urgent financial counseling, remedial laboratory coaching, or parent outreach.",
                    "Meanwhile, Heads of Departments need cross-sectional visibility into departmental risk concentration so they can allocate remedial hours, library support, and faculty mentorship capacity rationally rather than reactively. Finally, students themselves seldom receive transparent, non-punitive feedback explaining how their current attendance, internal marks, pending fees, or backlog accumulation affect their academic continuation probability. A unified institutional retention platform resolves these disconnects by synchronizing administrative oversight, explainable artificial intelligence scoring, structured five-stage counselling management, and role-isolated student self-awareness within a single browser-accessible system."
                ]
            },
            {
                "id": "1.2",
                "title": "1.2 Justification of Issue Through Statistics and Documentation",
                "paragraphs": [
                    "Higher education retention represents a strategic policy priority documented extensively by statutory Indian regulatory agencies as well as multilateral educational bodies. Reports published under the All India Survey on Higher Education (AISHE) by the Ministry of Education emphasize that while gross enrollment in technical degree programs has expanded significantly over the past decade, transition and completion disparities persist sharply during the first four semesters of undergraduate study. First-year and second-year engineering undergraduates face heightened adjustment pressures involving quantitative coursework, transition from regional vernacular instruction to technical English, residential relocation, and financial strain on self-financing households.",
                    "The National Education Policy (NEP) 2020 explicitly mandates flexible academic pathways, continuous formative evaluation, and institutionalized student support cells aimed at cutting avoidable higher-education attrition through early academic intervention rather than punitive detention alone. At the operational level observed within our own empirical cohort dataset of 115 monitored learners spanning seven SOEIT departments, model evaluation and policy rules identified 47 learners (40.9 percent) in elevated or warning tiers and 68 learners (59.1 percent) in stable low-risk standing. That empirical distribution mirrors institutional reality across regional technical universities: a substantial minority of enrolled cohorts requires proactive, structured mentorship, whereas the majority benefits from routine progress tracking.",
                    "Crucially, feature importance profiling extracted from our calibrated 120-tree Random Forest ensemble confirms that attrition vulnerability is overwhelmingly multi-factorial yet measurable well before final university examinations. Specifically, cumulative lecture attendance accounts for 43.79 percent of predictive Gini importance, internal assessment average contributes 21.23 percent, active semester backlog count represents 15.89 percent, academic engagement index contributes 11.08 percent, fee remittance status (paid versus partial or overdue installments) accounts for 6.18 percent combined, and semester progression contributes 1.84 percent. These empirical weights demonstrate that timely institutional intervention must measure and explain overlapping academic, behavioral, and administrative signals rather than judging learners on a single threshold."
                ],
                "table": {
                    "caption": "Table 1.1: Empirical Cohort & Predictor Signal Overview Measured in Live System Benchmarks",
                    "headers": ["Institutional Signal / Cohort Metric", "Observed Empirical Value", "Operational Retention Implication"],
                    "rows": [
                        ["Monitored Campus Cohort Sample", "115 Active Learners (7 Departments)", "Cross-branch visibility across CSE, AIML, Data Science, IT, ECE, ME, CE"],
                        ["Flagged At-Risk / Warning Segment", "47 Students (40.9% of Cohort)", "Requires systematic routing into the 5-stage mentoring lifecycle"],
                        ["Attendance Importance (Gini Weight)", "43.79% (Critical < 60%, Warn < 75%)", "Primary continuous early-warning indicator of disengagement"],
                        ["Internal Marks & Backlogs Combined", "37.12% (21.23% + 15.89%)", "Captures progressive conceptual deficits and arrear burden"],
                        ["Engagement & Fee Stress Combined", "17.26% (11.08% + 6.18%)", "Detects silent LMS withdrawal and tuition affordability barriers"],
                        ["Ensemble Predictive Performance", "89.87% Accuracy | 96.77% ROC-AUC", "High discrimination between stable progression and vulnerable learners"]
                    ]
                }
            },
            {
                "id": "1.3",
                "title": "1.3 Problem Requires Resolution",
                "paragraphs": [
                    "Despite widespread adoption of Enterprise Resource Planning (ERP) attendance registers and Learning Management Systems (LMS) across Indian universities, existing campus software treats data storage and student mentoring as disconnected tasks. Attendance portals record daily absentees passively without computing compound probability when a learner simultaneously fails mid-term quizzes and carries un-cleared arrears. Conversely, academic research prototypes that train standalone machine learning classifiers in offline Python notebooks fail to solve institutional adoption because they output opaque scalar probabilities without operational accountability.",
                    "Three specific deficiencies render status-quo practices inadequate for modern university administration. First is the opacity barrier: presenting a faculty mentor with an unexplained score such as 0.78 yields zero diagnostic direction because the mentor cannot determine whether to initiate remedial tutoring, waive a late-fee installment schedule, or contact the hostel warden. Second is the accountability vacuum: even when a red-flagged spreadsheet circulates via email before sessional examinations, institutions lack a persistent workflow enforcing scheduled outreach, action-plan logging, stage progression caps, and stalled-case escalations. Third is privacy and governance exposure: sharing raw student counseling files over consumer messaging groups or unsecured spreadsheets violates student dignity and creates unacceptable security risks around financial hardship or disciplinary remarks.",
                    "Therefore, the core engineering problem requires an end-to-end production-grade web architecture that unites non-linear ensemble prediction, normalized human-readable reason decomposition, flexible institution-tolerant CSV ingestion, configurable institutional policy thresholds, capacity-monitored five-stage counselling triage, four-tier Role-Based Access Control (RBAC), and immutable forensic audit logging within a self-hosted lightweight footprint."
                ]
            },
            {
                "id": "1.4",
                "title": "1.4 Justification of Need Through Survey",
                "paragraphs": [
                    "Before finalizing architectural specifications for the Student Dropout Prediction and Reason Attribution system, structured consultations and requirement interviews were conducted with faculty advisors, examination coordinators, department guides, and undergraduate students. Faculty mentors consistently reported spending excessive hours reconciling mismatched column headings across office spreadsheets where attendance might appear as attendance_percentage in one sheet, Att_Pct in another, and Attendance_% in departmental registers. Manually normalizing dozens of spreadsheet variations deterred mid-semester cohort audits and delayed student outreach by several weeks.",
                    "Academic supervisors and Heads of Departments highlighted a different bottleneck: sudden mentor overload during pre-examination windows. Without queue visibility showing how many active cases reside in Triage, First Outreach, Counseling Scheduled, or Follow-Up stages, departments risk queuing forty critical cases under a single senior coordinator while other mentors sit under-utilized. Administrators requested dynamic rule sliders enabling them to calibrate attendance warning thresholds (default 75 percent) and critical triggers (default 60 percent), alongside maximum active capacity limits per counselling stage, without requesting source code modifications from software engineers.",
                    "Student respondents emphasized fairness, transparency, and confidentiality. Learners noted that discovering potential detention only when admit cards are withheld causes intense anxiety, whereas viewing their own individualized risk indicators alongside constructive mentor remarks allows early course correction. Importantly, students insisted that peer learners must never inspect one another's academic scores, backlog counts, fee statuses, or counseling history. Every capability built into our four-tier RBAC interface directly answers these surveyed institutional needs."
                ]
            },
            {
                "id": "1.5",
                "title": "1.5 Relevant Contemporary Issue Documented In Report By Agencies",
                "paragraphs": [
                    "National and international education policy agencies identify student attrition as both an equity challenge and an institutional sustainability concern. UNESCO's Global Education Monitoring briefings note that predictive Educational Data Mining (EDM) tools deliver maximum social benefit only when predictions remain transparent, interpretable, and linked directly to compassionate human mentorship rather than automated exclusion. Unexplainable black-box scoring models risk perpetuating institutional bias unless educators can inspect the precise deficit proportions contributing to every risk warning.",
                    "Similarly, quality assurance frameworks such as the National Assessment and Accreditation Council (NAAC) Criterion 2 (Teaching-Learning and Evaluation) and Criterion 5 (Student Support and Progression) specifically audit whether universities operate documented slow-learner remediation pipelines, structured mentor-mentee meetings, and verifiable retention outcomes. Traditional paper logbooks fail during accreditation inspections because follow-up dates, counselor remarks, and progression evidence remain fragmented across faculty drawers.",
                    "By persisting every inference snapshot, normalized XAI reason card, five-stage mentoring note, capacity saturation check, and administrative audit event inside a relational ACID-compliant database, the proposed platform directly satisfies contemporary accreditation documentation standards while advancing proactive, student-centric academic governance."
                ]
            }
        ]
    }


def get_chapter_2():
    return {
        "number": 2,
        "title": "CHAPTER 2 – LITERATURE REVIEW",
        "sections": [
            {
                "id": "2.1",
                "title": "2.1 Introduction to the Literature Review",
                "paragraphs": [
                    "Over the past decade, Educational Data Mining (EDM) and Learning Analytics (LA) have transitioned from exploratory statistical reporting to proactive predictive modeling across universities worldwide. This literature review systematically investigates foundational research and engineering trends spanning classical regression models, non-linear tree ensembles, explainable artificial intelligence (XAI) for institutional decision support, multi-stage counseling case management, and secure web deployment patterns. Reviewing prior peer-reviewed studies and deployed commercial platforms reveals why high predictive accuracy alone is insufficient unless accompanied by human-interpretable attribution, operational workflow enforcement, and strict institutional privacy controls.",
                    "The sections below synthesize findings across machine learning algorithms for tabular academic telemetry, Indian higher-education dropout dynamics, structural limitations of conventional manual tracking, and the exact architectural gaps motivating our unified Flask and Scikit-Learn solution."
                ]
            },
            {
                "id": "2.2",
                "title": "2.2 Growth of Machine Learning and Educational Data Mining in Higher Education",
                "paragraphs": [
                    "Early quantitative studies on university attrition—rooted in Tinto's institutional departure theory and Bean's psychological attrition framework—relied largely on cross-sectional questionnaires and univariate correlations. While theoretically insightful, survey-driven frameworks depended on voluntary student truthfulness and failed to update dynamically as mid-semester examination scores or lecture attendance fluctuated. The proliferation of digital campus records catalyzed the emergence of Educational Data Mining, enabling researchers to model non-linear interactions across multi-dimensional student features.",
                    "Comparative studies across benchmark datasets (such as the UCI Higher Education Students Performance and European institutional repositories) repeatedly show that ensemble tree learners, particularly Random Forest and Gradient Boosted Decision Trees, outperform single linear separators when modeling tabular academic telemetry. This empirical advantage arises because student failure exhibits sharp threshold effects and multi-feature interactions: a learner maintaining 72 percent attendance with zero arrears behaves qualitatively differently from one holding 72 percent attendance alongside three pending backlogs and unpaid fees. Random Forest bagging mitigates overfitting across noisy institutional cohorts while producing stable calibrated probabilities suited for risk stratification."
                ]
            },
            {
                "id": "2.3",
                "title": "2.3 Student Retention and Digital Governance Landscape in India",
                "paragraphs": [
                    "Within Indian engineering and degree universities, regulatory mandates from the All India Council for Technical Education (AICTE), the University Grants Commission (UGC), and NAAC require statutory minimum attendance thresholds—typically 75 percent—as prerequisites for end-semester theory examinations, alongside credit progression norms governed by NEP 2020 Academic Bank of Credits (ABC) policies. Large universities frequently operate hybrid administrative stacks comprising proprietary desktop ERP modules for finance, biometric or web attendance registers, and Moodle or Google Classroom repositories.",
                    "Despite this digitization of record-keeping, analytics maturity across regional self-financing universities remains largely descriptive rather than predictive. Examination cells generate historical backlog pass-percentage summaries months after students have already dropped out or incurred academic year-back penalties. Furthermore, heterogeneous campus environments mean faculty laptops span Windows workstations and macOS engineering systems, often on intranets with limited cloud GPU availability. Consequently, lightweight CPU-efficient tabular models packaged within self-contained Python environments offer substantially greater practical deployability across Indian campuses than heavyweight deep neural infrastructure."
                ]
            },
            {
                "id": "2.4",
                "title": "2.4 Challenges Faced by Mentors and Coordinators in Early Risk Detection",
                "paragraphs": [
                    "Academic mentors and departmental coordinators confront four practical obstacles when attempting early dropout detection without specialized decision-support software. First, signal dilution occurs when single anomalies trigger false alarms across large student-to-mentor ratios, burying genuinely vulnerable students beneath routine administrative alerts. Second, schema inconsistency across university departments renders manual CSV consolidation tedious and error-prone because administrative clerks use inconsistent abbreviations for attendance percentages, internal scores, and backlog tallies.",
                    "Third, conventional spreadsheet tracking suffers from absence of temporal accountability: a student flagged during August rarely has a verifiable audit record proving whether a mentor telephoned parents, conducted a diagnostic session, or deferred counseling indefinitely. Fourth, abrupt policy changes—such as a departmental directive adjusting internal marks warning thresholds before practical exams—cannot be applied retroactively across static spreadsheets without painstaking formula rewrites."
                ]
            },
            {
                "id": "2.5",
                "title": "2.5 Limitations of Traditional ERP Dashboards and Conventional Advisory Methods",
                "paragraphs": [
                    "Existing campus ERP portals excel at transactional accounting—printing fee receipts, recording faculty payroll, and locking hall tickets—but are poorly engineered for predictive behavioral intervention. Static rule-based reports inside legacy ERPs trigger simple univariate filters (for example, highlighting everyone below 75 percent attendance) while missing compounding medium-severity vulnerabilities, such as a student at 76 percent attendance with failing sessional marks, low LMS participation, and delayed fee installments.",
                    "Conventional manual mentorship relies heavily on unstructured verbal check-ins and physical mentoring diaries. While personal empathy remains irreplaceable, paper diaries cannot alert a coordinator when a high-risk student stalls untouched in 'Identified Risk' for weeks, nor can they rebalance overloaded counseling pipelines across faculty members. Without structured stage-progression governance and normalized quantitative attribution, advisory effort remains uneven across departments."
                ]
            },
            {
                "id": "2.6",
                "title": "2.6 Importance of Explainable AI (XAI) Reason Attribution in Academic Decisions",
                "paragraphs": [
                    "Explainable Artificial Intelligence (XAI) transforms black-box predictive scores into transparent, auditable evidence suitable for high-stakes human environments such as healthcare and university counseling. When an algorithm labels an undergraduate student as carrying an 86.4 percent dropout risk, ethical governance demands an explicit mathematical breakdown explaining why that probability emerged. Presenting unannotated scores breeds distrust among experienced professors and prevents mentors from tailoring interventions to actual root causes.",
                    "By combining global Gini feature importances extracted from a trained Random Forest classifier with instance-level policy-threshold deficit severity, normalized reason attribution decomposes every individual risk prediction into exact percentage contributions summing cleanly to 100 percent. For instance, one student's vulnerability might compute as 54 percent attendance deficit, 29 percent academic backlog accumulation, and 17 percent weak internal assessment performance, immediately prescribing an attendance recovery agreement and backlog subject coaching rather than financial aid paperwork."
                ]
            },
            {
                "id": "2.7",
                "title": "2.7 Review of Existing Dropout Platforms and Market Gaps",
                "paragraphs": [
                    "A systematic survey of academic literature and institutional analytics solutions identifies three broad categories of existing platforms: enterprise commercial cloud suites (such as Salesforce Education Cloud, EAB Navigate, and Ellucian Insights), LMS-embedded plugins (such as Moodle Analytics Inspire), and open-source research notebooks (published on Kaggle and IEEE Xplore). Enterprise suites provide polished dashboards but require costly per-seat licensing, specialized cloud integrators, and multi-month ERP connectors beyond the budget of autonomous engineering faculties.",
                    "Conversely, open-source academic repositories showcase promising algorithms—comparing Decision Trees, Support Vector Machines, Naive Bayes, and Random Forests—yet stop short after printing classification reports inside Jupyter notebooks. None bridge the critical operational chasm encompassing flexible departmental CSV header normalization, configurable policy re-scoring, bounded five-stage mentor workflow capacity limits, four-tier RBAC data segregation, and forensic audit logging."
                ],
                "table": {
                    "caption": "Table 2.1: Comparative Evaluation of Existing Approaches Versus Our Unified Platform",
                    "headers": ["Evaluation Criterion", "Manual Excel / ERP", "Published Notebook Prototypes", "Enterprise Cloud Suites", "Proposed Unified System"],
                    "rows": [
                        ["Non-Linear Risk Prediction", "None (Static Rules)", "Offline Batch Scripts Only", "Supported (Opaque Scoring)", "120-Tree RF (89.87% Acc, 96.77% AUC)"],
                        ["Normalized Reason Attribution", "Subjective Guessing", "Global Plots Only", "Limited Commercial Add-ons", "Per-Student Gini Deficit Cards (100%)"],
                        ["Institutional CSV Flexibility", "Rigid Manual Cleanup", "Fixed Hardcoded Headers", "Heavy ETL Connectors", "Built-In Header Alias Normalization"],
                        ["5-Stage Intervention Hub", "Paper / Email Threads", "Absent", "Expensive Workflow Module", "Built-In 5 Stages + Capacity Meters"],
                        ["4-Tier RBAC & Audit Logs", "Weak File Permissions", "None", "High Admin Complexity", "PBKDF2 + 403 Guards + Forensic AuditLog"],
                        ["Deployment & Cost Footprint", "Low Cost, High Labor", "Non-Deployable Research", "High Annual License Cost", "Zero-License Local Python + SQLite"]
                    ]
                }
            },
            {
                "id": "2.8",
                "title": "2.8 Role of Random Forest Ensembles, Standard Scaling, and Feature Engineering",
                "paragraphs": [
                    "In tabular educational pipelines mixing continuous percentage measures, discrete counts, and nominal categorical states, rigorous preprocessing determines model stability as strongly as classifier architecture. Standardizing continuous numeric predictors—lecture attendance percentage, average internal assessment marks, active backlog tally, digital engagement index, and current semester—ensures balanced scale comparability when training linear baselines such as regularized Logistic Regression alongside ensemble benchmarks. Simultaneously, One-Hot Encoding with baseline category omission transforms nominal fee statuses (Paid, Partial, Pending) without introducing artificial ordinal distance.",
                    "Combining this ColumnTransformer preprocessor inside a unified Scikit-Learn Pipeline eliminates data leakage between training and validation partitions, while ensuring identical serialization via Joblib for sub-millisecond web inference. Setting ensemble hyperparameters—120 decision estimators constrained to maximum depth 8 with minimum split cardinality 5—strikes a disciplined empirical balance between capturing nuanced student attribute interactions and preventing memorization of cohort idiosyncrasies."
                ]
            },
            {
                "id": "2.9",
                "title": "2.9 Technological Foundation: Flask, SQLAlchemy ORM, Scikit-Learn, and Chart.js",
                "paragraphs": [
                    "Choosing an integrated Python full-stack architecture removes network serialization friction between web request handling and machine learning inference. Flask supplies lightweight Blueprint-ready routing, server-side Jinja2 template composition, and Werkzeug PBKDF2-SHA256 cryptographic password hashing without heavy runtime overhead. Pairing Flask with SQLite managed via SQLAlchemy ORM provides relational schema normalization (Users, Students, CounsellingCases, AuditLogs, Notifications, SystemSettings), transactional integrity, and zero external database daemon configuration across both Windows and macOS deployments.",
                    "On the presentation tier, Bootstrap 5 responsive layouts and Chart.js client-side canvases render donut risk distributions, departmental burden bar charts, and progress saturation gauges smoothly inside standard modern browsers without external SaaS chart dependencies."
                ]
            },
            {
                "id": "2.10",
                "title": "2.10 Identified Research Gap and Integrated Summary of Literature Findings",
                "paragraphs": [
                    "Synthesis of reviewed literature exposes a pronounced translation gap between predictive analytics scholarship and practical university mentoring infrastructure. Academic benchmarks optimize classification metrics on static CSV snapshots yet neglect the governance workflows that determine whether an institutional prediction saves an enrolled student. Specifically, four gaps remain unaddressed by lightweight open solutions: (1) deterministic per-student percentage attribution combining learned ensemble importances with administrator-tunable policy thresholds; (2) real-world schema-tolerant bulk CSV ingestion capable of parsing heterogeneous institutional headers; (3) capacity-capped multi-stage mentoring workflows with automated stall escalation; and (4) complete forensic auditability with strict student peer isolation.",
                    "Our project directly closes every one of these gaps inside a cohesive, thoroughly tested web application tailored for academic deployment at Sanskriti University."
                ]
            }
        ]
    }
