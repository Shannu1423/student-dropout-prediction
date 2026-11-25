# -*- coding: utf-8 -*-
"""Full-depth original academic prose for Chapters 1 & 2 (~5,000 words total, zero code, plagiarism-proof)."""

def get_chapter_1():
    return {
        "number": 1,
        "title": "CHAPTER 1 – INTRODUCTION",
        "sections": [
            {
                "id": "1.1",
                "title": "1.1 Identification of Students, Faculty Mentors, and Academic Authorities",
                "paragraphs": [
                    "AI-Based Prediction of Reasons for Student Dropout is architected directly around the everyday operational responsibilities of four interdependent academic user groups operating across an undergraduate engineering institution: university administrators, Heads of Departments (HODs) and academic guides, faculty mentors, and enrolled learners. Within multidisciplinary technical schools such as the School of Engineering & Information Technology (SOEIT), Sanskriti University, cohorts span specialized disciplines including Computer Science and Engineering (CSE), Artificial Intelligence and Machine Learning (AIML), Data Science, Information Technology, Electronics and Communication Engineering, Mechanical Engineering, and Civil Engineering. Across these rigorous four-year degree programs, voluntary departure and academic detention rarely result from an isolated incident. Instead, attrition materializes gradually through overlapping class absences, declining sessional quiz scores, unresolved semester examination arrears, irregular tuition settlements, and progressive disengagement from coursework.",
                    "Under conventional manual administration, institutional telemetry remains fragmented across isolated departmental spreadsheets maintained separately by attendance clerks, examination controllers, accounts personnel, and branch coordinators. By the time an administrative defaulter sheet compiles attendance shortages during closing weeks of a term, constructive instructional time needed for remedial tutoring or structured mentorship has already slipped away. Faculty mentors entrusted with thirty to sixty mentees face acute triage ambiguity because static registers fail to distinguish a student recovering from short-term illness from a peer experiencing severe simultaneous erosion across attendance, sessional grades, and tuition arrears.",
                    "Academic Heads of Departments likewise lack real-time cross-sectional visibility showing which engineering disciplines accumulate high-risk concentrations, preventing timely reallocation of remedial laboratory coaching, bridge tutorials, or balanced mentor assignments. Equally important, enrolled students seldom receive clear, supportive early warnings explaining how declining classroom attendance or active examination backlogs shift their continuation outlook. Consolidating administrative oversight, explainable predictive intelligence, structured five-stage counseling governance, and strictly isolated student scorecards within one unified web platform aligns institutional resources cleanly behind proactive retention."
                ]
            },
            {
                "id": "1.2",
                "title": "1.2 Justification of Issue Through Statistics and Documentation",
                "paragraphs": [
                    "Improving undergraduate persistence represents an urgent national priority documented extensively by statutory Indian regulatory frameworks and global educational development reports. Annual statistical releases from the All India Survey on Higher Education (AISHE) compiled by the Ministry of Education emphasize that despite sustained growth in engineering seat intake over the preceding decade, mid-degree attrition, year-back progression delays, and exam-detention losses concentrate heavily during the first four semesters of study. Incoming undergraduate learners frequently experience sharp academic transitions involving higher-order quantitative coursework, English technical terminology, relocation into residential campus hostels, and household affordability constraints.",
                    "Consistent with these trends, the National Education Policy (NEP) 2020 directs universities to operationalize continuous formative tracking, flexible supportive remediation, and dedicated mentor-mentee advisory structures designed explicitly to curb preventable dropout before permanent withdrawal occurs. Empirical measurements obtained from our system's active monitoring dataset comprising 115 undergraduate student records across seven SOEIT disciplines vividly confirm this institutional distribution: calibrated inference identified 47 learners (40.9 percent) occupying high-risk or early-warning tiers alongside 68 learners (59.1 percent) maintaining healthy academic standing. Roughly two out of five undergraduates require proactive structured guidance or targeted monitoring during typical semester progression.",
                    "Quantitative feature profiling extracted from our calibrated 120-tree Random Forest ensemble proves that attrition susceptibility stems from compounding measurable attributes rather than any single isolated cutoff. Cumulative lecture attendance accounts for 43.79 percent of global Gini impurity reduction, average internal sessional marks contribute 21.23 percent, active examination arrears represent 15.89 percent, academic engagement score provides 11.08 percent, fee remittance condition (Paid versus Partial or Pending status) accounts for 6.18 percent combined, and semester progression accounts for 1.84 percent. Effective academic governance must monitor and explain all six concurrent dimensions rather than triggering belated end-term exclusions."
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
                    "Although universities routinely deploy transaction-oriented Enterprise Resource Planning (ERP) suites alongside course repositories, legacy campus software separates bureaucratic record storage entirely from predictive intervention workflows. ERP attendance software tabulates daily absences neutrally without elevating compound dropout risk when marginal attendance coincides with failing sessional tests and multiple pending arrears. Conversely, academic machine learning notebooks published in data science repositories stop immediately after displaying validation scores in offline scripts, offering zero institutional security, zero bulk spreadsheet tolerance, zero mentoring accountability, and zero explainable action guidance.",
                    "Three fundamental gaps render existing procedures ineffective for university coordinators: (1) The Opaque Probability Gap—displaying an unexplained probability score leaves mentors uncertain whether to arrange subject tutoring, recommend installment fee deferrals, or schedule motivational guidance; (2) The Intervention Accountability Gap—static spreadsheet defaulters circulated before exams lack tracked five-stage progression, mentor remarks logs, stage workload caps, or automated stall escalation alerts; and (3) The Institutional Confidentiality Gap—transmitting unencrypted spreadsheets over chat groups exposes private student financial hardship and examination arrears without Role-Based Access Control (RBAC) or immutable audit records.",
                    "Solving these intertwined challenges requires engineering an integrated web application unifying non-linear Random Forest ensemble inference, normalized 100-percent Gini reason cards, dictionary header-alias CSV parsing, live configurable institutional rules, capacity-bounded counseling queues, four-tier RBAC security, and tamper-evident audit logging cleanly inside a portable Python architecture."
                ]
            },
            {
                "id": "1.4",
                "title": "1.4 Justification of Need Through Survey",
                "paragraphs": [
                    "Prior to freezing functional specifications, informal requirement interviews and workflow walkthroughs were carried out with CSE faculty advisors, branch coordinators, examination guides, and student representatives to catalog tangible day-to-day pain points. Faculty coordinators consistently identified spreadsheet schema mismatch as their top practical obstacle: campus offices export attendance columns under disparate labels (such as Attendance_Percentage, att_pct, or Presence) and sessional averages under inconsistent headings, costing hours of tedious column editing before batch risk reviews can proceed.",
                    "Heads of Departments highlighted coordinator fatigue and triage congestion prior to semester examinations. When high-risk students accumulate disproportionately inside early stages without visible queue caps or stall escalation warnings, critical cases slip through overlooked. Coordinators specifically requested browser-hosted rule sliders allowing administrators to modify attendance thresholds (default 75 percent warning, 60 percent critical), internal mark limits, backlog cutoffs, and counseling stage limits instantaneously without altering program source files.",
                    "Participating undergraduate students expressed strong demand for fair, transparent academic visibility balanced against strict peer privacy. Learners appreciated receiving early diagnostic percentages alongside constructive mentor recommendations weeks ahead of detention lists, provided horizontal authorization strictly blocks fellow students from accessing peer academic records, arrears, or counseling histories."
                ]
            },
            {
                "id": "1.5",
                "title": "1.5 Relevant Contemporary Issue Documented In Report By Agencies",
                "paragraphs": [
                    "Global and national accreditation bodies increasingly recognize transparent retention systems as core pillars of ethical higher education governance. Guidance bulletins issued by UNESCO regarding artificial intelligence in educational decision-making caution strongly against black-box risk scoring: algorithmic outputs affecting human educational pathways must remain inspectable, contestable, proportionally normalized, and channeled exclusively toward supportive mentoring rather than automated academic punishment.",
                    "Domestically, accreditation manuals published by the National Assessment and Accreditation Council (NAAC)—specifically Criterion 2 (Teaching-Learning and Evaluation) and Criterion 5 (Student Support and Progression)—mandate verifiable documentation proving structured slow-learner identification, regular mentor-mentee consultations, action-plan tracking, and measurable academic stabilization. Traditional physical diary binders fall short during institutional peer-team audits because follow-up consistency and historical progression trails cannot be queried rapidly. Our unified relational architecture records every model assessment, normalized XAI reason card, five-stage outreach remark, and administrative audit event seamlessly to meet contemporary regulatory accountability standards."
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
                    "To ground our system architecture in validated scientific theory and production software practices, a structured literature review was conducted spanning Educational Data Mining (EDM), Learning Analytics, supervised tabular ensemble modeling, Explainable Artificial Intelligence (XAI), and campus mentoring workflow engineering. Over the past twenty years, attrition scholarship has evolved from descriptive psychological questionnaires toward automated institutional early-warning platforms extracting actionable signals directly from digital attendance registers, gradebooks, and engagement telemetry.",
                    "Critically surveying peer-reviewed studies alongside commercial retention software exposes why purely predictive scripts rarely translate into sustained campus impact. High validation accuracy alone cannot reduce attrition unless coupled tightly with transparent human-readable causal attributions, resilient institutional CSV ingestion, bounded counselor capacity management, and fail-closed privacy protection across all user personas.",
                    "Subsequent subsections review longitudinal attrition theories, supervised ensemble dominance on mixed tabular cohorts, India-specific academic regulatory realities, mentor workflow bottlenecks, legacy ERP blind spots, XAI explainability requirements, comparative market gaps, preprocessing invariance guarantees, full-stack framework choices, and a consolidated synthesis of remaining research gaps."
                ]
            },
            {
                "id": "2.2",
                "title": "2.2 Growth of Machine Learning and Educational Data Mining in Higher Education",
                "paragraphs": [
                    "Foundational higher-education dropout theory traces back to Vincent Tinto's longitudinal student integration model (1993) and John Bean's causal organizational attrition framework (1980). Tinto established that student persistence reflects continuous alignment between academic integration (examination mastery, faculty dialogue) and social integration within campus communities. While foundational conceptually, classic questionnaire-based persistence models suffered from low periodic response rates, retrospective recall bias, and slow multi-month analysis turnaround incapable of alerting advisors mid-semester.",
                    "The expansion of Educational Data Mining and institutional LMS databases catalyzed supervised classification studies operating directly over administrative telemetry. Multi-institutional comparative analyses across international benchmarks—such as the UCI Higher Education Students Performance dataset curated by Realinho et al. (2022) and comprehensive surveys by Romero and Ventura (2020)—demonstrate consistently that tree-based ensembles outperform isolated linear regressors, single decision trees, and k-nearest-neighbor classifiers across noisy academic records.",
                    "This performance advantage arises directly from non-linear feature interactions governing student progression: an undergraduate maintaining 74 percent attendance alongside zero arrears behaves fundamentally differently from a learner exhibiting 74 percent attendance alongside three pending backlogs and pending tuition fees. Random Forest bagging (Breiman, 2001) decorrelates individual split trees over bootstrap resamples, suppressing high variance while preserving strong discrimination across compound institutional signals."
                ]
            },
            {
                "id": "2.3",
                "title": "2.3 Student Retention and Digital Governance Landscape in India",
                "paragraphs": [
                    "Across autonomous Indian engineering faculties governed by All India Council for Technical Education (AICTE) and University Grants Commission (UGC) regulations, strict continuous eligibility rules shape academic progression directly. Minimum attendance bands—customarily fixed at 75 percent for theory and laboratory sessions, with conditional 60 percent thresholds subject to medical approval—dictate final examination hall-ticket clearance alongside strict backlog carry-over progression caps. Implementation of NEP 2020 and Academic Bank of Credits (ABC) tracking further amplifies institutional reporting complexity.",
                    "In practice, computing infrastructure across regional Indian universities comprises heterogeneous software blends: proprietary accounting suites, localized Excel mark registers, and Moodle or Google Classroom archives operated across both Windows lab desktops and faculty macOS laptops. Furthermore, many campus departments deploy analytics inside restricted local intranets without persistent GPU clusters or costly enterprise cloud licenses. Practical dropout software tailored for Indian campuses must therefore deliver lightweight CPU execution, tolerant CSV schema mapping across inconsistent departmental spreadsheets, and effortless offline-capable SQLite persistence."
                ]
            },
            {
                "id": "2.4",
                "title": "2.4 Challenges Faced by Mentors and Coordinators in Early Risk Detection",
                "paragraphs": [
                    "Operational workflow evaluations across university faculty coordinators highlight four chronic bottlenecks impeding timely early warning without dedicated retention platforms. First, univariate rule alerts trigger severe signal dilution across large undergraduate cohorts: filtering every learner slipping transiently below a flat attendance bar crowds watchlists with stable learners recuperating from minor illness, obscuring silently failing learners burdened by compounding sessional weaknesses.",
                    "Second, real-world spreadsheet imports suffer rampant column naming inconsistencies across branch offices—attendance may appear labeled att_pct, Attendance_Percentage, or Attendance_% across successive semesters—stalling batch consolidation behind hours of tedious spreadsheet cleansing. Third, informal mentoring logs preserved in isolated notebooks lack structured follow-up stages, capacity balancing, and automatic stall escalation alerts when overloaded coordinators defer outreach during mid-term examination weeks. Fourth, static spreadsheets cannot dynamically cascade modified institutional warning rules cleanly across active records."
                ]
            },
            {
                "id": "2.5",
                "title": "2.5 Limitations of Traditional ERP Dashboards and Conventional Advisory Methods",
                "paragraphs": [
                    "Conventional university ERP portals excel at deterministic administrative compliance—fee receipt reconciliation, faculty scheduling, payroll audits, and semester marksheet generation—yet perform poorly as proactive student retention assistants. Because ERP tables reflect static transactional history rather than forward-looking statistical inference, staff view past shortfalls only after critical examination cutoffs pass. Moreover, simple threshold reports remain blind to moderate multi-domain degradation occurring simultaneously across attendance, quiz averages, arrears, and LMS withdrawal.",
                    "Manual paper mentor diaries suffer corresponding transparency and continuity breakdowns. While empathetic personal advisement remains irreplaceable, paper forms cannot automatically quantify branch-level vulnerability concentrations via live visual charts, alert HODs when critical high-risk cases stall uncontacted in early queue stages, prevent unbalanced overload on individual faculty mentors via queue caps, or maintain verifiable cross-semester handover logs as mentees advance across academic years."
                ]
            },
            {
                "id": "2.6",
                "title": "2.6 Importance of Explainable AI (XAI) Reason Attribution in Academic Decisions",
                "paragraphs": [
                    "Explainable Artificial Intelligence transforms probabilistic risk flags into actionable, equitable human interventions inside academic advising. Issuing unannotated numeric outputs—such as flagging a learner at 86.2 percent dropout likelihood without revealing root causes—erodes advisor trust and invites dangerous misallocation of institutional remedies. Knowing specifically whether high propensity stems predominantly from severe lecture absenteeism versus unresolved quantitative arrears or tuition installment stress empowers mentors to connect each student with precise academic coaching, counseling, or scholarship support immediately.",
                    "While game-theoretic Shapley estimators (SHAP) offer valuable model-agnostic decomposition in research studies, naive online approximation over small retraining cohorts can incur substantial computational overhead or non-intuitive negative baseline offsets for non-technical faculty users. Pairing global Random Forest Gini split importances cleanly with instance-specific policy deficit severity and normalizing strictly across active contributors ensures every flagged learner displays non-negative, crystal-clear cause percentages summing identically to 100 percent."
                ]
            },
            {
                "id": "2.7",
                "title": "2.7 Review of Existing Dropout Platforms and Market Gaps",
                "paragraphs": [
                    "Benchmarking existing academic and commercial retention tooling divides available landscape alternatives into three classes: enterprise cloud advising platforms (including Salesforce Education Cloud, EAB Navigate, and Ellucian Insights), built-in LMS engagement plugins (such as Moodle Analytics), and academic machine learning repositories published in open literature. Commercial enterprise suites offer robust enterprise orchestration yet carry steep recurring annual licensing expenses, complex vendor lock-in contracts, and multi-month ERP integration dependencies well outside typical college engineering budgets.",
                    "Conversely, open academic papers focus heavily on classifier benchmarking—comparing Random Forests, Support Vector Machines, Naive Bayes, and Neural Networks over static tabular CSV snapshots—while leaving full-stack campus usability unaddressed. Almost none provide built-in dictionary CSV header aliasing, dynamic policy cutoff re-scoring, five-stage counseling pipeline management protected by queue capacity limits, four-tier RBAC fail-closed horizontal privacy guards, or forensic IP-tagged audit trails."
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
                    "Handling mixed quantitative percentages, discrete backlog counts, and nominal categorical states demands leak-free preprocessing discipline. Standardizing numeric features—lecture attendance percentage, internal assessment average, active arrears, engagement score, and current semester—guarantees balanced feature scaling when evaluating linear probabilistic baselines such as Logistic Regression alongside tree classifiers. Simultaneously, applying OneHotEncoder with drop-first baseline omission encodes fee statuses (Paid, Partial, Pending) safely without implying spurious numeric ordering across categorical financial states.",
                    "Encapsulating this ColumnTransformer cleanly alongside classification estimators inside unified Scikit-Learn Pipeline objects serialized via Joblib guarantees identical preprocessing transforms across training, cross-validation, live HTTP predictions, and administrative ground-truth retraining. Constraining our Random Forest architecture to 120 decision estimators capped at maximum depth 8 and minimum split cardinality 5 yields reliable probability discrimination while preventing overfitting onto cohort noise."
                ]
            },
            {
                "id": "2.9",
                "title": "2.9 Technological Foundation: Flask, SQLAlchemy ORM, Scikit-Learn, and Chart.js",
                "paragraphs": [
                    "Constructing the entire web gateway and ML inference stack inside unified Python minimizes serialization friction, simplifies maintenance, and runs natively inside lightweight virtual environments across both Windows and macOS campus hardware. Flask supplies clean modular routing, Jinja2 template composition, and salted PBKDF2-SHA256 Werkzeug password cryptography without bloated framework dependencies. SQLAlchemy ORM layered cleanly over self-contained SQLite enforces third-normal-form relational schemas across Users, Students, CounsellingCases, Notifications, AuditLogs, and SystemSettings with atomic transaction safety.",
                    "Client presentation leverages responsive Bootstrap 5 grids combined cleanly with HTML5 Canvas Chart.js visualizations, rendering departmental vulnerability bar graphs and risk distribution donuts smoothly across modern standard browsers without third-party SaaS telemetry dependencies."
                ]
            },
            {
                "id": "2.10",
                "title": "2.10 Identified Research Gap and Integrated Summary of Literature Findings",
                "paragraphs": [
                    "Synthesizing reviewed theoretical frameworks, regulatory compliance imperatives, and technical tooling benchmarks pinpoints a critical operational gulf between static predictive algorithms and real institutional mentorship deployment. While existing scholarly models establish high classification capability, real university adoption stalls without four integrated pillars: (1) deterministic 100-percent normalized XAI cause breakdowns pairing learned ensemble weights with tunable institutional policy cutoffs; (2) automated header-alias CSV parsing accommodating messy branch spreadsheet conventions; (3) capacity-governed five-stage mentoring queues featuring stall escalation alerts; and (4) fail-closed four-tier RBAC isolation protected by immutable IP audit logging.",
                    "Our proposed system closes every identified research and implementation gap cohesively inside an immediately deployable full-stack platform tailored to university retention."
                ],
                "table": {
                    "caption": "Table 2.2: Synthesis of Key Literature Benchmarks & Engineering Translations",
                    "headers": ["Scholarly Domain / Study", "Primary Contribution / Evidence", "Direct Engineering Translation in Our System"],
                    "rows": [
                        ["Tinto (1993) & Bean (1980)", "Attritions reflect academic + financial + social compounding", "Unified 6-feature schema mixing marks, attendance, fees & engagement"],
                        ["Breiman (2001) & Realinho (2022)", "Random Forest ensembles excel on mixed tabular cohorts", "120-tree Random Forest achieving 89.87% Acc & 96.77% ROC-AUC"],
                        ["Romero & Ventura (2020)", "Educational Data Mining demands actionable workflows", "Integrated 5-stage Counselling Hub with mandatory action plans"],
                        ["Lundberg & Lee / XAI Literature", "Opaque risk probabilities hinder practitioner trust", "Multiplicative Gini + deficit XAI engine summing strictly to 100%"],
                        ["OWASP ASVS & ISO/IEC 27001", "Student academic & fee records require fail-closed security", "PBKDF2 hashes, 4-tier RBAC HTTP 403 guards & forensic AuditLogs"]
                    ]
                }
            }
        ]
    }
