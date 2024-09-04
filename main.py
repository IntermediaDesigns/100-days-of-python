print(" 🌟 Life Organizer 🌟 ")
print()
toDoList = []
def printList():
  print()
  for item in toDoList:
    print(item)
  print()
while True:
  menu = input("Do you want to add, view, edit or remove a to do? ")
  print()
  if menu == "add":
    item = input("What is the task? ")
    print()
    due = input("When is it due by? ")
    print()
    priority = input("What is the priority? ")
    print()
    row = [item, due, priority]
    toDoList.append(row)
    print("Thanks, this task has been added.")
    print()
  elif menu == "view":
    view = input("Do you want to view all or view priority? ")
    print()
    if view == "all":
      print("Here is your to do list: ")
      print()
      printList()
      print()
    elif view == "priority":
      priority = input("What priority? ")
      print()
      for row in toDoList:
        if priority in row:
          for item in row:
            print(item, end=" | ")
          print()
      print()
  elif menu == "edit":
    edit = input("What do you want to edit? ")
    print()
    for row in toDoList:
      if edit in row:
        toDoList.remove(row)
        item = input("What is the task? ")
        print()
        due = input("When is it due by? ")
        print()
        priority = input("What is the priority? ")
        print()
        row = [item, due, priority]
        toDoList.append(row)
        print("Thanks, this task has been edited.")
        print()
  elif menu == "remove":
    remove = input("What do you want to remove? ")
    print()
    for row in toDoList:
      if remove in row:
        toDoList.remove(row)
        print("Thanks, this task has been removed.")
        print()
  else:
    print("Invalid input")
    print()

  quit = input("Do you want to see the menu again or quit? ")
  print()
  if quit == "quit" or quit == "no":
    exit()
  else:
    continue