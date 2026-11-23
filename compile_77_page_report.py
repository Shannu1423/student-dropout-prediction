"""
Orchestrator to compile and verify the exact 77-page Sanskriti University Project Report.
"""
import os
import pypdf
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, PageBreak, Table, TableStyle, Preformatted, Paragraph
from reportlab.pdfgen import canvas

from page_builder_front import add_front_matter_and_ch1
from page_builder_middle import add_middle_chapters
from page_builder_back import add_back_chapters

PROJECT_DIR = r"C:\Users\ASUS\.gemini\antigravity\scratch\student_dropout_prediction"
LOGO_PATH = os.path.join(PROJECT_DIR, "static", "images", "sanskriti_logo.png")
OUTPUT_PDF = os.path.join(PROJECT_DIR, "PROJECT_REPORT.pdf")

class SanskritiCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, total_pages):
        page_num = self._pageNumber
        width, height = A4

        self.saveState()

        if page_num == 1:
            # Professional institutional double border on Cover Page
            self.setStrokeColor(colors.HexColor("#1A365D"))  # Sanskriti Deep Navy
            self.setLineWidth(1.8)
            self.rect(34, 34, width - 68, height - 68)
            self.setStrokeColor(colors.HexColor("#C5A880"))  # Institutional Gold Accent
            self.setLineWidth(0.7)
            self.rect(38, 38, width - 76, height - 76)
            self.restoreState()
            return

        # Double frame border on all body pages (Pages 2 to 77)
        # Outer primary border
        self.setStrokeColor(colors.HexColor("#1A365D"))
        self.setLineWidth(1.1)
        self.rect(36, 25, width - 72, height - 50)

        # Inner subtle hairline border
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.rect(39, 28, width - 78, height - 56)

        # Header divider line inside the border frame
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.6)
        self.line(39, height - 48, width - 39, height - 48)

        # Running Top Header
        self.setFont("Times-Bold", 8.5)
        self.setFillColor(colors.HexColor("#1A365D"))
        self.drawString(48, height - 42, "SANSKRITI UNIVERSITY")
        self.setFont("Times-Italic", 8.2)
        self.setFillColor(colors.HexColor("#4A5568"))
        self.drawString(162, height - 42, "|   Department of Computer Science & Engineering")
        self.drawRightString(width - 48, height - 42, "AI-Based Prediction of Student Dropout")

        # Footer divider line above page numbering
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.6)
        self.line(39, 46, width - 39, 46)

        # Footer text
        self.setFont("Times-Roman", 8.0)
        self.setFillColor(colors.HexColor("#718096"))
        self.drawString(48, 34, "B.Tech Final Year Major Project Report — 2026")
        self.drawRightString(width - 48, 34, "SOEIT, Sanskriti University")

        # Page numbering
        self.setFont("Times-Bold", 9.0)
        self.setFillColor(colors.HexColor("#1A202C"))
        if 2 <= page_num <= 11:
            romans = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi"]
            label = romans[page_num] if page_num < len(romans) else str(page_num)
            self.drawCentredString(width / 2.0, 34, label)
        else:
            arabic_page = page_num - 11
            self.drawCentredString(width / 2.0, 34, str(arabic_page))

        self.restoreState()

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        leftMargin=85.04,   # 30 mm
        rightMargin=56.69,  # 20 mm
        topMargin=70.87,    # 25 mm
        bottomMargin=70.87  # 25 mm
    )

    usable_width = 595.28 - 85.04 - 56.69  # 453.55 pt

    base_styles = getSampleStyleSheet()

    styles = {
        'CoverTitle': ParagraphStyle('CoverTitle', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=17.0, leading=21, alignment=1, textColor=colors.HexColor('#1A365D')),
        'CoverSub': ParagraphStyle('CoverSub', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=11.5, leading=15.5, alignment=1, textColor=colors.HexColor('#2D3748')),
        'CoverBold': ParagraphStyle('CoverBold', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=12.0, leading=16.5, alignment=1, textColor=colors.HexColor('#1A202C')),
        'ChapterH1': ParagraphStyle('ChapterH1', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=15.0, leading=18.0, alignment=1, textColor=colors.HexColor('#1A365D'), spaceAfter=7),
        'SectionH2': ParagraphStyle('SectionH2', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=12.0, leading=15.0, alignment=0, textColor=colors.HexColor('#1A202C'), spaceBefore=4, spaceAfter=2),
        'SubSectionH3': ParagraphStyle('SubSectionH3', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=10.5, leading=13.5, alignment=0, textColor=colors.HexColor('#2D3748'), spaceBefore=3, spaceAfter=2),
        'ReportBody': ParagraphStyle('ReportBody', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=10.0, leading=13.0, alignment=4, textColor=colors.HexColor('#2D3748'), spaceAfter=3),
        'ReportBodyIndent': ParagraphStyle('ReportBodyIndent', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=10.0, leading=13.0, alignment=4, textColor=colors.HexColor('#2D3748'), firstLineIndent=14, spaceAfter=3),
        'CodeText': ParagraphStyle('CodeText', parent=base_styles['Normal'], fontName='Courier', fontSize=7.2, leading=9.0, textColor=colors.HexColor('#1A202C')),
        'TableText': ParagraphStyle('TableText', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=8.0, leading=10.0, textColor=colors.HexColor('#2D3748')),
        'TableHeader': ParagraphStyle('TableHeader', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=8.5, leading=10.5, alignment=1, textColor=colors.HexColor('#FFFFFF')),
        'Caption': ParagraphStyle('Caption', parent=base_styles['Normal'], fontName='Times-Italic', fontSize=8.8, leading=11.2, alignment=1, textColor=colors.HexColor('#4A5568'), spaceAfter=2)
    }

    def make_table(header_data, rows_data, col_widths, custom_style=None):
        table_content = [[Paragraph(h, styles['TableHeader']) for h in header_data]]
        for row in rows_data:
            table_content.append([Paragraph(str(cell), styles['TableText']) for cell in row])
        t = Table(table_content, colWidths=col_widths)
        default_style = TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1A365D')),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#FFFFFF'), colors.HexColor('#F7FAFC')])
        ])
        t.setStyle(custom_style or default_style)
        return t

    def make_diagram_box(ascii_str):
        p = Preformatted(ascii_str.strip(), styles['CodeText'])
        t = Table([[p]], colWidths=[usable_width])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
            ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#CBD5E0')),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    pages = []
    add_front_matter_and_ch1(pages, styles, LOGO_PATH, usable_width, make_table)
    add_middle_chapters(pages, styles, usable_width, make_table, make_diagram_box)
    add_back_chapters(pages, styles, usable_width, make_table, make_diagram_box)

    print(f"Total page buckets planned: {len(pages)}")

    story = []
    for idx, page_elems in enumerate(pages):
        story.extend(page_elems)
        if idx < len(pages) - 1:
            story.append(PageBreak())

    print("Building PDF...")
    doc.build(story, canvasmaker=SanskritiCanvas)

    reader = pypdf.PdfReader(OUTPUT_PDF)
    actual_pages = len(reader.pages)
    print(f"\n==================================================")
    print(f"Target Pages: 77")
    print(f"Actual Pages Generated: {actual_pages}")
    print(f"File Size: {os.path.getsize(OUTPUT_PDF)} bytes")
    print(f"==================================================")

    if actual_pages == 77:
        print("[SUCCESS] PDF exactly matches 77 pages target!")
    else:
        print(f"[NOTE] Discrepancy detected: {actual_pages} != 77. Adjusting...")

if __name__ == "__main__":
    build_pdf()
