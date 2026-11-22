"""
Sanskriti University B.Tech Project Report Compiler
Converts PROJECT_REPORT.md into:
1. PROJECT_REPORT.html (Styled, responsive academic web report)
2. PROJECT_REPORT.pdf (Official submission-ready A4 PDF document)
"""
import os
import re
import subprocess
import time
import markdown

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(PROJECT_DIR, "PROJECT_REPORT.md")
HTML_PATH = os.path.join(PROJECT_DIR, "PROJECT_REPORT.html")
PDF_PATH = os.path.join(PROJECT_DIR, "PROJECT_REPORT.pdf")

def build_report():
    if not os.path.exists(MD_PATH):
        print(f"Error: {MD_PATH} not found.")
        return

    with open(MD_PATH, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Normalize existing page breaks
    md_text = re.sub(
        r'<div style="page-break-after:\s*always;"></div>',
        r'<div class="page-break"></div>',
        md_text
    )

    # Ensure clean page breaks before major structural divisions
    page_break_headers = [
        r"(# Department of Computer Science and Engineering &ndash; School of Engineering and Information Technology \(SOEIT\)\s*\n\s*## CERTIFICATE)",
        r"(# Department of Computer Science and Engineering &ndash; School of Engineering and Information Technology \(SOEIT\)\s*\n\s*## DECLARATION)",
        r"(# ACKNOWLEDGEMENT)",
        r"(# ABSTRACT)",
        r"(# TABLE OF CONTENTS)",
        r"(# LIST OF TABLES)",
        r"(# LIST OF FIGURES)",
        r"(# LIST OF ABBREVIATIONS)",
        r"(# CHAPTER \d+)",
        r"(# REFERENCES)",
        r"(# APPENDIX)"
    ]

    for pattern in page_break_headers:
        md_text = re.sub(
            r'(?<!<div class="page-break"></div>\n\n)' + pattern,
            r'<div class="page-break"></div>\n\n\1',
            md_text
        )

    # Convert Markdown to HTML with full academic extensions
    md_converter = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'attr_list',
        'def_list',
        'toc'
    ])
    body_html = md_converter.convert(md_text)

    # Comprehensive academic print stylesheet
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI-Based Prediction of Reasons for Student Dropout - Sanskriti University</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {{
    --primary-color: #1a365d;
    --secondary-color: #2b6cb0;
    --accent-color: #c53030;
    --text-color: #1a202c;
    --bg-color: #ffffff;
    --table-border: #cbd5e0;
    --table-header: #edf2f7;
    --code-bg: #f8fafc;
    --code-border: #e2e8f0;
  }}

  * {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Times New Roman', Times, 'Crimson Pro', Georgia, serif;
    font-size: 12pt;
    line-height: 1.55;
    color: var(--text-color);
    background-color: #e2e8f0;
    margin: 0;
    padding: 20px 0;
    text-align: justify;
  }}

  .document-container {{
    width: 210mm;
    min-height: 297mm;
    margin: 0 auto;
    background: #ffffff;
    padding: 25mm 20mm 20mm 30mm; /* Standard Indian university thesis margins: 30mm left for binding */
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    border-radius: 4px;
    position: relative;
  }}

  /* Floating print control bar */
  .control-bar {{
    position: fixed;
    top: 20px;
    right: 25px;
    z-index: 1000;
    background: #1a202c;
    color: #ffffff;
    padding: 10px 18px;
    border-radius: 50px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    display: flex;
    align-items: center;
    gap: 15px;
  }}

  .control-bar button {{
    background: #3182ce;
    color: #ffffff;
    border: none;
    padding: 8px 16px;
    border-radius: 20px;
    cursor: pointer;
    font-family: sans-serif;
    font-weight: 600;
    font-size: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: background 0.2s;
  }}

  .control-bar button:hover {{
    background: #2b6cb0;
  }}

  .control-bar span {{
    font-family: sans-serif;
    font-size: 13px;
    color: #e2e8f0;
  }}

  /* Typography */
  h1, h2, h3, h4, h5, h6 {{
    font-family: 'Times New Roman', Times, Georgia, serif;
    color: #000000;
    margin-top: 1.4em;
    margin-bottom: 0.5em;
    page-break-after: avoid;
    break-after: avoid;
  }}

  h1 {{
    font-size: 17pt;
    text-transform: uppercase;
    text-align: center;
    border-bottom: 2px solid #2d3748;
    padding-bottom: 6px;
    margin-top: 1.8em;
    letter-spacing: 0.5px;
  }}

  h1:has(+ h1), h1 + h1 {{
    margin-top: 0.2em;
    border-bottom: none;
  }}

  h2 {{
    font-size: 13.5pt;
    font-weight: bold;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
  }}

  h3 {{
    font-size: 12pt;
    font-weight: bold;
  }}

  p {{
    margin-top: 0.4em;
    margin-bottom: 0.7em;
    text-indent: 1.5em;
  }}

  p:first-of-type, table + p, ul + p, ol + p, pre + p, .page-break + p {{
    text-indent: 0;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.2em 0;
    font-size: 10pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  th, td {{
    border: 1px solid var(--table-border);
    padding: 7px 9px;
    text-align: left;
    vertical-align: top;
  }}

  th {{
    background-color: var(--table-header);
    font-weight: bold;
    color: #1a202c;
    text-align: center;
  }}

  tr:nth-child(even) td {{
    background-color: #fafafa;
  }}

  /* Code Blocks & Terminal */
  pre {{
    background-color: var(--code-bg);
    border: 1px solid var(--code-border);
    border-left: 4px solid var(--secondary-color);
    padding: 10px 14px;
    border-radius: 4px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.4;
    page-break-inside: avoid;
    break-inside: avoid;
    margin: 1em 0;
    white-space: pre-wrap;
    word-break: break-word;
  }}

  code {{
    font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
    font-size: 9.5pt;
    background: #edf2f7;
    padding: 2px 4px;
    border-radius: 3px;
    color: #805ad5;
  }}

  pre code {{
    background: transparent;
    padding: 0;
    color: #2d3748;
  }}

  /* Lists */
  ul, ol {{
    margin-top: 0.3em;
    margin-bottom: 0.6em;
    padding-left: 1.8em;
  }}

  li {{
    margin-bottom: 0.25em;
  }}

  /* Page breaks */
  .page-break {{
    page-break-before: always;
    break-before: page;
    height: 0;
    margin: 0;
    border: none;
    display: block;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 1.5em 0;
  }}

  /* Print specific rules for generating pristine PDF */
  @media print {{
    body {{
      background: #ffffff !important;
      padding: 0 !important;
      color: #000000 !important;
      font-size: 11pt !important;
      line-height: 1.45 !important;
    }}

    .document-container {{
      width: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
      box-shadow: none !important;
      border-radius: 0 !important;
    }}

    .no-print, .control-bar {{
      display: none !important;
    }}

    @page {{
      size: A4 portrait;
      margin: 25mm 20mm 20mm 30mm; /* Top 25mm, Right 20mm, Bottom 20mm, Left 30mm for binding */
    }}

    a {{
      color: #000000 !important;
      text-decoration: none !important;
    }}

    pre, table, blockquote {{
      page-break-inside: avoid !important;
      break-inside: avoid !important;
    }}

    h1, h2, h3 {{
      page-break-after: avoid !important;
      break-after: avoid !important;
    }}

    .page-break {{
      page-break-before: always !important;
      break-before: page !important;
      height: 0 !important;
      margin: 0 !important;
      display: block !important;
    }}
  }}
</style>
</head>
<body>

<div class="control-bar no-print">
  <span><i class="fa-solid fa-graduation-cap"></i> Sanskriti University Project Report</span>
  <button onclick="window.print()"><i class="fa-solid fa-file-pdf"></i> Print / Save as PDF</button>
</div>

<div class="document-container">
{body_html}
</div>

</body>
</html>
"""

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"[OK] Generated HTML: {HTML_PATH} ({os.path.getsize(HTML_PATH)} bytes)")

    # Call compile_77_page_report to maintain exact 77 pages
    from compile_77_page_report import build_pdf
    build_pdf()

if __name__ == "__main__":
    build_report()
