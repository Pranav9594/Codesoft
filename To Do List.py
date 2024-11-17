todo_list = []

def display_menu():
    print("\n-- To-Do List Menu --")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, 1):
            print(f"{index}. {task}")

def add_task():
    task = input("\nEnter a task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def remove_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 0 < task_num <= len(todo_list):
                removed_task = todo_list.pop(task_num - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

while True:
    display_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
