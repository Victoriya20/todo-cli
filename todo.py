todo_list = []

def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again!")
