<div align="center">

# ☕ SnackCafe

**A lightweight Cafe Ordering & Menu Management practice project**

<p>
  <a href="https://github.com/VINAY-160/SnackCafe"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://x.com/"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" alt="X" /></a>
  <a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
  <a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" /></a>
</p>

</div>

---

A beginner-friendly practice project that simulates a cafe ordering and menu management system. Built to practice core programming concepts, API design, data handling, and project structuring.

---

## 🚀 Features

- 📋 **Menu Viewing**: Display available snacks, beverages, and pricing.
- 🛒 **Order Management**: Add or remove items from the order cart.
- 🧾 **Bill Calculation**: Automatically compute totals, apply discounts, or calculate taxes.
- 🛠️ **Simple Interface**: Clean layout for quick navigation and testing.

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** SQLite / JSON / In-memory lists
- **Editor:** VS Code
- **Version Control:** Git & GitHub

---

## 📁 Repository Structure

```text
SnackCafe/
├── assets/            # Screenshots, logos, or static images
├── src/               # Source code / application logic
├── requirements.txt   # Project dependencies
├── .gitignore         # Untracked files (.venv, __pycache__, etc.)
└── README.md          # Project documentation
```

---

## ⚙️ Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/VINAY-160/SnackCafe.git
cd SnackCafe
```

### 2. Set Up a Virtual Environment (Optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# .venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

(Replace `main` with your entry-point file name if different, e.g. `app`.)

Then open:

- API: http://127.0.0.1:8000
- Interactive docs (Swagger): http://127.0.0.1:8000/docs

---

## 🔮 Future Enhancements & Roadmap

- [ ] Add user authentication (Admin vs. Customer).
- [ ] Implement database persistence (PostgreSQL / SQLite).
- [ ] Generate downloadable digital PDF receipts.
- [ ] Improve UI/UX with responsive design.

---

## 📄 License

This project is created for educational and practice purposes.
