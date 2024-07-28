import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter task name: ")
    task_due = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"name": task_name, "due": task_due})
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['name']} (Due: {task['due']})")

def delete_task(tasks):
    """Delete a task by index."""
    list_tasks(tasks)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"Task '{removed_task['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Tracker")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
