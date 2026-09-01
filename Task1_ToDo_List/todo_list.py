# CODSOFT Python Programming Internship
# Task 1: To-Do List

tasks = []


def show_tasks():
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n------ YOUR TASKS ------")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def add_task():
    task = input("\nEnter a new task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def delete_task():
    show_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n==============================")
        print("        TO-DO LIST APP")
        print("==============================")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("Thank you for using the To-Do List!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
