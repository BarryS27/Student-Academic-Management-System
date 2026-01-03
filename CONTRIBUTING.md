# 🎓 Contributing to SAMS

First off, thank you for considering contributing to the **Student Academic Management System (SAMS)**! It's people like you who make this tool better for students everywhere.

To maintain code quality and project stability, please follow these guidelines.

## 🚀 Getting Started

1.  **Fork the Repository**: Create your own copy of the project on your GitHub account.
2.  **Clone Locally**: 
    ```bash
    git clone [https://github.com/BarryS27/Project-Student-Academic-Management-System.git](https://github.com/BarryS27/Project-Student-Academic-Management-System.git)
    ```
3.  **Install Dependencies**: Ensure you have all required libraries installed:
    ```bash
    pip install -r requirements.txt
    ```

## 🛠️ Development Workflow

### 1. Create a Branch
**Do not commit directly to the `main` branch.** Due to our branch protection rules, direct pushes to `main` are blocked.
* Create a feature branch: `git checkout -b feature/your-feature-name`
* For bug fixes: `git checkout -b fix/issue-description`

### 2. Coding Standards
* **PEP 8 Compliance**: All Python code must follow PEP 8 standards for readability.
* **Docstrings**: Add descriptive docstrings to all new functions and classes to explain their purpose.
* **MVC Architecture**: Respect the modular structure:
    * `core.py`: Data logic and CSV CRUD operations.
    * `ui.py`: User interface and menu rendering.
    * `viz.py`: Data visualization and charts.

### 3. Submission
1.  Push your changes to your fork.
2.  Submit a **Pull Request (PR)** to our `main` branch.
3.  Ensure your PR description clearly explains the changes made and references any related Issue numbers (e.g., `Closes #1`).

## ⚖️ Review Process

* **Approval Required**: All PRs must be reviewed and approved by at least one maintainer before merging.
* **Resolve Conversations**: If comments are left on your code, you must resolve all conversations before the PR can be merged.
* **Bypass Restrictions**: Administrators are also bound by these protection settings to ensure project integrity.

## 🔒 Security
If you are working on the **AI Chat** feature, ensure your `.env` file containing your `API_KEY` is **never** committed to the repository.

---
*Built with Python 🐍*
