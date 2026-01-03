# 📐 Project Design Overview

## 🎯 1. Project Purpose

The **Student Academic Management System (SAMS)** is a local, command-line based application designed to help students track academic records, visualize performance trends, and receive AI-driven advice.

The project prioritizes **modularity**, **maintainability**, and **Python best practices** (packaging, relative imports, type safety) while remaining accessible for educational purposes.

---

## 📂 2. Directory Structure

The project follows a **Package-based Architecture**, separating the source code from the entry point and data storage.

```text
MY-REPO/
├── main.py              # 🚀 Application Entry Point
├── .env                 # 🔐 API Keys (Local only)
├── mydata/              # 💾 CSV Storage (Auto-generated)
│   ├── G9.csv
│   └── ...
└── app/                 # 📦 Main Application Package
    ├── __init__.py      #    Package Exporter
    ├── config.py        #    Settings & Path Resolution
    ├── core.py          #    Business Logic (Model)
    ├── ui.py            #    Interface (View)
    ├── viz.py           #    Visualization
    └── ai.py            #    AI Service Integration
```

## 🧱 3. Architectural Style

The project utilizes a **Modular MVC (Model-View-Controller)** pattern wrapped in a Python Package structure.

* 🗃️ **Model (`core.py`)**: Manages data state, logic, and persistence.
* 🖥️ **View (`ui.py` & `viz.py`)**: Handles user interaction and visual output.
* 🎛️ **Controller (`core.py` & `main.py`)**: Coordinates the flow of data between the user, the database, and external services (AI).

---

## 📦 4. Module Responsibilities

### ▶️ `main.py` (Root)
* **Role**: Entry Point & Bootstrapper.
* **Responsibilities**:
    * Sets up the Python system path to recognize the `app` package.
    * Instantiates the System Core and UI.
    * Launches the main event loop.
    * Handles top-level global exceptions (Crash protection).

### ⚙️ `app/config.py`
* **Role**: Configuration Center.
* **Responsibilities**:
    * Uses `pathlib` for dynamic, OS-agnostic path resolution.
    * Defines the schema for CSV files (Columns).
    * Maps internal table names to file paths in `mydata/`.
    * Stores system prompts for the AI.

### 🧠 `app/core.py`
* **Role**: The "Brain" / Data Manager.
* **Responsibilities**:
    * Loads data from `app/config.py` definitions.
    * Provides CRUD (Create, Read, Update, Delete) methods.
    * Acts as the bridge between the UI and the AI agent.
    * Ensures data integrity during Save operations.

### 🖥️ `app/ui.py`
* **Role**: Console Interface.
* **Responsibilities**:
    * Renders menus and tables (using `tabulate`).
    * Validates user input types (converting strings to floats).
    * Routes user commands to the `core` manager.
    * **Decoupled**: Contains no direct file I/O logic.

### 📊 `app/viz.py`
* **Role**: Visualization Engine.
* **Responsibilities**:
    * Generates charts using `matplotlib`.
    * Features: Subject Breakdown (Bar), GPA Trend (Spline/Line), Radar Charts.
    * Styling: Uses a custom Dark Mode theme defined internally.

### 🤖 `app/ai.py`
* **Role**: AI Service Adapter.
* **Responsibilities**:
    * Manages connection to OpenAI API.
    * **Security**: Loads API keys securely from `.env` via `python-dotenv`.
    * **Resilience**: Fails gracefully if keys or libraries are missing, ensuring the app continues to work without AI features.

---

## 💾 5. Data Persistence

* **Storage Location**: `mydata/` directory (located at project root).
* **Format**: CSV (Comma Separated Values).
* **Mechanism**:
    * Data is loaded into memory (Pandas DataFrames) on startup.
    * Changes are written back to disk only when explicitly saved.
* **Auto-Provisioning**: The system automatically creates the `mydata/