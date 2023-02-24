# Eric Cuevas, Andrew Molina
# Assigned February 21, due February 23, submitted February 23, 2023
# A program that maintains a task list for the user.  The user should be able to view the current task, mark the current task complete, postpone the current task, or to add a new task.  The program will read the list from a file (‘tasklist.txt’) when the program begins and then store the updated list by overwriting the old contents when the user quits the program.

from task import Task


def main_menu():
  """Displays the main menu and returns the user’s valid input.
  """
  print("-Task List-\n")
  print("1. Display current task")
  print("2. Mark current task complete")
  print("3. Postpone current task")
  print("4. Add new task")
  print("5. Save and quit")
  choice = input("\nEnter your choice (1-5): ")
  while choice not in ["1", "2", "3", "4", "5"]:
    choice = input("Invalid choice. Enter your choice (1-5): ")
  return int(choice)


def read_file(filename):
  """Passes in a string with the file’s name.  Open the file and read in each line that consists of the task description, due date, and time separated by commas. Construct a task from each line and add it to a list.  Return the filled task list. 
  """
  tasks = []
  try:
    with open(filename, "r") as f:
      for line in f:
        line = line.strip()
        if line:
          description, date, time = line.split(",")
          tasks.append(Task(description, date, time))
  except FileNotFoundError:
    pass
  return tasks


def write_file(filename, task_lists):
  """Passes in a string with the file’s name and the list of tasks to be written to the file.  Iterate through the list of tasks and write each one to the file using the Task’s repr method (ie. description, date, and time separated by spaces). 
  """
  with open(filename, "w") as f:
    for tasks in task_lists:
      f.write(repr(tasks) + "\n")


def get_date():
  """Prompts the user to enter the year, month, and day.  Valid years are 2000-3000, valid months are 1-12, and valid days are 1-31 (no need to verify that it is a correct day for the month (ie. Feb 31st is valid)).  Return the date in the format: YYYY/MM/DD. If the inputted month or day is less than 10, then add a 0 to format it correctly. 
  """
  year = input("Enter year (2000-3000): ")
  while not year.isdigit() or not 2000 <= int(year) <= 3000:
    year = input("Invalid year. Enter year (2000-3000): ")
  month = input("Enter month (1-12): ")
  while not month.isdigit() or not 1 <= int(month) <= 12:
    month = input("Invalid month. Enter month (1-12): ")
  day = input("Enter day (1-31): ")
  while not day.isdigit() or not 1 <= int(day) <= 31:
    day = input("Invalid day. Enter day (1-31): ")
  date = f"{year}/{month.zfill(2)}/{day.zfill(2)}"
  return date


def get_time():
  """Prompts the user to enter the hour (military time) and minute.  Valid hours are 0-23 and valid minutes are 0-59. Return the date in the format: HH:MM.  If the inputted hour or minute is less than 10, then add a 0 to format it correctly. 
  """
  hour = input("Enter hour (0-23): ")
  while not hour.isdigit() or not 0 <= int(hour) <= 23:
    hour = input("Invalid hour. Enter hour (0-23): ")
  minute = input("Enter minute (0-59): ")
  while not minute.isdigit() or not 0 <= int(minute) <= 59:
    minute = input("Invalid minute. Enter minute (0-59): ")
  time = f"{hour.zfill(2)}:{minute.zfill(2)}"
  return time


def main():
  """The function starts by reading in the contents of the tasklist.txt file and storing them in a list called 'task_list'. It then enters a loop where it displays the number of tasks in the list and prompts the user for their choice. Depending on the user's choice, the function calls the appropriate function to display the current task, mark the current task complete, postpone the current task, add a new task, or save and quit. If the user chooses to save and quit, the function writes the contents of the 'task_list' back to the 'tasklist.txt' file and exits the loop to end the program.
  """
  task_list = read_file('tasklist.txt')
  while True:
    print(f"Number of tasks: {len(task_list)}\n")
    choice = main_menu()
    if choice == 1:
      if len(task_list) > 0:
        print(f"Current task:\n{task_list[0]}")
      else:
        print("All tasks are complete!")
    elif choice == 2:
      if len(task_list) > 0:
        print(f"Completing task:\n{task_list[0]}")
        task_list.pop(0)
        if len(task_list) > 0:
          print(f"\nNew current task:\n{task_list[0]}")
        else:
          print("\nAll tasks are complete!")
      else:
        print("All tasks are complete!")
    elif choice == 3:
      if len(task_list) > 0:
        print(f"Postponing task:\n{task_list[0]}")
        new_date = get_date()
        new_time = get_time()
        task_list[0].date = new_date
        task_list[0].time = new_time
        task_list.sort()
        print(f"\nNew current task:\n{task_list[0]}")
      else:
        print("All tasks are complete!")
    elif choice == 4:
      desc = input("Enter task description: ")
      date = get_date()
      time = get_time()
      task = Task(desc, date, time)
      task_list.append(task)
      task_list.sort()
      print(f"\nNew task added:\n{task}")
    elif choice == 5:
      write_file('tasklist.txt', task_list)
      print("Your task list was saved. Goodbye!")
      break
    else:
      print("Invalid choice. Please choose again.\n")


main()
