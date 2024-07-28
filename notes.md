### 1. **Imports and Constants**

```python
import json
import os

TASKS_FILE = 'tasks.json'
```

- **Imports**:
  - `json`: Used for reading and writing tasks in JSON format.
  - `os`: Provides functions to interact with the operating system (e.g., checking if a file exists).

- **Constants**:
  - `TASKS_FILE`: The name of the file where tasks will be stored.

### 2. **Functions**

#### **2.1 Load Tasks**

```python
def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []
```

- **Purpose**: Loads tasks from the `tasks.json` file if it exists.
- **Implementation**:
  - Check if the file exists using `os.path.exists()`.
  - If it exists, open it in read mode and load the content using `json.load()`.
  - Return the list of tasks. If the file doesn’t exist, return an empty list.

#### **2.2 Save Tasks**

```python
def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)
```

- **Purpose**: Saves the tasks list to the `tasks.json` file.
- **Implementation**:
  - Open the file in write mode (`'w'`).
  - Use `json.dump()` to write the tasks list to the file with pretty-printing (indentation).

#### **2.3 Add Task**

```python
def add_task(tasks):
    """Add a new task."""
    task_name = input("Enter task name: ")
    task_due = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"name": task_name, "due": task_due})
    save_tasks(tasks)
    print(f"Task '{task_name}' added.")
```

- **Purpose**: Adds a new task to the list.
- **Implementation**:
  - Prompt the user to enter a task name and due date.
  - Append the new task to the `tasks` list as a dictionary.
  - Save the updated tasks list to the file.
  - Print a confirmation message.

#### **2.4 List Tasks**

```python
def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task['name']} (Due: {task['due']})")
```

- **Purpose**: Displays all tasks with their due dates.
- **Implementation**:
  - If the `tasks` list is empty, print a message indicating no tasks.
  - Otherwise, iterate over the list and print each task with its index, name, and due date.

#### **2.5 Delete Task**

```python
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
```

- **Purpose**: Deletes a task based on user input.
- **Implementation**:
  - Call `list_tasks()` to show all tasks to the user.
  - Prompt the user to enter the number of the task to delete and convert it to an integer.
  - Validate the input to ensure it’s within the valid range.
  - Remove the task using `tasks.pop()` and save the updated list.
  - Print a confirmation message or an error if the input is invalid.

### 3. **Main Function**

```python
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
```

- **Purpose**: Manages the main application loop.
- **Implementation**:
  - Load the tasks at the start.
  - Continuously display the menu and prompt the user for their choice.
  - Call the appropriate function based on user input.
  - Break the loop and exit the program if the user chooses to exit.
  - Handle invalid choices by prompting the user to choose again.

### 4. **Run the Script**

```python
if __name__ == "__main__":
    main()
```

- **Purpose**: Ensures the `main()` function is executed only if the script is run directly (not when imported as a module).
- **Implementation**: Calls `main()` to start the application.

This script provides a basic CLI task tracker with essential functionality, making it a good starting point for more advanced features or a more sophisticated interface.
