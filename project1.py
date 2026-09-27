tasks = []

while True:

    print("\n==============================")
    print("       SMART TO-DO LIST")
    print("==============================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task Completed")
    print("5. Search Task")
    print("6. Task Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":

        task = input("Enter your task: ")

        tasks.append({
            "task": task,
            "status": "Pending"
        })

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            print("\n--------- MY TASKS ---------")

            for i in range(len(tasks)):
                print(
                    i + 1,
                    ".",
                    tasks[i]["task"],
                    "[",
                    tasks[i]["status"],
                    "]"
                )

    # Delete Task
    elif choice == "3":

        if len(tasks) == 0:
            print("No tasks to delete.")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])

            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print("Deleted:", deleted["task"])

            else:
                print("Invalid task number.")

    # Complete Task
    elif choice == "4":

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i in range(len(tasks)):
                print(
                    i + 1,
                    ".",
                    tasks[i]["task"],
                    "[",
                    tasks[i]["status"],
                    "]"
                )

            number = int(input("Enter task number: "))

            if number >= 1 and number <= len(tasks):
                tasks[number - 1]["status"] = "Completed"
                print("Task completed!")

            else:
                print("Invalid task number.")

    # Search Task
    elif choice == "5":

        search = input("Enter keyword to search: ")

        found = False

        for i in range(len(tasks)):

            if search.lower() in tasks[i]["task"].lower():

                print(
                    i + 1,
                    ".",
                    tasks[i]["task"],
                    "[",
                    tasks[i]["status"],
                    "]"
                )

                found = True

        if found == False:
            print("No matching task found.")

    # Statistics
    elif choice == "6":

        total = len(tasks)
        completed = 0
        pending = 0

        for task in tasks:

            if task["status"] == "Completed":
                completed += 1

            else:
                pending += 1

        print("\n--------- STATISTICS ---------")
        print("Total Tasks     :", total)
        print("Completed Tasks :", completed)
        print("Pending Tasks   :", pending)

    # Exit
    elif choice == "7":

        print("Thank you for using Smart To-Do List!")
        break

    else:

        print("Invalid choice. Please try again.")