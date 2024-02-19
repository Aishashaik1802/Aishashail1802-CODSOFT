class TodoList:
  def __init__(self):
      self.tasks = []

  def add_task(self, task):
      self.tasks.append(task)
      print(f"Task '{task}' added.")

  def view_tasks(self):
      if self.tasks:
          print("Tasks:")
          for index, task in enumerate(self.tasks, start=1):
              print(f"{index}. {task}")
      else:
          print("No tasks.")

  def complete_task(self, index):
      if 1 <= index <= len(self.tasks):
          task = self.tasks[index - 1]
          print(f"Completed task: {task}")
          del self.tasks[index - 1]
      else:
          print("Invalid task index.")

  def remove_task(self, index):
      if 1 <= index <= len(self.tasks):
          task = self.tasks[index - 1]
          print(f"Removed task: {task}")
          del self.tasks[index - 1]
      else:
          print("Invalid task index.")

  def clear_tasks(self):
      self.tasks = []
      print("All tasks cleared.")

def main():
  todo_list = TodoList()

  while True:
      print("\n1. Add Task")
      print("2. View Tasks")
      print("3. Complete Task")
      print("4. Remove Task")
      print("5. Clear All Tasks")
      print("6. Quit")

      choice = input("Enter your choice: ")

      if choice == "1":
          task = input("Enter task: ")
          todo_list.add_task(task)
      elif choice == "2":
          todo_list.view_tasks()
      elif choice == "3":
          index = int(input("Enter task index to mark as completed: "))
          todo_list.complete_task(index)
      elif choice == "4":
          index = int(input("Enter task index to remove: "))
          todo_list.remove_task(index)
      elif choice == "5":
          todo_list.clear_tasks()
      elif choice == "6":
          break
      else:
          print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()