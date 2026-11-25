# -*- coding: utf-8 -*-
"""Original, plagiarism-proof academic prose for Chapters 3 and 4 of the Sanskriti University B.Tech Project Report."""

def get_chapter_3():
    return {
        "number": 3,
        "title": "CHAPTER 3 – METHODOLOGY",
        "sections": [
            {
                "id": "3.1",
                "title": "3.1 Timeline of the Reported Problem",
                "paragraphs": [
                    "Understanding how institutional attrition unfolds across an engineering degree curriculum clarifies why continuous software-assisted monitoring is indispensable. Rather than manifesting suddenly during final-year placement drives, dropout vulnerability follows a predictable semester-by-semester trajectory across university cohorts. Historically, institutions relied on manual register tallies at the close of an eighteen-week academic term—long after formative damage had accumulated.",
                    "During Weeks 1 to 4 of an active semester, subtle early warning indicators appear in irregular laboratory attendance and delayed fee settlement. Between Weeks 5 and 9, first sessional examinations expose conceptual gaps among learners carrying unresolved prior-semester arrears. By Weeks 10 to 14, discouraged students disengage silently from classroom tutorials and digital learning portals. Under legacy manual practices, coordinators compile shortage lists only in Week 16, leaving insufficient instructional days for attendance recovery or structured faculty remediation. Our methodology compresses this detection-to-intervention cycle from sixteen weeks to real-time instant scoring upon single registration or weekly CSV roster upload."
                ]
            },
            {
                "id": "3.2",
                "title": "3.2 Existing Solutions and Comparative Limitations",
                "paragraphs": [
                    "Existing institutional solutions fall into three primary patterns: disconnected spreadsheet trackers, rule-only ERP alert modules, and academic batch scripts. Spreadsheet trackers allow easy departmental editing but lack statistical calibration, version history, privacy locks, and standardized mentoring stages. ERP alert plugins depend strictly on rigid cutoff rules that either flood mentors with false positives or overlook moderate compound deficits across attendance, marks, and fee status.",
                    "Standalone Python research notebooks prove that machine learning algorithms can model dropout risk mathematically, yet fail campus operationalization because non-technical clerks and department heads cannot execute scripts, retrain classifiers with updated semester data, or document student counselling conversations inside an auditable portal. Our solution inherits the statistical strengths of supervised ensembles while wrapping them inside an accessible browser workflow guarded by strict authentication and ACID persistence."
                ]
            },
            {
                "id": "3.3",
                "title": "3.3 Bibliometric and Empirical Research Analysis",
                "paragraphs": [
                    "Analysis of recent Educational Data Mining publications across IEEE, Springer, and Elsevier venues reflects rapid convergence around hybrid human-in-the-loop architectures. Early EDM studies (2015–2019) concentrated predominantly on accuracy maximization via neural networks and support vector machines. Subsequent institutional deployment evaluations (2020–2025) revealed low faculty adoption of black-box scores and documented a decisive methodological shift toward Explainable AI (XAI) techniques—particularly tree-ensemble feature attribution and counterfactual deficit diagnostics.",
                    "Guided by these empirical findings, our engineering methodology prioritizes interpretable ensemble engineering over opaque black-box tuning. Every algorithmic decision inside our training and inference module balances three measurable attributes: high discrimination (verified via 96.77 percent ROC-AUC on held-out test partitions), fast deterministic CPU execution (under 15 milliseconds per cohort inference pass), and exact percentage reason decomposition aligned directly with institutional counseling playbooks."
                ]
            },
            {
                "id": "3.4",
                "title": "3.4 Review Summary",
                "paragraphs": [
                    "Synthesizing pedagogical literature, regulatory compliance norms, and software engineering principles yields five non-negotiable methodological pillars for our system: (1) heterogeneous tabular preprocessing combining scaled continuous indicators and encoded nominal states within an atomic Scikit-Learn Pipeline; (2) comparative model benchmarking pairing a linear Logistic Regression baseline with a regularized 120-tree Random Forest classifier; (3) dynamic hybrid explainability combining learned Gini feature weights with configurable administrative policy boundaries; (4) structured five-stage counseling triage enforcing coordinator workload quotas and automatic alert escalation; and (5) strict cryptographic session governance backed by tamper-evident audit trails."
                ]
            },
            {
                "id": "3.5",
                "title": "3.5 Problem Definition",
                "paragraphs": [
                    "Formally, let each enrolled student record at epoch t be represented by a six-dimensional institutional feature tuple capturing attendance percentage, average internal assessment score, active backlog count, tuition fee status, digital learning engagement score, and current academic semester. The dual computational and operational problem comprises: first, learning and calibrating a probabilistic estimator mapping that feature vector onto a continuous dropout probability bounded in [0, 1] alongside an interpretable reason attribution vector whose non-negative root-cause weights sum strictly to 100 percent; and second, orchestrating role-isolated campus intervention pipelines where every flagged learner advances traceably across bounded counselling states until stabilized retention is documented."
                ]
            },
            {
                "id": "3.6",
                "title": "3.6 Goals and Objectives",
                "paragraphs": [
                    "The project methodology establishes six clear, verifiable engineering and institutional objectives:",
                    "1. Multi-Factor Predictive Accuracy: Train, evaluate, and deploy a supervised Random Forest classifier benchmarked directly against a Logistic Regression baseline over realistic correlated cohort distributions, achieving strong accuracy and ROC-AUC separation.",
                    "2. Normalized XAI Reason Attribution: Decompose every prediction into ranked, human-readable causal deficits (such as Attendance Deficit, Internal Assessment Struggle, Active Backlogs Burden, Fee Payment Stress, and Low Academic Engagement) summing cleanly to 100 percent.",
                    "3. Institutional Schema Tolerance: Construct a dictionary-based CSV header-alias engine capable of normalizing real-world departmental exports automatically without demanding brittle manual column renaming.",
                    "4. Capacity-Governed Counselling Lifecycle: Implement a structured five-stage counselling hub featuring configurable per-stage active queue limits, mandatory session logs, and automated high-risk stall escalation alerts.",
                    "5. Four-Tier RBAC Privacy Enforcement: Enforce cryptographic PBKDF2-SHA256 authentication and route-level authorization isolating Administrator, Guide/HOD, Faculty Mentor, and Student views with strict HTTP 403 peer-protection guards.",
                    "6. Dynamic Governance and Cross-Platform Reproducibility: Deliver live administrative threshold re-scoring, labelled dataset retraining, forensic audit trail inspection, and verified one-command startup across both Windows PowerShell and macOS Terminal environments."
                ]
            },
            {
                "id": "3.7",
                "title": "3.7 Scope of the System",
                "paragraphs": [
                    "The developed application spans complete lifecycle support across academic cohort ingestion, predictive ML inference, individual diagnostics, multi-stage mentor interventions, administrative rule governance, and security auditing. Within a single browser portal, authorized staff can register individual learners or upload multi-hundred-row CSV cohorts spanning all SOEIT branches, review visual KPI analytics, inspect per-student reason breakdown cards, assign mentors, advance students through five structured counselling stages, calibrate warning cutoffs, retrain predictive weights on labeled historical datasets, and inspect immutable IP-tagged audit logs.",
                    "Consistent with institutional security guidelines, the current system scopes persistence to an embedded self-contained SQLite relational store optimized for seamless offline-capable campus hosting without external cloud lock-in, while preserving clean SQLAlchemy ORM abstraction for straightforward migration to PostgreSQL or MySQL in multi-campus cluster deployments."
                ]
            },
            {
                "id": "3.8",
                "title": "3.8 System Requirements",
                "paragraphs": [
                    "Software and hardware requirements were minimized deliberately so any standard departmental server, laboratory workstation, Windows notebook, or Apple Silicon / Intel MacBook executes both live web serving and on-demand Random Forest retraining comfortably inside an isolated virtual environment."
                ],
                "table": {
                    "caption": "Table 3.1: Verified Hardware and Software Environment Specifications",
                    "headers": ["Component Layer", "Minimum / Verified Specification", "Engineering Role in System"],
                    "rows": [
                        ["Operating System", "Windows 10/11 (PowerShell) or macOS 12+ (zsh/bash) or Linux", "Cross-platform campus deployment without OS lock-in"],
                        ["Processor & Memory", "Dual-Core x86_64 / ARM64 CPU, 4 GB RAM (8 GB Recommended)", "Fast CPU inference (<15 ms) and sub-3s ensemble retraining"],
                        ["Python Runtime", "Python 3.10+ inside isolated .venv environment", "Reproducible dependency isolation via requirements.txt"],
                        ["Web & Security Stack", "Flask 3.x, Werkzeug PBKDF2-SHA256, Jinja2 Templates", "Session cookies, @roles_required RBAC, HTML rendering"],
                        ["ML & Data Stack", "Scikit-Learn, Pandas, NumPy, Joblib Serialization", "ColumnTransformer, 120-Tree RF, LR Baseline, CSV Aliasing"],
                        ["Database Engine", "SQLite 3 via SQLAlchemy ORM", "Normalized ACID tables (Users, Students, Cases, Logs, Rules)"],
                        ["Client Interface", "Bootstrap 5 + Chart.js (Chrome, Safari, Edge, Firefox)", "Responsive dashboards, risk charts, zero-plugin UI"]
                    ]
                }
            }
        ]
    }


def get_chapter_4():
    return {
        "number": 4,
        "title": "CHAPTER 4 – DESIGN FLOW/PROCESS",
        "sections": [
            {
                "id": "4.1",
                "title": "4.1 Evaluation & Selection of Specifications and Features",
                "paragraphs": [
                    "Selecting the minimal yet diagnostically complete feature schema required balancing predictive sensitivity against institutional data availability across typical university registrar offices. Overly intrusive socio-economic survey attributes—such as parental psychological questionnaires or private banking statements—often suffer from high missingness, respondent bias, and privacy objections. Conversely, purely demographic records cannot evolve mid-semester as a student's academic standing improves or deteriorates.",
                    "Consequently, six high-signal institutional telemetry attributes already tracked routinely within departmental operations were selected: (1) cumulative attendance percentage [0–100], (2) internal assessment marks average [0–100], (3) active academic backlog count [0–15], (4) tuition fee settlement state [Paid, Partial, Pending], (5) digital/classroom engagement index [0–100], and (6) active semester index [1–8]. Combined with student metadata (full name, unique university enrollment identifier, department code, and optional assigned mentor), these six predictors capture attendance discipline, conceptual mastery, examination carry-over stress, financial friction, and silent withdrawal simultaneously."
                ]
            },
            {
                "id": "4.2",
                "title": "4.2 Design Constraints",
                "paragraphs": [
                    "Architectural design operated under five explicit institutional and technical constraints: (1) Cross-Platform Determinism—all file paths, virtual environment commands, and SQLite bindings must run identically across Windows development workstations and macOS evaluation laptops (accounting cleanly for macOS AirPlay Receiver occupying TCP port 5000 when needed); (2) Strict Confidentiality—route authorization must enforce fail-closed RBAC so logged-in students cannot enumerate peer URLs via direct browser address tampering; (3) Non-Destructive Governance—modifying warning thresholds via the Admin governance panel must re-score existing records transactionally without wiping historical mentoring remarks; (4) Explainable Transparency—every model prediction must carry deterministic, auditable reason weights rather than arbitrary text strings; and (5) Graceful Schema Flexibility—CSV bulk uploads must accept real-world column capitalization and spacing variants seamlessly."
                ]
            },
            {
                "id": "4.3",
                "title": "4.3 Analysis and Feature Finalization Subject to Constraints",
                "paragraphs": [
                    "Evaluating design alternatives against these constraints guided three critical architectural refinements. First, rather than exposing raw asynchronous microservices requiring Redis brokers and Celery workers—which complicate university lab installations—alert escalation checks and CSV batch scoring execute synchronously within atomic SQLAlchemy database transactions. Second, our ML inference module loads a serialized Joblib bundle containing both the tuned Random Forest pipeline and Logistic Regression benchmark pipeline upon application startup, delivering sub-millisecond row predictions while allowing single-click retraining directly inside the Admin panel.",
                    "Third, institutional counselling progression was formalized into five explicit, ordered lifecycle stages: 'Identified Risk', 'First Outreach', 'Counselling Scheduled', 'Follow-Up Active', and 'Resolved'. Coupling these stages with configurable maximum capacity limits ensures faculty mentors immediately observe queue bottlenecks via live progress meters before bottlenecks harm vulnerable students."
                ]
            },
            {
                "id": "4.4",
                "title": "4.4 Design Flow",
                "paragraphs": [
                    "The overall system design flow coordinates authentication, input sanitization, machine learning inference, explainable attribution synthesis, risk stratification, counselling queue assignment, SQLite ACID persistence, and interactive analytics rendering along deterministic execution branches. Every entry route funnels through cryptographic identity verification before dispatching to role-tailored views."
                ],
                "subsections": [
                    {
                        "id": "4.4.1",
                        "title": "4.4.1 Design Flow Diagram",
                        "paragraphs": [
                            "Figure 4.4.1 illustrates the complete operational flowchart of the Student Dropout Prediction and Reason Attribution system. Upon user login through PBKDF2-SHA256 verification, role claims govern access across Administrative / HOD ingestion, Mentor triage, or isolated Student self-monitoring. When an Admin or HOD registers a student record or uploads a bulk CSV roster, the header alias engine normalizes column labels and verifies domain bounds. Valid rows pass through the Scikit-Learn ColumnTransformer and 120-tree Random Forest classifier before the Gini feature-deficit engine calculates normalized percentage attributions summing to 100 percent.",
                            "Records exceeding configured institutional probability thresholds or breaching active academic deficit bounds enter the five-stage Counselling Hub queue after automated capacity verification, where assigned faculty mentors document structured action plans. Parallel low-risk records update clean student scorecards directly. All state transitions commit inside ACID SQLite transactions alongside immutable IP-tagged forensic audit logs before refreshing live Chart.js visualizations."
                        ],
                        "figure": {
                            "path": "static/images/diagrams/diag_4_4_1_design_flow.png",
                            "caption": "Figure 4.4.1 Design Flow Diagram",
                            "width_in": 6.1
                        }
                    },
                    {
                        "id": "4.4.2",
                        "title": "4.4.2 System Navigation Flow Diagram",
                        "paragraphs": [
                            "Figure 4.4.2 presents the three-tier architectural topology and role-governed navigation structure across Presentation, Application Gateway, Machine Learning Engine, and Persistence tiers. At the top tier, four strictly scoped RBAC personas connect over standard browser HTTP sessions. The Jinja2 and Bootstrap 5 Presentation Tier renders role-filtered KPIs, Chart.js analytics canvases, normalized XAI deficit breakdown cards, and five-stage queue capacity bars.",
                            "All form submissions and bulk uploads pass through the Flask Application Gateway, where Werkzeug security utilities, @roles_required authorization decorators, the dictionary header-alias CSV mapper, and the automated stall scanner coordinate execution. Below the gateway, the modular ML engine, 3NF SQLite relational database, and disk storage assets maintain clean separation of concerns so model updates never corrupt web controller stability."
                        ],
                        "figure": {
                            "path": "static/images/diagrams/diag_4_4_2_architecture.png",
                            "caption": "Figure 4.4.2 System Navigation Flow Diagram",
                            "width_in": 6.1
                        }
                    }
                ]
            },
            {
                "id": "4.5",
                "title": "4.5 Design Selection",
                "paragraphs": [
                    "Multiple technology combinations were weighed carefully before finalizing our implementation stack. Deploying a decoupled React Single Page Application (SPA) paired with a remote FastAPI inference cluster was evaluated and intentionally rejected for this campus scope because maintaining Node build pipelines, CORS token policies, and cross-process queues adds fragile operational overhead for university faculty administrators. Server-rendered Jinja2 templates paired with targeted Bootstrap 5 interactions and Chart.js visualizations deliver crisp responsiveness inside zero-build-step Python packaging.",
                    "Similarly, while deep tabular neural networks require large labeled campus archives to generalize reliably without hyperparameter instability, our regularized 120-tree Random Forest ensemble achieves superior out-of-the-box calibration on medium-sized institutional cohorts (n = 115–2,500) while exposing exact deterministic Gini feature importances required for transparent educational accountability."
                ]
            },
            {
                "id": "4.6",
                "title": "4.6 Implementation Plan and Methodology",
                "paragraphs": [
                    "Software construction followed a six-phase iterative Software Development Life Cycle (SDLC) tailored specifically around faculty validation feedback, institutional data ethics, and automated regression testing. Figure 4.6 maps the cyclic engineering progression connecting institutional requirement discovery, three-tier schema architecture, full-stack ML/XAI construction, eight-suite automated validation, cross-platform environment packaging, and continuous post-deployment threshold recalibration."
                ],
                "figure_inline": {
                    "path": "static/images/diagrams/diag_4_6_sdlc.png",
                    "caption": "Figure 4.6 Software Development Life Cycle of Student Dropout Prediction System",
                    "width_in": 6.1
                },
                "subsections": [
                    {
                        "id": "4.6.1",
                        "title": "4.6.1 Use Case Diagram",
                        "paragraphs": [
                            "Figure 4.6.1 depicts actor interactions across the system boundary, cleanly isolating privileges among Admin / HOD authority users, Faculty Mentors, Students, and the automated ML & XAI Inference Engine. Administrators and HODs initiate onboarding, bulk cohort CSV ingestion (which implicitly includes Random Forest inference and XAI decomposition), policy threshold adjustments, mentor workload allocation, audit log review, and ground-truth retraining.",
                            "Faculty Mentors concentrate exclusively on inspecting departmental alerts, analyzing normalized deficit cards, scheduling sessions, and progressing flagged learners across the five-stage lifecycle. Students access strictly their own academic profile, risk tier badge, and constructive counsellor guidance, ensuring total peer-to-peer privacy inside shared computer labs."
                        ],
                        "figure": {
                            "path": "static/images/diagrams/diag_4_6_1_usecase.png",
                            "caption": "Figure 4.6.1 Use Case Diagram",
                            "width_in": 6.1
                        }
                    },
                    {
                        "id": "4.6.2",
                        "title": "4.6.2 Four-Tier Closed-Loop User Module",
                        "paragraphs": [
                            "Figure 4.6.2 formalizes the closed-loop retention lifecycle connecting all four operational modules into a self-correcting institutional feedback cycle. First, Administrators or HODs ingest single learner updates or bulk CSV rosters into the platform. Second, the ML & XAI engine evaluates updated dropout probabilities and recomputes normalized reason attribution cards. Third, conditional branching routes vulnerable learners into the Mentor Counselling Workbench while updating transparent preventative scorecards inside the Student Self-Portal.",
                            "Finally, persistent counselling documentation, stage saturation alarms, and forensic audit events commit to SQLite storage. When administrators update institutional cutoff limits or trigger supervised model retraining from accumulated historical outcomes, updated predictive weights loop smoothly back into cohort scoring, closing the continuous improvement cycle."
                        ],
                        "figure": {
                            "path": "static/images/diagrams/diag_4_6_2_closed_loop.png",
                            "caption": "Figure 4.6.2 Four-Tier Closed-Loop User Module",
                            "width_in": 6.1
                        }
                    },
                    {
                        "id": "4.6.3",
                        "title": "4.6.3 Sequence Diagram",
                        "paragraphs": [
                            "Figure 4.6.3 traces chronological message exchanges during a real-time cohort ingestion, prediction, queueing, and audit sequence. After the Admin/HOD browser submits a validated form or bulk CSV payload, the Flask router enforces RBAC decorators and normalizes CSV aliases before invoking the singleton ML & XAI engine. The engine applies fitted scaling and encoding transformations, computes ensemble dropout probabilities, generates normalized 100-percent deficit breakdowns, and returns structured predictions to the router.",
                            "The controller persists updated student rows via ACID SQLite commits, dispatches high-risk alerts across the Counselling Hub queue after evaluating active stage capacities, emits tamper-evident AuditLog records, and returns updated analytical dashboards to the client browser."
                        ],
                        "figure": {
                            "path": "static/images/diagrams/diag_4_6_3_sequence.png",
                            "caption": "Figure 4.6.3 Sequence Diagram",
                            "width_in": 6.1
                        }
                    },
                    {
                        "id": "4.6.4",
                        "title": "4.6.4 Class Diagram",
                        "paragraphs": [
                            "Figure 4.6.4 illustrates the normalized object-relational domain schema and predictive engine abstractions underpinning platform persistence. Six core domain classes coordinate cleanly through explicit cardinalities: User governs authentication credentials and departmental scopes; Student retains six core predictors alongside cached ensemble risk scores and counselling statuses; MLEngine encapsulates the serialized Random Forest and Logistic Regression pipelines alongside retraining routines; CounsellingCase tracks mentor remarks, action plans, and five-stage workflow positions; AuditLog and Notification record forensic user events and system escalations; and SystemSetting preserves dynamic institutional warning cutoffs and queue capacity quotas."
                        ],
                        "figure": {
                            "path": "static/images/diagrams/diag_4_6_4_class.png",
                            "caption": "Figure 4.6.4 Class Diagram",
                            "width_in": 6.1
                        }
                    }
                ]
            }
        ]
    }
