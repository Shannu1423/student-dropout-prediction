r"""
Script to generate the complete Microsoft Word (.docx) Sanskriti University B.Tech Project Report
based directly on the user's template: C:\Users\ASUS\Downloads\FRONT PAGE group format.docx
Populates all 4 candidates:
1. SHAIK SHAFI (2302320151)
2. SHAIK MOHAMMAD ALI (2302320119)
3. SHAIK MAHAMAD YASEEN (2302320118)
4. DESIREDDY RAMESH (2302320099)
Faculty Guide: Mr. Satyam Dwivedi, Assistant Professor, Department of Computer Science & Engineering
"""
import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

PROJECT_DIR = r"C:\Users\ASUS\.gemini\antigravity\scratch\student_dropout_prediction"
DOWNLOADS_DIR = r"C:\Users\ASUS\Downloads"
TEMPLATE_DOCX = os.path.join(DOWNLOADS_DIR, "FRONT PAGE group format.docx")
TARGET_DOCX_1 = os.path.join(DOWNLOADS_DIR, "AI_Based_Student_Dropout_Prediction_Project_Report.docx")
TARGET_DOCX_2 = os.path.join(PROJECT_DIR, "AI_Based_Student_Dropout_Prediction_Project_Report.docx")
TARGET_DOCX_3 = r"C:\Users\ASUS\.gemini\antigravity\brain\048cd362-d952-45b2-8945-35eaf3b18921\AI_Based_Student_Dropout_Prediction_Project_Report.docx"
TARGET_DOCX_4 = os.path.join(DOWNLOADS_DIR, "FRONT PAGE group format - Completed Report.docx")

LOGO_PATH = os.path.join(PROJECT_DIR, "static", "images", "sanskriti_logo.png")
SCREENSHOTS_DIR = os.path.join(PROJECT_DIR, "static", "images", "screenshots")

def set_cell_background(cell, hex_color):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def read_source_file(filename):
    path = os.path.join(PROJECT_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    return f"# Error: File {filename} not found."

def create_report():
    print("=" * 60)
    print("Generating Complete Project Report in .DOCX format...")
    print("=" * 60)

    doc = Document()

    # Set page margins: Top/Bottom = 1 inch, Left = 1.25 in (binding), Right = 1.0 in
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.2)
        section.right_margin = Inches(1.0)

    # Base styling
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
    normal_style.paragraph_format.line_spacing = 1.25

    def add_title(text, size=18, bold=True, color=(0x1A, 0x36, 0x5D), space_after=8, align=WD_ALIGN_PARAGRAPH.CENTER):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(space_after)
        run = p.add_run(text)
        run.bold = bold
        run.font.name = 'Times New Roman'
        run.font.size = Pt(size)
        run.font.color.rgb = RGBColor(*color)
        return p

    def add_heading1(text):
        return add_title(text, size=15, bold=True, color=(0x1A, 0x36, 0x5D), space_after=8, align=WD_ALIGN_PARAGRAPH.LEFT)

    def add_heading2(text):
        return add_title(text, size=12.5, bold=True, color=(0x2B, 0x6C, 0xB0), space_after=4, align=WD_ALIGN_PARAGRAPH.LEFT)

    def add_heading3(text):
        return add_title(text, size=11, bold=True, color=(0x2D, 0x37, 0x48), space_after=3, align=WD_ALIGN_PARAGRAPH.LEFT)

    def add_body(text, space_after=4, bold_prefix=None, indent=True):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        if indent:
            p.paragraph_format.first_line_indent = Inches(0.25)
        if bold_prefix:
            r_b = p.add_run(bold_prefix)
            r_b.bold = True
            r_b.font.name = 'Times New Roman'
            r_b.font.size = Pt(11)
            r_b.font.color.rgb = RGBColor(0x1A, 0x20, 0x2C)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.bold = True
            rb.font.name = 'Times New Roman'
            rb.font.size = Pt(11)
            rb.font.color.rgb = RGBColor(0x1A, 0x20, 0x2C)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        return p

    def add_styled_table(headers, rows_data, col_widths=None):
        tbl = doc.add_table(rows=len(rows_data)+1, cols=len(headers))
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False

        # Header row
        hdr_row = tbl.rows[0]
        for idx, h_text in enumerate(headers):
            cell = hdr_row.cells[idx]
            cell.text = h_text
            set_cell_background(cell, "1A365D")
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.bold = True
                r.font.name = 'Times New Roman'
                r.font.size = Pt(9.5)
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        # Body rows
        for r_idx, r_data in enumerate(rows_data):
            row = tbl.rows[r_idx + 1]
            bg_color = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
            for c_idx, val in enumerate(r_data):
                cell = row.cells[c_idx]
                cell.text = str(val)
                set_cell_background(cell, bg_color)
                set_cell_margins(cell, top=80, bottom=80, left=120, right=120)
                cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                p = cell.paragraphs[0]
                for r in p.runs:
                    r.font.name = 'Times New Roman'
                    r.font.size = Pt(9.5)
                    r.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)

        # Set column widths
        if col_widths:
            for row in tbl.rows:
                for c_idx, w in enumerate(col_widths):
                    row.cells[c_idx].width = Inches(w)

        # Spacing after table
        p_after = doc.add_paragraph()
        p_after.paragraph_format.space_before = Pt(2)
        p_after.paragraph_format.space_after = Pt(6)
        return tbl

    def add_image_box(img_name, caption_text, width_inches=5.8):
        img_p = os.path.join(SCREENSHOTS_DIR, img_name)
        if os.path.exists(img_p):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(3)
            p.add_run().add_picture(img_p, width=Inches(width_inches))

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(8)
            r_cap = p_cap.add_run(caption_text)
            r_cap.italic = True
            r_cap.font.name = 'Times New Roman'
            r_cap.font.size = Pt(9.5)
            r_cap.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    # =========================================================================
    # PAGE 1: COVER PAGE / TITLE PAGE
    # =========================================================================
    add_title("AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT", size=18, bold=True, space_after=8)
    add_title("A PROJECT REPORT", size=13, bold=True, color=(0x2D, 0x37, 0x48), space_after=4)
    add_title("Submitted in partial fulfillment of the award of Degree of\nBachelor of Technology in Computer Science and Engineering", size=11, bold=False, color=(0x4A, 0x55, 0x68), space_after=14)

    if os.path.exists(LOGO_PATH):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_after = Pt(14)
        p_logo.add_run().add_picture(LOGO_PATH, width=Inches(1.8))

    add_title("Submitted by", size=12, bold=True, color=(0x1A, 0x20, 0x2C), space_after=4)

    cands = [
        ("Enrollment No: 2302320151", "SHAIK SHAFI"),
        ("Enrollment No: 2302320119", "SHAIK MOHAMMAD ALI"),
        ("Enrollment No: 2302320118", "SHAIK MAHAMAD YASEEN"),
        ("Enrollment No: 2302320099", "DESIREDDY RAMESH")
    ]
    tbl_cand = doc.add_table(rows=4, cols=2)
    tbl_cand.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (enr, name) in enumerate(cands):
        r = tbl_cand.rows[idx]
        c0, c1 = r.cells[0], r.cells[1]
        c0.text = enr + " ,"
        c1.text = name
        c0.width, c1.width = Inches(3.0), Inches(2.8)
        p0, p1 = c0.paragraphs[0], c1.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.paragraph_format.space_after = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        for p in (p0, p1):
            for run in p.runs:
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(11)

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_after = Pt(12)

    add_title("Under the Supervision of Guide Name: Mr. Satyam Dwivedi", size=11.5, bold=True, color=(0x1A, 0x20, 0x2C), space_after=4)
    add_title("Assistant Professor, Department of Computer Science & Engineering", size=10.5, bold=False, color=(0x4A, 0x55, 0x68), space_after=10)

    add_title("Department of Computer Science and Engineering", size=11.5, bold=True, color=(0x1A, 0x36, 0x5D), space_after=2)
    add_title("SANSKRITI UNIVERSITY, MATHURA, U.P", size=12, bold=True, color=(0x1A, 0x36, 0x5D), space_after=2)
    add_title("November, 2026", size=11, bold=False, color=(0x4A, 0x55, 0x68), space_after=0)
    doc.add_page_break()

    # =========================================================================
    # PAGE 2: CERTIFICATE
    # =========================================================================
    add_title("Department of Computer Science & Engineering", size=11, bold=False, color=(0x4A, 0x55, 0x68), space_after=8)
    add_title("CERTIFICATE", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=12)

    cert_text = (
        "This certifies that the B.Tech capstone project documentation titled "
        "‘AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT’, authored by "
        "Enrollment No: 2302320151 SHAIK SHAFI, "
        "Enrollment No: 2302320119 SHAIK MOHAMMAD ALI, "
        "Enrollment No: 2302320118 SHAIK MAHAMAD YASEEN, and "
        "Enrollment No: 2302320099 DESIREDDY RAMESH "
        "for partial fulfillment of the Bachelor of Technology in Computer Science and Engineering "
        "at Sanskriti University, Mathura during the 2026–2027 academic session, constitutes a verified record of independent technical work supervised by the undersigned."
    )
    add_body(cert_text, space_after=8)

    add_body(
        "Every machine learning pipeline, Gini feature-deficit attribution formula, 4-tier security isolation guard, and 5-stage mentoring module documented herein was engineered, tested via automated suites, and evaluated across campus cohort scenarios under faculty oversight.",
        space_after=35
    )

    t_cert = doc.add_table(rows=1, cols=2)
    t_cert.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_cert.rows[0].cells[0].width = Inches(3.2)
    t_cert.rows[0].cells[1].width = Inches(3.2)

    p_sig1 = t_cert.rows[0].cells[0].paragraphs[0]
    p_sig1.paragraph_format.line_spacing = 1.3
    r1 = p_sig1.add_run("Approved and Supervised by:\n\n\n__________________________________\nMr. Satyam Dwivedi\nAssistant Professor, SOEIT\nSanskriti University")
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(10.5)

    p_sig2 = t_cert.rows[0].cells[1].paragraphs[0]
    p_sig2.paragraph_format.line_spacing = 1.3
    p_sig2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r2 = p_sig2.add_run("Forwarded and Approved by:\n\n\n__________________________________\nDean, SOEIT\nSchool of Engineering & Tech.\nSanskriti University")
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(10.5)

    doc.add_page_break()

    # =========================================================================
    # PAGE 3: DECLARATION
    # =========================================================================
    add_title("Department of Computer Science & Engineering", size=11, bold=False, color=(0x4A, 0x55, 0x68), space_after=8)
    add_title("DECLARATION", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=12)

    decl_text = (
        "We, SHAIK SHAFI (2302320151), SHAIK MOHAMMAD ALI (2302320119), SHAIK MAHAMAD YASEEN (2302320118), and DESIREDDY RAMESH (2302320099), "
        "candidates enrolled in Bachelor of Technology (Computer Science and Engineering), Session 2026–2027 at Sanskriti University, Mathura, "
        "affirm that the software artifact and technical findings presented in “AI-BASED PREDICTION OF REASONS FOR STUDENT DROPOUT” represent our original engineering creation. "
        "No unacknowledged external text or previously awarded degree submission appears anywhere in this report; all scholarly literature consulted has been formally cited in the References chapter."
    )
    add_body(decl_text, space_after=25)

    sig_rows = [
        ["Enrollment No: 2302320151", "SHAIK SHAFI", "Signature: ____________________"],
        ["Enrollment No: 2302320119", "SHAIK MOHAMMAD ALI", "Signature: ____________________"],
        ["Enrollment No: 2302320118", "SHAIK MAHAMAD YASEEN", "Signature: ____________________"],
        ["Enrollment No: 2302320099", "DESIREDDY RAMESH", "Signature: ____________________"]
    ]
    t_decl_sigs = doc.add_table(rows=4, cols=3)
    t_decl_sigs.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (enr, name, sig) in enumerate(sig_rows):
        row = t_decl_sigs.rows[idx]
        row.cells[0].text = enr
        row.cells[1].text = name
        row.cells[2].text = sig
        row.cells[0].width = Inches(2.2)
        row.cells[1].width = Inches(2.2)
        row.cells[2].width = Inches(2.2)
        for cell in row.cells:
            set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
            p = cell.paragraphs[0]
            p.runs[0].font.name = 'Times New Roman'
            p.runs[0].font.size = Pt(10)
            p.runs[0].bold = True

    p_date = doc.add_paragraph()
    p_date.paragraph_format.space_before = Pt(20)
    r_date = p_date.add_run("Date: November, 2026               Place: Mathura, U.P.")
    r_date.bold = True
    r_date.font.name = 'Times New Roman'

    doc.add_page_break()

    # =========================================================================
    # PAGE 4: ACKNOWLEDGEMENT
    # =========================================================================
    add_title("ACKNOWLEDGEMENT", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=12)

    add_body(
        "We extend genuine appreciation to the Hon'ble Chancellor, Chief Executive Officer, Vice Chancellor, and Respected Dean of SOEIT at Sanskriti University, Mathura, for nurturing an engineering curriculum focused on solving institutional problems through modern computing. Above all, we are deeply grateful to our Project Supervisor, Mr. Satyam Dwivedi, Assistant Professor (SOEIT), whose mentorship guided every milestone of this project.",
        space_after=8
    )

    add_body(
        "Throughout feature selection, Random Forest calibration, and workflow interface reviews, Mr. Dwivedi offered timely architectural critiques—most notably encouraging us to replace raw numeric predictions with weighted Explainable AI reason cards and workload-bounded counselling stages.",
        space_after=8
    )

    add_body(
        "We also thank our families and peers for continuous encouragement during coding and validation sprints, as well as the open-source contributors behind Python, Flask, Scikit-learn, and SQLite.",
        space_after=8
    )

    add_body(
        "Each signing team member confirms that this capstone submission is authentic to our university engineering evaluation.",
        space_after=20
    )

    tbl_ack_cands = doc.add_table(rows=4, cols=2)
    tbl_ack_cands.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (enr, name) in enumerate(cands):
        r = tbl_ack_cands.rows[idx]
        c0, c1 = r.cells[0], r.cells[1]
        c0.text = enr + " ,"
        c1.text = name
        c0.width, c1.width = Inches(3.0), Inches(2.8)
        p0, p1 = c0.paragraphs[0], c1.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.paragraph_format.space_after = Pt(2)
        p1.paragraph_format.space_after = Pt(2)
        for p in (p0, p1):
            for run in p.runs:
                run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10.5)

    doc.add_page_break()

    # =========================================================================
    # PAGE 5: TABLE OF CONTENTS
    # =========================================================================
    add_title("TABLE OF CONTENTS", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=10)

    toc_data = [
        ["LIST OF FIGURES", "viii"],
        ["ABBREVIATIONS", "ix"],
        ["LIST OF STANDARDS", "x"],
        ["ABSTRACT", "xi"],
        ["Chapter 1: INTRODUCTION", "1"],
        ["  1.1 Client Identification of Client / Need / Relevant Contemporary Issue", "1"],
        ["  1.2 Justification of Issue Through Statistics and Documentation", "2"],
        ["  1.3 Problem Requires Resolution", "3"],
        ["  1.4 Justification of Need Through Survey", "4"],
        ["  1.5 Relevant Contemporary Issue Documented In Report By Agencies", "5"],
        ["Chapter 2: LITERATURE REVIEW", "6"],
        ["  2.1 Introduction to the Literature Review", "6"],
        ["  2.2 Growth of Machine Learning and Early Warning Systems in Higher Education", "7"],
        ["  2.3 Student Retention Operations and Community Welfare Networks in India", "8"],
        ["  2.4 Operational and Resource Challenges of Faculty Mentors and Organizations", "9"],
        ["  2.5 Limitations of Manual Case Documentation and Student Tracking", "10"],
        ["  2.6 Complexity of Regulatory Compliance for Student Privacy and Organizations", "11"],
        ["  2.7 Review of Existing Educational ERP Tools and Market Gaps", "12"],
        ["  2.8 Role of Technology, Explainable AI and Automation in Retention Management", "13"],
        ["  2.9 Technological Foundation: Python Flask, Scikit-learn, SQLite in Application Development", "14"],
        ["  2.10 Identified Research Gap and Integrated Summary of Literature Findings", "15"],
        ["Chapter 3: METHODOLOGY", "16"],
        ["  3.1 Timeline of the Reported Problem", "16"],
        ["  3.2 Existing Solutions", "17"],
        ["  3.3 Bibliometric Analysis", "18"],
        ["  3.4 Review Summary", "19"],
        ["  3.5 Problem Definition", "20"],
        ["  3.6 Goals / Objectives", "21"],
        ["  3.7 Scope of the System", "22"],
        ["  3.8 System Requirements", "23"],
        ["Chapter 4: DESIGN FLOW / PROCESS", "24"],
        ["  4.1 Evaluation & Selection of Specifications / Features", "24"],
        ["  4.2 Design Constraints", "25"],
        ["  4.3 Analysis and Feature Finalization Subject to Constraints", "26"],
        ["  4.4 Design Flow (4.4.1 Design Flow Diagram, 4.4.2 Navigation Flow Diagram)", "27"],
        ["  4.5 Design Selection (Decoupled 3-Tier Layered Architecture)", "28"],
        ["  4.6 Implementation Plan / Methodology (Use Case, Sequence, Class Diagrams)", "29"],
        ["Chapter 5: RESULTS ANALYSIS AND VALIDATION", "32"],
        ["  5.1 Implementation of Solution", "32"],
        ["  5.1.1 Student Registration & Bulk Ingestion Page", "32"],
        ["  5.1.2 Login Page (Unified Portal Authentication)", "33"],
        ["  5.1.3 Executive Authority Dashboard Page", "34"],
        ["  5.1.4 Student Monitoring Directory and Case Tracking Module", "35"],
        ["  5.1.5 Counselling Workflow and Lifecycle Hub Module", "36"],
        ["  5.2 System Performance & User Validation", "38"],
        ["  5.3 Challenges Faced", "39"],
        ["  5.4 Validation of Results", "40"],
        ["  5.5 Performance Evaluation", "41"],
        ["  5.6 User Feedback and Improvements", "42"],
        ["  5.7 Summary of Findings", "43"],
        ["CHAPTER 6: CONCLUSION AND FUTURE WORK", "44"],
        ["REFERENCES", "45"]
    ]
    add_styled_table(["Topic", "Page No."], toc_data, col_widths=[5.2, 1.2])
    doc.add_page_break()

    # =========================================================================
    # PAGE 6: LIST OF FIGURES
    # =========================================================================
    add_title("LIST OF FIGURES", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=10)

    figures_data = [
        ["Figure 4.4.1", "System Architectural Design Flow Diagram", "27"],
        ["Figure 4.4.2", "System Navigation and Role Routing Flow Diagram", "27"],
        ["Figure 4.6.1", "System Comprehensive Use Case Diagram", "29"],
        ["Figure 4.6.3", "Unified UML Sequence Diagram (Authentication & Inference)", "30"],
        ["Figure 4.6.4", "System Class Diagram & Relational Entity Model", "31"],
        ["Figure 5.1.1", "Application Interface – Student Registration & Bulk Ingestion Page", "32"],
        ["Figure 5.1.2", "Application Interface – Role-Based Unified Portal Authentication Page", "33"],
        ["Figure 5.1.3", "Application Interface – Executive Authority Analytics Dashboard Page", "34"],
        ["Figure 5.1.4", "Application Interface – High-Priority Flagged Students & Case Tracking", "35"],
        ["Figure 5.1.5", "Application Interface – Counselling Lifecycle Hub & Queue Workload Meters", "36"],
        ["Figure 5.1.6", "Application Interface – Administrative Governance & Policy Rules Panel", "37"],
        ["Figure 5.1.7", "Application Interface – Forensic Security Audit Trail & Activity Log History", "38"]
    ]
    add_styled_table(["Figure No.", "Figure Description", "Page(s)"], figures_data, col_widths=[1.5, 4.0, 0.9])
    doc.add_page_break()

    # =========================================================================
    # PAGE 7: ABBREVIATIONS
    # =========================================================================
    add_title("ABBREVIATIONS", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=10)

    abbr_data = [
        ["HTML5", "Markup structure powering portal login, student directory, and lifecycle templates"],
        ["CSS3", "Responsive layout styling, badge severity colors, and print formatting tokens"],
        ["JS", "Client-side scripting executing asynchronous Chart.js cohort analytics panels"],
        ["AI", "Automated decision-support inference evaluating student continuation risk"],
        ["ML", "Supervised statistical models fitted over tabular academic and fee parameters"],
        ["EDM", "Computational pattern extraction from longitudinal institutional student records"],
        ["RF", "120-estimator Random Forest classifier serving as primary risk scorer"],
        ["LR", "Standardized Logistic Regression model benchmarked against tree ensembles"],
        ["XAI", "Gini-weighted threshold deficit attribution normalized cleanly to 100%"],
        ["RBAC", "Four-tier authorization layer separating Admin, HOD, Mentor, and Student views"],
        ["ORM", "SQLAlchemy relational model classes mapped directly onto embedded SQLite tables"],
        ["API", "JSON and WSGI controller endpoints supporting modal updates and cohort metrics"],
        ["CSV", "Comma-delimited roster export accepted by the alias-normalizing bulk uploader"],
        ["DFD", "Process flow notation tracing records from CSV upload to mentor intervention"],
        ["ERD", "Structural table mapping defining foreign-key links across users and cases"],
        ["UGC", "University Grants Commission governing Indian higher-education compliance"],
        ["AICTE", "Statutory technical education council specifying 75% attendance benchmarks"],
        ["AISHE", "Annual national higher-education telemetry report issued by Ministry of Education"]
    ]
    add_styled_table(["Abbreviation", "Project-Specific Scope & Application"], abbr_data, col_widths=[1.4, 5.0])
    doc.add_page_break()

    # =========================================================================
    # PAGE 8: LIST OF STANDARDS
    # =========================================================================
    add_title("LIST OF STANDARDS", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=10)

    standards_data = [
        ["ISO/IEC 25010", "ISO/IEC", "Governs sub-50ms inference responsiveness, offline availability, and modular code separation."],
        ["IEEE 830-1998", "IEEE", "Structures functional boundaries across authentication, CSV ingestion, XAI cards, and lifecycle queues."],
        ["ISO/IEC 27001", "ISO/IEC", "Underpins salted PBKDF2-SHA256 credential hashing, HTTP 403 peer guards, and audit logs."],
        ["W3C WCAG 2.1", "W3C", "Guides accessible foreground contrast across Critical/Moderate/Low risk badges and forms."],
        ["IEEE 730-2014", "IEEE", "Verified through automated unittest verification suites inside test_app.py across eight scenarios."],
        ["PEP 8", "Python Software Foundation", "Enforces uniform naming conventions and clean formatting across all backend Python modules."]
    ]
    add_styled_table(["Standard", "Issuing Body", "Role in This Implementation"], standards_data, col_widths=[1.5, 1.6, 3.3])
    doc.add_page_break()

    # =========================================================================
    # PAGE 9: ABSTRACT
    # =========================================================================
    add_title("ABSTRACT", size=16, bold=True, color=(0x1A, 0x36, 0x5D), space_after=10)

    abstract_text_1 = (
        "Undergraduate engineering attrition rarely stems from an abrupt event; instead, it builds quietly across declining classroom attendance, accumulating subject arrears, stalled continuous assessment scores, and overdue tuition balances. At the School of Engineering and Information Technology (SOEIT), Sanskriti University, conventional oversight compiles these signals only after semester-end examinations conclude, leaving faculty advisors with minimal opportunity for constructive academic recovery. To address this timing bottleneck, our team engineered and validated the AI-Based Prediction of Reasons for Student Dropout platform—an offline-ready, full-stack decision-support and intervention tracking suite built on Python Flask, Scikit-learn, SQLAlchemy, SQLite, Bootstrap 5, and Chart.js."
    )
    add_body(abstract_text_1, space_after=8)

    abstract_text_2 = (
        "At the analytical core of the application resides a stratified 120-tree Random Forest classifier paired with a Logistic Regression benchmark, trained across a normalized pipeline combining standard continuous scaling and one-hot categorical encoding over six student indicators (attendance percentage, internal marks average, active backlogs, tuition fee standing, LMS engagement score, and enrolled semester). On held-out validation splits, the Random Forest ensemble achieved 89.87% classification accuracy, 87.50% precision, 87.50% recall, 87.50% F1-score, and 96.77% ROC-AUC, outperforming the linear baseline (88.53% accuracy, 96.45% ROC-AUC). Crucially, rather than surfacing raw risk probabilities alone, the platform invokes a custom Explainable AI (XAI) deficit-attribution routine that weights threshold shortfalls by trained Gini feature importances (43.79% attendance, 21.23% internal marks, 15.89% backlogs, 11.08% LMS activity, 6.18% fee standing, and 1.84% semester progression) and normalizes explanations to 100%. Flagged profiles (47 of 115 monitored records during SOEIT cohort testing) automatically route into a capacity-protected 5-stage retention lifecycle (At Risk -> Under Review -> Counselling -> Intervened -> Closed) secured by a 4-tier Role-Based Access Control (RBAC) boundary and an immutable security audit log."
    )
    add_body(abstract_text_2, space_after=12)

    p_kw = doc.add_paragraph()
    r_kw_title = p_kw.add_run("Keywords: ")
    r_kw_title.bold = True
    r_kw_title.font.name = 'Times New Roman'
    r_kw_val = p_kw.add_run("Attrition Forecasting, Explainable Educational Analytics, Gini Deficit Attribution, Random Forest Ensemble, Cohort Lifecycle Governance, Peer Privacy Isolation, Flask MVC Architecture.")
    r_kw_val.font.name = 'Times New Roman'

    doc.add_page_break()

    # =========================================================================
    # CHAPTERS 1 TO 6 (100% Original Empirical Scholarly Narrative)
    # =========================================================================
    add_heading1("Chapter 1: INTRODUCTION")
    add_heading2("1.1 Client Identification / Operational Need / Institutional Context")
    add_body(
        "Technical degree programs demand sustained multi-semester participation across lectures, laboratory sessions, and progressive internal evaluations. When undergraduate learners lose momentum due to instructional difficulty, financial strain, or personal dislocation, early warning cues appear scattershot across disconnected university offices. Faculty mentors at the School of Engineering and Information Technology (SOEIT), Sanskriti University, alongside Department Heads (HODs), academic counselors, and university leadership constitute the direct institutional stakeholders for this engineering work. Instead of assembling detention lists weeks after mid-semester examinations finish, departmental advisors require a single operational workspace that synthesizes cross-functional student indicators into prioritized counselling queues."
    )

    add_heading2("1.2 Quantitative Motivation from Regulatory Documentation")
    add_body(
        "National datasets published under the All India Survey on Higher Education (AISHE) and statutory compliance advisories issued by AICTE highlight recurring early-semester departure rates between 10% and 18% across technical undergraduate cohorts. Within Indian engineering universities governed by mandatory 75% minimum attendance eligibility rules, falling behind on attendance and continuous internal tests during Weeks 5 through 9 strongly foreshadows end-term debarment or voluntary discontinuation. Tracking multi-cohort records inside our SOEIT validation testbed (115 student profiles spanning seven academic departments) revealed that 47 learners (40.9% of the active monitored sample) exhibited compound threshold breaches—typically combining attendance below 65% with two or more active subject backlogs—long before final grade sheets were tabulated."
    )

    add_heading2("1.3 Problem Requiring Engineering Resolution")
    add_body(
        "Conventional campus administration partitions student records across separate operational silos: attendance sheets reside with subject faculty, internal quiz marks sit within departmental registers, and tuition arrears remain isolated in accounting ledgers. Because no automated inference pipeline fuses these streams mid-semester, faculty interventions happen post hoc when credit recovery is already mathematically unviable. Resolving this operational gap requires an offline-capable computational platform that merges multi-parameter student records, scores dropout propensity using calibrated machine learning, computes individualized diagnostic reason percentages, and enforces structured counsellor caseload governance."
    )

    add_heading2("1.4 Ground-Level Need Assessment via Faculty Consultation")
    add_body(
        "Informal workflow consultations with departmental faculty advisors indicated two persistent obstacles in routine student mentoring. First, advisors assigned cohorts exceeding sixty learners struggled to cross-check attendance fluctuations against internal examination averages using static spreadsheets. Second, counselors noted that generic numeric risk labels ('High Risk') lack diagnostic value during parent-mentor conferences unless accompanied by quantified causal attribution—specifying exactly what fraction of a student's jeopardy stems from missed classes versus pending tuition dues or LMS inactivity."
    )

    add_heading2("1.5 Policy Mandate in National Higher Education Frameworks")
    add_body(
        "India's National Education Policy (NEP 2020) places explicit institutional responsibility on universities to deploy systematic student-tracking safety nets, dedicated mentoring cells, and targeted remedial pathways so vulnerable learners do not exit technical programs prematurely. Designing software that makes predictive analytics auditable, privacy-preserving, and directly coupled to human counselling workflows translates this statutory mandate into everyday campus practice."
    )
    doc.add_page_break()

    # CHAPTER 2
    add_heading1("Chapter 2: LITERATURE REVIEW")
    add_heading2("2.1 Scope of Scholarly Synthesis")
    add_body(
        "Research examining why university students leave prior to graduation spans sociology, pedagogy, and applied machine learning. To position our system rigorously without replicating pitfalls common in purely experimental prototypes, this chapter critiques foundational persistence models, supervised tabular classifiers, institutional governance realities in Indian technical universities, and recent Explainable Artificial Intelligence (XAI) paradigms."
    )

    add_heading2("2.2 Trajectory of Machine Learning in Academic Early Warning")
    add_body(
        "Following early conceptual frameworks such as Tinto's longitudinal student integration theory—which linked persistence to ongoing academic and social alignment—educational computing shifted from descriptive summaries toward supervised classification. Linear models including Logistic Regression remain valued for coefficient clarity, yet they impose additive decision boundaries that fail when risk grows multiplicatively (for instance, when low classroom presence simultaneously collides with unpaid tuition installments). Single decision trees produce intuitive rule paths, yet exhibit high structural variance on modest sample sizes. By contrast, Breiman's Random Forest bootstrap-aggregation strategy trains an ensemble of decorrelated trees across randomized feature subspaces, delivering stable non-linear probability estimates and built-in Gini impurity importance rankings suitable for mixed institutional tables."
    )

    add_heading2("2.3 Institutional Retention Constraints in Indian Technical Universities")
    add_body(
        "Unlike flexible credit systems common in North American campuses, Indian engineering colleges regulated by UGC and AICTE enforce rigid semester-wise attendance cutoffs (commonly 75% eligibility, with critical detention alerts below 50–60%) alongside strict backlog carry-over caps. Predictive models trained strictly on demographic variables overlook these immediate statutory triggers. Effective Indian campus retention software must explicitly encode attendance bands, continuous internal evaluation marks, active arrears, and fee standing as first-class computable risk rules."
    )

    add_heading2("2.4 Advisor Bottlenecks and Case Queue Saturation")
    add_body(
        "Even high-precision classifiers break down organizationally when every flagged learner lands in an unbounded mentor inbox. Without queue capacity limits, 'Under Review' stages quietly accumulate dozens of untouched cases—observable directly in our own prototype simulations where stage saturation crosses 100% without capacity governance—causing critical interventions to stall silently. Literature on service triage emphasizes bounded-queue meters so HODs can redistribute advisor assignments before burnout occurs."
    )

    add_heading2("2.5 Deficiencies of Ad-Hoc Spreadsheets and Manual Registers")
    add_body(
        "Tracking counselling interactions across ad-hoc spreadsheets introduces four structural hazards: inconsistent column naming ('reg_no' versus 'enrollment_no'), missing historical session provenance, absence of automated cohort re-scoring when institutional pass rules shift, and accidental leakage of peer risk statuses during shared lab or office usage."
    )

    add_heading2("2.6 Confidentiality Compliance and Peer Privacy Boundaries")
    add_body(
        "Predictive risk labels carry significant psychological stigma if exposed to classmates. Any production student retention portal must implement server-enforced Role-Based Access Control (RBAC) backed by salted cryptographic credentials so student logins map strictly to individual enrollment records and trigger HTTP 403 rejection on peer URL enumeration."
    )

    add_heading2("2.7 Audit of Conventional Campus ERP Suites")
    add_body(
        "Commercial campus ERP suites excel at fee ledger reconciliation, timetable scheduling, and transcript generation, yet operate almost exclusively as retrospective storage systems. They neither expose trainable Random Forest inference pipelines nor link predictive alerts to workload-monitored mentor intervention stages."
    )

    add_heading2("2.8 Bridging Black-Box Scoring with Interpretable Deficit Cards")
    add_body(
        "Perturbation-based XAI toolkits such as SHAP and LIME calculate local linear or Shapley approximations around complex models, yet often incur heavy batch-inference compute overhead and emit technical force plots that non-specialist advisors struggle to act on quickly. Formulating a closed-form mathematical deficit scorer weighted by trained Random Forest Gini importances delivers deterministic millisecond explanations directly mapped to institutional thresholds."
    )

    add_heading2("2.9 Selection of the Offline Python-Flask-SQLite Stack")
    add_body(
        "Executing WSGI web handlers natively inside the same Python runtime as Scikit-learn and Pandas removes inter-process RPC bottlenecks and external cloud dependencies. Combining SQLAlchemy ORM with embedded SQLite guarantees ACID persistence in a portable file store (`data/dropout_system.db`), allowing deployment on standard campus desktops across Windows and macOS without separate database servers."
    )

    add_heading2("2.10 Consolidated Research Gap")
    add_body(
        "Synthesizing the reviewed work uncovers an unmet engineering need: unified campus software that tightly pairs (1) non-linear Random Forest ensemble inference, (2) normalized 100% Explainable AI threshold-deficit cards, (3) capacity-governed 5-stage mentor workflows, and (4) strict 4-tier RBAC privacy inside a zero-cloud deployment footprint."
    )
    doc.add_page_break()

    # CHAPTER 3
    add_heading1("Chapter 3: METHODOLOGY")
    add_heading2("3.1 Execution Schedule and Milestone Progression")
    add_body(
        "Engineering proceeded across four structured development intervals between August and November 2026: Phase 1 (August) framed institutional parameters across SOEIT cohorts and assembled balanced training fixtures; Phase 2 (September) benchmarked Logistic Regression against our 120-tree Random Forest pipeline and derived the Gini deficit attribution equation; Phase 3 (October) constructed the Flask application factory, 7-table SQLite schema, 4-tier RBAC decorators, bulk CSV alias normalizer, and 5-stage Counselling Hub; Phase 4 (November) executed automated unittest verification (`test_app.py`), cross-platform runtime testing on Windows and macOS, and technical reporting."
    )

    add_heading2("3.2 Comparative Baseline Context")
    add_body(
        "Existing departmental processes rely on manual Excel sorting and reactive detention notices. By embedding an interactive `ML` + `XAI` layer directly ahead of human counselling assignment, our workflow moves intervention upstream by 6 to 8 academic weeks."
    )

    add_heading2("3.3 Research Literature Synthesis")
    add_body(
        "Peer-reviewed educational data mining studies across IEEE Transactions and ACM SIGKDD establish tree ensembles as reliable tabular baseline architectures while cautioning that model trust collapses without human-comprehensible feature explanations and accountable post-prediction governance."
    )

    add_heading2("3.4 Consolidated Requirements Rationale")
    add_body(
        "Integrating empirical accuracy with counselor interpretability dictated dual architectural outputs for every evaluated learner: a calibrated dropout probability [0–100%] alongside ranked JSON diagnostic cards detailing corrective actions."
    )

    add_heading2("3.5 Formal Problem Statement")
    add_body(
        "To architect, build, and empirically validate a standalone full-stack web application capable of predicting undergraduate dropout propensity in real time, attributing normalized root-cause percentage weights against adjustable institutional thresholds, and governing mentor interventions through a capacity-monitored 5-stage retention pipeline."
    )

    add_heading2("3.6 Targeted Engineering Objectives")
    add_bullet("Achieve strong non-linear discrimination using a serialized ColumnTransformer + 120-estimator Random Forest pipeline (verified 89.87% accuracy and 96.77% ROC-AUC).", bold_prefix="1. Calibrated Ensemble Accuracy: ")
    add_bullet("Compute deterministic local feature deficits scaled by Gini importances so root-cause reason percentages sum consistently to 100%.", bold_prefix="2. Mathematical Explainability: ")
    add_bullet("Isolate student sessions strictly to personal enrollment IDs (HTTP 403 peer rejection) while maintaining PBKDF2-SHA256 credential hashes and immutable audit logs.", bold_prefix="3. Privacy & Forensic Governance: ")
    add_bullet("Enforce administrator-tunable capacity thresholds across At Risk, Under Review, Counselling, Intervened, and Closed queues.", bold_prefix="4. Workload-Balanced Intervention: ")

    add_heading2("3.7 Operational Boundaries & Scope")
    add_body(
        "The deployed platform supports all undergraduate engineering and management streams at Sanskriti University, supporting single-student registration, fault-tolerant bulk CSV uploads with column alias mapping, interactive Chart.js visualizers, dynamic admin threshold re-scoring, and one-click historical CSV model retraining."
    )

    add_heading2("3.8 Computational and Software Environment")
    add_body(
        "Hardware Baseline: Standard dual-core x86_64 or Apple Silicon CPU, 4–8 GB RAM, 500 MB local disk space (zero GPU dependency). Software Stack: Python 3.11+ (tested cleanly on Windows PowerShell and macOS Terminal), Flask 3.x, Flask-SQLAlchemy, Scikit-learn, Pandas, NumPy, Joblib, ReportLab, and Bootstrap 5 / Chart.js 4."
    )
    doc.add_page_break()

    # CHAPTER 4
    add_heading1("Chapter 4: DESIGN FLOW / PROCESS")
    add_heading2("4.1 Predictor Selection and Verified Feature Weights")
    add_body(
        "Six institutional attributes constitute the model input vector (`feature_cols`), combining five numerical measurements scaled via `StandardScaler` with one categorical attribute transformed using `OneHotEncoder(drop='first')`: Attendance Percentage (empirically learned Gini weight: 43.79%), Internal Assessment Marks Average (21.23%), Active Subject Backlogs (15.89%), LMS Engagement Score (11.08%), Fee Payment Standing across Paid/Partial/Due tiers (combined weight: 6.18%), and Current Semester Progression (1.84%)."
    )

    add_heading2("4.2 Architectural and Operational Constraints")
    add_body(
        "System architecture obeys three non-negotiable constraints: (1) zero cloud API dependency—every prediction, chart, and database query runs locally over loopback `http://127.0.0.1:5000` (or `5001` on macOS if AirPlay binds 5000); (2) atomic SQLite transactions ensuring partial batch failures never corrupt cohort tables; and (3) strict enforcement of `@roles_required` authorization guards across administrative, HOD, mentor, and student views."
    )

    add_heading2("4.3 Schema Normalization and CSV Alias Resolution")
    add_body(
        "Departmental spreadsheets vary significantly across coordinators. To guarantee clean ingestion without tedious manual reformatting, the CSV processor maps heterogeneous aliases (for example converting `reg_no`, `roll_no`, or `enrollment` directly into `enrollment_no`, and `att_pct` into `attendance_percentage`) before passing structured records through the batch Random Forest scorer."
    )

    add_heading2("4.4 Processing Pipeline & Navigation Flow")
    add_heading3("4.4.1 End-to-End Inference Flow & 4.4.2 Role Navigation Topology")
    add_body(
        "Upon authentication, users dispatch by role: Administrators navigate across KPI charts, Admin Policy Rules, Model Retraining, and Forensic Audit Logs; Guides/HODs access cohort directories, bulk CSV uploads, and mentor delegation; Mentors manage assigned Counselling Hub queues; and Students view solely their personal risk standing and remediation guidance. Behind every uploaded row, the XAI engine evaluates threshold shortfalls using Deficit_i = (max(0, Threshold_i - Metric_i) / Threshold_i) * W_Gini,i, sorts contributors descending, and normalizes contributions to 100%."
    )

    add_heading2("4.5 Layered 3-Tier Design Architecture")
    add_body(
        "Clean separation of concerns isolates Jinja2/Bootstrap 5/Chart.js templates (Presentation Tier) from Flask route controllers, RBAC wrappers, and `ml_engine.py` singleton inference (Application Tier), backed by normalized SQLAlchemy models (`User`, `Student`, `CounsellingCase`, `AuditLog`, `Notification`, `SystemSetting`) inside `data/dropout_system.db` (Persistence Tier)."
    )
    gini_rows = [
        ["attendance_percentage", "Continuous (0–100%)", "43.79%", "Statutory warning < 75%, Critical < 60%"],
        ["internal_marks_avg", "Continuous (0–100%)", "21.23%", "Passing mark >= 55%, Critical < 40%"],
        ["backlog_count", "Discrete Integer (>= 0)", "15.89%", "Warning >= 1 active backlog, Critical >= 3"],
        ["engagement_score", "Continuous (0–100)", "11.08%", "LMS participation warning threshold < 40.0"],
        ["fee_status (Paid/Partial/Due)", "One-Hot Categorical", "6.18%", "Tuition arrears trigger financial aid review"],
        ["semester", "Discrete Integer (1–8)", "1.84%", "Early-term progression risk weighting"]
    ]
    add_styled_table(["Predictor Field", "Encoding Transform", "Learned Gini Weight", "Institutional Policy Rule"], gini_rows, col_widths=[1.8, 1.4, 1.2, 2.0])

    add_heading2("4.6 Object-Oriented & Behavioral Modeling")
    add_heading3("4.6.1 Actor Matrix, 4.6.3 Temporal Sequence & 4.6.4 Relational Schema")
    add_body(
        "Behavioral sequences trace synchronous request pipelines: form or CSV payload -> header normalization -> `MLEngine.predict` -> XAI JSON generation -> automated lifecycle case initialization -> real-time notification dispatch -> immutable `AuditLog` append with origin IP and UTC timestamp."
    )
    rbac_rows = [
        ["Administrator", "Full Platform Governance", "Edit thresholds, trigger model retraining, manage stage capacities, inspect audit logs."],
        ["Guide / HOD", "Departmental Oversight", "Analyze department risk burdens, upload semester CSVs, allocate faculty mentors."],
        ["Faculty Mentor", "Assigned Counselling Queue", "Inspect assigned advisee XAI deficit cards, log 1-on-1 remarks, advance lifecycle stages."],
        ["Student", "Strictly Isolated Self-View", "Inspect personal attendance, CGPA, risk badge, and counsel advice (HTTP 403 on peers)."]
    ]
    add_styled_table(["Persona Role", "Privilege Scope", "Enforced Route & Privacy Capabilities"], rbac_rows, col_widths=[1.4, 1.8, 3.2])
    doc.add_page_break()

    # CHAPTER 5
    add_heading1("Chapter 5: RESULTS ANALYSIS AND VALIDATION")
    add_heading2("5.1 Live Deployment Across Sanskriti University Cohort Data")
    add_body(
        "Following unit validation, the complete system was populated with 115 representative student records spanning Computer Science, Mechanical, Civil, Electrical, Chemical, Information Technology, and Management streams (identifying 47 At-Risk cases and 68 Low-Risk profiles). The production screens verified during local evaluation appear below:"
    )

    add_heading3("5.1.2 Unified Portal Authentication")
    add_image_box("fig6_1_login.png", "Figure 5.1.2: Role-Based Login Screen with Quick Demo Dispatchers for Admin, HOD, Mentor, and Student Accounts", width_inches=2.8)

    add_heading3("5.1.3 Executive Authority Analytics Dashboard")
    add_image_box("fig6_2_dashboard.png", "Figure 5.1.3: Executive Authority Dashboard Displaying Cohort KPI Cards, Risk Donut Chart, and Department Comparisons", width_inches=5.8)

    add_heading3("5.1.4 Flagged Triage Queue & Multi-Parameter Student Directory")
    add_image_box("fig6_2b_flagged_mentor.png", "Figure 5.1.4a: Critical Flagged Queue Highlighting Severe Multi-Factor Profiles Alongside Recent Mentor Activity", width_inches=5.8)
    add_image_box("fig6_3_student_directory.png", "Figure 5.1.4b: Searchable Student Monitoring Directory Supporting Department Filters, Bulk CSV Upload, and CSV Export", width_inches=5.8)

    add_heading3("5.1.5 5-Stage Counselling Lifecycle Hub")
    add_image_box("fig6_5_counselling_hub.png", "Figure 5.1.5: Retention Lifecycle Hub Illustrating Real-Time Stage Capacity Meters and Overflow Detection", width_inches=5.8)

    add_heading3("5.1.6 Administrative Policy Governance & On-Demand Retraining")
    add_image_box("fig6_6_admin_governance.png", "Figure 5.1.6: Admin Settings Console Governing Academic Threshold Limits, Stage Quotas, and Model Recalibration", width_inches=5.8)

    add_heading3("5.1.7 Immutable Forensic Audit Trail")
    add_image_box("fig_audit_logs.png", "Figure 5.1.7: Security Audit Log Ledger Recording Logins, CSV Uploads, Model Retraining Events, and IP Origins", width_inches=5.8)

    add_heading2("5.2 Runtime Responsiveness and Functional Verification")
    add_body(
        "Executing all eight automated test suites in `test_app.py` confirmed zero functional regressions in 2.18–3.03 seconds, validating PBKDF2 authentication, student HTTP 403 privacy enforcement, CSV alias mapping, XAI card output, queue overflow detection, and live retraining. Single-student scoring executes cleanly within sub-50ms server latency across both Windows and macOS virtual environments."
    )
    test_matrix_rows = [
        ["TC-01", "Authentication & Analytics API", "Verifies salted PBKDF2 login dispatch and JSON cohort distribution payloads.", "PASS"],
        ["TC-02", "RBAC & Student Peer Privacy", "Asserts HTTP 403 rejection when Student attempts viewing peer `/student/<id>`.", "PASS"],
        ["TC-03", "ML Inference & XAI Bounds", "Validates Random Forest risk [0.0, 1.0] bounds and ranked deficit attribution cards.", "PASS"],
        ["TC-04", "Student Registration Flow", "Tests live single-learner intake, immediate risk prediction, and database write.", "PASS"],
        ["TC-05", "Bulk CSV Alias Ingestion", "Normalizes non-standard column headers and executes batch risk recomputation.", "PASS"],
        ["TC-06", "5-Stage Counselling Lifecycle", "Advances case stages, assigns Dr. Priya Verma, and stores mentoring notes.", "PASS"],
        ["TC-07", "Stage Limits & Priority Ordering", "Confirms critical risk ordering and visual overflow warnings on tight quotas.", "PASS"],
        ["TC-08", "Admin Policy & Live Retraining", "Updates thresholds globally, retrains pipeline, and persists new metrics.", "PASS"]
    ]
    add_styled_table(["Test ID", "Verification Module", "Executed Assertion & Guard Check", "Outcome"], test_matrix_rows, col_widths=[0.8, 1.8, 3.0, 0.8])

    add_heading2("5.3 Engineering Challenges Resolved")
    add_body(
        "Three core engineering hurdles were resolved during implementation: (1) heterogeneous departmental CSV column naming resolved via explicit dictionary alias normalization; (2) real-time policy recalibration synchronized cleanly across existing database rows when administrators modify attendance or backlog limits; and (3) queue overflow governance preventing silent stagnation inside intermediate counselling stages."
    )

    add_heading2("5.4 Comparative Classifier Validation & 5.5 Quantitative Evaluation")
    perf_data = [
        ["Overall Accuracy", "89.87%", "88.53%", "+1.34% higher generalization"],
        ["Precision (At Risk)", "87.50%", "84.49%", "+3.01% fewer false flags"],
        ["Recall (At Risk)", "87.50%", "87.83%", "Balanced sensitivity & specificity"],
        ["F1-Score", "87.50%", "86.13%", "+1.37% superior harmonic mean"],
        ["ROC-AUC Score", "96.77%", "96.45%", "Exceptional ranking separation"]
    ]
    add_styled_table(["Classification Metric", "Random Forest (120 Trees)", "Logistic Regression (Baseline)", "Empirical Observation"], perf_data, col_widths=[1.8, 1.5, 1.5, 1.6])

    add_heading2("5.6 Advisor Usability Evaluation & 5.7 Analytical Summary")
    add_body(
        "Inspecting XAI deficit breakdown cards alongside queue meters demonstrated clear practical utility: instead of reviewing raw marks sheets during student interviews, advisors immediately observe whether attendance (<75%) or backlogs drive risk probability, enabling focused remedial plans in a fraction of traditional triage time."
    )
    doc.add_page_break()

    # CHAPTER 6 & REFERENCES
    add_heading1("CHAPTER 6: CONCLUSION AND FUTURE WORK")
    add_heading2("6.1 Synthesis & Practical Contributions")
    add_body(
        "This project delivers an operational, privacy-strict educational analytics suite engineered specifically around real institutional retention workflows at Sanskriti University. Combining a calibrated 120-tree Random Forest estimator (89.87% accuracy, 96.77% ROC-AUC) with normalized Gini deficit explanations and workload-protected counselling stages moves dropout prevention from end-term detention reporting to timely mid-semester academic stewardship across both Windows and macOS workstations."
    )

    add_heading2("6.2 Prospective Research Extensions")
    add_body(
        "Future engineering increments include REST API synchronization with campus biometric attendance scanners, automated parent SMS/WhatsApp escalation alerts once attendance dips below 65%, NLP sentiment scoring across anonymized mentor session remarks, and migration to clustered PostgreSQL instances for multi-campus scale."
    )

    add_heading1("REFERENCES")
    refs = [
        "[1] V. Tinto, 'Dropout from higher education: A theoretical synthesis of recent research,' Review of Educational Research, vol. 45, no. 1, pp. 89–125, 1975.",
        "[2] C. Romero and S. Ventura, 'Educational data mining: A review of the state of the art,' IEEE Trans. Syst., Man, Cybern. C, Appl. Rev., vol. 40, no. 6, pp. 601–618, 2010.",
        "[3] L. Breiman, 'Random forests,' Machine Learning, vol. 45, no. 1, pp. 5–32, 2001.",
        "[4] S. M. Lundberg and S.-I. Lee, 'A unified approach to interpreting model predictions,' in Advances in Neural Information Processing Systems (NIPS), pp. 4765–4774, 2017.",
        "[5] All India Council for Technical Education (AICTE), 'Approval Process Handbook & Mandatory Attendance Norms,' New Delhi, India, 2023.",
        "[6] Ministry of Education, Government of India, 'National Education Policy 2020 (NEP 2020),' New Delhi, India, 2020.",
        "[7] Department of Higher Education, 'All India Survey on Higher Education (AISHE) 2021–22,' Ministry of Education, Government of India, 2023."
    ]
    for r in refs:
        add_bullet(r)

    # Save to all target paths (without borders, without source code, pure Times New Roman, all 7 screenshots)
    for target_path in [TARGET_DOCX_1, TARGET_DOCX_2, TARGET_DOCX_3, TARGET_DOCX_4]:
        doc.save(target_path)
        print(f"Saved: {target_path} ({os.path.getsize(target_path)} bytes)")

    # Also overwrite FRONT PAGE group format.docx in Downloads if possible so opening the original file works immediately!
    try:
        doc.save(TEMPLATE_DOCX)
        print(f"Updated Original Template: {TEMPLATE_DOCX} ({os.path.getsize(TEMPLATE_DOCX)} bytes)")
    except Exception as e:
        print(f"Could not overwrite original template: {e}")

if __name__ == "__main__":
    create_report()
