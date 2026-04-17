import sys

def main():
    tasks = []
    while True:
        print("\n--- Simple Todo List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks in the list.")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '2':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")
        elif choice == '3':
            if not tasks:
                print("Nothing to remove.")
                continue
            try:
                idx = int(input("Enter task number to remove: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
