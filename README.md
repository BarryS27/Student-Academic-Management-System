# 🎓 Student Academic Management System (SAMS)

**A comprehensive, Python-based CLI tool designed for high school students to track academic performance, manage portfolios, and visualize progress.**

> **Status:** Active Development  
> **Python Version:** 3.8+
> **Style:** iOS Dark Mode / Industrial

---

## 📖 Overview

SAMS is a personal data management system built with a modular **MVC (Model-View-Controller)** architecture. It moves beyond simple spreadsheets by offering a robust Command Line Interface (CLI) to manage Grades (G9-G12), Self-Development activities, and University applications.

Unlike basic scripts, SAMS includes **data persistence** (CSV), **input validation**, and **advanced data visualization** using Seaborn to analyze academic strengths.

## ✨ Key Features

### 1. 📊 Smart Data Management
- **Flexible Records**: Track grades, weights, and detailed scores (Q1-Q4) for multiple years (G9-G12).
- **Portfolio Tracking**: Manage non-academic data like "Self Development" skills and "Dream Schools".
- **CRUD Operations**: Fully supported **C**reate, **R**ead, **U**pdate, and **D**elete functionalities.
- **Auto-Save**: All changes are instantly persisted to local CSV files.

### 2. 🎨 Advanced Visualization
- **iOS-Style Analytics**: Integrated `viz.py` module generates aesthetic, "Apple-style" performance charts.
- **Seaborn & Matplotlib**: Uses advanced plotting libraries to visualize course performance based on total points.
- **Clean UI**: Visualizations feature rounded bars, pastel color palettes, and minimal "junk" (despined axes).

### 3. 🖥️ User Experience (UX) Focused
- **Human-Centric UI**: 1-based indexing for all lists (no more mental math converting 0-based indexes).
- **Tabulate Integration**: Data is presented in clean, rounded ASCII tables for high readability.
- **Menu-Driven**: No need to type complex table names; select operations via simple numeric menus.

---

## 🛠️ Tech Stack

- **Core Logic**: `Python`, `Pandas`, `NumPy`
- **Visualization**: `Seaborn`, `Matplotlib`, `SciPy`
- **Interface**: `Tabulate`, `Console Input`
- **Data Storage**: CSV (Local File System)

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

### 1. Installation
Clone the repository and install the required dependencies:
```bash
# Install dependencies from requirements.txt
pip install -r requirements.txt
```

### 2. Run the Application

Once dependencies are installed, start the system by running:
```bash
python main.py
```

---

## 📂 Project Structure

The project follows a modular design to ensure maintainability:
```text
.
├── main.py           # 🚀 Entry Point: Initializes the Controller
├── core.py           # 🧠 Model: Handles Data Logic & CSV CRUD operations
├── ui.py             # 🖥️ View: Handles User Interaction & Menu rendering
├── viz.py            # 🎨 Visualization: Generates Seaborn/Matplotlib charts
├── config.py         # ⚙️ Configuration: File paths & Column definitions
├── requirements.txt  # 📦 Dependencies list
├── .gitignore        # 🔒 Privacy: Excludes personal CSV data from Git
└── README.md         # 📖 Documentation
```

---

## ⚙️ Configuration

SAMS is designed to be flexible. You can customize the system behavior in `config.py`:

* **Add New Academic Years**: Simply add a new key (e.g., `'G8': 'G8.csv'`) to the `FILES` dictionary.
* **Modify Data Columns**: Adjust the `COLUMNS` dictionary to track different metrics (e.g., adding `'Midterm_Exam'` or `'Teacher_Comment'`).
* **Input Validation**: The `NUMERIC_COLS` list defines which fields require strict numeric input.

---

## 🔒 Privacy & Data Security

This system is designed with privacy in mind:

* **Local Storage**: All data is stored locally in `.csv` files on your machine.
* **Git Protection**: The included `.gitignore` file ensures your personal grades, dream school lists, and private notes are **never uploaded** to GitHub.

---

## 🔮 Future Roadmap

Things I plan to add in the future:

* [ ] **GPA Calculator**: Auto-calculate weighted/unweighted GPA based on course weights.
* [ ] **Export to PDF**: Generate a summary report for college counselors.
* [ ] **GUI Version**: Port the interface to a web app using Streamlit.

---

## 📄 License

This project is open-source and available for personal use.

*Built with Python 🐍*
