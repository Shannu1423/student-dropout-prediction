"""
Generates crisp high-resolution visual assets matching the Sanskriti University reference report aesthetic:
1. sanskriti_banner.png (Top institutional banner for Certificate, Declaration, Acknowledgement)
2. diag_4_4_1_design_flow.png (End-to-End System Design Flow with diamonds & feedback paths)
3. diag_4_4_2_architecture.png (System Architecture & Role Navigation Flow)
4. diag_4_6_sdlc.png (Iterative Agile SDLC Cycle)
5. diag_4_6_1_usecase.png (4-Tier RBAC Use Case Diagram)
6. diag_4_6_2_closed_loop.png (Closed-Loop Tri-Role Risk & Counselling Flow)
7. diag_4_6_3_sequence.png (UML Sequence Diagram)
8. diag_4_6_4_class.png (UML Class Diagram)
"""
import os
import math
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\Users\ASUS\.gemini\antigravity\scratch\student_dropout_prediction"
LOGO_PATH = os.path.join(BASE_DIR, "static", "images", "sanskriti_logo.png")
OUT_DIR = os.path.join(BASE_DIR, "static", "images", "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

FONT_REG = r"C:\Windows\Fonts\times.ttf"
FONT_BOLD = r"C:\Windows\Fonts\timesbd.ttf"
FONT_SANS = r"C:\Windows\Fonts\arial.ttf"
FONT_SANS_BD = r"C:\Windows\Fonts\arialbd.ttf"

def fnt(path, size):
    return ImageFont.truetype(path, size)

def draw_centered_text(draw, box, text, font, fill="#1A202C", line_spacing=6):
    x0, y0, x1, y1 = box
    lines = text.split("\n")
    heights = []
    widths = []
    for ln in lines:
        bb = draw.textbbox((0, 0), ln, font=font)
        widths.append(bb[2] - bb[0])
        heights.append(bb[3] - bb[1])
    total_h = sum(heights) + line_spacing * max(0, len(lines) - 1)
    cur_y = y0 + ((y1 - y0) - total_h) / 2
    for ln, w, h in zip(lines, widths, heights):
        cur_x = x0 + ((x1 - x0) - w) / 2
        draw.text((cur_x, cur_y), ln, font=font, fill=fill)
        cur_y += h + line_spacing

def draw_arrow(draw, x1, y1, x2, y2, color="#2D3748", width=3, dashed=False, head=11):
    if dashed:
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        steps = max(1, int(dist / 14))
        for i in range(0, steps, 2):
            sx = x1 + dx * (i / steps)
            sy = y1 + dy * (i / steps)
            ex = x1 + dx * (min(i + 1, steps) / steps)
            ey = y1 + dy * (min(i + 1, steps) / steps)
            draw.line([(sx, sy), (ex, ey)], fill=color, width=width)
    else:
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(angle - math.pi / 6), y2 - head * math.sin(angle - math.pi / 6))
    p2 = (x2 - head * math.cos(angle + math.pi / 6), y2 - head * math.sin(angle + math.pi / 6))
    draw.polygon([(x2, y2), p1, p2], fill=color)

def draw_line_seg(draw, x1, y1, x2, y2, color="#2D3748", width=3, dashed=False):
    if dashed:
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        steps = max(1, int(dist / 14))
        for i in range(0, steps, 2):
            sx = x1 + dx * (i / steps)
            sy = y1 + dy * (i / steps)
            ex = x1 + dx * (min(i + 1, steps) / steps)
            ey = y1 + dy * (min(i + 1, steps) / steps)
            draw.line([(sx, sy), (ex, ey)], fill=color, width=width)
    else:
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)

def build_banner():
    W, H = 900, 175
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    if os.path.exists(LOGO_PATH):
        logo = Image.open(LOGO_PATH).convert("RGB").resize((175, 138), Image.Resampling.LANCZOS)
        im.paste(logo, (60, 18))
    d.text((262, 22), "SANSKRITI", font=fnt(FONT_REG, 56), fill="#263B5E")
    d.text((265, 86), "UNIVERSITY", font=fnt(FONT_REG, 33), fill="#263B5E")
    d.line([(265, 128), (745, 128)], fill="#C5A880", width=3)
    d.text((312, 136), "FOR EXCELLENCE IN LIFE", font=fnt(FONT_REG, 21), fill="#263B5E")
    out = os.path.join(OUT_DIR, "sanskriti_banner.png")
    im.save(out, quality=95)
    return out

def build_design_flow():
    W, H = 1600, 1850
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((430, 26), "Student Dropout AI: End-to-End System Design Flow", font=fnt(FONT_SANS_BD, 28), fill="#1A202C")
    d.line([(160, 74), (1440, 74)], fill="#718096", width=2)

    # Start pill
    d.rounded_rectangle([470, 100, 1130, 170], radius=35, fill="#1E3A2F", outline="#1E3A2F")
    draw_centered_text(d, (470, 100, 1130, 170), "START: Institutional User Accesses Portal", fnt(FONT_SANS_BD, 22), "#FFFFFF")
    draw_arrow(d, 800, 170, 800, 215, "#2D3748", 3)

    # Login Box
    d.rounded_rectangle([380, 215, 1220, 300], radius=14, fill="#E2F0E8", outline="#2F855A", width=3)
    draw_centered_text(d, (380, 215, 1220, 300), "PBKDF2 Authentication & 4-Tier RBAC Session Verification\n(Admin  |  Guide / HOD  |  Faculty Mentor  |  Student)", fnt(FONT_SANS, 20), "#1A202C")

    # Branch lines to 3 horizontal role portals (plus student self view note)
    d.line([(800, 300), (800, 330)], fill="#2D3748", width=3)
    d.line([(330, 330), (1320, 330)], fill="#2D3748", width=3)
    draw_arrow(d, 330, 330, 330, 365, "#2D3748", 3)
    draw_arrow(d, 960, 330, 960, 365, "#2D3748", 3)
    draw_arrow(d, 1320, 330, 1320, 365, "#2D3748", 3)

    # 3 Portals
    d.rounded_rectangle([140, 365, 520, 445], radius=14, fill="#C6F6D5", outline="#2F855A", width=3)
    draw_centered_text(d, (140, 365, 520, 445), "Admin / HOD Portal\n(Cohort Upload & Policy)", fnt(FONT_SANS_BD, 19), "#1A202C")

    d.rounded_rectangle([760, 365, 1140, 445], radius=14, fill="#BEE3F8", outline="#2B6CB0", width=3)
    draw_centered_text(d, (760, 365, 1140, 445), "Mentor Workbench\n(Counselling Triage)", fnt(FONT_SANS_BD, 19), "#1A202C")

    d.rounded_rectangle([1170, 365, 1480, 445], radius=14, fill="#E9D8FD", outline="#6B46C1", width=3)
    draw_centered_text(d, (1170, 365, 1480, 445), "Student Portal\n(Isolated Self-Card)", fnt(FONT_SANS_BD, 19), "#1A202C")

    draw_arrow(d, 330, 445, 330, 495, "#2D3748", 3)

    # Upload Box
    d.rounded_rectangle([130, 495, 550, 585], radius=14, fill="#E6FFFA", outline="#2C7A7B", width=3)
    draw_centered_text(d, (130, 495, 550, 585), "Single Student Form or Bulk CSV Roster\n(Attendance, Marks, Backlogs, Fees, LMS)", fnt(FONT_SANS, 18), "#1A202C")
    draw_arrow(d, 340, 585, 340, 635, "#2D3748", 3)

    # Diamond 1: Schema Validation & Alias Map
    pts1 = [(340, 635), (530, 725), (340, 815), (150, 725)]
    d.polygon(pts1, fill="#FEFCBF", outline="#B7791F", width=3)
    draw_centered_text(d, (210, 665, 470, 785), "Header Alias Map\n& Range Check\nPass?", fnt(FONT_SANS_BD, 18), "#744210")

    # Fail branch to right
    draw_arrow(d, 530, 725, 680, 725, "#C53030", 3)
    d.text((555, 698), "No (Invalid)", font=fnt(FONT_SANS_BD, 16), fill="#C53030")
    d.rounded_rectangle([680, 675, 1080, 775], radius=14, fill="#FED7D7", outline="#C53030", width=3)
    draw_centered_text(d, (680, 675, 1080, 775), "Reject Malformed Row & Prompt\nUser to Fix CSV / Input Fields", fnt(FONT_SANS, 18), "#742A2A")
    draw_line_seg(d, 880, 675, 880, 540, "#C53030", 2, dashed=True)
    draw_arrow(d, 880, 540, 550, 540, "#C53030", 2, dashed=True)

    # Pass down
    draw_arrow(d, 340, 815, 340, 870, "#2F855A", 3)
    d.text((352, 830), "Yes (Valid)", font=fnt(FONT_SANS_BD, 16), fill="#2F855A")

    # ML Inference Box
    d.rounded_rectangle([120, 870, 580, 965], radius=14, fill="#EBF8FF", outline="#2B6CB0", width=3)
    draw_centered_text(d, (120, 870, 580, 965), "ML Inference Micro-Pipeline (ml_engine.py)\nStandardScaler + OneHotEncoder + 120-Tree RF", fnt(FONT_SANS, 18), "#1A202C")
    draw_arrow(d, 350, 965, 350, 1015, "#2D3748", 3)

    # XAI Attribution Box
    d.rounded_rectangle([120, 1015, 580, 1110], radius=14, fill="#E6FFFA", outline="#2C7A7B", width=3)
    draw_centered_text(d, (120, 1015, 580, 1110), "Gini Feature-Deficit XAI Attribution Engine\nCompute Weighted Reasons Summing to 100%", fnt(FONT_SANS, 18), "#1A202C")
    draw_arrow(d, 350, 1110, 350, 1165, "#2D3748", 3)

    # Diamond 2: Risk >= Threshold?
    pts2 = [(350, 1165), (540, 1265), (350, 1365), (160, 1265)]
    d.polygon(pts2, fill="#FEFCBF", outline="#B7791F", width=3)
    draw_centered_text(d, (215, 1200, 485, 1330), "Risk >= Threshold\nOR Active\nDeficit >= Limit?", fnt(FONT_SANS_BD, 17), "#744210")

    # Yes -> Right to Counselling Hub Queue
    draw_arrow(d, 540, 1265, 700, 1265, "#2B6CB0", 3)
    d.text((575, 1238), "Yes (At Risk)", font=fnt(FONT_SANS_BD, 16), fill="#2B6CB0")
    d.rounded_rectangle([700, 1215, 1160, 1315], radius=14, fill="#BEE3F8", outline="#2B6CB0", width=3)
    draw_centered_text(d, (700, 1215, 1160, 1315), "Route to At-Risk Queue & Check\n5-Stage Capacity Limit Meters", fnt(FONT_SANS, 18), "#1A202C")
    draw_arrow(d, 930, 1315, 930, 1375, "#2B6CB0", 3)

    d.rounded_rectangle([700, 1375, 1160, 1465], radius=14, fill="#BEE3F8", outline="#2B6CB0", width=3)
    draw_centered_text(d, (700, 1375, 1160, 1465), "Mentor Logs Session Notes,\nAction Plan & Advances Stage", fnt(FONT_SANS, 18), "#1A202C")

    # No -> Down to Low Risk Baseline
    draw_arrow(d, 350, 1365, 350, 1425, "#2F855A", 3)
    d.text((295, 1380), "No", font=fnt(FONT_SANS_BD, 16), fill="#2F855A")
    d.rounded_rectangle([140, 1425, 560, 1505], radius=14, fill="#C6F6D5", outline="#2F855A", width=3)
    draw_centered_text(d, (140, 1425, 560, 1505), "Classify Low Risk Baseline\n& Update Student Scorecard", fnt(FONT_SANS, 18), "#1A202C")

    # Convergence to Persistence + Audit Log
    draw_line_seg(d, 350, 1505, 350, 1560, "#2D3748", 3)
    draw_line_seg(d, 930, 1465, 930, 1560, "#2D3748", 3)
    draw_line_seg(d, 350, 1560, 930, 1560, "#2D3748", 3)
    draw_arrow(d, 640, 1560, 640, 1595, "#2D3748", 3)

    # Dashed links from Mentor & Student portals cleanly down to Queue & DB
    draw_line_seg(d, 1110, 445, 1110, 1215, "#718096", 2, dashed=True)
    draw_arrow(d, 1110, 1190, 1110, 1215, "#718096", 2, dashed=True)
    draw_line_seg(d, 1325, 445, 1325, 1635, "#718096", 2, dashed=True)
    draw_arrow(d, 1325, 1635, 1180, 1635, "#718096", 2, dashed=True)

    d.rounded_rectangle([140, 1595, 1180, 1675], radius=14, fill="#E2F0E8", outline="#2F855A", width=3)
    draw_centered_text(d, (140, 1595, 1180, 1675), "Persist Student State, CounsellingCase & Forensic AuditLog inside SQLite Database", fnt(FONT_SANS_BD, 19), "#1A202C")
    draw_arrow(d, 660, 1675, 660, 1715, "#2D3748", 3)

    d.rounded_rectangle([140, 1715, 1180, 1785], radius=14, fill="#E9D8FD", outline="#6B46C1", width=3)
    draw_centered_text(d, (140, 1715, 1180, 1785), "Update Chart.js Dashboards, Escalation Alerts & Exportable Reports", fnt(FONT_SANS_BD, 19), "#1A202C")
    draw_arrow(d, 660, 1785, 660, 1810, "#2D3748", 3)

    d.rounded_rectangle([460, 1805, 860, 1842], radius=18, fill="#1E3A2F")
    draw_centered_text(d, (460, 1805, 860, 1842), "END", fnt(FONT_SANS_BD, 18), "#FFFFFF")

    out = os.path.join(OUT_DIR, "diag_4_4_1_design_flow.png")
    im.save(out, quality=95)
    return out

def build_architecture_nav():
    W, H = 1600, 1120
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((340, 26), "Student Dropout System: 3-Tier Architecture & Role Navigation Flow", font=fnt(FONT_SANS_BD, 28), fill="#1A202C")
    d.line([(90, 74), (1510, 74)], fill="#718096", width=2)

    # Top User Tier
    d.rounded_rectangle([80, 95, 1520, 235], radius=16, fill="#EDF2F7", outline="#2D3748", width=3)
    d.rounded_rectangle([95, 110, 1505, 165], radius=10, fill="#1E3A2F")
    draw_centered_text(d, (95, 110, 1505, 165), "FOUR-TIER ROLE-BASED ACCESS CONTROL (RBAC) USERS", fnt(FONT_SANS_BD, 21), "#FFFFFF")
    draw_centered_text(d, (95, 172, 1505, 225), "Admin: Thresholds, Retrain & Audit  |  Guide/HOD: Cohort Burden & CSV  |  Mentor: 5-Stage Cases & XAI  |  Student: Isolated Profile", fnt(FONT_SANS, 19), "#1A202C")

    draw_arrow(d, 800, 235, 800, 290, "#2D3748", 3)
    draw_arrow(d, 800, 290, 800, 235, "#2D3748", 3)
    d.text((818, 248), "Browser HTTP / Session Navigation", font=fnt(FONT_SANS, 16), fill="#2D3748")

    # Presentation & Orchestration middle row
    d.rounded_rectangle([80, 290, 680, 560], radius=16, fill="#EBF8FF", outline="#2B6CB0", width=3)
    d.rounded_rectangle([95, 305, 665, 360], radius=10, fill="#2B6CB0")
    draw_centered_text(d, (95, 305, 665, 360), "PRESENTATION TIER (Jinja2 + Bootstrap 5)", fnt(FONT_SANS_BD, 20), "#FFFFFF")
    draw_centered_text(d, (105, 375, 655, 545), "• Responsive Role Dashboards & Directory Filters\n• Chart.js Risk Donut & Dept Burden Bars\n• 5-Stage Queue Capacity Progress Meters\n• XAI Deficit Breakdown Cards (Sum = 100%)\n• Bulk CSV Modal & Admin Threshold Sliders", fnt(FONT_SANS, 18), "#1A202C")

    d.rounded_rectangle([880, 290, 1520, 560], radius=16, fill="#E6FFFA", outline="#2F855A", width=3)
    d.rounded_rectangle([895, 305, 1505, 360], radius=10, fill="#2F855A")
    draw_centered_text(d, (895, 305, 1505, 360), "APPLICATION GATEWAY (Flask + Werkzeug)", fnt(FONT_SANS_BD, 20), "#FFFFFF")
    draw_centered_text(d, (905, 375, 1495, 545), "• PBKDF2-SHA256 Auth & Signed Cookies\n• @roles_required & HTTP 403 Peer Guards\n• Dictionary Header-Alias CSV Normalizer\n• Escalation Scanner & Lifecycle Router\n• Tamper-Evident Audit Event Logger", fnt(FONT_SANS, 18), "#1A202C")

    # Bidirectional arrow between Presentation & Flask
    draw_arrow(d, 680, 425, 880, 425, "#2D3748", 3)
    draw_arrow(d, 880, 425, 680, 425, "#2D3748", 3)
    d.rounded_rectangle([700, 380, 860, 470], radius=8, fill="#FFFFFF", outline="#CBD5E0", width=2)
    draw_centered_text(d, (700, 380, 860, 470), "REST / HTML\n& JSON APIs", fnt(FONT_SANS_BD, 16), "#2D3748")

    # Lower 3 boxes
    draw_line_seg(d, 1200, 560, 1200, 620, "#2D3748", 3)
    draw_line_seg(d, 280, 620, 1340, 620, "#2D3748", 3)
    draw_arrow(d, 280, 620, 280, 675, "#2D3748", 3)
    draw_arrow(d, 800, 620, 800, 675, "#2D3748", 3)
    draw_arrow(d, 1340, 620, 1340, 675, "#2D3748", 3)

    # Box L: AI & XAI Engine
    d.rounded_rectangle([80, 675, 520, 1020], radius=16, fill="#FEFCBF", outline="#B7791F", width=3)
    d.rounded_rectangle([95, 690, 505, 745], radius=10, fill="#B7791F")
    draw_centered_text(d, (95, 690, 505, 745), "ML & XAI ENGINE (ml_engine.py)", fnt(FONT_SANS_BD, 19), "#FFFFFF")
    draw_centered_text(d, (105, 760, 495, 1005), "• ColumnTransformer Pipeline\n• StandardScaler + OneHotEncoder\n• 120-Tree Random Forest Classifier\n• Logistic Regression Benchmark\n• Gini Deficit XAI Scorer (100%)\n• On-Demand Labeled CSV Retrain", fnt(FONT_SANS, 18), "#1A202C")

    # Box M: Persistence Tier
    d.rounded_rectangle([570, 675, 1030, 1020], radius=16, fill="#E9D8FD", outline="#6B46C1", width=3)
    d.rounded_rectangle([585, 690, 1015, 745], radius=10, fill="#6B46C1")
    draw_centered_text(d, (585, 690, 1015, 745), "PERSISTENCE TIER (SQLite + ORM)", fnt(FONT_SANS_BD, 19), "#FFFFFF")
    draw_centered_text(d, (595, 760, 1005, 1005), "• Users & Salted Credentials\n• 115+ Student Academic Records\n• CounsellingCases & Remarks\n• AuditLogs (IP & UTC Timestamps)\n• SystemSettings & Stage Quotas\n• Notifications & Alert Queue", fnt(FONT_SANS, 18), "#1A202C")

    # Box R: Artifacts & Cross-Platform Deployment
    d.rounded_rectangle([1080, 675, 1520, 1020], radius=16, fill="#E6FFFA", outline="#2C7A7B", width=3)
    d.rounded_rectangle([1095, 690, 1505, 745], radius=10, fill="#2C7A7B")
    draw_centered_text(d, (1095, 690, 1505, 745), "STORAGE & HOST RUNTIME", fnt(FONT_SANS_BD, 19), "#FFFFFF")
    draw_centered_text(d, (1105, 760, 1495, 1005), "• models/dropout_models.pkl\n• data/dropout_system.db\n• data/uploads/ CSV Archive\n• Cross-Platform Python .venv\n• Windows & macOS Local Host\n• Automated 8-Test Suite", fnt(FONT_SANS, 18), "#1A202C")

    out = os.path.join(OUT_DIR, "diag_4_4_2_architecture.png")
    im.save(out, quality=95)
    return out

def build_sdlc():
    W, H = 1600, 980
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((380, 26), "Student Dropout AI: Iterative Software Development Life Cycle", font=fnt(FONT_SANS_BD, 28), fill="#1A202C")
    d.line([(90, 74), (1510, 74)], fill="#718096", width=2)

    # Center circle
    cx, cy = 800, 520
    d.ellipse([cx - 170, cy - 170, cx + 170, cy + 170], fill="#1E3A2F")
    draw_centered_text(d, (cx - 160, cy - 160, cx + 160, cy + 160), "Student Dropout\nAgile SDLC\n\nExplainable\nRetention Loop", fnt(FONT_SANS_BD, 23), "#FFFFFF")

    phases = [
        (550, 115, 1050, 240, "#E2F0E8", "#2F855A", "1. Requirement Analysis\nFaculty Surveys, AISHE/NEP Policy\n& Institutional Risk Rules"),
        (1090, 280, 1520, 410, "#EBF8FF", "#2B6CB0", "2. System & Schema Design\n3-Tier Flask Blueprints, 3NF ORM,\nUML Flows & RBAC Guards"),
        (1090, 620, 1520, 750, "#FEFCBF", "#B7791F", "3. ML, XAI & Full-Stack Build\n120-Tree RF, Gini Deficits, CSV Aliasing\n& 5-Stage Lifecycle Hub"),
        (550, 795, 1050, 925, "#E9D8FD", "#6B46C1", "4. Validation & Testing\n8-Suite test_app.py, HTTP 403 Privacy\n& Empirical ROC-AUC Benchmarks"),
        (80, 620, 510, 750, "#E6FFFA", "#2C7A7B", "5. Cross-Platform Packaging\nWindows & macOS .venv Setup,\nGitHub Sync & Offline SQLite"),
        (80, 280, 510, 410, "#FED7D7", "#C53030", "6. Monitoring & Calibration\nSupervisor Reviews, Threshold Tuning\n& On-Demand Retraining")
    ]
    for x0, y0, x1, y1, bg, bd, txt in phases:
        d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=bg, outline=bd, width=3)
        draw_centered_text(d, (x0, y0, x1, y1), txt, fnt(FONT_SANS_BD, 18), "#1A202C")

    # Cycle arrows
    draw_arrow(d, 1050, 178, 1260, 280, "#2D3748", 3)
    draw_arrow(d, 1305, 410, 1305, 620, "#2D3748", 3)
    draw_arrow(d, 1260, 750, 1050, 860, "#2D3748", 3)
    draw_arrow(d, 550, 860, 340, 750, "#2D3748", 3)
    draw_arrow(d, 295, 620, 295, 410, "#2D3748", 3)
    draw_arrow(d, 340, 280, 550, 178, "#2D3748", 3)

    out = os.path.join(OUT_DIR, "diag_4_6_sdlc.png")
    im.save(out, quality=95)
    return out

def draw_stick_actor(d, cx, cy, label, color="#2D3748"):
    d.ellipse([cx - 22, cy - 75, cx + 22, cy - 31], outline=color, width=3)
    d.line([(cx, cy - 31), (cx, cy + 20)], fill=color, width=3)
    d.line([(cx - 30, cy - 12), (cx + 30, cy - 12)], fill=color, width=3)
    d.line([(cx, cy + 20), (cx - 22, cy + 62)], fill=color, width=3)
    d.line([(cx, cy + 20), (cx + 22, cy + 62)], fill=color, width=3)
    draw_centered_text(d, (cx - 95, cy + 68, cx + 95, cy + 125), label, fnt(FONT_SANS_BD, 17), "#1A202C")

def build_use_case():
    W, H = 1600, 1050
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((480, 26), "Student Dropout Platform: 4-Tier Use Case Diagram", font=fnt(FONT_SANS_BD, 28), fill="#1A202C")
    d.line([(90, 74), (1510, 74)], fill="#718096", width=2)

    # System boundary
    d.rectangle([340, 95, 1260, 995], outline="#2D3748", width=3, fill="#FAFAFA")
    d.text((545, 108), "SYSTEM BOUNDARY: DROPOUT PREDICTION PLATFORM", font=fnt(FONT_SANS_BD, 20), fill="#1A202C")

    # Actors
    draw_stick_actor(d, 160, 320, "Admin / HOD\n(Authority)", "#2B6CB0")
    draw_stick_actor(d, 160, 730, "Student\n(Self-View)", "#2F855A")
    draw_stick_actor(d, 1440, 420, "Faculty\nMentor", "#6B46C1")
    draw_stick_actor(d, 1440, 800, "ML & XAI\nEngine", "#B7791F")

    usecases = [
        (430, 165, 840, 255, "#E2F0E8", "#2F855A", "Authenticate & Role Dispatch\n(PBKDF2 Session Security)"),
        (880, 165, 1220, 255, "#FEFCBF", "#B7791F", "Configure Policy Rules\n& Stage Capacity Quotas"),
        (430, 290, 840, 385, "#E2F0E8", "#2F855A", "Register Student or Upload\nBulk Cohort CSV (Alias Map)"),
        (430, 425, 840, 520, "#EBF8FF", "#2B6CB0", "Inspect Cohort KPI Charts &\nDepartment Risk Burden"),
        (860, 425, 1220, 520, "#FEFCBF", "#B7791F", "Run 120-Tree RF Inference\n& Gini XAI Attribution (100%)"),
        (430, 560, 840, 655, "#EBF8FF", "#2B6CB0", "Assign Mentors & Escalate\nStalled High-Risk Alerts"),
        (860, 560, 1220, 655, "#E9D8FD", "#6B46C1", "Log Counselling Session &\nAdvance 5-Stage Hub"),
        (430, 700, 840, 795, "#E2F0E8", "#2F855A", "View Own Academic Standing\n& Prescribed Mentor Advice"),
        (430, 840, 840, 935, "#E9D8FD", "#6B46C1", "Inspect Immutable Forensic\nAudit Trail & IP Logs"),
        (860, 840, 1220, 935, "#FED7D7", "#C53030", "Trigger On-Demand Model\nRetraining on Ground Truth")
    ]
    for x0, y0, x1, y1, bg, bd, txt in usecases:
        d.ellipse([x0, y0, x1, y1], fill=bg, outline=bd, width=3)
        draw_centered_text(d, (x0, y0, x1, y1), txt, fnt(FONT_SANS, 16), "#1A202C")

    # Associations
    for py in [210, 338, 472, 608, 888]:
        d.line([(200, 310), (430, py)], fill="#2B6CB0", width=2)
    d.line([(200, 295), (370, 145), (1050, 145), (1050, 165)], fill="#2B6CB0", width=2)
    d.line([(200, 720), (430, 210)], fill="#2F855A", width=2)
    d.line([(200, 720), (430, 748)], fill="#2F855A", width=2)

    for py in [210, 472, 608]:
        d.line([(1395, 410), (1220, py)], fill="#6B46C1", width=2)
    d.line([(1395, 790), (1220, 472)], fill="#B7791F", width=2)
    d.line([(1395, 790), (1220, 888)], fill="#B7791F", width=2)

    draw_arrow(d, 840, 338, 860, 468, "#B7791F", 2, dashed=True)
    d.text((740, 392), "<<include>>", font=fnt(FONT_SANS_BD, 14), fill="#B7791F")

    out = os.path.join(OUT_DIR, "diag_4_6_1_usecase.png")
    im.save(out, quality=95)
    return out

def build_closed_loop():
    W, H = 1600, 1080
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((400, 26), "Four-Tier Closed-Loop Student Retention Interaction Flow", font=fnt(FONT_SANS_BD, 28), fill="#1A202C")
    d.line([(90, 74), (1510, 74)], fill="#718096", width=2)

    d.rounded_rectangle([380, 105, 1220, 215], radius=16, fill="#E2F0E8", outline="#2F855A", width=3)
    draw_centered_text(d, (380, 105, 1220, 215), "1. Cohort Data Ingestion (Admin / HOD)\nSingle Registration Form or Bulk CSV Upload (Attendance, Marks, Backlogs, Fees, LMS)", fnt(FONT_SANS_BD, 19), "#1A202C")
    draw_arrow(d, 800, 215, 800, 265, "#2D3748", 3)

    d.rounded_rectangle([380, 265, 1220, 375], radius=16, fill="#FEFCBF", outline="#B7791F", width=3)
    draw_centered_text(d, (380, 265, 1220, 375), "2. Predictive ML & XAI Attribution Engine\n120-Tree Random Forest Probability + Normalized Gini Deficit Cards (Sum = 100%)", fnt(FONT_SANS_BD, 19), "#1A202C")
    draw_arrow(d, 800, 375, 800, 425, "#2D3748", 3)

    pts = [(800, 425), (1050, 535), (800, 645), (550, 535)]
    d.polygon(pts, fill="#FEF3C7", outline="#B7791F", width=3)
    draw_centered_text(d, (640, 470, 960, 600), "Risk >= Cutoff\nOR Deficit Breach?", fnt(FONT_SANS_BD, 19), "#744210")

    # Left branch Low Risk
    draw_line_seg(d, 550, 535, 360, 535, "#2F855A", 3)
    draw_arrow(d, 360, 535, 360, 665, "#2F855A", 3)
    d.text((440, 505), "No (Low Risk)", font=fnt(FONT_SANS_BD, 17), fill="#2F855A")
    d.rounded_rectangle([140, 665, 620, 785], radius=16, fill="#C6F6D5", outline="#2F855A", width=3)
    draw_centered_text(d, (140, 665, 620, 785), "3A. Student Self-Portal View\nLow-Risk Standing & Preventative Tips", fnt(FONT_SANS_BD, 18), "#1A202C")

    # Right branch Flagged At Risk
    draw_line_seg(d, 1050, 535, 1240, 535, "#C53030", 3)
    draw_arrow(d, 1240, 535, 1240, 665, "#C53030", 3)
    d.text((1095, 505), "Yes (Flagged)", font=fnt(FONT_SANS_BD, 17), fill="#C53030")
    d.rounded_rectangle([980, 665, 1480, 785], radius=16, fill="#BEE3F8", outline="#2B6CB0", width=3)
    draw_centered_text(d, (980, 665, 1480, 785), "3B. Faculty Mentor Workbench\n5-Stage Triage, Capacity Check & Remarks", fnt(FONT_SANS_BD, 18), "#1A202C")

    # Bottom hub
    draw_arrow(d, 380, 785, 520, 885, "#2D3748", 3)
    draw_arrow(d, 1230, 785, 1080, 885, "#2D3748", 3)
    d.rounded_rectangle([380, 885, 1220, 1005], radius=16, fill="#E9D8FD", outline="#6B46C1", width=3)
    draw_centered_text(d, (380, 885, 1220, 1005), "4. SQLite Persistence, Analytics & Feedback Governance\nStage Queue Alerts  |  Dynamic Policy Re-Scoring  |  Forensic Audit Logs", fnt(FONT_SANS_BD, 19), "#1A202C")

    # Feedback arrow back to step 1
    draw_line_seg(d, 380, 945, 90, 945, "#6B46C1", 2, dashed=True)
    draw_line_seg(d, 90, 945, 90, 160, "#6B46C1", 2, dashed=True)
    draw_arrow(d, 90, 160, 380, 160, "#6B46C1", 2, dashed=True)
    d.rounded_rectangle([30, 470, 170, 540], radius=8, fill="#FFFFFF", outline="#6B46C1", width=2)
    draw_centered_text(d, (30, 470, 170, 540), "Re-Score &\nRetrain Loop", fnt(FONT_SANS_BD, 15), "#553C9A")

    out = os.path.join(OUT_DIR, "diag_4_6_2_closed_loop.png")
    im.save(out, quality=95)
    return out

def build_sequence():
    W, H = 1600, 1050
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((340, 26), "UML Sequence Diagram: Cohort Upload, Scoring & Counselling Workflow", font=fnt(FONT_SANS_BD, 26), fill="#1A202C")
    d.line([(90, 74), (1510, 74)], fill="#718096", width=2)

    actors = [
        (140, "#1E3A2F", "Admin / HOD\n(Browser)"),
        (390, "#2B6CB0", "Flask Web\nRouter"),
        (650, "#B7791F", "ML & XAI\nEngine"),
        (920, "#2F855A", "SQLite ORM\nDatabase"),
        (1185, "#6B46C1", "Counselling\nHub Queue"),
        (1445, "#2C7A7B", "Audit & Alert\nService")
    ]
    for cx, col, lbl in actors:
        d.rounded_rectangle([cx - 90, 95, cx + 90, 165], radius=10, fill=col)
        draw_centered_text(d, (cx - 90, 95, cx + 90, 165), lbl, fnt(FONT_SANS_BD, 15), "#FFFFFF")
        draw_line_seg(d, cx, 165, cx, 980, "#718096", 2, dashed=True)

    # Activation bars
    for cx, y0, y1, col in [(390, 215, 935, "#EBF8FF"), (650, 345, 540, "#FEFCBF"), (920, 575, 705, "#E2F0E8"), (1185, 735, 885, "#E9D8FD")]:
        d.rectangle([cx - 12, y0, cx + 12, y1], fill=col, outline="#4A5568", width=2)

    msgs = [
        (222, 140, 378, False, "#2B6CB0", "1. Authenticate & Submit Form / CSV"),
        (272, 390, 390, False, "#2B6CB0", "2. Map Header Aliases & Check RBAC"),
        (355, 402, 638, False, "#B7791F", "3. Run StandardScaler + 120-Tree RF"),
        (415, 650, 650, False, "#B7791F", "4. Compute Gini Deficit Cards (100%)"),
        (510, 638, 402, True, "#2F855A", "5. Return Risk Score & Ranked Reasons"),
        (585, 402, 908, False, "#2F855A", "6. Persist Student Metrics & Risk Tier"),
        (665, 908, 402, True, "#2F855A", "7. Confirm ACID Transaction Commit"),
        (745, 402, 1173, False, "#6B46C1", "8. Route At-Risk & Check Stage Quotas"),
        (825, 1197, 1433, False, "#2C7A7B", "9. Emit Alert & AuditLog"),
        (905, 378, 140, True, "#2B6CB0", "10. Render Charts, XAI Cards & Queue Status")
    ]
    for y, x1, x2, dash, col, txt in msgs:
        if x1 == x2:
            d.line([(x1 + 12, y), (x1 + 52, y), (x1 + 52, y + 26), (x1 + 12, y + 26)], fill=col, width=2)
            draw_arrow(d, x1 + 28, y + 26, x1 + 12, y + 26, col, 2)
            d.text((x1 + 60, y + 1), txt, font=fnt(FONT_SANS_BD, 15), fill=col)
        else:
            draw_arrow(d, x1, y, x2, y, col, 3, dashed=dash)
            mx = min(x1, x2) + 18
            d.rectangle([mx - 4, y - 24, mx + len(txt) * 8 + 10, y - 3], fill="#FFFFFF")
            d.text((mx, y - 23), txt, font=fnt(FONT_SANS_BD, 15), fill=col)

    out = os.path.join(OUT_DIR, "diag_4_6_3_sequence.png")
    im.save(out, quality=95)
    return out

def draw_uml_class(d, x0, y0, w, hdr_col, title, attrs, methods):
    row_h = 24
    h_hdr = 42
    h_att = len(attrs) * row_h + 18
    h_mth = len(methods) * row_h + 18
    total_h = h_hdr + h_att + h_mth
    d.rectangle([x0, y0, x0 + w, y0 + total_h], fill="#FFFFFF", outline="#2D3748", width=3)
    d.rectangle([x0, y0, x0 + w, y0 + h_hdr], fill=hdr_col, outline="#2D3748", width=2)
    draw_centered_text(d, (x0, y0, x0 + w, y0 + h_hdr), title, fnt(FONT_SANS_BD, 18), "#FFFFFF")
    cur_y = y0 + h_hdr + 8
    for a in attrs:
        d.text((x0 + 12, cur_y), a, font=fnt(FONT_SANS, 15), fill="#1A202C")
        cur_y += row_h
    d.line([(x0, y0 + h_hdr + h_att), (x0 + w, y0 + h_hdr + h_att)], fill="#2D3748", width=2)
    cur_y = y0 + h_hdr + h_att + 8
    for m in methods:
        d.text((x0 + 12, cur_y), m, font=fnt(FONT_SANS_BD, 15), fill="#2B6CB0")
        cur_y += row_h
    return (x0, y0, x0 + w, y0 + total_h)

def build_class_diagram():
    W, H = 1600, 1020
    im = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(im)
    d.text((380, 26), "UML Class Diagram: Core Domain Entities & ML Pipeline", font=fnt(FONT_SANS_BD, 28), fill="#1A202C")
    d.line([(90, 74), (1510, 74)], fill="#718096", width=2)

    draw_uml_class(d, 70, 110, 410, "#1E3A2F", "User (RBAC Actor)",
                   ["+ id: Integer (PK)", "+ username: String (UQ)", "+ password_hash: String", "+ role: Admin/HOD/Mentor/Student", "+ department: String"],
                   ["+ set_password()", "+ check_password()"])

    draw_uml_class(d, 580, 110, 440, "#2B6CB0", "Student",
                   ["+ enrollment_no: String (UQ)", "+ attendance_percentage: Float", "+ internal_marks_avg: Float", "+ backlog_count: Integer", "+ fee_status, engagement_score", "+ risk_score, lifecycle_status"],
                   ["+ reasons_list()", "+ assign_mentor()"])

    draw_uml_class(d, 1120, 110, 410, "#B7791F", "MLEngine (Singleton)",
                   ["+ rf_pipeline: Pipeline(120 Trees)", "+ lr_pipeline: Pipeline", "+ feature_importances: Dict", "+ metrics: Accuracy / ROC_AUC"],
                   ["+ predict(student_dict)", "+ analyze_reasons(rules)", "+ retrain(custom_df)"])

    draw_uml_class(d, 70, 580, 410, "#2F855A", "AuditLog & Notification",
                   ["+ id: Integer (PK)", "+ user_id: Integer (FK)", "+ action: String", "+ details, ip_address: String", "+ timestamp: DateTime"],
                   ["+ log_audit()", "+ create_notification()"])

    draw_uml_class(d, 580, 595, 440, "#6B46C1", "CounsellingCase",
                   ["+ id: Integer (PK)", "+ student_id: Integer (FK)", "+ mentor_id: Integer (FK)", "+ status: 5-Stage Enum", "+ mentor_remarks, action_plan"],
                   ["+ advance_stage()", "+ log_session()"])

    draw_uml_class(d, 1120, 595, 410, "#2C7A7B", "SystemSetting",
                   ["+ key: String (PK)", "+ value: String", "+ category: Policy / Capacity", "+ updated_at: DateTime"],
                   ["+ get_risk_rules()", "+ get_stage_limits()"])

    # Relationships
    draw_arrow(d, 480, 210, 580, 210, "#2D3748", 3)
    d.text((500, 182), "1..*", font=fnt(FONT_SANS_BD, 15), fill="#2D3748")
    draw_arrow(d, 1120, 220, 1020, 220, "#B7791F", 3, dashed=True)
    d.text((1032, 192), "scores", font=fnt(FONT_SANS_BD, 15), fill="#B7791F")
    draw_arrow(d, 800, 415, 800, 595, "#6B46C1", 3)
    d.text((812, 495), "1 : 0..* cases", font=fnt(FONT_SANS_BD, 15), fill="#6B46C1")
    draw_arrow(d, 275, 360, 275, 580, "#2F855A", 3)
    d.text((285, 470), "1 : 0..* logs", font=fnt(FONT_SANS_BD, 15), fill="#2F855A")
    draw_arrow(d, 1325, 595, 1325, 370, "#2C7A7B", 3, dashed=True)
    d.text((1335, 480), "configures", font=fnt(FONT_SANS_BD, 15), fill="#2C7A7B")

    out = os.path.join(OUT_DIR, "diag_4_6_4_class.png")
    im.save(out, quality=95)
    return out

def generate_all_assets():
    files = [
        build_banner(),
        build_design_flow(),
        build_architecture_nav(),
        build_sdlc(),
        build_use_case(),
        build_closed_loop(),
        build_sequence(),
        build_class_diagram()
    ]
    for f in files:
        print(f"Generated visual asset: {f} ({os.path.getsize(f)} bytes)")

if __name__ == "__main__":
    generate_all_assets()
