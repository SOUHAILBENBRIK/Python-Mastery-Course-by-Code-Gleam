import os

# File to store the to-do list
FILE_NAME = 'tasks.txt'

# Read tasks from the file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r') as file:
        tasks = [line.strip().split(' - ') for line in file.readlines()]
        return [{'task': t[0], 'status': t[1]} for t in tasks]

# Save tasks to the file
def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(f"{task['task']} - {task['status']}\n")

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = '✔' if task['status'] == 'complete' else '✗'
        print(f"{idx}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task: ").strip()
    if task_name:
        tasks.append({'task': task_name, 'status': 'incomplete'})
        print(f"Task '{task_name}' added.")
    else:
        print("Task cannot be empty.")

# Mark a task as complete
def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]['status'] = 'complete'
            print(f"Task '{tasks[task_num - 1]['task']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 0 < task_num <= len(tasks):
            task = tasks.pop(task_num - 1)
            print(f"Task '{task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point
if __name__ == '__main__':
    main()
