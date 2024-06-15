import sys

tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    print("\nTo-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def update_task():
    view_tasks()
    task_number = int(input("Enter the task number to update: "))
    if 1 <= task_number <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_number - 1] = new_task
        print(f"Task {task_number} updated.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)
        print(f"Task {task_number} deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
