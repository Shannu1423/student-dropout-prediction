"""
Pages 1 to 15: Cover Page, Certificate, Declaration, Acknowledgement, Abstract,
Table of Contents (vi, vii, viii), Lists of Tables, Figures, Abbreviations, and Chapter 1.
"""
import os
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, Image

def add_front_matter_and_ch1(pages, styles, LOGO_PATH, usable_width, make_table):
    title_style = styles['CoverTitle']
    cover_sub = styles['CoverSub']
    cover_bold = styles['CoverBold']
    h1_chap = styles['ChapterH1']
    h2_sec = styles['SectionH2']
    h3_subsec = styles['SubSectionH3']
    body = styles['ReportBody']
    body_indent = styles['ReportBodyIndent']
    tbl_text = styles['TableText']
    caption_style = styles['Caption']

    def new_page():
        pages.append([])
        return pages[-1]

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    p = new_page()
    p.append(Spacer(1, 8))
    p.append(Paragraph("AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT", title_style))
    p.append(Spacer(1, 6))
    p.append(Paragraph("A Project Report", cover_bold))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Submitted in partial fulfillment of the award of Degree of Bachelor of Technology in Computer Science and Engineering", cover_sub))
    p.append(Spacer(1, 10))
    p.append(Paragraph("Submitted by", cover_bold))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Enrollment No : 2302320151, SHAIK SHAFI", cover_sub))
    p.append(Paragraph("Enrollment No : 2302320119, SHAIK MOHAMMAD ALI", cover_sub))
    p.append(Paragraph("Enrollment No : 2302320118, SHAIK MAHAMAD YASEEN", cover_sub))
    p.append(Paragraph("Enrollment No : 2302320099, DESIREDDY RAMESH", cover_sub))
    p.append(Spacer(1, 14))
    if os.path.exists(LOGO_PATH):
        p.append(Image(LOGO_PATH, width=115, height=90))
    p.append(Spacer(1, 14))
    p.append(Paragraph("Under the supervision of", cover_bold))
    p.append(Spacer(1, 4))
    p.append(Paragraph("Mr. Satyam Dwivedi", cover_bold))
    p.append(Paragraph("Assistant Professor", cover_sub))
    p.append(Spacer(1, 10))
    p.append(Paragraph("School of Engineering and Information Technology (SOEIT)", cover_sub))
    p.append(Paragraph("SANSKRITI UNIVERSITY, MATHURA, U.P.", cover_bold))
    p.append(Paragraph("NOVEMBER, 2026", cover_sub))

    # =========================================================================
    # PAGE 2: CERTIFICATE (ii)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("Department of Computer Science and Engineering – School of Engineering and Information Technology (SOEIT)", cover_sub))
    p.append(Spacer(1, 8))
    p.append(Paragraph("CERTIFICATE", h1_chap))
    p.append(Spacer(1, 8))
    p.append(Paragraph(
        "This certifies that the B.Tech capstone project report titled <b>‘AI-Based Prediction of Reasons for Student Dropout’</b>, authored by <b>SHAIK SHAFI</b> (Enrollment No: <b>2302320151</b>), <b>SHAIK MOHAMMAD ALI</b> (Enrollment No: <b>2302320119</b>), <b>SHAIK MAHAMAD YASEEN</b> (Enrollment No: <b>2302320118</b>), and <b>DESIREDDY RAMESH</b> (Enrollment No: <b>2302320099</b>) toward partial fulfillment of the <b>Bachelor of Technology in Computer Science and Engineering</b> at <b>Sanskriti University, Mathura</b> during session <b>2026–2027</b>, constitutes an authentic record of supervised engineering development.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "All predictive classifiers, localized Gini deficit attribution logic, role-isolated database views, and verification suites presented across this volume were independently engineered and empirically validated under faculty oversight.",
        body_indent
    ))
    p.append(Spacer(1, 40))
    sig_data = [
        [
            Paragraph("________________________________________<br/><b>(Signature of Faculty Guide)</b><br/><b>Mr. Satyam Dwivedi</b><br/>Assistant Professor, SOEIT<br/>Date: ____________________", tbl_text),
            Paragraph("________________________________________<br/><b>(Signature of the Dean, with official seal)</b><br/><b>Dean, SOEIT</b><br/>Sanskriti University<br/>Date: ____________________", tbl_text)
        ]
    ]
    t_sig = Table(sig_data, colWidths=[usable_width*0.5, usable_width*0.5])
    t_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    p.append(t_sig)
    p.append(Spacer(1, 14))
    p.append(Paragraph("<i>Note: Signature, date and seal fields are intentionally left blank. This certificate takes effect only after it has been signed by the Faculty Guide and the Dean.</i>", caption_style))

    # =========================================================================
    # PAGE 3: DECLARATION (iii)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("Department of Computer Science and Engineering – School of Engineering and Information Technology (SOEIT)", cover_sub))
    p.append(Spacer(1, 8))
    p.append(Paragraph("DECLARATION", h1_chap))
    p.append(Spacer(1, 8))
    p.append(Paragraph(
        "We, <b>SHAIK SHAFI</b> (Enrollment No: <b>2302320151</b>), <b>SHAIK MOHAMMAD ALI</b> (Enrollment No: <b>2302320119</b>), <b>SHAIK MAHAMAD YASEEN</b> (Enrollment No: <b>2302320118</b>), and <b>DESIREDDY RAMESH</b> (Enrollment No: <b>2302320099</b>), students of <b>Bachelor of Technology in Computer Science and Engineering</b>, Session <b>2026–2027</b>, Sanskriti University, Mathura, hereby declare that the work presented in this project report entitled <b>“AI-Based Prediction of Reasons for Student Dropout”</b> is the outcome of our own bonafide work, is correct to the best of our knowledge, and has been carried out with due regard to engineering ethics.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "The report contains no material previously published or written by another person, and no material accepted for the award of any other degree or diploma of this or any other institution, except where due acknowledgement has been made in the text and in the list of references.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "We further confirm that the software architecture, classification models, algorithmic feature deficit logic, and user interfaces documented herein were designed, tested, and implemented by our team in consultation with our project supervisor.",
        body_indent
    ))
    p.append(Spacer(1, 25))
    decl_data = [
        [
            Paragraph("____________________________________<br/><b>(Signature of Candidate 1)</b><br/><b>SHAIK SHAFI</b><br/>Enrollment No: 2302320151<br/>Date: ______________", tbl_text),
            Paragraph("____________________________________<br/><b>(Signature of Candidate 2)</b><br/><b>SHAIK MOHAMMAD ALI</b><br/>Enrollment No: 2302320119<br/>Date: ______________", tbl_text)
        ],
        [
            Paragraph("<br/>____________________________________<br/><b>(Signature of Candidate 3)</b><br/><b>SHAIK MAHAMAD YASEEN</b><br/>Enrollment No: 2302320118<br/>Date: ______________", tbl_text),
            Paragraph("<br/>____________________________________<br/><b>(Signature of Candidate 4)</b><br/><b>DESIREDDY RAMESH</b><br/>Enrollment No: 2302320099<br/>Date: ______________", tbl_text)
        ]
    ]
    t_decl = Table(decl_data, colWidths=[usable_width*0.5, usable_width*0.5])
    t_decl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    p.append(t_decl)

    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT (iv)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("ACKNOWLEDGEMENT", h1_chap))
    p.append(Spacer(1, 8))
    p.append(Paragraph(
        "We extend sincere appreciation to the Hon'ble Chancellor, Chief Executive Officer, Vice Chancellor, and Respected Dean of SOEIT at <b>Sanskriti University, Mathura</b> for sustaining an environment committed to applied engineering research. Above all, we convey deep gratitude to our Faculty Supervisor, <b>Mr. Satyam Dwivedi</b>, Assistant Professor, SOEIT, whose continuous technical feedback made this capstone achievable.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "Throughout architectural prototyping, algorithmic tuning, and cohort validation, our supervisor identified subtle edge cases early and steered the implementation toward practical mentor usability. Constructive evaluation reviews pushed our team to pair raw predictions with transparent Explainable AI cards and queue safeguards.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "We remain indebted to our families and classmates for steady encouragement across late debugging sprints and data preparation cycles, alongside the maintainers of Python, Flask, Scikit-learn, and SQLite.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "Each contributing student verifies that this technical report reflects original engineering effort created strictly for this undergraduate evaluation.",
        body_indent
    ))
    p.append(Spacer(1, 20))
    ack_data = [
        [
            Paragraph("<b>SHAIK SHAFI</b><br/>Enrollment No: 2302320151<br/>B.Tech CSE, SOEIT<br/>Sanskriti University, Mathura", tbl_text),
            Paragraph("<b>SHAIK MOHAMMAD ALI</b><br/>Enrollment No: 2302320119<br/>B.Tech CSE, SOEIT<br/>Sanskriti University, Mathura", tbl_text)
        ],
        [
            Paragraph("<br/><b>SHAIK MAHAMAD YASEEN</b><br/>Enrollment No: 2302320118<br/>B.Tech CSE, SOEIT<br/>Sanskriti University, Mathura", tbl_text),
            Paragraph("<br/><b>DESIREDDY RAMESH</b><br/>Enrollment No: 2302320099<br/>B.Tech CSE, SOEIT<br/>Sanskriti University, Mathura", tbl_text)
        ]
    ]
    t_ack = Table(ack_data, colWidths=[usable_width*0.5, usable_width*0.5])
    t_ack.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
    p.append(t_ack)

    # =========================================================================
    # PAGE 5: ABSTRACT (v)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("ABSTRACT", h1_chap))
    p.append(Spacer(1, 8))
    p.append(Paragraph(
        "Undergraduate departure across technical degree programs rarely strikes abruptly; rather, disengagement accumulates steadily across missed lectures, unresolved subject arrears, eroding quiz averages, and delayed tuition payments. Because departmental registers compile such records only after semester examinations conclude, faculty remediation routinely arrives too late. This capstone presents a full-stack <b>AI-Based Prediction of Reasons for Student Dropout</b> platform engineered to diagnose early attrition signals and guide timely intervention workflows.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "Analytical scoring couples a 120-tree Random Forest classifier with a Logistic Regression reference pipeline over normalized feature vectors covering classroom attendance, internal assessment marks, active backlogs, LMS engagement score, fee payment standing, and enrolled semester. Rather than surfacing an opaque numeric score, a localized Explainable AI (XAI) deficit-attribution routine weights threshold shortfalls by empirical Gini importances to render transparent diagnostic cards and targeted remedial actions.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "Implemented using Python Flask alongside SQLite and SQLAlchemy ORM, the application protects learner confidentiality via a 4-tier Role-Based Access Control (RBAC) architecture spanning Administrators, Department Guides/HODs, Faculty Mentors, and Students. Operational workflows unify bulk CSV header alias mapping, live threshold re-scoring, immutable security audit trails, and a capacity-protected 5-stage retention lifecycle hub.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "Cross-validated testing confirms <b>89.87%</b> accuracy, <b>87.50%</b> precision, <b>87.50%</b> recall, <b>87.50%</b> F1-score, and <b>96.77%</b> ROC-AUC across our SOEIT validation cohort (115 student profiles), providing Sanskriti University advisors an offline-capable decision support instrument.",
        body_indent
    ))

    # =========================================================================
    # PAGE 6: TABLE OF CONTENTS (vi)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("TABLE OF CONTENTS", h1_chap))
    p.append(Spacer(1, 4))
    toc_p1 = [
        ("CERTIFICATE", "ii"),
        ("DECLARATION", "iii"),
        ("ACKNOWLEDGEMENT", "iv"),
        ("ABSTRACT", "v"),
        ("TABLE OF CONTENTS", "vi"),
        ("LIST OF TABLES", "ix"),
        ("LIST OF FIGURES", "x"),
        ("LIST OF ABBREVIATIONS", "xi"),
        ("CHAPTER 1: INTRODUCTION", "1"),
        ("   1.1 Introduction to Educational Data Mining & Dropout Prediction", "1"),
        ("   1.2 Background of the Project", "1"),
        ("   1.3 Introduction to the Dropout Prediction System", "2"),
        ("   1.4 Problem Statement", "3"),
        ("   1.5 Aim of the Project", "3"),
        ("   1.6 Objectives", "3"),
        ("   1.7 Scope of the Project", "3"),
        ("   1.8 Motivation and Rationale", "4"),
        ("   1.9 Organization of the Report", "4"),
        ("CHAPTER 2: LITERATURE REVIEW", "5"),
        ("   2.1 Introduction", "5"),
        ("   2.2 Evolution of Student Retention Systems", "5"),
        ("   2.3 Review of Machine Learning Algorithms in Higher Education", "6"),
        ("   2.4 Review of Existing Technologies", "6"),
        ("   2.5 Explainable AI (XAI) in Educational Analytics", "8"),
        ("   2.6 Comparative Analysis of Existing Systems", "9"),
        ("   2.7 Research Gap and Identified Problems", "9"),
        ("   2.8 Summary", "9"),
        ("CHAPTER 3: SYSTEM ANALYSIS AND REQUIREMENTS", "10"),
        ("   3.1 Existing System", "10"),
        ("   3.2 Limitations of the Existing System", "10"),
        ("   3.3 Proposed System", "10"),
        ("   3.4 Advantages of the Proposed System", "11"),
        ("   3.5 Functional Requirements", "11"),
        ("   3.6 Non-Functional Requirements", "12"),
        ("   3.7 Software Requirements", "12"),
        ("   3.8 Hardware Requirements", "13"),
        ("   3.9 Feasibility Study", "13"),
        ("   3.10 Use Case Analysis", "14"),
        ("CHAPTER 4: SYSTEM DESIGN AND METHODOLOGY", "15"),
        ("   4.1 System Architecture", "15")
    ]
    t_toc1 = Table([[Paragraph(f"<b>{item[0]}</b>" if item[0].startswith("CHAPTER") or not item[0].startswith(" ") else item[0], tbl_text), Paragraph(item[1], tbl_text)] for item in toc_p1], colWidths=[usable_width*0.88, usable_width*0.12])
    t_toc1.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#EDF2F7')), ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5), ('ALIGN', (1,0), (1,-1), 'RIGHT')]))
    p.append(t_toc1)

    # =========================================================================
    # PAGE 7: TABLE OF CONTENTS (vii)
    # =========================================================================
    p = new_page()
    toc_p2 = [
        ("   4.2 Overall System Architecture Diagram", "15"),
        ("   4.3 Machine Learning Pipeline Architecture", "16"),
        ("   4.4 Backend Web Architecture", "17"),
        ("   4.5 Database Architecture", "18"),
        ("   4.6 Data Flow Diagram – Level 0", "18"),
        ("   4.7 Data Flow Diagram – Level 1", "19"),
        ("   4.8 Use Case Diagram", "20"),
        ("   4.9 Activity Diagram", "21"),
        ("   4.10 Sequence Diagram", "22"),
        ("   4.11 Entity Relationship (ER) Diagram", "22"),
        ("   4.12 Database Design & Schema", "23"),
        ("   4.13 Database Schema & Data Dictionary", "24"),
        ("   4.14 API Design and Route Architecture", "25"),
        ("   4.15 Authentication, Role-Based Access Control and Security Design", "26"),
        ("   4.16 UI/UX Design", "27"),
        ("   4.17 Development Methodology", "27"),
        ("   4.18 Project Workflow", "28"),
        ("CHAPTER 5: SYSTEM IMPLEMENTATION", "29"),
        ("   5.1 Introduction", "29"),
        ("   5.2 Development Environment", "29"),
        ("   5.3 Machine Learning Model Implementation", "29"),
        ("   5.4 Explainable AI (XAI) Attribution Engine Implementation", "30"),
        ("   5.5 Backend Web Implementation (Flask & SQLAlchemy)", "30"),
        ("   5.6 Database Implementation & Model Serialization", "31"),
        ("   5.7 Authentication and Session Management", "31"),
        ("   5.8 Student Profile & Risk Recalculation Engine", "32"),
        ("   5.9 Bulk CSV Ingestion & Header Normalization", "32"),
        ("   5.10 Counselling Lifecycle Hub & Queue Workload Implementation", "33"),
        ("   5.11 Escalation Engine & In-Portal Notifications", "33"),
        ("   5.12 Admin Policy Settings & Dynamic Threshold Implementation", "34"),
        ("   5.13 On-Demand Model Retraining Implementation", "34"),
        ("   5.14 Audit Logging & Security Subsystem", "34"),
        ("   5.15 Analytics Visualizations (Chart.js Integration)", "35"),
        ("   5.16 Frontend-Backend Integration", "35"),
        ("   5.17 GitHub Version Control & Offline Local Deployment", "35"),
        ("CHAPTER 6: TESTING AND RESULTS", "36"),
        ("   6.1 Introduction to Testing", "36"),
        ("   6.2 Testing Methodology", "36"),
        ("   6.3 Unit Testing", "37"),
        ("   6.4 Integration Testing", "37"),
        ("   6.5 Functional Testing", "37"),
        ("   6.6 User Interface Testing", "38"),
        ("   6.7 API and Route Testing", "38"),
        ("   6.8 System and Security Testing", "38"),
        ("   6.9 Test Cases and Recorded Results", "39"),
        ("   6.10 Application Screenshots", "42")
    ]
    t_toc2 = Table([[Paragraph(f"<b>{item[0]}</b>" if item[0].startswith("CHAPTER") or not item[0].startswith(" ") else item[0], tbl_text), Paragraph(item[1], tbl_text)] for item in toc_p2], colWidths=[usable_width*0.88, usable_width*0.12])
    t_toc2.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#EDF2F7')), ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5), ('ALIGN', (1,0), (1,-1), 'RIGHT')]))
    p.append(t_toc2)

    # =========================================================================
    # PAGE 8: TABLE OF CONTENTS (viii)
    # =========================================================================
    p = new_page()
    toc_p3 = [
        ("   6.11 Empirical ML Performance and Results", "48"),
        ("   6.12 Performance and Usability Discussion", "48"),
        ("CHAPTER 7: PROJECT MANAGEMENT AND WORK ALLOCATION", "49"),
        ("   7.1 Project Timeline", "49"),
        ("   7.2 Project Planning", "49"),
        ("   7.3 Project Start Date", "50"),
        ("   7.4 Mid-Term Checkpoint", "50"),
        ("   7.5 Work Allocation and Responsibilities", "50"),
        ("   7.6 Individual Contributions", "51"),
        ("   7.7 Team Coordination and Version Control", "51"),
        ("   7.8 Challenges Faced", "52"),
        ("   7.9 Solutions Implemented", "52"),
        ("CHAPTER 8: LEARNING OUTCOMES AND DISCUSSION", "53"),
        ("   8.1 Technical Skills Acquired", "53"),
        ("   8.2 Machine Learning & Data Mining Learning", "53"),
        ("   8.3 Backend Web Development Learning", "53"),
        ("   8.4 Database Management & ORM Learning", "54"),
        ("   8.5 UI/UX & Data Visualization Learning", "54"),
        ("   8.6 Security, RBAC & Privacy Engineering Learning", "54"),
        ("   8.7 Problem-Solving Skills", "54"),
        ("   8.8 Industry-Relevant Competencies", "55"),
        ("   8.9 Ethical Considerations in Predictive Education", "55"),
        ("   8.10 Discussion", "55"),
        ("CHAPTER 9: LIMITATIONS AND FUTURE ENHANCEMENTS", "56"),
        ("   9.1 Current System Limitations", "56"),
        ("   9.2 Future Scope and Proposed Enhancements", "57"),
        ("CHAPTER 10: CONCLUSION", "58"),
        ("   10.1 Project Summary", "58"),
        ("   10.2 Achievement of Project Objectives", "58"),
        ("   10.3 Final Conclusion", "59"),
        ("REFERENCES", "60"),
        ("APPENDIX", "62"),
        ("   A.1 Project Links", "62"),
        ("   A.2 Repository Structure", "62"),
        ("   A.3 Important API Endpoints", "63"),
        ("   A.4 Selected Code Snippets", "63"),
        ("   A.5 Test Execution Verification Log", "65"),
        ("   A.6 Team Details", "65"),
        ("   A.7 Environment Variables", "66"),
        ("   A.8 Running the Project Locally", "66")
    ]
    t_toc3 = Table([[Paragraph(f"<b>{item[0]}</b>" if item[0].startswith("CHAPTER") or not item[0].startswith(" ") else item[0], tbl_text), Paragraph(item[1], tbl_text)] for item in toc_p3], colWidths=[usable_width*0.88, usable_width*0.12])
    t_toc3.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#EDF2F7')), ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5), ('ALIGN', (1,0), (1,-1), 'RIGHT')]))
    p.append(t_toc3)

    # =========================================================================
    # PAGE 9: LIST OF TABLES (ix)
    # =========================================================================
    p = new_page()
    p.append(Paragraph("LIST OF TABLES", h1_chap))
    p.append(Spacer(1, 4))
    tables_list = [
        ("Table 1.1", "Project summary and technical specifications", "2"),
        ("Table 2.1", "Technology stack selection and evaluation rationale", "7"),
        ("Table 2.2", "Comparative analysis with existing educational retention tools", "9"),
        ("Table 3.1", "Functional requirements specification matrix", "11"),
        ("Table 3.2", "Non-functional requirements specification matrix", "12"),
        ("Table 3.3", "Software requirements and version environment", "12"),
        ("Table 3.4", "Hardware specifications for host and client devices", "13"),
        ("Table 3.5", "Use case actor-goal interaction summary", "14"),
        ("Table 4.1", "Architectural tiers and decoupled system responsibilities", "15"),
        ("Table 4.2", "Client-side and administrative web routing architecture", "17"),
        ("Table 4.3", "Machine learning feature representation and baseline thresholds", "18"),
        ("Table 4.4", "Role-Based Access Control (RBAC) permission entitlement matrix", "20"),
        ("Table 4.5", "Database Schema – users table definition", "24"),
        ("Table 4.6", "Database Schema – students table definition", "24"),
        ("Table 4.7", "Database Schema – counselling_cases table definition", "25"),
        ("Table 4.8", "Database Schema – audit_logs table definition", "25"),
        ("Table 4.9", "REST API architecture and protected route endpoints", "26"),
        ("Table 4.10", "Security controls and role privacy boundaries", "27"),
        ("Table 6.1", "Unit testing candidate functions and coverage scope", "37"),
        ("Table 6.2", "API endpoint integration test matrix", "38"),
        ("Table 6.3", "Test cases – Authentication and role authorization", "39"),
        ("Table 6.4", "Test cases – Machine learning inference & XAI reason cards", "40"),
        ("Table 6.5", "Test cases – Bulk CSV ingestion & recalculation engine", "40"),
        ("Table 6.6", "Test cases – Counselling lifecycle hub & case transitions", "41"),
        ("Table 6.7", "Test cases – Admin retraining & queue capacity meters", "41"),
        ("Table 6.8", "Empirical machine learning evaluation metrics", "48"),
        ("Table 7.1", "Project timeline, sprint phases and deliverables", "49"),
        ("Table 7.2", "Module work distribution across subsystems", "50"),
        ("Table 7.3", "Individual candidate contribution matrix", "51"),
        ("Table 7.4", "Technical challenges encountered and solutions implemented", "52"),
        ("Table 9.1", "Current system limitations and interim operational workarounds", "56"),
        ("Table 9.2", "Proposed enhancements and future technical roadmap", "57"),
        ("Table 10.1", "Achievement matrix against initial project objectives", "58"),
        ("Table A.1", "Project repository and environment links", "62"),
        ("Table A.2", "Candidate and supervision academic details", "65"),
        ("Table A.3", "System environment variables and runtime configurations", "66")
    ]
    t_tbls = Table([[Paragraph(f"<b>{row[0]}</b>", tbl_text), Paragraph(row[1], tbl_text), Paragraph(row[2], tbl_text)] for row in tables_list], colWidths=[usable_width*0.16, usable_width*0.74, usable_width*0.10])
    t_tbls.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#EDF2F7')), ('TOPPADDING', (0,0), (-1,-1), 1.5), ('BOTTOMPADDING', (0,0), (-1,-1), 1.5), ('ALIGN', (2,0), (2,-1), 'RIGHT')]))
    p.append(t_tbls)

    # =========================================================================
    # PAGE 10: LIST OF FIGURES (x)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("LIST OF FIGURES", h1_chap))
    p.append(Spacer(1, 4))
    figures_list = [
        ("Figure 4.1", "Overall 3-tier system architecture diagram", "16"),
        ("Figure 4.2", "Data Flow Diagram – Level 0 (Context Level)", "19"),
        ("Figure 4.3", "Data Flow Diagram – Level 1 (Subsystem Decomposition)", "20"),
        ("Figure 4.4", "Use Case Diagram for administrative, mentor and student roles", "20"),
        ("Figure 4.5", "Activity Diagram – Risk evaluation and remedial intervention lifecycle", "21"),
        ("Figure 4.6", "Sequence Diagram – Risk prediction and case progression workflow", "22"),
        ("Figure 4.7", "Entity Relationship (ER) Diagram of the relational persistence model", "23"),
        ("Figure 4.8", "Project execution and agile development lifecycle flowchart", "28"),
        ("Figure 6.1", "Application Interface – Unified user authentication and role routing", "42"),
        ("Figure 6.2", "Application Interface – Administrative / HOD executive overview dashboard", "43"),
        ("Figure 6.3", "Application Interface – Cohort risk registry with color-coded severity badges", "44"),
        ("Figure 6.4", "Application Interface – Student deep-dive profile with XAI deficit reason cards", "45"),
        ("Figure 6.5", "Application Interface – 5-stage counselling hub with queue capacity workload meters", "46"),
        ("Figure 6.6", "Application Interface – Dynamic policy controls, risk thresholds and retraining", "47"),
        ("Figure A.1", "Additional Interface – Audit logging subsystem and security trace history", "65")
    ]
    t_figs = Table([[Paragraph(f"<b>{row[0]}</b>", tbl_text), Paragraph(row[1], tbl_text), Paragraph(row[2], tbl_text)] for row in figures_list], colWidths=[usable_width*0.16, usable_width*0.74, usable_width*0.10])
    t_figs.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#EDF2F7')), ('TOPPADDING', (0,0), (-1,-1), 3), ('BOTTOMPADDING', (0,0), (-1,-1), 3), ('ALIGN', (2,0), (2,-1), 'RIGHT')]))
    p.append(t_figs)

    # =========================================================================
    # PAGE 11: LIST OF ABBREVIATIONS (xi)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("LIST OF ABBREVIATIONS", h1_chap))
    p.append(Spacer(1, 4))
    abbrevs = [
        ("AI", "Artificial Intelligence"),
        ("ML", "Machine Learning"),
        ("XAI", "Explainable Artificial Intelligence"),
        ("EDM", "Educational Data Mining"),
        ("LA", "Learning Analytics"),
        ("AUC-ROC", "Area Under the Receiver Operating Characteristic Curve"),
        ("RF", "Random Forest Classifier"),
        ("LR", "Logistic Regression"),
        ("CGPA", "Cumulative Grade Point Average"),
        ("LMS", "Learning Management System"),
        ("SOEIT", "School of Engineering and Information Technology"),
        ("RBAC", "Role-Based Access Control"),
        ("ORM", "Object-Relational Mapping (SQLAlchemy)"),
        ("REST", "Representational State Transfer"),
        ("API", "Application Programming Interface"),
        ("DFD", "Data Flow Diagram"),
        ("ERD", "Entity Relationship Diagram"),
        ("CSRF", "Cross-Site Request Forgery"),
        ("CSV", "Comma-Separated Values"),
        ("UI/UX", "User Interface / User Experience")
    ]
    t_abbr = Table([[Paragraph(f"<b>{row[0]}</b>", tbl_text), Paragraph(row[1], tbl_text)] for row in abbrevs], colWidths=[usable_width*0.25, usable_width*0.75])
    t_abbr.setStyle(TableStyle([('LINEBELOW', (0,0), (-1,-1), 0.3, colors.HexColor('#EDF2F7')), ('TOPPADDING', (0,0), (-1,-1), 2), ('BOTTOMPADDING', (0,0), (-1,-1), 2)]))
    p.append(t_abbr)

    # =========================================================================
    # PAGE 12: CHAPTER 1 (Numbered Page 1)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("CHAPTER 1", h1_chap))
    p.append(Paragraph("INTRODUCTION", h1_chap))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.1 Introduction to Educational Data Mining & Dropout Prediction", h2_sec))
    p.append(Paragraph(
        "Analytical modeling across institutional student records—commonly termed Educational Data Mining (EDM) and Learning Analytics (LA)—transforms fragmented academic ledgers into actionable predictive signals. Preserving semester-to-semester student progression safeguards learner career outcomes, elevates graduation benchmarks, and stabilizes institutional resource allocation across university departments.",
        body_indent
    ))
    p.append(Paragraph(
        "Traditional departmental oversight depends heavily on isolated attendance sheets and delayed semester-end grade tabulations. That calendar lag leaves faculty advisors reactive: once formal debarment lists circulate after final examinations begin, meaningful academic recovery is rarely achievable. Automated mid-semester risk synthesis spots multi-factor warning cues six to eight weeks earlier, restoring practical intervention windows.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.2 Background of the Project", h2_sec))
    p.append(Paragraph(
        "Rigorous undergraduate engineering syllabi test learners across sustained theoretical lectures, weekly lab evaluations, and continuous internal credits. Inside the School of Engineering and Information Technology (SOEIT) at Sanskriti University, learners navigate varied academic preparation levels, commuting constraints, and fee schedules. Cohort audits demonstrate that departures build cumulatively through missed lectures, rising active arrears, LMS inactivity, and delayed fee installments.",
        body_indent
    ))
    p.append(Paragraph(
        "Commissioned as an applied B.Tech engineering capstone, this work delivers an offline-capable predictive web portal uniting calibrated Scikit-learn classifiers with normalized feature-deficit reason breakdowns formatted cleanly for daily faculty mentorship.",
        body_indent
    ))

    # =========================================================================
    # PAGE 13: CHAPTER 1 cont. (Numbered Page 2)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("1.3 Introduction to the Dropout Prediction System", h2_sec))
    p.append(Paragraph(
        "Designed as a modular three-tier Flask web suite, the AI-Based Prediction of Reasons for Student Dropout platform binds statistical inference directly into structured mentor workflow queues. Instead of issuing unexplained probability scores, its local Explainable AI (XAI) routine checks classroom presence (<75% threshold), continuous marks (<55% passing target), active arrears, and tuition standing against Gini weights to generate prescriptive remediation actions.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    t11_headers = ["Project Specification Item", "Implementation Detail & Environment Parameters"]
    t11_rows = [
        ["Project Title", "AI-Based Prediction of Reasons for Student Dropout"],
        ["Candidate Team", "SHAIK SHAFI (2302320151), SHAIK MOHAMMAD ALI (2302320119), SHAIK MAHAMAD YASEEN (2302320118), DESIREDDY RAMESH (2302320099)"],
        ["Faculty Guide", "Mr. Satyam Dwivedi, Assistant Professor, SOEIT, Sanskriti University"],
        ["Academic Year", "2026–2027 (Evaluation: November 2026)"],
        ["Repository (GitHub)", "https://github.com/Shannu1423/student-dropout-prediction.git"],
        ["System Architecture", "Decoupled 3-Tier Web System (Flask, SQLite/SQLAlchemy, Bootstrap 5)"],
        ["Machine Learning Stack", "scikit-learn 1.3+, pandas 2.0+, numpy 1.24+, joblib 1.3+"],
        ["Classification Engines", "120-Tree Random Forest Classifier & Logistic Regression Baseline"],
        ["Active Cohort Test Size", "115 Sanskriti University student profiles (47 At Risk, 68 Low Risk)"]
    ]
    p.append(make_table(t11_headers, t11_rows, [usable_width*0.38, usable_width*0.62]))
    p.append(Paragraph("Table 1.1 Project summary and technical specifications", caption_style))
    p.append(Paragraph(
        "Server-side Role-Based Access Control isolates four distinct operational views—Administrator, Guide/HOD, Faculty Mentor, and Student—ensuring student users see exclusively personal progression diagnostics with strict peer privacy protection.",
        body_indent
    ))

    # =========================================================================
    # PAGE 14: CHAPTER 1 cont. (Numbered Page 3)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("1.4 Problem Statement", h2_sec))
    p.append(Paragraph(
        "University advising workflows suffer when attendance books, internal quiz tallies, and accounts ledgers operate as disconnected silos. Standard campus ERP portals record past transactions rather than flagging emerging disengagement mid-term. Even where raw grades exist, overloaded faculty advisors lack automated root-cause explanations and capacity-governed tracking queues needed for systematic early outreach.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.5 Aim of the Project", h2_sec))
    p.append(Paragraph(
        "We aim to architect, build, and validate an offline-ready full-stack software platform that synthesizes multi-source student indicators, scores attrition risk using calibrated tree ensembles, attributes weighted deficit causes through Explainable AI, and enforces structured counsellor stage progression.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.6 Objectives", h2_sec))
    p.append(Paragraph("Our implementation fulfills seven verifiable engineering goals:", body))
    p.append(Paragraph("1. Construct clean institutional training and cohort fixtures capturing academic, LMS engagement, and fee payment standing across SOEIT engineering departments.", body))
    p.append(Paragraph("2. Train and benchmark Random Forest and Logistic Regression Scikit-learn pipelines targeting robust generalization (~90% accuracy and >0.96 ROC-AUC).", body))
    p.append(Paragraph("3. Formulate a normalized Gini feature-deficit attribution engine producing readable diagnostic cards and remedial suggestions.", body))
    p.append(Paragraph("4. Build a 4-tier RBAC Flask security layer isolating student self-views via PBKDF2 hashing and HTTP 403 peer guards.", body))
    p.append(Paragraph("5. Deploy a 5-stage retention lifecycle hub featuring live mentor queue workload meters and stage saturation warnings.", body))
    p.append(Paragraph("6. Enable administrator threshold sliders, bulk CSV alias ingestion, and live model retraining directly from the GUI.", body))
    p.append(Paragraph("7. Verify authentication, XAI determinism, privacy guards, and retraining routines via automated unittest test cases.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.7 Scope of the Project", h2_sec))
    p.append(Paragraph(
        "This release spans individual registration, fault-tolerant CSV batch uploads, ensemble scoring, explainable deficit cards, 5-stage queue management, portal notifications, and audit logging. External hardware biometric scanners and paid SMS/WhatsApp gateways remain reserved for subsequent institutional rollout phases.",
        body_indent
    ))

    # =========================================================================
    # PAGE 15: CHAPTER 1 cont. (Numbered Page 4)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("1.8 Motivation and Rationale", h2_sec))
    p.append(Paragraph(
        "Unchecked academic withdrawal inflicts lasting educational and financial setbacks on undergraduates while reducing cohort completion benchmarks across university departments. Shifting institutional oversight from end-semester failure compilation toward compassionate mid-term remediation turns archived student telemetry into measurable human support.",
        body_indent
    ))
    p.append(Paragraph(
        "From an engineering standpoint, building this system unifies supervised ensemble learning, interpretable mathematical feature attribution, relational database design, REST API controllers, cryptographic access governance, and responsive dashboard engineering inside one cohesive software product.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.9 Organization of the Report", h2_sec))
    p.append(Paragraph("Remaining chapters progress through the full engineering lifecycle:", body))
    p.append(Paragraph("• <b>Chapter 2: Literature Review</b> critiques prior EDM models, Indian statutory retention constraints, XAI methods, and commercial ERP gaps.", body))
    p.append(Paragraph("• <b>Chapter 3: System Analysis and Requirements</b> compares baseline manual workflows against functional, hardware, security, and feasibility criteria.", body))
    p.append(Paragraph("• <b>Chapter 4: System Design and Methodology</b> specifies the 3-tier layout, ML transformations, 3NF SQLite tables, DFDs, UML flows, and REST routes.", body))
    p.append(Paragraph("• <b>Chapter 5: System Implementation</b> walks through `ml_engine.py`, XAI deficit formulas, RBAC decorators, CSV header mapping, and queue logic.", body))
    p.append(Paragraph("• <b>Chapter 6: Testing and Results</b> presents test fixture execution results, verified screenshots, and comparative RF metrics (89.87% accuracy, 0.968 AUC).", body))
    p.append(Paragraph("• <b>Chapter 7: Project Management</b> details agile schedules, cross-team contributions across all four members, and resolved engineering challenges.", body))
    p.append(Paragraph("• <b>Chapter 8: Learning Outcomes</b> reflects on applied ML tradeoffs, SQLAlchemy transactions, cryptographic safety, and ethical AI safeguards.", body))
    p.append(Paragraph("• <b>Chapter 9 & 10: Limitations, Future Scope & Conclusion</b> records current operational boundaries, planned integrations, and objective fulfillment.", body))

    print(f"Front matter + Ch1 complete: {len(pages)} pages.")
