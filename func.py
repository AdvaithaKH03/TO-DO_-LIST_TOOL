import json
import os

TASKS_FILE = "memo.json"

def entry():
    print("Welcome to TO-DO List Program")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    
def load_from_file():
    """Loads tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_to_file(tasks):
    """Saves tasks to JSON file"""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def create_task():
    """Creates a new task and saves it to JSON"""
    tasks = load_from_file()
    task = input("Enter Task: ")
    tasks.append({"task": task, "status": "Not Done"})  # Store as dictionary
    save_to_file(tasks)
    print("Task saved successfully!")

def load_tasks():
    """Displays all tasks from memo.json"""
    tasks = load_from_file()
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['task']} | {task['status']}")
    else:
        print("No tasks found!")

def mark_task(task_number):
    """Marks a task as Done"""
    tasks = load_from_file()
    index = task_number - 1  # Convert task number to list index

    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
        return

    if tasks[index]["status"] == "Not Done":
        tasks[index]["status"] = "Done"
        save_to_file(tasks)
        print(f"Task {task_number} marked as Done!")
    else:
        print(f"Task {task_number} is already marked as Done!")

def delete_task(task_number):
    """Deletes a task from the list"""
    tasks = load_from_file()
    index = task_number - 1  # Convert task number to list index

    if index < 0 or index >= len(tasks):
        print("Invalid task number!")
        return
    
    removed_task = tasks.pop(index)  # Remove task from list
    save_to_file(tasks)
    print(f"Task {task_number} deleted!")

"""ALL THE FUNCTIONS AND FEATURES OF THE PROGRAM IS STORED IN THIS FILE"""
