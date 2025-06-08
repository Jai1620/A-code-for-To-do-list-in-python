todo_list = []

def show_tasks():
    print("\n Your Tasks:")
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, taks in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print("f Added task: {task}")


def delete_task(index):
    try:
        removed = todo_list.pop(index -1)
        print(f" Deleted task: {removed}")

    except IndexError:
        print("Invalid task number.")


#Main loop
while True:
    print("\n ---  TO-DO LIST MENU---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")


    choice = input("Enter your choice (1-4):")


    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter task:")
        add_task(task)
    elif choice == "3":
        show_task()
        try:
            num = int(input("Enter task number to delete:"))
            delete_task(num)
        except ValueError:
            print("Enter a valid number.")
    elif choice == "4":
        print("See ya, Stay productive!")
        break
    else:
        print("Invalid choice, try again!")
