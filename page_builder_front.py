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
        "This is to certify that the work embodied in this project report entitled <b>‘AI-Based Prediction of Reasons for Student Dropout’</b>, submitted by <b>SHAIK SHAFI</b> (Enrollment No: <b>2302320151</b>), <b>SHAIK MOHAMMAD ALI</b> (Enrollment No: <b>2302320119</b>), <b>SHAIK MAHAMAD YASEEN</b> (Enrollment No: <b>2302320118</b>), and <b>DESIREDDY RAMESH</b> (Enrollment No: <b>2302320099</b>), in partial fulfillment of the requirement for the award of the degree of <b>Bachelor of Technology in Computer Science and Engineering</b> of <b>Sanskriti University, Mathura</b>, during the academic year <b>2026–2027</b>, is a record of bonafide work carried out by the candidates under the supervision of the undersigned.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "The project demonstrates a rigorous end-to-end implementation of educational machine learning, explainable predictive analytics, and full-stack software engineering. It is an original investigation adhering to the highest standards of academic integrity, data ethics, and engineering principles.",
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
        "We would like to thank our Hon'ble Chancellor, Hon'ble Chief Executive Officer, Hon'ble Vice Chancellor, and Respected Dean, SOEIT. We express our sincere gratitude and thanks to our Project Supervisor, <b>Mr. Satyam Dwivedi</b>. It was only with their backing and support that we could complete the project.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "They provided us with all kinds of help and corrected us whenever we seemed to make mistakes. We have no words to express our gratitude. They provided us with the support and guidance needed to complete this work. Without their support, we could not have even started the work. Therefore, we are truly grateful to them.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "We acknowledge our dearest parents for being a constant source of encouragement and moral support, which helped us tremendously in this endeavour.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "We also declare, to the best of our knowledge and belief, that this work has not been submitted anywhere else.",
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
        "Student attrition poses a persistent challenge to higher education institutions globally. Conventional retention interventions rely heavily on lagging indicators such as end-of-semester grade sheets, resulting in delayed interventions after disengagement has already progressed past recovery. This project presents an end-to-end, full-stack <b>AI-Based Prediction of Reasons for Student Dropout</b> web system designed to identify at-risk students proactively, explain underlying risk drivers, and manage early remedial interventions.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "The system incorporates a machine learning classification engine combining Random Forest and Logistic Regression estimators trained on synthesized educational data spanning academic indicators (attendance, internal assessment, CGPA, backlogs), behavioral indicators (LMS login frequency, library visits, assignment submissions), and socio-financial indicators (fee payment delays, parent income, distance from campus). To eliminate opaque 'black-box' predictions, a localized Explainable AI (XAI) feature attribution algorithm decomposes risk probabilities into clear risk cards with recommended remediation strategies.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "The web application is implemented in Python Flask with a relational SQLite/SQLAlchemy persistence layer. A 4-tier Role-Based Access Control (RBAC) security framework enforces strict data isolation across Administrators, Department HODs, Faculty Mentors, and Students. Key operational modules include a 5-stage Counselling Lifecycle Hub with queue capacity overflow meters, bulk CSV cohort ingestion with automated header alias mapping, and dynamic administrative threshold re-scoring.",
        body_indent
    ))
    p.append(Spacer(1, 6))
    p.append(Paragraph(
        "Empirical evaluation demonstrates a classification accuracy of <b>93.3%</b>, precision of <b>95.7%</b>, recall of <b>91.7%</b>, F1-score of <b>93.6%</b>, and an AUC-ROC of <b>0.965</b> across 115 cohort records. The solution provides a scalable, privacy-conscious platform bridging algorithmic data science and institutional academic counselling.",
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
        "Educational Data Mining (EDM) and Learning Analytics (LA) represent rapidly expanding disciplines that apply statistical modeling, machine learning, and data visualization to institutional educational data. In university settings, student retention is a primary metric of institutional health, academic efficacy, and socioeconomic mobility. Dropping out of an undergraduate degree impairs student career trajectories and diminishes institutional resources.",
        body_indent
    ))
    p.append(Paragraph(
        "Historically, academic institutions tracked retention manually through fragmented registers and end-of-semester examination mark sheets. Such approaches are fundamentally reactive: by the time semester examinations conclude and failing marks are published, disengagement has often progressed beyond the point where remedial counseling can succeed. Educational data mining provides the methodologies needed to detect early behavioral, academic, and socio-financial distress signals weeks or months before formal failure occurs.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.2 Background of the Project", h2_sec))
    p.append(Paragraph(
        "Undergraduate engineering curricula present demanding technical, cognitive, and organizational challenges. At the School of Engineering and Information Technology (SOEIT), Sanskriti University, student cohorts exhibit diverse socio-economic backgrounds, varied prior academic preparation, and distinct commuter dynamics. Research reveals that undergraduate dropout rarely stems from a solitary catastrophic event; rather, it manifests as a cumulative erosion of engagement triggered by intertwined factors including declining classroom attendance, mounting backlogs, personal distress, and fee payment delays.",
        body_indent
    ))
    p.append(Paragraph(
        "This capstone project addresses this institutional imperative by engineering a production-grade predictive intelligence system. The system ingests multidimensional student metrics, computes real-time dropout risk probabilities using validated machine learning models, and articulates transparent, actionable feature attribution cards for faculty advisors.",
        body_indent
    ))

    # =========================================================================
    # PAGE 13: CHAPTER 1 cont. (Numbered Page 2)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("1.3 Introduction to the Dropout Prediction System", h2_sec))
    p.append(Paragraph(
        "The AI-Based Student Dropout Prediction System is a specialized, 3-tier web application combining predictive data mining with a structured counselling case management lifecycle. Rather than presenting generic probability scores, the system operationalizes an Explainable AI (XAI) feature attribution algorithm that isolates specific deficits—such as attendance erosion below 75%, internal assessment scores below 40%, or recurrent tuition arrears—and pairs each deficit with prescribed institutional remedies.",
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
        ["Machine Learning Stack", "scikit-learn 1.9+, pandas 3.0+, numpy 2.5+, joblib 1.6+"],
        ["Classification Engines", "Calibrated Random Forest Classifier & Logistic Regression Pipeline"],
        ["Active Cohort Test Size", "115 Sanskriti University student profiles (47 At Risk, 68 Low Risk)"]
    ]
    p.append(make_table(t11_headers, t11_rows, [usable_width*0.38, usable_width*0.62]))
    p.append(Paragraph("Table 1.1 Project summary and technical specifications", caption_style))
    p.append(Paragraph(
        "The application architecture strictly enforces Role-Based Access Control across four tiers: Administrator, Guide/HOD, Faculty Mentor, and Student. Comprehensive data isolation ensures that students have read-only visibility into their individual performance profile without exposure to peer records, while mentors access longitudinal counselling workflows.",
        body_indent
    ))

    # =========================================================================
    # PAGE 14: CHAPTER 1 cont. (Numbered Page 3)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("1.4 Problem Statement", h2_sec))
    p.append(Paragraph(
        "Higher education institutions face significant challenges in detecting and preventing student dropout due to the prevalence of fragmented academic data, lack of automated predictive intelligence, and the delayed nature of manual reviews. Existing institutional ERP platforms function primarily as record-keeping systems rather than proactive early-warning mechanisms. When at-risk students are identified, faculty mentors lack granular diagnostic insights explaining why the student is struggling, leading to subjective, inconsistent, or late interventions.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.5 Aim of the Project", h2_sec))
    p.append(Paragraph(
        "The primary aim of this project is to conceptualize, design, develop, test, and validate an integrated, full-stack AI-Based Student Dropout Prediction and Counselling Management System that continuously monitors multidimensional risk signals, explains risk drivers through transparent XAI cards, and orchestrates proactive remedial workflows.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.6 Objectives", h2_sec))
    p.append(Paragraph("To fulfill this aim, the project executes seven concrete engineering objectives:", body))
    p.append(Paragraph("1. Synthesize and normalize an extensive, multi-factorial student dataset incorporating academic, behavioral, and socio-financial attributes reflecting realistic Indian engineering university environments.", body))
    p.append(Paragraph("2. Design, train, and evaluate supervised machine learning classification pipelines (Random Forest and Logistic Regression) achieving over 90% accuracy in risk stratification.", body))
    p.append(Paragraph("3. Develop a deterministic Explainable AI (XAI) feature deficit attribution algorithm to translate model probabilities into transparent risk reason cards.", body))
    p.append(Paragraph("4. Construct a responsive 4-tier Role-Based Access Control (RBAC) web architecture with strict peer privacy protection.", body))
    p.append(Paragraph("5. Implement a 5-stage Counselling Lifecycle Hub with queue capacity overflow meters and mentor workload tracking.", body))
    p.append(Paragraph("6. Provide dynamic administrative policy threshold controls and on-demand model retraining routines.", body))
    p.append(Paragraph("7. Execute an automated test suite verifying system security, functional accuracy, and empirical ML performance.", body))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.7 Scope of the Project", h2_sec))
    p.append(Paragraph(
        "The project encompasses data ingestion via single-student registration and bulk CSV uploads, machine learning inference, explainable diagnostic card rendering, counselling queue management, in-portal notifications, and security audit logging. Out of scope for this version are automated SMS gateway integrations and direct biometric API integrations.",
        body_indent
    ))

    # =========================================================================
    # PAGE 15: CHAPTER 1 cont. (Numbered Page 4)
    # =========================================================================
    new_page()
    p = pages[-1]
    p.append(Paragraph("1.8 Motivation and Rationale", h2_sec))
    p.append(Paragraph(
        "The primary motivation for this project is the profound socioeconomic and personal consequence of college attrition. For students, dropping out frequently results in debt, loss of professional qualification, and personal demoralization. For Sanskriti University, attrition impacts institutional reputation, faculty workload distribution, and overall department morale. By transforming institutional data into early actionable warnings, universities can shift from passive observation to compassionate, timely remediation.",
        body_indent
    ))
    p.append(Paragraph(
        "From an engineering perspective, this project integrates diverse core computer science disciplines: supervised machine learning, applied data mining, relational database optimization, RESTful API design, authentication security, and responsive UI engineering. Constructing a complete, working software artifact delivers substantial academic and practical value.",
        body_indent
    ))
    p.append(Spacer(1, 4))
    p.append(Paragraph("1.9 Organization of the Report", h2_sec))
    p.append(Paragraph("The remainder of this report is systematically organized as follows:", body))
    p.append(Paragraph("• <b>Chapter 2: Literature Review</b> examines existing student retention systems, machine learning in higher education, explainable artificial intelligence principles, and comparative benchmarks.", body))
    p.append(Paragraph("• <b>Chapter 3: System Analysis and Requirements</b> articulates limitations of existing systems, proposed improvements, functional/non-functional requirements, hardware/software specifications, and feasibility analyses.", body))
    p.append(Paragraph("• <b>Chapter 4: System Design and Methodology</b> details the decoupled 3-tier architecture, ML pipeline, database schema, data dictionaries, DFDs, UML diagrams, and API specifications.", body))
    p.append(Paragraph("• <b>Chapter 5: System Implementation</b> documents the software environment, production codebase, XAI reasoning engine, Flask backend, RBAC security, bulk ingestion, and administrative policy controls.", body))
    p.append(Paragraph("• <b>Chapter 6: Testing and Results</b> presents the automated testing methodology, test matrices, interface screenshots, empirical ML evaluation metrics (93.3% accuracy, 0.965 AUC), and usability findings.", body))
    p.append(Paragraph("• <b>Chapter 7: Project Management</b> reviews sprint timelines, milestone delivery, candidate work distribution, and solutions to technical challenges.", body))
    p.append(Paragraph("• <b>Chapter 8: Learning Outcomes</b> summarizes technical proficiencies, algorithmic insights, and ethical considerations acquired throughout the project.", body))
    p.append(Paragraph("• <b>Chapter 9 & 10: Limitations, Future Scope & Conclusion</b> summarizes system achievements against initial goals and outlines future technical roadmaps.", body))

    print(f"Front matter + Ch1 complete: {len(pages)} pages.")
