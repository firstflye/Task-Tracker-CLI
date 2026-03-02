import sys
import json
import typer
from datetime import datetime

app = typer.Typer()

FILE_NAME = "hello.json"

def read():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

            if not isinstance(data, dict):
                return {"tasks": []}

            data.setdefault("tasks", [])
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        return {"tasks": []}


def write(data):
    with open("hello.json", 'w') as file:
        return json.dump(data, file, indent = 4)



def generateid(tasks):
    if not tasks:
        return 1

    return max(task["task_id"] for task in tasks) + 1

@app.command()
def add(description: str):
    task_file = read()
    id = generateid(task_file["tasks"])
    new_task = {
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
        "updatedAt":None,
    }
    task_file["tasks"].append(new_task)
    write(task_file)

    typer.echo(f"Task {id} added")

@app.command()
def update(id, new_description):
    task_file = read()

    for task in task_file["tasks"]:
        if task["id"]== id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now(). strftime("%Y-%m-%d %H-%M-%S")
            write(task_file)
            typer.echo("Task updated")
            return
    typer.echo("Task not found")

@app.command()
def updatestus(task_id, new_status):
    task_file = read()

    for task in task_file["tasks"]:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now(). strftime("%Y-%m-%d %H-%M-%S")
    write(task_file)


@app.command()
def delete(id: int):
    """Delete a task"""
    task_file = read()

    new_tasks = [task for task in task_file["tasks"] if task["id"] != id]

    if len(new_tasks) == len(task_file["tasks"]):
        typer.echo("Task not found ")
        return

    task_file["tasks"] = new_tasks
    write(task_file)

    typer.echo("Task deleted")


def list_tasks():
    task_file = read()
    for task in task_file["tasks"]:
        print(task)


def list_by_status(status):
    task_file = read()
    for task in task_file["tasks"]:
        if task["status"] == status:
            print(task)

if __name__ == "__main__":
    app()
