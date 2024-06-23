class Task:
    def __init__(self, id, Name, Description):
        self.id = id
        self.name = Name
        self.description = Description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, id, name, description):
        new_task = Task(id, name, description)
        self.tasks.append(new_task)
        print(f"Task '{id}''{name}' created successfully.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(f"ID: {task.id}, Name: {task.name}, Description: {task.description}")

    def update_task(self, id, name, description):
        for task in self.tasks:
            if task.id == id:
                task.name = name
                task.description = description
                print(f"Task '{id}' '{name}' updated successfully.")
                return
        print(f"Task with ID '{id}' not found.")

    def delete_task(self, id):
        for task in self.tasks:
            if task.id == id:
                self.tasks.remove(task)
                print(f"Task '{id}' deleted successfully.")
                return
        print(f"Task with ID '{id}' not found.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            id = input("Enter task ID: ")
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            task_manager.create_task(id, name, description)
        elif choice == '2':
            task_manager.read_tasks()
        elif choice == '3':
            id = input("Enter task ID to update: ")
            name = input("Enter new task name: ")
            description = input("Enter new task description: ")
            task_manager.update_task(id, name, description)
        elif choice == '4':
            id = input("Enter task ID to delete: ")
            task_manager.delete_task(id)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
