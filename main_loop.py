import func



def loop():
    while True:
        func.entry()

        inpt = input("\nChoose an option: ")

        if inpt == "1":
            func.create_task()
        elif inpt == "2":
            func.load_tasks()
        elif inpt == "3":
            func.load_tasks()
            try:
                task_num = int(input("Enter task number to mark as done: "))
                func.mark_task(task_num)
            except ValueError:
                print("Please enter a valid number!")
        elif inpt == "4":
            func.load_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                func.delete_task(task_num)
            except ValueError:
                print("Please enter a valid number!")
        elif inpt == "5":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
