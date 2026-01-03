Tasks = []
print("Welcome to your To-Do List!")
print("Type 1 to add a task\nType 2 to view tasks\nType 3 to remove a task\nType 4 to exit the program")
while True:
    choice = input("Enter your choice: ")
    if choice.lower() == '4':
        print("Thank you using our TO-DO List")
        break
    elif choice == "1":
        task = input("Enter your task:  ")
        Tasks.append(task)
    elif choice == "2":
        if not Tasks:
            print("Your to-do list is empty.")
        else:
            print("Your current active task are shown here:")
            for idx, task in enumerate(Tasks, 1):
                print(f"{idx}. {task}")
    elif choice == "3":
        if not Tasks:
            print("Your to-do list is empty.")
        else:
            print("the active tasks are shown here.:")
            for idx, task in enumerate(Tasks, 1):
                print(f"{idx}. {task}")
                delete = input("Enter the task number you want to delete from the list:  \nType 'done' when completed: ")
                if delete.lower == "done":
                    break
                if delete.isdigit():
                    delete_index = int(delete)
                    if 1 < delete_index:
                        print("invalid task number.\n\tPlease enter a valid task number.")
                    else:
                        Tasks.pop(delete_index-1)
                        print(f"the task {delete_index} has been removed from the list..")
                        if not Tasks:
                            print("Your list is now empty.")
                        else:
                            print("Your active tasks are represented below for your guineune consont:")
                            for idx, task in enumerate(Tasks, 1):
                                print(f"{idx}. {Tasks}")
                            else:
                                print("Your to-do list is Empty.")