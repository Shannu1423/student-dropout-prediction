# -*- coding: utf-8 -*-
"""
Exact-Format Sanskriti University Project Report Generator (PDF + DOCX).
Matches the pure white borderless Times New Roman B.Tech Thesis layout
with 2-pass exact dynamic TOC / List of Figures page collection,
cover logo, front-matter banner, 7 Chapter-4 diagrams, and all 7 UI screenshots.
"""
import os
import shutil
from PIL import Image as PILImage

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    Image, PageBreak, Flowable, NextPageTemplate
)

from docx import Document
from docx.shared import Inches, Pt, Cm, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

from report_chapters_1_2 import get_chapter_1, get_chapter_2
from report_chapters_3_4 import get_chapter_3, get_chapter_4
from report_chapters_5_6 import get_chapter_5, get_chapter_6, get_references
from report_chapters_extended import enrich_chapters

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "static", "images", "sanskriti_logo.png")
BANNER_PATH = os.path.join(BASE_DIR, "static", "images", "diagrams", "sanskriti_banner.png")

PDF_OUT = os.path.join(BASE_DIR, "Sanskriti_Exact_Format_Project_Report.pdf")
DOCX_OUT = os.path.join(BASE_DIR, "Sanskriti_Exact_Format_Project_Report.docx")

DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
ARTIFACTS_DIR = r"C:\Users\ASUS\.gemini\antigravity\brain\048cd362-d952-45b2-8945-35eaf3b18921"

TITLE_TEXT = "AI-Based Prediction of Reasons for Student Dropout"
SUPERVISOR = "Mr. Satyam Dwivedi"
TEAM = [
    ("SHAIK SHAFI", "2302320151"),
    ("SHAIK MOHAMMAD ALI", "2302320119"),
    ("SHAIK MAHAMAD YASEEN", "2302320118"),
    ("DESIREDDY RAMESH", "2302320099"),
]


def to_roman(n):
    vals = [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"),
            (100, "c"), (90, "xc"), (50, "l"), (40, "xl"),
            (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]
    res = []
    for v, sym in vals:
        while n >= v:
            res.append(sym)
            n -= v
    return "".join(res)


class SectionMarker(Flowable):
    """Zero-height marker to record start/end physical page numbers during Pass 1."""
    def __init__(self, kind, key, label, collector):
        super().__init__()
        self.kind = kind
        self.key = key
        self.label = label
        self.collector = collector
        self.width = 0
        self.height = 0

    def draw(self):
        pass


class ReportDocTemplate(BaseDocTemplate):
    def __init__(self, filename, collector, **kwargs):
        super().__init__(filename, **kwargs)
        self.collector = collector
        self.body_start_abs_page = None
        self.logical_page_label = ""

    def handle_flowable(self, flowables):
        f = flowables[0] if flowables else None
        if isinstance(f, SectionMarker):
            abs_p = self.page
            if f.kind == "BODY_START" and self.body_start_abs_page is None:
                self.body_start_abs_page = abs_p
            if f.kind in ("FRONT_START", "CH_START", "SEC_START", "FIG"):
                lbl = self._format_page(abs_p, is_front=(f.kind == "FRONT_START"))
                self.collector["starts"][f.key] = lbl
                if f.kind == "FIG":
                    self.collector["figs"].append((f.key, f.label, lbl))
            elif f.kind in ("FRONT_END", "CH_END"):
                lbl = self._format_page(abs_p, is_front=(f.kind == "FRONT_END"))
                self.collector["ends"][f.key] = lbl
        super().handle_flowable(flowables)

    def _format_page(self, abs_p, is_front=False):
        if is_front or self.body_start_abs_page is None or abs_p < self.body_start_abs_page:
            return to_roman(abs_p)
        return str(abs_p - self.body_start_abs_page + 1)

    def afterPage(self):
        # Nothing extra needed; chrome drawn via template onPage
        pass


def make_onpage(mode, doc_ref):
    def _on_page(canvas, doc):
        W, H = A4
        canvas.saveState()
        abs_p = doc.page
        if mode == "cover":
            pass
        elif mode == "front_nohdr":
            canvas.setFont("Times-Roman", 11)
            canvas.drawCentredString(W / 2.0, 36, to_roman(abs_p))
        elif mode == "front_hdr":
            canvas.setFont("Times-Roman", 10.5)
            canvas.drawString(68, H - 42, "Sanskriti University, Mathura")
            canvas.setFont("Times-Roman", 11)
            canvas.drawCentredString(W / 2.0, 36, to_roman(abs_p))
        elif mode == "body":
            if doc_ref.body_start_abs_page is None:
                doc_ref.body_start_abs_page = abs_p
            arabic_no = abs_p - doc_ref.body_start_abs_page + 1
            canvas.setFont("Times-Roman", 10.5)
            canvas.drawString(68, H - 42, "Sanskriti University, Mathura")
            canvas.setFont("Times-Roman", 11)
            canvas.drawCentredString(W / 2.0, 36, str(arabic_no))
        canvas.restoreState()
    return _on_page


def scaled_image(path, target_width_in=6.0, max_height_in=7.6):
    if not os.path.exists(path):
        return Spacer(1, 12)
    with PILImage.open(path) as im:
        pw, ph = im.size
    w_pt = target_width_in * inch
    h_pt = w_pt * (ph / float(pw))
    max_h = max_height_in * inch
    if h_pt > max_h:
        h_pt = max_h
        w_pt = h_pt * (pw / float(ph))
    img = Image(path, width=w_pt, height=h_pt)
    img.hAlign = "CENTER"
    return img


def styles_dict():
    return {
        "cover_title": ParagraphStyle("cover_title", fontName="Times-Bold", fontSize=22, leading=28, alignment=TA_CENTER, spaceAfter=18),
        "cover_sub_bold": ParagraphStyle("cover_sub_bold", fontName="Times-Bold", fontSize=14, leading=20, alignment=TA_CENTER, spaceAfter=8),
        "cover_sub": ParagraphStyle("cover_sub", fontName="Times-Roman", fontSize=12, leading=18, alignment=TA_CENTER, spaceAfter=6),
        "cover_stu": ParagraphStyle("cover_stu", fontName="Times-Bold", fontSize=12, leading=17, alignment=TA_CENTER, spaceAfter=2),
        "dept_hdr": ParagraphStyle("dept_hdr", fontName="Times-Bold", fontSize=13, leading=18, alignment=TA_CENTER, spaceBefore=10, spaceAfter=10),
        "front_h1": ParagraphStyle("front_h1", fontName="Times-Bold", fontSize=15, leading=20, alignment=TA_CENTER, spaceBefore=6, spaceAfter=16),
        "ch_title": ParagraphStyle("ch_title", fontName="Times-Bold", fontSize=16, leading=22, alignment=TA_CENTER, spaceBefore=10, spaceAfter=20),
        "h2": ParagraphStyle("h2", fontName="Times-Bold", fontSize=13.5, leading=20, alignment=TA_LEFT, spaceBefore=18, spaceAfter=10),
        "h3": ParagraphStyle("h3", fontName="Times-Bold", fontSize=12.5, leading=19, alignment=TA_LEFT, spaceBefore=16, spaceAfter=8),
        "body": ParagraphStyle("body", fontName="Times-Roman", fontSize=12, leading=26, alignment=TA_JUSTIFY, spaceAfter=14),
        "sig_right": ParagraphStyle("sig_right", fontName="Times-Roman", fontSize=12, leading=17, alignment=TA_RIGHT),
        "sig_left": ParagraphStyle("sig_left", fontName="Times-Roman", fontSize=12, leading=17, alignment=TA_LEFT),
        "caption": ParagraphStyle("caption", fontName="Times-Italic", fontSize=11, leading=15, alignment=TA_CENTER, spaceBefore=8, spaceAfter=16),
        "tbl_hdr": ParagraphStyle("tbl_hdr", fontName="Times-Bold", fontSize=10.5, leading=14, alignment=TA_LEFT),
        "tbl_cell": ParagraphStyle("tbl_cell", fontName="Times-Roman", fontSize=10.5, leading=14, alignment=TA_LEFT),
        "tbl_cell_c": ParagraphStyle("tbl_cell_c", fontName="Times-Roman", fontSize=10.5, leading=14, alignment=TA_CENTER),
        "toc_ch": ParagraphStyle("toc_ch", fontName="Times-Bold", fontSize=10, leading=12.5, alignment=TA_LEFT),
        "toc_sec": ParagraphStyle("toc_sec", fontName="Times-Roman", fontSize=9.5, leading=11.5, alignment=TA_LEFT, leftIndent=10),
        "toc_sub": ParagraphStyle("toc_sub", fontName="Times-Roman", fontSize=9.2, leading=11.2, alignment=TA_LEFT, leftIndent=20),
        "toc_pg": ParagraphStyle("toc_pg", fontName="Times-Roman", fontSize=9.5, leading=11.5, alignment=TA_CENTER),
        "ref_grp": ParagraphStyle("ref_grp", fontName="Times-Bold", fontSize=12.5, leading=19, alignment=TA_LEFT, spaceBefore=14, spaceAfter=8),
        "ref_item": ParagraphStyle("ref_item", fontName="Times-Roman", fontSize=11.5, leading=22, alignment=TA_LEFT, leftIndent=16, firstLineIndent=-16, spaceAfter=11),
    }


def make_grid_table(rows, col_widths, vpad=5):
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.6, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), vpad),
        ("BOTTOMPADDING", (0, 0), (-1, -1), vpad),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.95, 0.95, 0.95)),
    ]))
    return t


def get_abbreviations():
    return [
        ("AI", "Artificial Intelligence: Machine-driven pattern learning applied to student academic risk modeling."),
        ("ML", "Machine Learning: Supervised classification algorithms predicting dropout propensity from institutional telemetry."),
        ("XAI", "Explainable Artificial Intelligence: Normalized Gini-weighted deficit breakdown explaining every risk score."),
        ("RF", "Random Forest: Bagged ensemble of 120 decision trees calibrated for non-linear tabular dropout prediction."),
        ("LR", "Logistic Regression: Linear probabilistic baseline benchmarked against the Random Forest classifier."),
        ("ROC-AUC", "Receiver Operating Characteristic – Area Under Curve: Discrimination metric evaluating ranking separation."),
        ("RBAC", "Role-Based Access Control: Four-tier permission governance isolating Admin, HOD, Mentor, and Student views."),
        ("PBKDF2", "Password-Based Key Derivation Function 2: Salted SHA-256 cryptographic hashing protecting user passwords."),
        ("ORM", "Object-Relational Mapping: SQLAlchemy database abstraction enforcing normalized relational schemas."),
        ("ACID", "Atomicity, Consistency, Isolation, Durability: Transactional reliability guarantee on SQLite commits."),
        ("CSV", "Comma-Separated Values: Tabular interchange file ingested through dictionary header-alias normalization."),
        ("KPI", "Key Performance Indicator: Summary cohort metrics including At-Risk ratio, branch burden, and ROC-AUC."),
        ("SOEIT", "School of Engineering & Information Technology, Sanskriti University, Mathura."),
        ("NEP 2020", "National Education Policy 2020: Indian statutory education framework encouraging early learner support."),
        ("AISHE", "All India Survey on Higher Education: National statistical portal tracking university retention."),
        ("NAAC", "National Assessment and Accreditation Council: Quality framework auditing structured remediation workflows."),
    ]


def get_standards():
    return [
        ("ISO/IEC 25010", "ISO / IEC", "Defines software product quality models covering functional suitability, usability, reliability, maintainability, and security across browser-based student support portals."),
        ("ISO/IEC 29119", "ISO / IEC", "Establishes systematic software verification guidelines governing our 8-test automated regression suite across ML inference, CSV aliasing, and privacy enforcement."),
        ("ISO/IEC 27001", "ISO / IEC", "Specifies information security management controls protecting sensitive student academic records, fee statuses, counselling remarks, and salted login credentials."),
        ("ISO/IEC 12207", "ISO / IEC", "Defines structured software engineering lifecycle processes spanning requirement surveys, UML architecture design, Flask/SQLite build, testing, and maintenance."),
        ("IEEE 830", "IEEE", "Provides clear specifications structure ensuring testable functional, security, and cross-platform performance requirements throughout documentation."),
        ("ISO/IEC 23053", "ISO / IEC", "Establishes framework governance for AI systems using machine learning, mandating transparent explainability and human-in-the-loop mentor oversight."),
        ("OWASP ASVS v4.0", "OWASP", "Guides application verification controls including fail-closed route authorization (HTTP 403), cryptographic PBKDF2 hashing, and append-only audit trails."),
        ("WCAG 2.1 Level AA", "W3C WAI", "Recommends high-contrast typography, semantic table markup, keyboard navigation, and accessible color-paired risk indicators across student dashboards."),
        ("AISHE / NEP 2020", "Ministry of Education", "National policy benchmarks promoting proactive retention counseling, early deficit remediation, and equitable undergraduate degree completion."),
    ]


def get_abstract_paragraphs():
    return [
        "AI-Based Prediction of Reasons for Student Dropout is a full-stack, human-centered academic retention and explainable decision-support web platform engineered to help university administrators, Heads of Departments (HODs), faculty mentors, and students identify and resolve undergraduate attrition risks before academic failure becomes irreversible. Across traditional campus operations, student attendance registers, sessional marks, pending semester arrears, tuition remittance ledgers, and learning management participation are maintained in fragmented spreadsheets. Consequently, coordinators discover vulnerable learners only at the close of an academic term when detention or course withdrawal notices have already been issued, leaving inadequate time for supportive mentoring.",
        "Unlike black-box predictive scripts that emit unexplained probabilities, our system unifies non-linear supervised machine learning with deterministic Explainable Artificial Intelligence (XAI) reason decomposition and bounded five-stage counselling management. A Scikit-Learn ColumnTransformer pipeline couples standard feature scaling on numeric indicators (attendance percentage, internal marks average, active backlog count, academic engagement index, and current semester) with one-hot encoding on tuition fee status, feeding a calibrated 120-tree Random Forest classifier. Validated across realistic held-out cohorts against a Logistic Regression baseline (88.53 percent accuracy, 96.45 percent ROC-AUC), the Random Forest ensemble achieves 89.87 percent accuracy and 96.77 percent ROC-AUC. Global Gini feature importances (43.79 percent attendance, 21.23 percent internal marks, 15.89 percent backlogs, 11.08 percent engagement, 6.18 percent fee status, and 1.84 percent semester) are multiplied with instance-level policy deficits to produce normalized root-cause percentages summing mathematically to 100 percent for every student.",
        "Engineered cleanly on Flask, SQLAlchemy ORM, SQLite, Bootstrap 5, and Chart.js, the platform incorporates a schema-tolerant dictionary header-alias CSV mapper enabling instant bulk departmental cohort imports without tedious column reformatting. Vulnerable learners automatically enter a structured Five-Stage Counselling Hub (Identified Risk, First Outreach, Counselling Scheduled, Follow-Up Active, and Resolved) fortified with administrator-defined queue capacity meters and automatic stall escalation alerts. Strict four-tier Role-Based Access Control (PBKDF2-SHA256 authentication plus HTTP 403 peer guards), live administrative rule re-scoring, on-demand CSV model retraining, forensic IP-tagged audit logging, and full cross-platform reproducibility across Windows and macOS make the system immediately deployable across higher education campuses."
    ]


def build_toc_rows(st, page_map, chapters):
    starts = page_map.get("starts", {})
    ends = page_map.get("ends", {})

    def rng(key, default_val="—"):
        s = starts.get(key, default_val)
        e = ends.get(key, s)
        return s if s == e or e == "—" else f"{s} - {e}"

    rows = [[Paragraph("Topic", st["tbl_hdr"]), Paragraph("Page No.", st["tbl_hdr"])]]
    front_items = [
        ("LIST OF FIGURES", rng("LOF")),
        ("ABBREVIATIONS", rng("ABBR")),
        ("LIST OF STANDARDS", rng("STDS")),
        ("ABSTRACT", rng("ABS")),
    ]
    for title, pno in front_items:
        rows.append([Paragraph(title, st["toc_ch"]), Paragraph(pno, st["toc_pg"])])

    for ch in chapters:
        ch_key = f"CH_{ch['number']}"
        rows.append([Paragraph(ch["title"], st["toc_ch"]), Paragraph(rng(ch_key), st["toc_pg"])])
        for sec in ch["sections"]:
            rows.append([Paragraph(sec["title"], st["toc_sec"]), Paragraph(starts.get(sec["id"], "—"), st["toc_pg"])])
            for sub in sec.get("subsections", []):
                rows.append([Paragraph(sub["title"], st["toc_sub"]), Paragraph(starts.get(sub["id"], "—"), st["toc_pg"])])

    rows.append([Paragraph("REFERENCES", st["toc_ch"]), Paragraph(rng("REFS"), st["toc_pg"])])
    return rows


def build_lof_rows(st, page_map):
    figs = page_map.get("figs", [])
    rows = [[Paragraph("Figure No.", st["tbl_hdr"]), Paragraph("Page(s)", st["tbl_hdr"])]]
    if not figs:
        rows.append([Paragraph("Computing figure locations...", st["tbl_cell"]), Paragraph("—", st["toc_pg"])])
    else:
        for _, label, pno in figs:
            rows.append([Paragraph(label, st["tbl_cell"]), Paragraph(pno, st["toc_pg"])])
    return rows


def assemble_pdf_story(st, collector, prev_pages, chapters, refs):
    story = []
    # ---- PAGE i: COVER ----
    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph(TITLE_TEXT, st["cover_title"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph("A PROJECT REPORT", st["cover_sub_bold"]))
    story.append(Spacer(1, 0.08 * inch))
    story.append(Paragraph("Submitted in partial fulfillment of the award of Degree of", st["cover_sub"]))
    story.append(Paragraph("<b>Bachelor of Technology in Computer Science and Engineering</b>", st["cover_sub"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(scaled_image(LOGO_PATH, target_width_in=1.65, max_height_in=1.65))
    story.append(Spacer(1, 0.22 * inch))
    story.append(Paragraph("Submitted by", st["cover_sub"]))
    for name, enr in TEAM:
        story.append(Paragraph(f"{name} &nbsp;&nbsp; (Enrollment No: {enr})", st["cover_stu"]))
    story.append(Spacer(1, 0.22 * inch))
    story.append(Paragraph("Under the Supervision of", st["cover_sub"]))
    story.append(Paragraph(SUPERVISOR, st["cover_sub_bold"]))
    story.append(Spacer(1, 0.25 * inch))
    story.append(Paragraph("Department of Computer Science and Engineering", st["cover_sub_bold"]))
    story.append(Paragraph("SANSKRITI UNIVERSITY, MATHURA, U.P", st["cover_sub_bold"]))
    story.append(Paragraph("November, 2026", st["cover_sub"]))

    # ---- PAGE ii: CERTIFICATE ----
    story.append(NextPageTemplate("front_nohdr"))
    story.append(PageBreak())
    story.append(scaled_image(BANNER_PATH, target_width_in=6.2, max_height_in=1.1))
    story.append(Paragraph("Department of Computer Science &amp; Engineering", st["dept_hdr"]))
    story.append(Paragraph("CERTIFICATE", st["front_h1"]))
    cert_txt = (
        f"This is to certify that the work embodied in this project report entitled "
        f"<b>\u201c{TITLE_TEXT.upper()}\u201d</b> being submitted by <b>Shaik Shafi</b> (Enrollment No: 2302320151), "
        f"<b>Shaik Mohammad Ali</b> (Enrollment No: 2302320119), <b>Shaik Mahamad Yaseen</b> (Enrollment No: 2302320118), "
        f"and <b>Desireddy Ramesh</b> (Enrollment No: 2302320099), for partial fulfillment of the requirement for the award of "
        f"Bachelor of Technology in Computer Science and Engineering to Sanskriti University, Mathura, during the academic "
        f"year 2026\u201327 is a record of a bonafide piece of work, undertaken by them under the supervision of the undersigned."
    )
    story.append(Paragraph(cert_txt, st["body"]))
    story.append(Spacer(1, 0.7 * inch))
    sig_tbl = Table([
        [Paragraph("", st["sig_left"]), Paragraph(f"<b>Approved and Supervised by</b><br/>{SUPERVISOR}<br/>Assistant Professor, SOEIT", st["sig_right"])],
        [Spacer(1, 0.35 * inch), Spacer(1, 0.35 * inch)],
        [Paragraph("", st["sig_left"]), Paragraph("<b>Forwarded by</b><br/>Dean, SOEIT", st["sig_right"])],
    ], colWidths=[3.0 * inch, 3.2 * inch])
    story.append(sig_tbl)

    # ---- PAGE iii: DECLARATION ----
    story.append(PageBreak())
    story.append(scaled_image(BANNER_PATH, target_width_in=6.2, max_height_in=1.1))
    story.append(Paragraph("Department of Computer Science &amp; Engineering", st["dept_hdr"]))
    story.append(Paragraph("DECLARATION", st["front_h1"]))
    decl_txt = (
        f"We, <b>Shaik Shafi</b> (2302320151), <b>Shaik Mohammad Ali</b> (2302320119), "
        f"<b>Shaik Mahamad Yaseen</b> (2302320118), and <b>Desireddy Ramesh</b> (2302320099), students of Bachelor of Technology "
        f"in Computer Science and Engineering, Session: 2026\u201327, Sanskriti University, Mathura, hereby declare that the work "
        f"presented in this project report entitled <b>\u201c{TITLE_TEXT.upper()}\u201d</b> is the outcome of our own bonafide work "
        f"and is correct to the best of our knowledge and this work has been undertaken taking care of Engineering Ethics. "
        f"It contains no material previously published or written by another person nor material which has been accepted for the "
        f"award of any other degree or diploma of the university or any other institute of higher learning, except where due "
        f"acknowledgment has been made in the text."
    )
    story.append(Paragraph(decl_txt, st["body"]))
    story.append(Spacer(1, 0.45 * inch))
    decl_sigs = Table([
        [Paragraph(f"<b>{TEAM[0][0]}</b><br/>Enrollment No: {TEAM[0][1]}", st["sig_left"]),
         Paragraph(f"<b>{TEAM[1][0]}</b><br/>Enrollment No: {TEAM[1][1]}", st["sig_left"])],
        [Spacer(1, 0.25 * inch), Spacer(1, 0.25 * inch)],
        [Paragraph(f"<b>{TEAM[2][0]}</b><br/>Enrollment No: {TEAM[2][1]}", st["sig_left"]),
         Paragraph(f"<b>{TEAM[3][0]}</b><br/>Enrollment No: {TEAM[3][1]}", st["sig_left"])],
        [Spacer(1, 0.25 * inch), Spacer(1, 0.25 * inch)],
        [Paragraph("Date: ____________________", st["sig_left"]), Paragraph("", st["sig_left"])],
    ], colWidths=[3.1 * inch, 3.1 * inch])
    story.append(decl_sigs)

    # ---- PAGE iv: ACKNOWLEDGEMENT ----
    story.append(PageBreak())
    story.append(scaled_image(BANNER_PATH, target_width_in=6.2, max_height_in=1.1))
    story.append(Paragraph("Department of Computer Science &amp; Engineering", st["dept_hdr"]))
    story.append(Paragraph("ACKNOWLEDGEMENT", st["front_h1"]))
    ack1 = (
        f"We would like to express our sincere gratitude to the Hon'ble Chancellor, Hon'ble Chief Executive Officer, "
        f"Hon'ble Vice Chancellor, and Respected Dean, SOEIT, Sanskriti University, Mathura for providing the opportunity and "
        f"a supportive academic environment to successfully complete this project. We extend our heartfelt thanks to our Project "
        f"Supervisor, <b>{SUPERVISOR}</b>, for his valuable guidance, encouragement, and continuous support throughout the development "
        f"of the project titled <b>\u201c{TITLE_TEXT.upper()}.\u201d</b> His suggestions, motivation, and technical review played a "
        f"vital role in the successful completion of this work."
    )
    ack2 = (
        "We also thank the Department of Computer Science & Engineering for providing computing facilities and institutional "
        "encouragement throughout the development lifecycle. Finally, we are deeply grateful to our parents, mentors, and peers "
        "whose constant support enabled us to uphold high engineering and ethical standards."
    )
    story.append(Paragraph(ack1, st["body"]))
    story.append(Paragraph(ack2, st["body"]))
    story.append(Spacer(1, 0.35 * inch))
    for nm, enr in TEAM:
        story.append(Paragraph(f"<b>{nm}</b> ({enr})", st["sig_right"]))

    # ---- PAGES v-vi: TABLE OF CONTENTS ----
    story.append(PageBreak())
    story.append(Paragraph("TABLE OF CONTENTS", st["front_h1"]))
    toc_rows = build_toc_rows(st, prev_pages, chapters)
    story.append(make_grid_table(toc_rows, [5.15 * inch, 1.05 * inch], vpad=2))

    # ---- PAGE vii: LIST OF FIGURES (front_hdr starts here!) ----
    story.append(NextPageTemplate("front_hdr"))
    story.append(PageBreak())
    story.append(SectionMarker("FRONT_START", "LOF", "LIST OF FIGURES", collector))
    story.append(Paragraph("LIST OF FIGURES", st["front_h1"]))
    lof_rows = build_lof_rows(st, prev_pages)
    story.append(make_grid_table(lof_rows, [5.15 * inch, 1.05 * inch], vpad=4))
    story.append(SectionMarker("FRONT_END", "LOF", "LIST OF FIGURES", collector))

    # ---- PAGE viii: ABBREVIATIONS ----
    story.append(PageBreak())
    story.append(SectionMarker("FRONT_START", "ABBR", "ABBREVIATIONS", collector))
    story.append(Paragraph("ABBREVIATIONS", st["front_h1"]))
    abbr_rows = [[Paragraph("Acronym / Term", st["tbl_hdr"]), Paragraph("Expanded Definition & System Context", st["tbl_hdr"])]]
    for k, desc in get_abbreviations():
        abbr_rows.append([Paragraph(f"<b>{k}</b>", st["tbl_cell"]), Paragraph(desc, st["tbl_cell"])])
    story.append(make_grid_table(abbr_rows, [1.45 * inch, 4.75 * inch], vpad=4))
    story.append(SectionMarker("FRONT_END", "ABBR", "ABBREVIATIONS", collector))

    # ---- PAGES ix-x: LIST OF STANDARDS ----
    story.append(PageBreak())
    story.append(SectionMarker("FRONT_START", "STDS", "LIST OF STANDARDS", collector))
    story.append(Paragraph("LIST OF STANDARDS", st["front_h1"]))
    std_rows = [[Paragraph("Standard (Abbreviation)", st["tbl_hdr"]), Paragraph("Publishing Agency", st["tbl_hdr"]), Paragraph("About the Standard", st["tbl_hdr"])]]
    for code, ag, ab in get_standards():
        std_rows.append([Paragraph(f"<b>{code}</b>", st["tbl_cell"]), Paragraph(ag, st["tbl_cell"]), Paragraph(ab, st["tbl_cell"])])
    story.append(make_grid_table(std_rows, [1.45 * inch, 1.25 * inch, 3.50 * inch], vpad=15))
    story.append(SectionMarker("FRONT_END", "STDS", "LIST OF STANDARDS", collector))

    # ---- PAGES xi-xii: ABSTRACT ----
    story.append(PageBreak())
    story.append(SectionMarker("FRONT_START", "ABS", "ABSTRACT", collector))
    story.append(Paragraph("ABSTRACT", st["front_h1"]))
    for p in get_abstract_paragraphs():
        story.append(Paragraph(p, st["body"]))
    story.append(SectionMarker("FRONT_END", "ABS", "ABSTRACT", collector))

    # ---- BODY CHAPTERS 1..6 (Arabic numbering starts at 1!) ----
    story.append(NextPageTemplate("body"))
    story.append(PageBreak())
    story.append(SectionMarker("BODY_START", "BODY", "BODY", collector))

    def emit_table(tbl):
        rows = [[Paragraph(h, st["tbl_hdr"]) for h in tbl["headers"]]]
        for r in tbl["rows"]:
            rows.append([Paragraph(str(c), st["tbl_cell"]) for c in r])
        ncols = len(tbl["headers"])
        total_w = 6.2 * inch
        widths = [total_w / ncols] * ncols
        if ncols == 3:
            widths = [1.85 * inch, 1.85 * inch, 2.50 * inch]
        elif ncols == 4:
            widths = [1.55 * inch, 0.90 * inch, 0.90 * inch, 2.85 * inch]
        elif ncols == 5:
            widths = [1.20 * inch, 1.15 * inch, 1.25 * inch, 1.25 * inch, 1.35 * inch]
        elif ncols == 6:
            widths = [2.45 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch, 0.75 * inch]
        story.append(Spacer(1, 6))
        story.append(Paragraph(tbl["caption"], st["caption"]))
        story.append(make_grid_table(rows, widths))
        story.append(Spacer(1, 10))

    def emit_figure(fig):
        fpath = os.path.join(BASE_DIR, fig["path"])
        story.append(Spacer(1, 8))
        story.append(SectionMarker("FIG", fig["caption"], fig["caption"], collector))
        story.append(scaled_image(fpath, target_width_in=fig.get("width_in", 6.0), max_height_in=7.3))
        story.append(Paragraph(fig["caption"], st["caption"]))

    for idx, ch in enumerate(chapters):
        if idx > 0:
            story.append(PageBreak())
        ch_key = f"CH_{ch['number']}"
        story.append(SectionMarker("CH_START", ch_key, ch["title"], collector))
        story.append(Paragraph(ch["title"], st["ch_title"]))
        for sec in ch["sections"]:
            story.append(SectionMarker("SEC_START", sec["id"], sec["title"], collector))
            story.append(Paragraph(sec["title"], st["h2"]))
            for p in sec["paragraphs"]:
                story.append(Paragraph(p, st["body"]))
            if "figure_inline" in sec:
                emit_figure(sec["figure_inline"])
            if "table" in sec:
                emit_table(sec["table"])
            for sub in sec.get("subsections", []):
                story.append(SectionMarker("SEC_START", sub["id"], sub["title"], collector))
                story.append(Paragraph(sub["title"], st["h3"]))
                for sp in sub["paragraphs"]:
                    story.append(Paragraph(sp, st["body"]))
                if "figure" in sub:
                    emit_figure(sub["figure"])
                if "table" in sub:
                    emit_table(sub["table"])
        story.append(SectionMarker("CH_END", ch_key, ch["title"], collector))

    # ---- REFERENCES ----
    story.append(PageBreak())
    story.append(SectionMarker("FRONT_START" if False else "CH_START", "REFS", "REFERENCES", collector))
    story.append(Paragraph(refs["title"], st["ch_title"]))
    for grp in refs["groups"]:
        story.append(Paragraph(grp["heading"], st["ref_grp"]))
        for item in grp["items"]:
            story.append(Paragraph(item, st["ref_item"]))
    story.append(SectionMarker("CH_END", "REFS", "REFERENCES", collector))

    return story


def run_pdf_pass(out_path, prev_pages, chapters, refs):
    collector = {"starts": {}, "ends": {}, "figs": []}
    W, H = A4
    frame = Frame(68, 56, W - 136, H - 114, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc = ReportDocTemplate(out_path, collector, pagesize=A4)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[frame], onPage=make_onpage("cover", doc)),
        PageTemplate(id="front_nohdr", frames=[frame], onPage=make_onpage("front_nohdr", doc)),
        PageTemplate(id="front_hdr", frames=[frame], onPage=make_onpage("front_hdr", doc)),
        PageTemplate(id="body", frames=[frame], onPage=make_onpage("body", doc)),
    ])
    st = styles_dict()
    story = assemble_pdf_story(st, collector, prev_pages, chapters, refs)
    doc.build(story)
    return collector


# ================= DOCX BUILDER =================
def set_cell_margins_and_borders(table):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
        '</w:tblBorders>'
    )
    tblPr.append(borders)


def add_page_number_field(run, fmt="decimal"):
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)


def set_section_page_format(section, fmt="lowerRoman", start=None):
    sectPr = section._sectPr
    pgNumType = OxmlElement('w:pgNumType')
    pgNumType.set(qn('w:fmt'), fmt)
    if start is not None:
        pgNumType.set(qn('w:start'), str(start))
    sectPr.append(pgNumType)


def build_docx(out_path, page_map, chapters, refs):
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)

    def cfg_sec(sec):
        sec.page_width = Mm(210)
        sec.page_height = Mm(297)
        sec.top_margin = Inches(0.85)
        sec.bottom_margin = Inches(0.85)
        sec.left_margin = Inches(0.95)
        sec.right_margin = Inches(0.95)

    def add_p(text, size=12, bold=False, italic=False, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=8, before=0, spacing=1.5):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = spacing
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        return p

    def add_img(rel_path, width_in=6.0):
        full = os.path.join(BASE_DIR, rel_path) if not os.path.isabs(rel_path) else rel_path
        if os.path.exists(full):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(full, width=Inches(width_in))

    # Section 0: Cover + ii..iv
    sec0 = doc.sections[0]
    cfg_sec(sec0)
    sec0.different_first_page_header_footer = True
    set_section_page_format(sec0, "lowerRoman", start=1)
    fp = sec0.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr = fp.add_run()
    fr.font.name = "Times New Roman"
    fr.font.size = Pt(11)
    add_page_number_field(fr)

    add_p(TITLE_TEXT, size=22, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=16, after=14, spacing=1.15)
    add_p("A PROJECT REPORT", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=8, spacing=1.15)
    add_p("Submitted in partial fulfillment of the award of Degree of", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, after=4, spacing=1.15)
    add_p("Bachelor of Technology in Computer Science and Engineering", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=14, spacing=1.15)
    add_img(LOGO_PATH, width_in=1.65)
    add_p("Submitted by", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, before=10, after=6, spacing=1.15)
    for nm, enr in TEAM:
        add_p(f"{nm}   (Enrollment No: {enr})", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=2, spacing=1.15)
    add_p("Under the Supervision of", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, before=14, after=4, spacing=1.15)
    add_p(SUPERVISOR, size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=14, spacing=1.15)
    add_p("Department of Computer Science and Engineering", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=4, spacing=1.15)
    add_p("SANSKRITI UNIVERSITY, MATHURA, U.P", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=4, spacing=1.15)
    add_p("November, 2026", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, after=4, spacing=1.15)

    # Certificate
    doc.add_page_break()
    add_img(BANNER_PATH, width_in=6.2)
    add_p("Department of Computer Science & Engineering", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=8, after=8, spacing=1.15)
    add_p("CERTIFICATE", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=14, spacing=1.15)
    add_p(
        f"This is to certify that the work embodied in this project report entitled \u201c{TITLE_TEXT.upper()}\u201d "
        f"being submitted by Shaik Shafi (Enrollment No: 2302320151), Shaik Mohammad Ali (Enrollment No: 2302320119), "
        f"Shaik Mahamad Yaseen (Enrollment No: 2302320118), and Desireddy Ramesh (Enrollment No: 2302320099), "
        f"for partial fulfillment of the requirement for the award of Bachelor of Technology in Computer Science and Engineering "
        f"to Sanskriti University, Mathura, during the academic year 2026\u201327 is a record of a bonafide piece of work, "
        f"undertaken by them under the supervision of the undersigned.", size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=24, spacing=1.5
    )
    add_p(f"Approved and Supervised by\n{SUPERVISOR}\nAssistant Professor, SOEIT", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, after=18, spacing=1.25)
    add_p("Forwarded by\nDean, SOEIT", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, after=8, spacing=1.25)

    # Declaration
    doc.add_page_break()
    add_img(BANNER_PATH, width_in=6.2)
    add_p("Department of Computer Science & Engineering", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=8, after=8, spacing=1.15)
    add_p("DECLARATION", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=14, spacing=1.15)
    add_p(
        f"We, Shaik Shafi (2302320151), Shaik Mohammad Ali (2302320119), Shaik Mahamad Yaseen (2302320118), and "
        f"Desireddy Ramesh (2302320099), students of Bachelor of Technology in Computer Science and Engineering, Session: 2026\u201327, "
        f"Sanskriti University, Mathura, hereby declare that the work presented in this project report entitled "
        f"\u201c{TITLE_TEXT.upper()}\u201d is the outcome of our own bonafide work and is correct to the best of our knowledge "
        f"and this work has been undertaken taking care of Engineering Ethics.", size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=18, spacing=1.5
    )
    for nm, enr in TEAM:
        add_p(f"{nm}  (Enrollment No: {enr})", size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, after=4, spacing=1.15)
    add_p("Date: ____________________", size=12, align=WD_ALIGN_PARAGRAPH.LEFT, before=14, after=4)

    # Acknowledgement
    doc.add_page_break()
    add_img(BANNER_PATH, width_in=6.2)
    add_p("Department of Computer Science & Engineering", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=8, after=8, spacing=1.15)
    add_p("ACKNOWLEDGEMENT", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=14, spacing=1.15)
    add_p(
        f"We would like to express our sincere gratitude to the Hon'ble Chancellor, Hon'ble Chief Executive Officer, "
        f"Hon'ble Vice Chancellor, and Respected Dean, SOEIT, Sanskriti University, Mathura for providing the opportunity and a "
        f"supportive academic environment to successfully complete this project. We extend our heartfelt thanks to our Project "
        f"Supervisor, {SUPERVISOR}, for his valuable guidance, encouragement, and continuous support throughout the development "
        f"of the project titled \u201c{TITLE_TEXT.upper()}.\u201d", size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=10, spacing=1.5
    )
    add_p("We are also deeply grateful to the Department of Computer Science & Engineering and our families for their continuous encouragement.", size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=18, spacing=1.5)
    for nm, enr in TEAM:
        add_p(f"{nm} ({enr})", size=11.5, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, after=2, spacing=1.15)

    # TOC
    doc.add_page_break()
    add_p("TABLE OF CONTENTS", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=12)
    starts = page_map["starts"]
    ends = page_map["ends"]

    def rng(key):
        s = starts.get(key, "—")
        e = ends.get(key, s)
        return s if s == e else f"{s} - {e}"

    toc_tbl = doc.add_table(rows=1, cols=2)
    toc_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins_and_borders(toc_tbl)
    toc_tbl.rows[0].cells[0].text = "Topic"
    toc_tbl.rows[0].cells[1].text = "Page No."
    toc_entries = [
        ("LIST OF FIGURES", rng("LOF"), True),
        ("ABBREVIATIONS", rng("ABBR"), True),
        ("LIST OF STANDARDS", rng("STDS"), True),
        ("ABSTRACT", rng("ABS"), True),
    ]
    for ch in chapters:
        toc_entries.append((ch["title"], rng(f"CH_{ch['number']}"), True))
        for sec in ch["sections"]:
            toc_entries.append(("    " + sec["title"], starts.get(sec["id"], "—"), False))
            for sub in sec.get("subsections", []):
                toc_entries.append(("        " + sub["title"], starts.get(sub["id"], "—"), False))
    toc_entries.append(("REFERENCES", rng("REFS"), True))
    for lbl, pno, b in toc_entries:
        row = toc_tbl.add_row()
        p0 = row.cells[0].paragraphs[0]
        r0 = p0.add_run(lbl)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10.5)
        r0.bold = b
        p1 = row.cells[1].paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p1.add_run(pno)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10.5)

    # Section 1: LOF..Abstract with top-left Sanskriti University header + Roman footer starting vii
    sec1 = doc.add_section()
    cfg_sec(sec1)
    sec1.header.is_linked_to_previous = False
    sec1.footer.is_linked_to_previous = False
    set_section_page_format(sec1, "lowerRoman", start=7)
    hp1 = sec1.header.paragraphs[0]
    hp1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    hr1 = hp1.add_run("Sanskriti University, Mathura")
    hr1.font.name = "Times New Roman"
    hr1.font.size = Pt(10.5)
    fp1 = sec1.footer.paragraphs[0]
    fp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr1 = fp1.add_run()
    fr1.font.name = "Times New Roman"
    fr1.font.size = Pt(11)
    add_page_number_field(fr1)

    add_p("LIST OF FIGURES", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=12)
    lof_tbl = doc.add_table(rows=1, cols=2)
    lof_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins_and_borders(lof_tbl)
    lof_tbl.rows[0].cells[0].text = "Figure No."
    lof_tbl.rows[0].cells[1].text = "Page(s)"
    for _, flbl, pno in page_map["figs"]:
        row = lof_tbl.add_row()
        r0 = row.cells[0].paragraphs[0].add_run(flbl)
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10.5)
        row.cells[1].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = row.cells[1].paragraphs[0].add_run(pno)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10.5)

    doc.add_page_break()
    add_p("ABBREVIATIONS", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=12)
    ab_tbl = doc.add_table(rows=1, cols=2)
    ab_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins_and_borders(ab_tbl)
    ab_tbl.rows[0].cells[0].text = "Acronym"
    ab_tbl.rows[0].cells[1].text = "Definition"
    for k, v in get_abbreviations():
        row = ab_tbl.add_row()
        r0 = row.cells[0].paragraphs[0].add_run(k)
        r0.bold = True
        r0.font.name = "Times New Roman"
        r0.font.size = Pt(10.5)
        r1 = row.cells[1].paragraphs[0].add_run(v)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(10.5)

    doc.add_page_break()
    add_p("LIST OF STANDARDS", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=12)
    st_tbl = doc.add_table(rows=1, cols=3)
    st_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_margins_and_borders(st_tbl)
    st_tbl.rows[0].cells[0].text = "Standard (Abbreviation)"
    st_tbl.rows[0].cells[1].text = "Publishing Agency"
    st_tbl.rows[0].cells[2].text = "About the Standard"
    for c0, c1, c2 in get_standards():
        row = st_tbl.add_row()
        for ci, txt in enumerate([c0, c1, c2]):
            r = row.cells[ci].paragraphs[0].add_run(txt)
            r.font.name = "Times New Roman"
            r.font.size = Pt(10.5)
            r.bold = (ci == 0)

    doc.add_page_break()
    add_p("ABSTRACT", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, after=12)
    for p in get_abstract_paragraphs():
        add_p(p, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=10, spacing=1.5)

    # Section 2: Main Body starting Arabic Page 1
    sec2 = doc.add_section()
    cfg_sec(sec2)
    sec2.header.is_linked_to_previous = False
    sec2.footer.is_linked_to_previous = False
    set_section_page_format(sec2, "decimal", start=1)
    hp2 = sec2.header.paragraphs[0]
    hp2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    hr2 = hp2.add_run("Sanskriti University, Mathura")
    hr2.font.name = "Times New Roman"
    hr2.font.size = Pt(10.5)
    fp2 = sec2.footer.paragraphs[0]
    fp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fr2 = fp2.add_run()
    fr2.font.name = "Times New Roman"
    fr2.font.size = Pt(11)
    add_page_number_field(fr2)

    def emit_docx_table(tbl):
        add_p(tbl["caption"], size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=6, after=4, spacing=1.15)
        t = doc.add_table(rows=1, cols=len(tbl["headers"]))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_cell_margins_and_borders(t)
        for j, h in enumerate(tbl["headers"]):
            r = t.rows[0].cells[j].paragraphs[0].add_run(h)
            r.bold = True
            r.font.name = "Times New Roman"
            r.font.size = Pt(10.5)
        for row_data in tbl["rows"]:
            row = t.add_row()
            for j, cell in enumerate(row_data):
                r = row.cells[j].paragraphs[0].add_run(str(cell))
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)
        add_p("", size=6, after=6, spacing=1.0)

    for idx, ch in enumerate(chapters):
        if idx > 0:
            doc.add_page_break()
        add_p(ch["title"], size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=4, after=14, spacing=1.15)
        for sec in ch["sections"]:
            add_p(sec["title"], size=13.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=12, after=6, spacing=1.15)
            for p in sec["paragraphs"]:
                add_p(p, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=10, spacing=1.5)
            if "figure_inline" in sec:
                fig = sec["figure_inline"]
                add_img(fig["path"], width_in=fig.get("width_in", 6.0))
                add_p(fig["caption"], size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=4, after=12, spacing=1.15)
            if "table" in sec:
                emit_docx_table(sec["table"])
            for sub in sec.get("subsections", []):
                add_p(sub["title"], size=12.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=10, after=6, spacing=1.15)
                for sp in sub["paragraphs"]:
                    add_p(sp, size=12, align=WD_ALIGN_PARAGRAPH.JUSTIFY, after=10, spacing=1.5)
                if "figure" in sub:
                    fig = sub["figure"]
                    add_img(fig["path"], width_in=fig.get("width_in", 6.0))
                    add_p(fig["caption"], size=11, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=4, after=12, spacing=1.15)
                if "table" in sub:
                    emit_docx_table(sub["table"])

    doc.add_page_break()
    add_p(refs["title"], size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, before=4, after=14, spacing=1.15)
    for grp in refs["groups"]:
        add_p(grp["heading"], size=12.5, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, before=10, after=6, spacing=1.15)
        for item in grp["items"]:
            add_p(item, size=11.5, align=WD_ALIGN_PARAGRAPH.LEFT, after=6, spacing=1.35)

    doc.save(out_path)


def generate_all():
    chapters = enrich_chapters([get_chapter_1(), get_chapter_2(), get_chapter_3(), get_chapter_4(), get_chapter_5(), get_chapter_6()])
    refs = get_references()

    dummy_prev = {"starts": {}, "ends": {}, "figs": []}
    pass1 = run_pdf_pass(PDF_OUT, dummy_prev, chapters, refs)
    pass2 = run_pdf_pass(PDF_OUT, pass1, chapters, refs)
    # Stabilize if TOC wrapping shifted front pages
    if pass2["starts"] != pass1["starts"]:
        pass2 = run_pdf_pass(PDF_OUT, pass2, chapters, refs)

    build_docx(DOCX_OUT, pass2, chapters, refs)

    for src in (PDF_OUT, DOCX_OUT):
        bn = os.path.basename(src)
        shutil.copy2(src, os.path.join(DOWNLOADS_DIR, bn))
        if os.path.isdir(ARTIFACTS_DIR):
            shutil.copy2(src, os.path.join(ARTIFACTS_DIR, bn))

    print("PDF generated:", PDF_OUT, os.path.getsize(PDF_OUT))
    print("DOCX generated:", DOCX_OUT, os.path.getsize(DOCX_OUT))
    print("Tracked TOC entries:", len(pass2["starts"]), "Figures:", len(pass2["figs"]))


if __name__ == "__main__":
    generate_all()
