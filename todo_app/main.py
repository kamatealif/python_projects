from datetime import datetime
import csv
from prettytable import PrettyTable

# Function to ensure the file exists and has headers
def ensure_file_with_headers(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            if headers != ['Task ID', 'Task', 'Status', 'Due Date']:
                raise FileNotFoundError
    except (FileNotFoundError, StopIteration):
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task ID', 'Task', 'Status', 'Due Date'])

# Function to get the next auto-increment ID
def get_next_id(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers
            ids = [int(row[0]) for row in reader if row]
            return max(ids) + 1 if ids else 1
    except FileNotFoundError:
        return 1

# Function to add a new task
def add_task(file_name):
    task_id = get_next_id(file_name)
    task = input("Enter task: ")
    status = input("Enter status (complete/pending/cancelled): ")
    due_date = input("Enter due date (yyyy-mm-dd, leave blank for today's date): ")

    # If due_date is empty, use today's date
    if not due_date.strip():
        due_date = datetime.today().strftime('%Y-%m-%d')  # Format: yyyy-mm-dd

    with open(file_name, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task_id, task, status, due_date])
    print(f"Task added successfully with ID {task_id}")

# Function to view tasks
def view_tasks(file_name):
    table = PrettyTable(['Task ID', 'Task', 'Status', 'Due Date'])
    try:
        with open(file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip headers
            for row in reader:
                table.add_row(row)
        print(table)
    except FileNotFoundError:
        print("No tasks found. Please add a task first.")

# Function to update a task
def update_task(file_name):
    task_id = input("Enter the task ID to update: ")
    updated_rows = []
    task_found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        updated_rows.append(headers)
        for row in reader:
            if row[0] == task_id:
                task_found = True
                row[1] = input("Enter the new task: ")
                row[2] = input("Enter the new status: ")
                row[3] = input("Enter the new due date: ")
            updated_rows.append(row)

    if task_found:
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("Task updated successfully.")
    else:
        print("Task ID not found.")

# Function to delete a task
def delete_task(file_name):
    task_id = input("Enter the task ID to delete: ")
    updated_rows = []
    task_found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        updated_rows.append(headers)
        for row in reader:
            if row[0] == task_id:
                task_found = True
                continue
            updated_rows.append(row)

    if task_found:
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        print("Task deleted successfully.")
    else:
        print("Task ID not found.")
# Function to delete all records but keep headers
def delete_all_tasks(file_name):
    try:
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Task ID', 'Task', 'Status', 'Due Date'])  # Write the headers back
        print("All tasks deleted successfully.")
    except FileNotFoundError:
        print("File not found. Please create or add tasks first.")

# Function to show the menu
def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    print("6. DELETE ALL THE TASKS AND EXIT")

# Main function
def main(file_name):
    ensure_file_with_headers(file_name)
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_task(file_name)
            case "2":
                view_tasks(file_name)
            case "3":
                update_task(file_name)
            case "4":
                delete_task(file_name)
            case "5":
                print("Exiting the application. Goodbye!")
                break
            case "6":
                delete_all_tasks(file_name)
                break;
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    file_name = "tasks.csv"
    main(file_name)
