tasks = []

def display_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} ({status})")
    else:
        print("Your to-do list is empty.")

def add_task(task_name):
    tasks.append({"task": task_name, "completed": False})
    print(f"Task '{task_name}' added.")

def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task '{removed['task']}' removed.")
    else:
        print("Invalid task number.")

while True:
    choice = input("\n1. Display to-do list\n2. Add a task\n3. Mark a task as completed\n4. Remove a task\n5. Quit\nEnter your choice: ")
    if choice == '1': display_tasks()
    elif choice == '2': add_task(input("Enter the task: "))
    elif choice == '3': display_tasks() or mark_completed(int(input("Enter task number: ")))
    elif choice == '4': display_tasks() or remove_task(int(input("Enter task number: ")))
    elif choice == '5': break
    else: print("Invalid choice. Please try again.")
