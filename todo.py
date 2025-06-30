# todo.py

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def show_menu():
    print("\n§ To-Do List §")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("\nNo tasks found.")

        elif choice == '2':
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks, filename)
            print("Task added.")

        elif choice == '3':
            if not tasks:
                print("No tasks to remove.")
                continue
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter the task number to remove: "))
                if 1 <= index <= len(tasks):
                    removed = tasks.pop(index - 1)
                    save_tasks(tasks, filename)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()
