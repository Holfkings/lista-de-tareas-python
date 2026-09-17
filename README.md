# Task List in Python

A console application for managing a task list: view, add, and remove tasks via an interactive menu. Tasks are **saved to a file** (`tasks.json`), so they are not lost when the program closes.

## 🚀 What it does

- **View tasks**: displays all saved tasks (numbered) or notifies if the list is empty.
- **Add tasks**: adds a new task and saves it to disk.
- **Remove tasks**: removes a task by its number, validating it exists.
- **Persistence**: tasks are saved in `tasks.json` and loaded on startup.
- **Exit**: closes the program.

## 🛠️ Technologies

- Python 3
- Standard modules: `json`, `os`

## ▶️ How to run

1. Clone this repository or download `Tareas.py`
2. Open a terminal in the project folder
3. Run:

```bash
python Tareas.py
```

4. Follow the menu instructions (choose an option from 1 to 4)

## 📸 Usage example

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
```

## 📚 What I learned with this project

- Handling **lists** in Python (`append`, `pop`, `len`)
- **Loops** `while` and **conditionals** `if / elif / else`
- **Functions** to organize code
- **Persistence** with `json` and `os` (save/load data)
- **Input validation** with `try / except`

## 🔜 Future improvements

- [ ] Mark tasks as completed
- [ ] Edit an existing task
- [ ] Graphical interface (Tkinter)

---

✍️ Made by **Holfkings Arenas** as part of my Python learning journey.
