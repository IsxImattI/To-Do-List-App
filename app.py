print("Welcome to To-Do-List App! \n")

tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!\n")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available!\n")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: "))
    if task_number > len(tasks):
        print("Invalid task number!\n")
    else:
        task = tasks.pop(task_number-1)
        print(f"Task '{task}' deleted successfully!\n")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        delete_task()
    elif choice == 4:
        break
    else:
        print("Invalid choice!\n")

print("Thank you for using To-Do-List App!")