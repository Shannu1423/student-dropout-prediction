"""
Sanskriti University B.Tech Project Report HTML Generator
Converts PROJECT_REPORT.md into a beautifully styled, print-ready HTML file (A4 format).
"""
import os
import re
import markdown

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MD_PATH = os.path.join(PROJECT_DIR, "PROJECT_REPORT.md")
HTML_PATH = os.path.join(PROJECT_DIR, "PROJECT_REPORT.html")

def generate_report_html():
    if not os.path.exists(MD_PATH):
        print(f"Error: {MD_PATH} not found.")
        return

    with open(MD_PATH, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Pre-process markdown for clean page breaks and chapter styling
    # Replace horizontal rules or break comments with page break divs if needed
    md_text = re.sub(
        r'<div style="page-break-after:\s*always;"></div>',
        r'<div class="page-break"></div>',
        md_text
    )

    # Convert Markdown to HTML with tables, code fences, and attributes
    md_converter = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'attr_list',
        'def_list',
        'toc'
    ])
    body_html = md_converter.convert(md_text)

    # Academic stylesheet for Sanskriti University guidelines
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI-Based Prediction of Reasons for Student Dropout - Project Report</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {{
    --primary-color: #1a365d;
    --secondary-color: #2b6cb0;
    --accent-color: #c53030;
    --text-color: #2d3748;
    --bg-color: #ffffff;
    --table-border: #cbd5e0;
    --table-header: #edf2f7;
    --code-bg: #f7fafc;
    --code-border: #e2e8f0;
  }}

  * {{
    box-sizing: border-box;
  }}

  body {{
    font-family: 'Times New Roman', Times, 'Crimson Pro', Georgia, serif;
    font-size: 12pt;
    line-height: 1.6;
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
    padding: 30mm 20mm 25mm 30mm; /* Standard Indian thesis margins: 1.25 in left, 1 in others */
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
    padding: 12px 20px;
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
    margin-bottom: 0.6em;
    page-break-after: avoid;
    break-after: avoid;
  }}

  h1 {{
    font-size: 18pt;
    text-transform: uppercase;
    text-align: center;
    border-bottom: 2px solid #2d3748;
    padding-bottom: 8px;
    margin-top: 2em;
    letter-spacing: 0.5px;
  }}

  /* Special chapter title styling */
  h1:has(+ h1), h1 + h1 {{
    margin-top: 0.3em;
    border-bottom: none;
  }}

  h2 {{
    font-size: 14pt;
    font-weight: bold;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
  }}

  h3 {{
    font-size: 12.5pt;
    font-weight: bold;
  }}

  p {{
    margin-top: 0.5em;
    margin-bottom: 0.8em;
    text-indent: 1.5em;
  }}

  p:first-of-type, table + p, ul + p, ol + p, pre + p, .page-break + p {{
    text-indent: 0;
  }}

  /* Tables */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
    break-inside: avoid;
  }}

  th, td {{
    border: 1px solid var(--table-border);
    padding: 8px 10px;
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
    background-color: #fcfcfc;
  }}

  /* Code Blocks & Terminal */
  pre {{
    background-color: var(--code-bg);
    border: 1px solid var(--code-border);
    border-left: 4px solid var(--secondary-color);
    padding: 12px 16px;
    border-radius: 4px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
    font-size: 9.5pt;
    line-height: 1.45;
    page-break-inside: avoid;
    break-inside: avoid;
    margin: 1.2em 0;
  }}

  code {{
    font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
    font-size: 10pt;
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
    margin-top: 0.4em;
    margin-bottom: 0.8em;
    padding-left: 2em;
  }}

  li {{
    margin-bottom: 0.3em;
  }}

  /* Blockquotes & Notes */
  blockquote {{
    border-left: 4px solid #4a5568;
    margin: 1em 0;
    padding: 0.5em 1em;
    color: #4a5568;
    background: #f7fafc;
    font-style: italic;
  }}

  /* Page breaks */
  .page-break {{
    page-break-after: always;
    break-after: page;
    height: 1px;
    margin: 0;
    border: none;
  }}

  hr {{
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 2em 0;
  }}

  /* Print specific rules for generating pristine PDF */
  @media print {{
    body {{
      background: none;
      padding: 0;
      color: #000000;
    }}

    .document-container {{
      width: 100%;
      margin: 0;
      padding: 0;
      box-shadow: none;
      border-radius: 0;
    }}

    .no-print, .control-bar {{
      display: none !important;
    }}

    @page {{
      size: A4 portrait;
      margin: 25mm 20mm 20mm 30mm;
    }}

    a {{
      color: #000000;
      text-decoration: none;
    }}

    pre, table, blockquote {{
      page-break-inside: avoid;
      break-inside: avoid;
    }}

    h1, h2, h3 {{
      page-break-after: avoid;
      break-after: avoid;
    }}

    .page-break {{
      page-break-after: always;
      break-after: page;
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

    print(f"Success: {HTML_PATH} generated successfully.")
    print(f"File size: {os.path.getsize(HTML_PATH)} bytes")

if __name__ == "__main__":
    generate_report_html()
