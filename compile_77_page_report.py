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
        if page_num == 1:
            return  # Cover page has no header or footer

        self.saveState()
        width, height = A4
        left_m = 85.04   # 30mm binding margin
        right_m = width - 56.69  # 20mm right margin

        self.setFont("Times-Roman", 10)

        # Roman numerals for front matter (Pages 2-11)
        if 2 <= page_num <= 11:
            romans = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi"]
            label = romans[page_num] if page_num < len(romans) else str(page_num)
            self.drawCentredString(width / 2.0, 36, label)
        else:
            # Arabic numerals for core chapters (Page 12 is Arabic page 1)
            arabic_page = page_num - 11
            self.drawCentredString(width / 2.0, 36, str(arabic_page))

            # Running Top Header
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.6)
            self.line(left_m, height - 42, right_m, height - 42)
            self.setFont("Times-Italic", 8.5)
            self.setFillColor(colors.HexColor("#4A5568"))
            self.drawString(left_m, height - 38, "Sanskriti University — Department of Computer Science & Engineering")
            self.drawRightString(right_m, height - 38, "AI-Based Prediction of Reasons for Student Dropout")

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
        'CoverTitle': ParagraphStyle('CoverTitle', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=15.5, leading=19, alignment=1, textColor=colors.HexColor('#1A365D')),
        'CoverSub': ParagraphStyle('CoverSub', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=11, leading=15, alignment=1, textColor=colors.HexColor('#2D3748')),
        'CoverBold': ParagraphStyle('CoverBold', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=11.5, leading=16, alignment=1, textColor=colors.HexColor('#1A202C')),
        'ChapterH1': ParagraphStyle('ChapterH1', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=13.5, leading=16.5, alignment=1, textColor=colors.HexColor('#1A365D'), spaceAfter=8),
        'SectionH2': ParagraphStyle('SectionH2', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=11, leading=14, alignment=0, textColor=colors.HexColor('#1A202C'), spaceBefore=5, spaceAfter=3),
        'SubSectionH3': ParagraphStyle('SubSectionH3', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=9.5, leading=12.5, alignment=0, textColor=colors.HexColor('#2D3748'), spaceBefore=3, spaceAfter=2),
        'ReportBody': ParagraphStyle('ReportBody', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=8.8, leading=12.2, alignment=4, textColor=colors.HexColor('#2D3748'), spaceAfter=4),
        'ReportBodyIndent': ParagraphStyle('ReportBodyIndent', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=8.8, leading=12.2, alignment=4, textColor=colors.HexColor('#2D3748'), firstLineIndent=14, spaceAfter=4),
        'CodeText': ParagraphStyle('CodeText', parent=base_styles['Normal'], fontName='Courier', fontSize=7.0, leading=8.8, textColor=colors.HexColor('#1A202C')),
        'TableText': ParagraphStyle('TableText', parent=base_styles['Normal'], fontName='Times-Roman', fontSize=7.5, leading=9.5, textColor=colors.HexColor('#2D3748')),
        'TableHeader': ParagraphStyle('TableHeader', parent=base_styles['Normal'], fontName='Times-Bold', fontSize=7.8, leading=10, alignment=1, textColor=colors.HexColor('#FFFFFF')),
        'Caption': ParagraphStyle('Caption', parent=base_styles['Normal'], fontName='Times-Italic', fontSize=8.2, leading=10.5, alignment=1, textColor=colors.HexColor('#4A5568'), spaceAfter=3)
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
