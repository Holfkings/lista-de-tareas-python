<div align="center">

# 📝 Task List in Python

### Console Task Manager · Python 3 · JSON Persistence · No Dependencies

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CLI-Console-grey?style=for-the-badge&logo=gnubash&logoColor=white" alt="CLI">
  <img src="https://img.shields.io/badge/JSON-Persistence-003B57?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
  <img src="https://img.shields.io/badge/Zero_Dependencies-✓-green?style=for-the-badge&logo=package&logoColor=white" alt="Zero Dependencies">
</p>

</div>

---

## 🚀 What It Does

A command-line task manager with full CRUD operations. Tasks are saved to a JSON file so they persist between sessions.

| Feature | Description |
|---------|-------------|
| **View tasks** | List all saved tasks with numbering |
| **Add tasks** | Create new tasks and save to disk |
| **Remove tasks** | Delete tasks by number with validation |
| **Persistence** | Auto-save/load from `tareas.json` |
| **Clean menu** | Interactive numbered menu (1-4) |

---

## 🛠️ Tech Stack

| Technology | Detail |
|------------|--------|
| **Language** | Python 3 |
| **Modules** | `json`, `os` (stdlib only) |
| **Dependencies** | **Zero** |
| **Storage** | `tareas.json` (local file) |

---

## ▶️ How to Run

```bash
# Clone or download
git clone https://github.com/Holfkings/lista-de-tareas-python.git
cd lista-de-tareas-python

# Run the app
python Tareas.py
```

Then follow the menu:

```text
----------------
Options menu
----------------
View tasks (1), add (2), remove (3) or exit (4)
Choose an option: 
```

---

## 📸 Usage Example

```text
----------------
Options menu
----------------
View tasks (1), add (2), remove (3) or exit (4)
Choose an option: 2
----------------
What task do you want to assign: Study Python
Task added ✔
----------------

Choose an option: 1
----------------
Your tasks:
1. Study Python
----------------
```

---

## 🧠 What I Learned

| Concept | How it's used |
|---------|---------------|
| **Lists** | `append()`, `pop()`, `len()` for task management |
| **Loops** | `while` for the main menu loop |
| **Conditionals** | `if / elif / else` for menu options |
| **Functions** | Code organization into reusable functions |
| **Persistence** | `json` module to save/load data |
| **Validation** | `try / except` for input handling |

---

## 🔜 Future Improvements

- [ ] Mark tasks as completed
- [ ] Edit existing tasks
- [ ] Priority levels
- [ ] Due dates
- [ ] Graphical interface (Tkinter)
- [ ] Export to CSV/PDF

---

## 📂 Project Structure

```text
lista-de-tareas-python/
└── Tareas.py       # Main application — all logic in one file
```

Simple and focused. Single file, no clutter.

---

## ✅ Status

| Metric | Value |
|--------|-------|
| **Lines of code** | ~100 |
| **Dependencies** | 0 |
| **External packages** | None |
| **Python version** | 3.x |

---

<div align="center">

✍️ Made by **Holfkings Arenas** — part of my Python learning journey.

<p align="center" style="color: #888; font-size: 0.85em; margin-top: 24px;">
  Simple tools, clean code.
</p>

</div>
