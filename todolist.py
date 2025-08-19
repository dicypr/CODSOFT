

tasks = []

def addTask():
  """Adds a new task to the list."""
  task = input("Please enter a task: ")
  if task:
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
  else:
    print("Task cannot be empty. Please try again.")

def listTasks():
  """Lists all tasks with a user-friendly, 1-based index."""
  if not tasks:
    print("There are no tasks currently.")
  else:
    print("\nCurrent Tasks:")
    print("--------------------")
    for index, task in enumerate(tasks):
      print(f"{index + 1}. {task}")
    print("--------------------")

def deleteTask():
  """Deletes a task by its number."""
  listTasks()  
  if not tasks:
    return 
    
  try:
    taskToDelete = int(input("\nEnter the number of the task to delete: ")) - 1
    
    if 0 <= taskToDelete < len(tasks):
      removed_task = tasks.pop(taskToDelete)
      print(f"Task '{removed_task}' has been removed.")
    else:
      print(f"Error: Task #{taskToDelete + 1} was not found. Please enter a valid number.")
  except ValueError:
    print("Invalid input. Please enter a number.")
  except IndexError:
    print("Error: The number you entered is out of range.")


if __name__ == "__main__":
 
  print("Welcome to the To-Do List App :)")
  while True:
    print("\nPlease select one of the following options")
    print("------------------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
      addTask()
    elif choice == "2":
      deleteTask()
    elif choice == "3":
      listTasks()
    elif choice == "4":
      break
    else:
      print("Invalid input. Please try again.")

  print("Goodbye 👋👋")
