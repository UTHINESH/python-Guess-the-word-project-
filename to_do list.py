# To-Do List Application

# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(tasks, new_task):
    tasks.append(new_task)
    print(f"Task '{new_task}' added successfully.")

# Function to mark a task as completed
def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")

# Main function
def main():
    tasks = []

    while True:
        print("\nMenu:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task index to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == '4':
            print("Quitting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
