# 🎓 Student Academic Management System (SAMS)

**A comprehensive, Python-based CLI tool designed for high school students to track academic performance, manage portfolios, and visualize progress.**

> **Status:** Active Development  
> **Python Version:** 3.12  
> **Style:** iOS Dark Mode / Industrial / Minimalist

---

## 📖 Overview

SAMS is a personal data management system built with a modular **MVC (Model-View-Controller)** architecture. It moves beyond simple spreadsheets by offering a robust Command Line Interface (CLI) to manage Grades (G9-G12), Self-Development activities, and University applications.

Unlike basic scripts, SAMS includes **data persistence** (CSV), **input validation**, and **advanced data visualization** using Seaborn to analyze academic strengths.

## 🎯 Target Audience

This project is designed as a local academic management tool for high school students with basic Python knowledge, especially suitable for learners in environments like the U.S. high school curriculum. It helps users practice Python, file handling (CSV), and basic data visualization while managing academic records locally.

⚠️ Note: This is **not** intended for large-scale deployment or production use.

---

## ✨ Key Features

### 1. 📊 Smart Data Management
- **Flexible Records**: Track grades, weights, and detailed scores (Q1-Q4) for multiple years (G9-G12).
- **Portfolio Tracking**: Manage non-academic data like "Self Development" skills and "Dream Schools".
- **CRUD Operations**: Fully supported **C**reate, **R**ead, **U**pdate, and **D**elete functionalities.
- **Auto-Provisioning**: Automatically creates the data storage directory (`mydata/`) on first run.

### 2. 🤖 AI Academic Advisor (Experimental)
- **GPT Integration**: Built-in AI chat module that acts as a personalized academic counselor.
- **Context-Aware**: Can be customized with specific personas to analyze your grades or suggest extracurriculars.
- **Privacy-First**: API keys are securely managed via `.env` files; the module degrades gracefully if offline.

### 3. 🎨 Advanced Visualization
- **Visualization Hub**: Dedicated `viz` module for generating publication-quality charts.
- **Chart Types**:
  - **Subject Breakdown**: Thin-bar horizontal charts for analyzing specific grade performance.
  - **GPA Trend**: Smooth spline curves showing your academic trajectory from G9 to G12.
  - **Skill Radar**: Spider charts to visualize subject balance.
- **Dark Mode**: All charts are styled with a custom "Industrial Dark" theme.

### 4. 🖥️ User Experience (UX)
- **Package Architecture**: Clean code structure (`from app import ...`) making it easy to maintain and extend.
- **Human-Centric**: 1-based indexing for lists (no more mental math converting 0-based indexes).
- **Tabulate UI**: Data is presented in clean, rounded ASCII tables.

---

## 🛠️ Tech Stack

- **Core Logic**: `Python 3.12`, `Pandas`, `NumPy`
- **Visualization**: `Seaborn`, `Matplotlib`, `SciPy`
- **Interface**: `Tabulate`, `Console Input`, `python-dotenv`
- **AI Services**: `OpenAI API`
- **Data Storage**: Local CSV (Comma Separated Values)

---

## 🚀 Getting Started

### Prerequisites
M### Prerequisites
* Python 3.10 or higher ( **3.12 Recommended** )
* It is recommended to use a virtual environment.
* An OpenAI API Key (Optional, for AI features)

### 1. Installation
Clone the repository and install the required dependencies:
```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 2. Setup AI (Optional)
Create a .env file in the project root to enable AI features:
```bash
# Create .env file
echo "API_KEY=sk-your-openai-api-key-here" > .env
```
(If you skip this, SAMS will still work, just without the AI Chat feature)

### 3. Run the Application
Once dependencies are installed, start the system by running:
```bash
python main.py
```

---

## 📂 Project Structure

The project follows a modular design to ensure maintainability:
```text
.
├── main.py              # 🚀 Entry Point: Bootstraps the application
├── .env                 # 🔒 Security: Stores API Keys (Ignored by Git)
├── mydata/              # 💾 Storage: Auto-generated CSV files
└── app/                 # 📦 Main Package
    ├── __init__.py      #    Package Exporter
    ├── config.py        #    Settings: Paths & Column Definitions
    ├── core.py          #    Model: Data Logic & CRUD
    ├── ui.py            #    View: CLI & User Interaction
    ├── viz.py           #    Viz: Chart Generation Engine
    └── ai.py            #    Service: AI Integration Logic
```

---

## ⚙️ Configuration

SAMS is designed to be flexible. You can customize the system behavior in `app/config.py`:

* **Add New Academic Years**: Simply add a new key (e.g., `'G8': 'G8.csv'`) to the `FILES` dictionary.
* **Modify Data Columns**: Adjust the `COLUMNS` dictionary to track different metrics (e.g., adding `'AP_Score'` or `'Teacher_Comment'`).
* **Input Validation**: The `NUMERIC_COLS` list defines which fields require strict numeric input.
* **AI Persona**: Change `DEFAULT_SYSTEM_PROMPT` to make the AI stricter or more casual.

---

## 🔒 Privacy & Data Security

* **Local Storage**: All grades and plans are stored locally in `mydata/`.
* **Git Protection**: The included `.gitignore` ensures `mydata/` and `.env` are **never** uploaded to GitHub.
* **Safe Coding**: The AI module is strictly opt-in and requires manual user confirmation before sending any queries.

---

## 🔮 Future Roadmap

* [ ] **GPA Calculator**: Auto-calculate weighted/unweighted GPA based on course credits.
* [ ] **PDF Export**: Generate a college-application-ready summary report.
* [ ] **GUI Port**: Migrate the frontend to Streamlit or PyQt for a desktop app experience.

---

## 📄 License

This project is open-source and available for personal use.

*Built with Python 🐍*
