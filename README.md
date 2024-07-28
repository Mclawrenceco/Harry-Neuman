
## Introduction

This is a simple command-line interface (CLI) application designed to help you manage your daily tasks. This Python script allows you to add, list, and delete tasks, providing a straightforward way to keep track of your to-dos. It uses a JSON file for persistent storage, making it easy to keep your tasks organized.

## Features

- **Add Task**: Add new tasks with a name and due date.
- **List Tasks**: View all your tasks with their due dates.
- **Delete Task**: Remove tasks from your list by specifying their number.
- **Persistent Storage**: Tasks are saved in a `tasks.json` file, so your data is preserved between sessions.

## Setup

### Prerequisites

- Python 3.x installed on your local machine.

### Installation

1. **Clone or Download the Repository**

   If you have Git installed, you can clone the repository:
   ```bash
   git clone <repository-url>
   ```

   Alternatively, download the script directly from the repository's page.

2. **Navigate to the Script Directory**

   Open your terminal or command prompt and navigate to the directory where the script is located:
   ```bash
   cd path/to/script
   ```

## Usage

1. **Run the Script**

   Execute the script using Python:
   ```bash
   python task_tracker.py
   ```

2. **Interact with the CLI**

   - **Add Task**: Choose option `1` and enter the task name and due date when prompted.
   - **List Tasks**: Choose option `2` to display all your tasks and their due dates.
   - **Delete Task**: Choose option `3`, then enter the number of the task you wish to delete.
   - **Exit**: Choose option `4` to exit the application.

## Example

Here’s an example of how the CLI interaction might look:

```plaintext
Task Tracker
1. Add Task
2. List Tasks
3. Delete Task
4. Exit
Choose an option: 1
Enter task name: Finish project report
Enter due date (YYYY-MM-DD): 2024-08-15
Task 'Finish project report' added.

Task Tracker
1. Add Task
2. List Tasks
3. Delete Task
4. Exit
Choose an option: 2
1. Finish project report (Due: 2024-08-15)

Task Tracker
1. Add Task
2. List Tasks
3. Delete Task
4. Exit
Choose an option: 3
Enter task number to delete: 1
Task 'Finish project report' deleted.
```

## Notes

- The `tasks.json` file will be created in the same directory as the script. If the file is deleted or corrupted, tasks will be lost.
- This application is a basic task tracker and is intended for personal use or as a learning project.

## Contributing

Feel free to fork the repository and submit pull requests if you have improvements or additional features to suggest.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
