# -*- coding: utf-8 -*-
"""Original, plagiarism-proof academic prose for Chapters 5, 6 and References of the Sanskriti University B.Tech Project Report."""

def get_chapter_5():
    return {
        "number": 5,
        "title": "CHAPTER 5 – RESULTS ANALYSIS AND VALIDATION",
        "sections": [
            {
                "id": "5.1",
                "title": "5.1 Implementation of Solution",
                "paragraphs": [
                    "The complete AI-Based Prediction of Reasons for Student Dropout platform was implemented using modular Python backend engineering (app.py and ml_engine.py), relational SQLite persistence, and responsive HTML5/Bootstrap 5 Jinja2 views enhanced with interactive Chart.js analytics. Upon initialization, the server executes create_app(), verifies normalized table construction, seeds default institutional risk thresholds and stage capacity quotas if uninitialized, loads pre-trained Scikit-Learn pipelines into memory, and exposes HTTPS-ready WSGI routing.",
                    "Subsections 5.1.1 through 5.1.7 document each operational screen captured directly from our running local server (http://127.0.0.1:5000), demonstrating real cohort telemetry, live explainable reason breakdowns, five-stage mentoring governance, administrative threshold recalibration, and forensic security logging."
                ],
                "subsections": [
                    {
                        "id": "5.1.1",
                        "title": "5.1.1 Login Page and Four-Tier Role Authentication Portal",
                        "paragraphs": [
                            "Figure 5.1.1 displays the unified authentication entry portal of the Student Dropout Prediction and Reason Attribution system. Built with an un-cluttered editorial layout optimized for desktop and mobile campus access, the sign-in card verifies user credentials against salted PBKDF2-SHA256 digests stored in the User table before issuing signed HTTP session cookies. Failed sign-in attempts automatically log security notices with requester IP addresses without leaking whether a username exists.",
                            "Immediately adjacent to the credential form, quick-access role badges clarify the four institutional permission tiers—Administrator, HOD/Guide, Faculty Mentor, and Student—enabling rapid authorized switching during faculty evaluations and institutional demonstrations."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig6_1_login.png",
                            "caption": "Figure 5.1.1 Login Page",
                            "width_in": 6.0
                        }
                    },
                    {
                        "id": "5.1.2",
                        "title": "5.1.2 Executive Cohort Dashboard Page",
                        "paragraphs": [
                            "Figure 5.1.2 captures the primary Executive Dashboard rendered after authenticated login by an Administrator or HOD/Guide. Four crisp KPI summary tiles highlight live cohort health metrics: 115 monitored students, 47 flagged At-Risk or Warning learners (40.9 percent), 68 stable Low-Risk learners (59.1 percent), and live model discrimination metrics (89.87 percent Random Forest Accuracy and 96.77 percent ROC-AUC).",
                            "Below the KPI strip, interactive Chart.js visualizations summarize cohort Risk Tier Distribution (donut ring) alongside Department-Wise Risk Burden across all seven SOEIT disciplines, allowing academic leadership to spot high-vulnerability branches at a glance without scrolling through dense raw spreadsheets."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig6_2_dashboard.png",
                            "caption": "Figure 5.1.2 Dashboard Page",
                            "width_in": 6.0
                        }
                    },
                    {
                        "id": "5.1.3",
                        "title": "5.1.3 Priority Flagged Students & Mentor Activity Feed",
                        "paragraphs": [
                            "Figure 5.1.3 shows the Priority Intervention Panel embedded within the operational dashboard, ranking urgent high-risk learners directly alongside each student's normalized Explainable AI (XAI) deficit weights and latest counsellor progression note. Rather than hiding reasoning behind vague numerical percentages, each row surfaces exact contributing drivers—such as attendance percentages below statutory cutoffs or pending semester arrears—linked seamlessly to one-click triage profiles.",
                            "Adjacent sidebar panels surface real-time automated escalation notifications triggered whenever high-risk cases stall unaddressed, ensuring coordinators prioritize stalled learners before end-semester examination deadlines."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig6_2b_flagged_mentor.png",
                            "caption": "Figure 5.1.3 Priority Flagged Students & Mentor Activity Feed",
                            "width_in": 6.0
                        }
                    },
                    {
                        "id": "5.1.4",
                        "title": "5.1.4 Student Monitoring Directory & Bulk Ingestion Hub",
                        "paragraphs": [
                            "Figure 5.1.4 demonstrates the searchable, filterable Student Monitoring Directory covering all 115 enrolled campus records across academic branches and risk statuses. Authorized coordinators can filter learners dynamically by Risk Tier, Department, or Name/Enrollment ID, inspect top AI-derived reason tags inline, export filtered cohort snapshots, register single students, or open the Bulk CSV Ingestion modal.",
                            "When a coordinator uploads departmental CSV spreadsheets containing mismatched column naming conventions, our dictionary header-alias mapper reconciles synonymous columns transparently, computes ensemble predictions row-by-row, and refreshes the directory table cleanly inside one atomic transaction."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig6_3_student_directory.png",
                            "caption": "Figure 5.1.4 Student Monitoring Directory & Bulk Ingestion Hub",
                            "width_in": 6.0
                        }
                    },
                    {
                        "id": "5.1.5",
                        "title": "5.1.5 Five-Stage Counselling Lifecycle Hub & Capacity Meters",
                        "paragraphs": [
                            "Figure 5.1.5 presents the dedicated Five-Stage Counselling Lifecycle Hub engineered to transform analytical alerts into structured, auditable human outreach. Live horizontal queue meters across the top panel monitor active utilization against Administrator-configured stage capacities across all five pipeline stages: Stage 1 (Identified Risk), Stage 2 (First Outreach), Stage 3 (Counselling Scheduled), Stage 4 (Follow-Up Active), and Stage 5 (Resolved).",
                            "Each case card displays mentor assignment, cumulative risk probability, normalized XAI root-cause progress bars summing to 100 percent, structured action-plan text fields, and stage advancement selectors. Attempting to move an excess case into a saturated stage alerts the coordinator immediately, protecting faculty mentors from silent burnout."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig6_5_counselling_hub.png",
                            "caption": "Figure 5.1.5 Five-Stage Counselling Lifecycle Hub",
                            "width_in": 6.0
                        }
                    },
                    {
                        "id": "5.1.6",
                        "title": "5.1.6 Administrative Governance, Threshold Tuning & On-Demand Retraining",
                        "paragraphs": [
                            "Figure 5.1.6 illustrates the Administrative Governance Console accessible strictly to university Admins. Through clean numeric forms, policy officers tune Warning and Critical limits for Attendance (default 75 and 60 percent), Internal Marks (default 55 and 40 percent), Active Backlogs (default 1 and 3 arrears), and Counselling Stage Capacity Limits, automatically triggering transactional cohort re-scoring across stored students.",
                            "The lower panel exposes live benchmark comparisons between our 120-tree Random Forest classifier and Logistic Regression baseline alongside an institutional Ground-Truth CSV uploader enabling on-demand ensemble retraining as new graduating cohorts complete their degrees."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig6_6_admin_governance.png",
                            "caption": "Figure 5.1.6 Administrative Governance & Retraining Module",
                            "width_in": 6.0
                        }
                    },
                    {
                        "id": "5.1.7",
                        "title": "5.1.7 Forensic Security Audit Trail & Immutable Event Logging",
                        "paragraphs": [
                            "Figure 5.1.7 exhibits the immutable Forensic Audit Trail module recording critical operational events across authentication logins, single student creations, bulk CSV imports, counselling stage transitions, institutional policy updates, and model retraining runs. Every event captures UTC timestamps, actor identities, role labels, source IP addresses, and contextual descriptions inside append-only database rows.",
                            "This verifiable forensic log equips university academic registrars and external NAAC auditors with transparent institutional accountability while supporting rapid investigation of unauthorized peer-route access attempts."
                        ],
                        "figure": {
                            "path": "static/images/screenshots/fig_audit_logs.png",
                            "caption": "Figure 5.1.7 Forensic Security Audit Trail Module",
                            "width_in": 6.0
                        }
                    }
                ]
            },
            {
                "id": "5.2",
                "title": "5.2 System Performance & Automated Suite Validation",
                "paragraphs": [
                    "System reliability, authorization security, and end-to-end functional accuracy were verified systematically through an automated regression suite (test_app.py) comprising eight integrated unit and workflow test scenarios executed against an isolated test Flask client and relational schema. Every core capability—authenticated login flows, role-based dashboard rendering, single student creation with live inference, multi-variant CSV upload with header aliasing, five-stage mentoring progression, capacity enforcement checks, student self-portal isolation, and admin threshold re-scoring—executed cleanly with zero uncaught exceptions and 8/8 passing assertions.",
                    "Crucially, horizontal privilege escalation verification explicitly tested whether an authenticated Student session attempting to request another peer's profile identifier receives a strict HTTP 403 Forbidden rejection rather than rendered data, confirming fail-closed RBAC privacy compliance."
                ],
                "table": {
                    "caption": "Table 5.1: Automated 8-Test Functional & Security Verification Summary",
                    "headers": ["Test Identifier", "Targeted Functional / Security Scope", "Verification Outcome"],
                    "rows": [
                        ["T1: Auth & Session Dispatch", "PBKDF2 login verification and 4-tier home routing", "PASSED (HTTP 200 / Valid Cookies)"],
                        ["T2: RBAC 403 Peer Guard", "Student blocked from viewing peer student records & Admin pages", "PASSED (Strict HTTP 403 Enforced)"],
                        ["T3: ML Scoring & XAI Cards", "RF prediction [0..1] + normalized reasons summing to 100%", "PASSED (Exact 100% Sum Verified)"],
                        ["T4: Alias CSV Bulk Upload", "Ingesting non-standard headers (Att_Pct, IntMarks, etc.)", "PASSED (Zero Row Loss)"],
                        ["T5: 5-Stage Lifecycle Hub", "Counselling case creation, remark logging & stage transitions", "PASSED (ACID Commit Confirmed)"],
                        ["T6: Capacity Quota Guard", "Enforcing Admin-defined stage maximum queue capacities", "PASSED (Overflow Blocked Cleanly)"],
                        ["T7: Live Policy Re-Score", "Modifying attendance/backlog limits & cascading cohort updates", "PASSED (Dynamic Tier Sync Verified)"],
                        ["T8: Forensic Audit & Export", "Append-only AuditLog IP entries & CSV reporting download", "PASSED (8/8 Full Suite Green)"]
                    ]
                }
            },
            {
                "id": "5.3",
                "title": "5.3 Challenges Faced During Development",
                "paragraphs": [
                    "Several subtle engineering challenges arose and were resolved cleanly during full-stack integration and multi-platform validation. First, early prototypes surfaced non-normalized string reasons where percentages either summed to arbitrary totals (such as 142 percent when multiple rule deficits fired simultaneously) or emitted empty strings for borderline low-risk students. Redesigning analyze_reasons() around multiplicative Gini-importance weighting followed by strict proportional normalization eliminated every rounding discrepancy so every flagged learner's attribution bars sum mathematically to 100 percent.",
                    "Second, cross-platform testing between Windows PowerShell and macOS Terminal uncovered an environment collision on macOS systems where Apple's native AirPlay Receiver service binds TCP port 5000 by default, triggering HTTP 403 blank responses when opening localhost:5000 in Safari or Chrome. Updating our WSGI entry module to respect standard PORT environment variables and documenting clean PORT=5001 startup commands in institutional setup guides resolved macOS deployment friction permanently."
                ]
            },
            {
                "id": "5.4",
                "title": "5.4 Validation of Predictive Results and XAI Feature Profiling",
                "paragraphs": [
                    "Quantitative evaluation of predictive discrimination across held-out validation splits confirms that our 120-tree Random Forest classifier outperforms the regularized Logistic Regression baseline across overall accuracy, precision, F1 balance, and ROC-AUC separation. Importantly, recall remains balanced at 87.50 percent for Random Forest and 87.83 percent for Logistic Regression, ensuring that genuine at-risk students are reliably flagged rather than silently overlooked while maintaining superior 87.50 percent precision that shields busy mentors from unnecessary false-alarm triage."
                ],
                "table": {
                    "caption": "Table 5.2: Verified Held-Out Model Benchmark Comparison",
                    "headers": ["Supervised Model Architecture", "Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"],
                    "rows": [
                        ["Random Forest Classifier (120 Trees, Max Depth 8)", "89.87%", "87.50%", "87.50%", "87.50%", "96.77%"],
                        ["Logistic Regression Baseline (Scaled + OHE)", "88.53%", "84.49%", "87.83%", "86.13%", "96.45%"]
                    ]
                }
            },
            {
                "id": "5.5",
                "title": "5.5 Feature Attribution Sensitivity Evaluation",
                "paragraphs": [
                    "Inspecting global Gini impurity reductions extracted directly from the fitted Random Forest ensemble confirms strong clinical alignment with academic domain intuition. Attendance consistency exerts the largest global influence at 43.79 percent, followed closely by progressive internal marks average at 21.23 percent and active academic backlogs at 15.89 percent. Together, these top three academic telemetry factors explain 80.91 percent of total tree-splitting power, while student engagement score (11.08 percent), fee payment stress (6.18 percent across Paid/Partial/Pending indicators), and current semester (1.84 percent) provide essential secondary refinement across ambiguous borderline students."
                ],
                "table": {
                    "caption": "Table 5.3: Learned Random Forest Gini Feature Importance Distribution",
                    "headers": ["Student Feature Predictor", "Gini Weight", "Share (%)", "Primary Diagnostic Signal Captured"],
                    "rows": [
                        ["Attendance Percentage", "0.4379", "43.79%", "Chronic class absenteeism & examination eligibility jeopardy"],
                        ["Internal Marks Average", "0.2123", "21.23%", "Mid-semester comprehension & laboratory performance trajectory"],
                        ["Active Backlog Count", "0.1589", "15.89%", "Cumulative academic arrear load & progression confidence"],
                        ["Academic Engagement Score", "0.1108", "11.08%", "LMS portal participation, assignment timeliness & interaction"],
                        ["Fee Status (Paid / Partial)", "0.0618", "6.18%", "Tuition affordability stress & installment settlement friction"],
                        ["Academic Semester", "0.0184", "1.84%", "Early transitional shock vs. senior upper-division stability"]
                    ]
                }
            },
            {
                "id": "5.6",
                "title": "5.6 User Feedback and Iterative Refinements",
                "paragraphs": [
                    "Following prototype walkthroughs with academic guides and supervising faculty at Sanskriti University, three high-value usability refinements were incorporated directly into the final release. First, visual progress meters displaying exact active student counts against stage caps were elevated onto the top header of the Five-Stage Counselling Hub so overloaded triage stages stand out immediately in amber or red contrast.",
                    "Second, explicit role-labelled navigation badges and persistent notification counters were integrated into the shared top navigation bar, saving mentors repetitive directory queries during busy sessional examination weeks. Third, full step-by-step setup documentation separating Windows PowerShell commands from macOS Terminal instructions—complete with port-conflict guidance—was packaged cleanly inside repository manuals."
                ]
            },
            {
                "id": "5.7",
                "title": "5.7 Summary of Validation Findings",
                "paragraphs": [
                    "Comprehensive software testing, empirical ML benchmarking, and stakeholder UI validation corroborate three core project achievements: (1) combining a 120-tree Random Forest classifier with policy-calibrated Gini attribution achieves 89.87 percent predictive accuracy and 96.77 percent ROC-AUC while guaranteeing 100-percent interpretable reason cards; (2) engineering dictionary header aliasing alongside a bounded five-stage counselling hub transforms predictive analytics into an immediately actionable departmental mentoring workflow; and (3) fail-closed four-tier RBAC security paired with immutable IP-tagged AuditLog trails safeguards sensitive student records to institutional compliance standards."
                ]
            }
        ]
    }


def get_chapter_6():
    return {
        "number": 6,
        "title": "CHAPTER 6 – CONCLUSION AND FUTURE WORK",
        "sections": [
            {
                "id": "Conclusion",
                "title": "6.1 Conclusion",
                "paragraphs": [
                    "Student attrition in higher education is fundamentally preventable when institutions combine early quantitative pattern detection with transparent, compassionate faculty mentorship. AI-Based Prediction of Reasons for Student Dropout addresses this critical operational challenge through a complete, end-to-end engineering platform engineered specifically around real university workflows. Rather than shipping a disconnected machine learning notebook or an unexplainable black-box alert script, our team delivered an integrated Flask, SQLite, and Scikit-Learn web application spanning cohort ingestion, explainable risk diagnosis, bounded five-stage counselling progression, administrative policy governance, and cryptographic privacy protection.",
                    "Empirical validation establishes both statistical strength and operational readiness. Evaluated across held-out validation splits, our 120-tree Random Forest pipeline attains 89.87 percent accuracy and 96.77 percent ROC-AUC—surpassing the Logistic Regression baseline—while Gini-weighted deficit decomposition translates every elevated risk score into exact normalized cause percentages summing cleanly to 100 percent. Deployed over a clean four-tier RBAC interface tested across all eight automated regression suites, the platform empowers Administrators, HODs, Faculty Mentors, and Students at Sanskriti University to act early, intervene specifically, and document student retention transparently."
                ]
            },
            {
                "id": "Future Scope and Enhancements",
                "title": "6.2 Future Scope and Enhancements",
                "paragraphs": [
                    "Several practical architectural extensions can further amplify institutional impact in subsequent multi-campus releases:",
                    "1. Real-Time ERP, Biometric & LMS Webhook Integration: Connecting REST webhooks directly to campus biometric attendance terminals, fee payment gateways, and Moodle LMS activity streams will automate weekly telemetry synchronization without manual CSV uploads.",
                    "2. Automated Parent & Student SMS / Email Escalation: Integrating institutional SMTP gateways and approved SMS templates will dispatch respectful attendance warnings and scheduled mentor appointment reminders automatically to parents and mentees upon Stage 2 transitions.",
                    "3. Temporal Longitudinal Sequence Modeling: Incorporating multi-semester trajectory features (semester-over-semester delta in GPA and attendance slope) will allow time-aware classifiers to distinguish rapidly recovering learners from chronically deteriorating trajectories.",
                    "4. Multi-Campus PostgreSQL Migration & NAAC Self-Study Export: Switching SQLAlchemy URI strings to pooled PostgreSQL storage and adding one-click PDF Criterion 2 / Criterion 5 remediation dossiers will streamline multi-institution accreditation audits."
                ]
            }
        ]
    }


def get_references():
    return {
        "title": "REFERENCES",
        "groups": [
            {
                "heading": "Academic Research on Student Dropout Prediction & Explainable AI (XAI)",
                "items": [
                    "1. Tinto, V. (1993). Leaving College: Rethinking the Causes and Cures of Student Attrition (2nd ed.). University of Chicago Press.",
                    "2. Bean, J. P. (1980). Dropouts and Turnover: The Synthesis and Test of a Causal Model of Student Attrition. Research in Higher Education, 12(2), 155–187.",
                    "3. Romero, C., & Ventura, S. (2020). Educational Data Mining and Learning Analytics: An Updated Survey. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 10(3), e1355.",
                    "4. Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5–32.",
                    "5. Lundberg, S. M., & Lee, S. I. (2017). A Unified Approach to Interpreting Model Predictions. Advances in Neural Information Processing Systems (NeurIPS), 30.",
                    "6. Realinho, V., Machado, J., Baptista, L., & Martins, M. V. (2022). Predicting Student Dropout and Academic Success. Data, 7(11), 146.",
                    "7. Delen, D. (2010). A Comparative Analysis of Machine Learning Techniques for Student Retention Management. Decision Support Systems, 49(4), 498–506.",
                    "8. Solis, M., Moreira, T., Gonzalez, R., Fernandez, T., & Hernandez, M. (2018). Perspectives to Predict Dropout in University Students with Machine Learning. IEEE International Work Conference on Bioinspired Intelligence (IWOBI).",
                    "9. Alban, M., & Mauricio, D. (2019). Predicting University Dropout through Data Mining: A Systematic Literature Review. Indian Journal of Science and Technology, 12(4), 1–12.",
                    "10. Baranyi, M., Nagy, M., & Molontay, R. (2020). Interpretable Deep Learning for University Dropout Prediction. Proceedings of the 21st Annual Conference on Information Technology Education (SIGITE)."
                ]
            },
            {
                "heading": "Machine Learning, Data Engineering & Scientific Computing Frameworks",
                "items": [
                    "11. Pedregosa, F., Varoquaux, G., Gramfort, A., et al. (2011). Scikit-Learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830. https://scikit-learn.org",
                    "12. McKinney, W. (2010). Data Structures for Statistical Computing in Python (Pandas). Proceedings of the 9th Python in Science Conference. https://pandas.pydata.org",
                    "13. Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array Programming with NumPy. Nature, 585, 357–362. https://numpy.org",
                    "14. Joblib Development Team (2024). Joblib: Running Python Functions as Pipeline Jobs. https://joblib.readthedocs.io",
                    "15. Fawcett, T. (2006). An Introduction to ROC Analysis. Pattern Recognition Letters, 27(8), 861–874."
                ]
            },
            {
                "heading": "Full-Stack Web Engineering, Relational Persistence & Security Standards",
                "items": [
                    "16. Pallets Projects (2024). Flask Web Development Framework Documentation. https://flask.palletsprojects.com",
                    "17. Pallets Projects (2024). Werkzeug WSGI Utility Library & Cryptographic Hashing. https://werkzeug.palletsprojects.com",
                    "18. Bayer, M. (2024). SQLAlchemy: The Database Toolkit for Python. https://www.sqlalchemy.org",
                    "19. SQLite Consortium (2024). SQLite Transactional Relational Database Engine. https://www.sqlite.org",
                    "20. Bootstrap Team (2024). Bootstrap 5 Responsive Frontend Component Library. https://getbootstrap.com",
                    "21. Chart.js Contributors (2024). Open-Source HTML5 Canvas Data Visualization Library. https://www.chartjs.org",
                    "22. OWASP Foundation (2023). Application Security Verification Standard (ASVS) v4.0 & PBKDF2 Guidelines. https://owasp.org"
                ]
            },
            {
                "heading": "Higher Education Regulatory Policy, Quality Assurance & Technical Standards",
                "items": [
                    "23. Ministry of Education, Government of India (2020). National Education Policy (NEP) 2020. https://www.education.gov.in",
                    "24. Ministry of Education, Government of India (2023). All India Survey on Higher Education (AISHE) Final Report. https://aishe.gov.in",
                    "25. National Assessment and Accreditation Council (NAAC) (2023). Institutional Accreditation Manual for Universities (Criteria 2 & 5). https://naac.gov.in",
                    "26. ISO/IEC 25010 (2023). Systems and Software Engineering — Systems and Software Quality Requirements and Evaluation (SQuaRE).",
                    "27. ISO/IEC 29119 (2022). Software and Systems Engineering — Software Testing Standards.",
                    "28. ISO/IEC 27001 (2022). Information Security, Cybersecurity and Privacy Protection — Information Security Management Systems.",
                    "29. ISO/IEC 23053 (2022). Framework for Artificial Intelligence (AI) Systems Using Machine Learning.",
                    "30. UNESCO (2023). Guidance for Generative AI and Predictive Analytics in Education and Research. https://unesdoc.unesco.org"
                ]
            }
        ]
    }
