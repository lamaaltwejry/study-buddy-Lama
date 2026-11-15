# Simple Daily Task Manager

def show_menu():
    print("\n--- Daily Task Manager ---")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Complete / Remove a task")
    print("4. Exit")

def main():
    tasks = ["Review study notes", "Organize workspace"]
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks available right now.")
            else:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == "2":
            new_task = input("Enter the new task name: ").strip()
            if len(new_task) > 0 and len(new_task) <= 30:
                tasks.append(new_task)
                print("Task added successfully!")
            else:
                print("Please enter a task name between 1 and 30 characters.")
                
        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                try:
                    task_num = int(input("Enter the task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == "4":
            print("Goodbye! Have a productive day.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
    .
