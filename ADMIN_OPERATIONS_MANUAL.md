# Sanskriti University &bull; School of Engineering & Technology
# AI-Based Prediction of Reasons for Student Dropout
## System Administrator & Senior Handover Operational Manual

* **Project Title:** AI-Based Prediction of Reasons for Student Dropout
* **Team Members:** SHAIK SHAFI (`2302320151`), SHAIK MOHAMMAD ALI (`2302320119`), SHAIK MAHAMAD YASEEN (`2302320118`), DESIREDDY RAMESH (`2302320099`)
* **Faculty Guide:** Mr. Satyam Dwivedi
* **Target Audience:** Future Project Admins, Department HODs, Lab In-Charges, and Senior Successors

---

## Table of Contents
1. [How to Run the Application Locally](#1-how-to-run-the-application-locally)
2. [Default Login Credentials & Authority Roles](#2-default-login-credentials--authority-roles)
3. [Admin Settings: Configuring Risk Factor Limits](#3-admin-settings-configuring-risk-factor-limits)
4. [Setting Stage Capacity Limits (Workload Meters)](#4-setting-stage-capacity-limits-workload-meters)
5. [Bulk Student Data Upload (CSV Ingestion)](#5-bulk-student-data-upload-csv-ingestion)
6. [AI Model Retraining: When and How to Retrain](#6-ai-model-retraining-when-and-how-to-retrain)
7. [Daily Operations: Mentoring, Lifecycles & Escalations](#7-daily-operations-mentoring-lifecycles--escalations)
8. [Student Data Privacy & Audit Trail](#8-student-data-privacy--audit-trail)
9. [System Maintenance, Backups & Verification](#9-system-maintenance-backups--verification)

---

## 1. How to Run the Application Locally

The application runs entirely offline on Windows or MacBook workstations with zero cloud dependencies.

### On MacBook (macOS Terminal):
```bash
git clone https://github.com/Shannu1423/student-dropout-prediction.git
cd student-dropout-prediction
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py   # Or PORT=5001 python app.py if macOS AirPlay Receiver occupies port 5000
```

### On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Step 3: Access the Portal
Open any web browser (Safari, Google Chrome, Microsoft Edge, Firefox) and visit **`http://127.0.0.1:5000`** (or `http://127.0.0.1:5001` if started on `PORT=5001`). Press `CTRL + C` to stop the server.

---

## 2. Default Login Credentials & Authority Roles

The system enforces strict **Role-Based Access Control (RBAC)** across 4 institutional roles:

| Authority Level | Account Username | Password | Designated User | Scope & Authority |
| :--- | :--- | :--- | :--- | :--- |
| **System Admin** | `admin` | `password123` | **Dr. A.K. Sharma** | **Full Control:** Can alter global risk limits, queue capacities, retrain ML models, export audit logs, and manage all departments. |
| **Guide / HOD** | `satyam` | `password123` | **Mr. Satyam Dwivedi** | **Department Head:** Computer Science & Engineering oversight, mentor assignments, escalation resolution, and cohort analytics. |
| **Faculty Mentor** | `priya` | `password123` | **Dr. Priya Verma** | **Counsellor:** Access scoped strictly to assigned mentees; conducts 1-on-1 sessions, logs action plans, and tracks recovery. |
| **Student** | `ramesh` | `password123` | **D. Ramesh** (`2302320099`) | **Strict Personal Isolation:** Can view only their personal academic score, Explainable AI (XAI) advice, and assigned mentor details. |

---

## 3. Admin Settings: Configuring Risk Factor Limits

As the administrator or senior managing this system, you can customize the exact numerical limits that trigger dropout risk alerts.

### How to Access:
Log in as `admin` &rarr; click **Admin Settings** in the top navigation bar (or navigate to `http://127.0.0.1:5000/admin/settings`).

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ADMINISTRATIVE POLICY CONTROLS                        │
├────────────────────────────────┬────────────────────────────────────────────┤
│ Policy Field                   │ Sanskriti University Nominal Baseline      │
├────────────────────────────────┼────────────────────────────────────────────┤
│ Attendance Warning Limit       │ < 75.0% (Triggers attendance warning)      │
│ Attendance Critical Limit      │ < 60.0% (Triggers urgent intervention)     │
│ Backlog Warning Limit          │ ≥ 1 active backlog                         │
│ Backlog Critical Limit         │ ≥ 3 active backlogs                        │
│ Internal Marks Warning Limit   │ < 55.0% internal test average              │
│ Internal Marks Critical Limit  │ < 40.0% internal test average              │
│ LMS Engagement Critical        │ < 40.0% portal activity                    │
│ Target Stage for Flagged Cases │ "At Risk" (routes to top queue)            │
│ Fee Due Severity Rating        │ "Danger" (Critical) or "Warning" (Moderate)│
└────────────────────────────────┴────────────────────────────────────────────┘
```

### Essential Admin Actions:
1. **Save Custom Changes:** Click the blue **"Save Risk Factor Limits"** button. The limits are stored immediately in the SQLite database (`SystemSetting` table).
2. **Re-Apply Rules to All Students:** Click **"Re-Apply Rules to All Students"** to immediately re-evaluate every student in the database against your new numbers without needing to re-upload data.
3. **Reset to Nominal Defaults:** If you ever make a mistake or want to return to standard institutional defaults, click **"Reset to Nominal Defaults"** to restore Sanskriti University's baseline in one click.

---

## 4. Setting Stage Capacity Limits (Workload Meters)

In real academic life, faculty mentors and counsellors have limited hours. If too many students pile into a stage, the system warns the department that counsellors are overloaded.

### Configurable Queue Capacities:
Located on the **Admin Settings** page under **"Stage Capacity Limits (Queue Meters)"**:

* **At Risk Limit (e.g., 10):** Maximum students waiting in the critical unassigned queue. If count exceeds 10, the Counselling Hub displays a red **"Queue Overflow"** banner telling HODs to assign more faculty mentors.
* **Under Review (e.g., 20):** Maximum cases undergoing preliminary diagnostic checks.
* **Counselling (e.g., 15):** Maximum active 1-on-1 guidance sessions mentors can conduct concurrently.
* **Intervened (e.g., 25):** Maximum students undergoing active remedial classes or fee installment plans.
* **Closed Archive (e.g., 150):** Maximum rehabilitated cases kept in view before archiving.
* **Low Risk Display (e.g., 200):** Maximum safe baseline students shown at the bottom of the hub.

### Lifecycle Queue Priority:
The **[Counselling Hub](http://127.0.0.1:5000/counselling)** arranges stages in strict risk-level priority:
1. 🔴 **Stage 1: Critical At-Risk Queue** *(Top Priority - Urgent Mentor Assignment)*
2. 🟠 **Stage 2: Under Diagnostic Review** *(High Priority - Diagnostic Evaluation)*
3. 🟡 **Stage 3: Active Mentorship & Counselling** *(Medium Priority - 1-on-1 Guidance)*
4. 🔵 **Stage 4: Intervened (Remedial & Fee Plans)** *(Active Remediation)*
5. 🟢 **Stage 5: Closed & Stable Cases** *(Resolved / Backlogs Cleared)*
6. ⚪ **Stage 6: Low Risk Cohort** *(Manageable Baseline at Bottom)*

*Note: Inside each stage, students are sorted in descending order of their predicted risk score (`risk_score DESC`) so mentors always attend to the highest-risk student first.*

---

## 5. Bulk Student Data Upload (CSV Ingestion)

To add an entire batch or semester of students at once, use the **Bulk CSV Upload** feature.

### How to Upload:
1. Log in as `admin`, `satyam`, or `priya`.
2. Go to the **Students** tab (`/students`).
3. Click the **"Bulk CSV Upload"** button at the top right.
4. Select your `.csv` file and click **"Upload & Predict"**.

### Supported CSV Format & Header Names:
The upload parser automatically accepts standard headers and common aliases:

| Header Name | Accepted Aliases | Data Type | Example Value | Description |
| :--- | :--- | :---: | :---: | :--- |
| `enrollment_no` | `enrollment`, `roll_no`, `reg_no`, `student_id` | Text | `2301000003` | Unique Student ID |
| `name` | `student_name`, `full_name` | Text | `Pari Naidu` | Student Full Name |
| `department` | `dept`, `branch` | Text | `Computer Science` | Academic Department |
| `semester` | `sem` | Integer | `3` | Current Semester (1-8) |
| `attendance_percentage` | `attendance`, `att_pct` | Float | `59.7` | Overall Attendance % |
| `internal_marks_avg` | `internal_marks`, `marks` | Float | `47.9` | Internal Exams Average (0-100) |
| `backlog_count` | `backlogs`, `active_backlogs` | Integer | `3` | Number of failed/active subjects |
| `fee_status` | `fee` | Text | `Paid`, `Partial`, `Due` | Institutional Fee Standing |
| `engagement_score` | `lms_score`, `engagement` | Float | `39.0` | Portal / LMS Engagement (0-100) |
| `campus_location` *(optional)* | `campus` | Text | `Main Campus` | Campus Site |

### File Storage:
When a CSV is uploaded, the application stores a copy in **two places**:
1. In the backend upload repository: `data/uploads/<filename>.csv`
2. Directly in your main project folder: `<filename>.csv` *(instantly visible in your file explorer)*

---

## 6. AI Model Retraining: When and How to Retrain

### ❓ The Golden Rule: "Should I retrain if I upload a new list?"

| Scenario | Retrain Needed? | What to Do |
| :--- | :---: | :--- |
| **Uploading current semester active students to monitor** | **NO ❌** | Use **Students &rarr; Bulk CSV Upload**. The existing model evaluates their risk scores immediately without needing retraining. |
| **Academic cycle concluded with known outcomes (`dropped_out = 1/0`)** | **YES ✅** | Go to **Admin Settings &rarr; Trigger AI Model Retraining** to teach the machine learning models the new historical patterns. |

### How to Retrain:
1. Log in as `admin`.
2. Go to **Admin Settings** (`/admin/settings`).
3. Scroll to the **"Trigger AI Model Retraining"** panel on the right side:
   * **Option 1 (One-Click Recalibrate):** Click *"Retrain Model Now"* to re-optimize model weights against institutional benchmark distributions.
   * **Option 2 (Upload Labeled CSV):** Choose a historical dataset containing the target column `dropped_out` (1 = Dropped Out, 0 = Retained) and click *"Upload Labeled CSV & Retrain"*.
4. Once completed, the updated model is serialized to `models/dropout_models.pkl` and new accuracy/ROC-AUC scores appear on the **AI Engine & Explainability** page (`/model-performance`).

---

## 7. Daily Operations: Mentoring, Lifecycles & Escalations

### Assigning Mentors (Admin & HOD):
1. Open any student's profile from the **Dashboard** or **Students** page.
2. In the right column under **Mentorship & Counselling Overview**, select a faculty mentor from the dropdown and click **"Assign Mentor"**.

### Documenting Counselling Sessions (Mentors):
1. On the student's profile page, click **"Log Counselling Session"**.
2. Select the updated status:
   * `Under Review` &rarr; Preliminary assessment.
   * `Counselling` &rarr; 1-on-1 meeting completed.
   * `Intervened` &rarr; Remedial classes or fee installment plan assigned.
   * `Closed` &rarr; Student cleared backlogs and normalized attendance.
3. Enter confidential **Mentor Remarks**, specific **Action Plans**, and set a **Next Follow-up Date**.
4. Click **"Save Session Record"**.

### Escalation Attention Checks:
The system automatically tracks any student whose risk is $\ge 70\%$ but who has remained unassigned. A persistent alert banner appears on the HOD/Admin dashboard:
> *"High-Risk Attention Alert: X student(s) have predicted dropout risk ≥ 70% without assigned counselling interventions."*

---

## 8. Student Data Privacy & Audit Trail

### Student Account Isolation (`ramesh`):
When a student logs in:
* They are automatically redirected to their personal academic card (`/students/<id>`).
* The system prevents peer stigma: students **cannot** see other students' names, marks, or risk scores.
* Attempting to access someone else's ID or admin URLs will flash: *"Access restricted: You may only view your personal academic standing."*
* Students cannot edit their attendance, marks, or backlogs.

### Audit Log & Accountability:
Every administrative action (logins, prediction re-evaluations, policy updates, mentor reassignments, bulk imports) is recorded in a tamper-evident audit log:
* Access via `/audit-logs` (Admin & HOD only).
* Records timestamp, acting user, action type, client IP address, and exact change details.

---

## 9. System Maintenance, Backups & Verification

### Running Automated Test Verification:
Before any demonstration or evaluation, verify all 8 decoupled subsystems inside your activated `.venv`:
```bash
# Mac / Linux / Windows (inside activated .venv)
python test_app.py
```
*(All 8 suites pass cleanly: Authentication, Bulk CSV Upload, Counselling Lifecycle, ML Engine, RBAC Privacy Isolation, Stage Limits, Student Registration, and Admin Retraining).*

### Database Location & Reset:
* The database file is located at: `data/dropout_system.db`.
* To completely reset and seed the database with initial Sanskriti University demo accounts and sample cohorts, run `python seed_data.py`.

---
*Document prepared for Sanskriti University Academic Archive &bull; Candidates: SHAIK SHAFI (2302320151), SHAIK MOHAMMAD ALI (2302320119), SHAIK MAHAMAD YASEEN (2302320118), DESIREDDY RAMESH (2302320099) &bull; Faculty Guide: Mr. Satyam Dwivedi.*
