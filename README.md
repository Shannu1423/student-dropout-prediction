# AI-Based Prediction of Reasons for Student Dropout
**Sanskriti University &bull; School of Engineering and Information Technology (SOEIT)**

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Shannu1423/student-dropout-prediction)

* **Candidate 1:** SHAIK SHAFI (Enrollment No: `2302320151`)
* **Candidate 2:** SHAIK MOHAMMAD ALI (Enrollment No: `2302320119`)
* **Candidate 3:** SHAIK MAHAMAD YASEEN (Enrollment No: `2302320118`)
* **Candidate 4:** DESIREDDY RAMESH (Enrollment No: `2302320099`)
* **Faculty Guide:** Mr. Satyam Dwivedi, Assistant Professor, Department of CSE, SOEIT
* **Academic Year:** 2026–2027 (November 2026)
* **GitHub Repository:** [https://github.com/Shannu1423/student-dropout-prediction.git](https://github.com/Shannu1423/student-dropout-prediction.git)

---

## 💻 How to Run Locally on MacBook (macOS Terminal)

Open the **Terminal** app (`Cmd + Space` &rarr; type `Terminal` &rarr; press `Enter`) and run these exact steps:

### Step 0: Clone & Open the Project Folder (If Running on a New MacBook)
```bash
git clone https://github.com/Shannu1423/student-dropout-prediction.git
cd student-dropout-prediction
```
*(If you already copied the folder locally, simply `cd /path/to/student_dropout_prediction`.)*

### Step 1: Create a Python Virtual Environment
*(On macOS, `python3` is the standard system Python command. Note: if Xcode Command Line Tools are missing, macOS will prompt you once to install them, or install Python 3 from [python.org](https://www.python.org/downloads/macos/) / Homebrew `brew install python`.)*
```bash
python3 -m venv .venv
```

### Step 2: Activate the Virtual Environment
```bash
source .venv/bin/activate
```
*(Your Terminal prompt will now start with `(.venv)` at the left.)*

### Step 3: Install All Required Libraries
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```
You will see:
```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```
Open Safari or Google Chrome and visit: **`http://127.0.0.1:5000`**

> **MacBook Pro/Air Port 5000 Tip (macOS Monterey / Ventura / Sonoma / Sequoia):**  
> Apple uses Port `5000` for **AirPlay Receiver** by default. If you see `Address already in use` or an Access Denied page in the browser, simply run on port `5001` instead:
> ```bash
> PORT=5001 python app.py
> ```
> Then open **`http://127.0.0.1:5001`** in your browser! (Or turn off *AirPlay Receiver* in **System Settings &rarr; General &rarr; AirDrop & Handoff**.)

---

## 🪟 How to Run Locally on Windows (PowerShell / CMD)

1. Open **PowerShell** and navigate to the project directory:
   ```powershell
   git clone https://github.com/Shannu1423/student-dropout-prediction.git
   cd student-dropout-prediction
   ```
2. Create and activate the virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```
   *(If PowerShell shows a script execution error, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` and activate again.)*
3. Install dependencies and start the server:
   ```powershell
   pip install -r requirements.txt
   python app.py
   ```
4. Open your browser to **`http://127.0.0.1:5000`**.

---

## ☁️ Live Cloud Deployment (Optional 1-Click Render)

This repository includes `render.yaml` and `Procfile` for deployment on Render, Railway, or any WSGI host:
1. Sign in at [dashboard.render.com](https://dashboard.render.com) with GitHub account `Shannu1423`.
2. Select **New + &rarr; Web Service &rarr; `Shannu1423/student-dropout-prediction`**.
3. Render automatically runs `pip install -r requirements.txt` and `gunicorn "app:create_app()"`.

---

## 🔑 Demo Login Credentials

The system enforces a strict 4-tier Role-Based Access Control (RBAC) architecture:

| Role | Username | Password | Operational Scope |
| :--- | :--- | :--- | :--- |
| **Administrator** | `admin` | `password123` | Global risk threshold rules, stage capacity limits, model retraining, forensic audit logs |
| **Guide / HOD** | `satyam` | `password123` | Department risk analytics, mentor allocation, bulk CSV ingestion, escalation alerts |
| **Faculty Mentor** | `priya` | `password123` | Assigned at-risk cohort, Explainable AI deficit breakdown, counseling notes, stage progression |
| **Student** | `ramesh` | `password123` | Read-only isolation strictly bound to personal academic metrics and counselor advice |

---

## 1. System Overview & Verified Empirical Performance

The **AI-Based Prediction of Reasons for Student Dropout** platform integrates supervised predictive modeling directly with an institutional retention workflow built for Sanskriti University (SOEIT):

1. **Multi-Parameter Student Telemetry:** Tracks 115 institutional student records across 7 engineering and management departments covering attendance percentage, continuous internal marks, active backlogs, LMS engagement score, fee payment standing, and current semester.
2. **Calibrated Random Forest Engine:** Benchmarked against a standardized Logistic Regression baseline across stratified evaluation splits:
   - **Random Forest Classifier:** **89.87% Accuracy**, **87.50% Precision**, **87.50% Recall**, **87.50% F1-Score**, and **96.77% ROC-AUC**.
   - **Logistic Regression Baseline:** **88.53% Accuracy**, **84.49% Precision**, **87.83% Recall**, **86.13% F1-Score**, and **96.45% ROC-AUC**.
3. **Localized Explainable AI (XAI) Deficit Engine:** Translates probability predictions into ranked human-readable attribution cards weighted by Random Forest Gini feature importances (`Attendance 43.79%`, `Internal Marks 21.23%`, `Active Backlogs 15.89%`, `LMS Engagement 11.08%`, `Tuition Standing 6.18%`, `Semester 1.84%`).
4. **5-Stage Retention Lifecycle Hub:** Manages cases cleanly across configurable capacity meters:
   $$\text{At Risk} \longrightarrow \text{Under Review} \longrightarrow \text{Counselling} \longrightarrow \text{Intervened} \longrightarrow \text{Closed}$$
5. **Automated Test Verification:** Run `python test_app.py` to execute all 8 unit and integration test suites covering authentication, peer privacy isolation (`HTTP 403`), bulk CSV alias normalization, lifecycle progression, and live model retraining.

---

## 2. Project Artifacts & Reports
* 📄 **[PROJECT_REPORT.pdf](PROJECT_REPORT.pdf)**: Official 77-page Sanskriti University B.Tech Capstone Report.
* 📘 **[COMPLETE_CODEBASE_AND_SYSTEM_ARCHITECTURE_REPORT.pdf](COMPLETE_CODEBASE_AND_SYSTEM_ARCHITECTURE_REPORT.pdf)**: 93-page complete codebase & technical blueprint.
* 📝 **[AI_Based_Student_Dropout_Prediction_Project_Report.docx](AI_Based_Student_Dropout_Prediction_Project_Report.docx)**: Editable plagiarism-free Word report matching the official university front-page structure.
* 🛠️ **[ADMIN_OPERATIONS_MANUAL.md](ADMIN_OPERATIONS_MANUAL.md)**: Institutional operations and system handover documentation.
