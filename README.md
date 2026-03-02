---

# 📝 Task CLI Manager

A simple **Command Line Interface (CLI)** task manager built with **Python** and **Typer**.
This application allows you to add, update, delete, and manage tasks stored in a JSON file.

---

## 🚀 Features

* ✅ Add new tasks
* ✏️ Update task descriptions
* 🔄 Change task status (`todo`, `in-progress`, `done`)
* ❌ Delete tasks
* 📅 Automatically track creation and update timestamps
* 💾 Persistent storage using a JSON file

---

## 📂 Project Structure

```
.
├── main.py        # CLI application
├── hello.json     # Task storage file (auto-created)
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2️⃣ Install dependencies

```bash
pip install typer
```

---

## ▶️ Usage

Run the application using:

```bash
python main.py [COMMAND]
```

---

## 📌 Available Commands

### ➕ Add a Task

```bash
python main.py add "Finish Python project"
```

✔ Creates a new task with:

* Status: `todo`
* `createdAt` timestamp
* Auto-incremented ID

---

### ✏️ Update a Task Description

```bash
python main.py update 1 "Finish CLI project"
```

✔ Updates the task description
✔ Sets `updatedAt` timestamp

---

### 🔄 Change Task Status

```bash
python main.py status 1 done
```

Example statuses:

* `todo`
* `in-progress`
* `done`

✔ Updates the status
✔ Sets `updatedAt` timestamp

---

### ❌ Delete a Task

```bash
python main.py delete 1
```

✔ Removes the task permanently

---

## 📄 Data Format (hello.json)

Tasks are stored in this structure:

```json
{
    "tasks": [
        {
            "id": 1,
            "description": "Finish project",
            "status": "todo",
            "createdAt": "2026-03-02 15-30-10",
            "updatedAt": null
        }
    ]
}
```

---

How It Works

* The program reads from `hello.json`
* If the file does not exist, it creates a default structure:

```json
{ "tasks": [] }
```

* Each task:

  * Has a unique auto-incremented ID
  * Stores creation time
  * Stores update time when modified

---
s

---

## 👨‍💻 Author

Amos Kipchirchir
Software Engineering Student
