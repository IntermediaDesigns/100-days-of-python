myToDoList = []


def printList():
  print()
  for item in myToDoList:
    print(item)
  print()


while True:
  menu = input("View, edit, add, remove, or erase?: ")
  print()
  # if list is empty, display message
  if menu == "view":
    if len(myToDoList) == 0:
      print("Your list is empty.")
      print()
    else:
      printList()
      print()

  elif menu == "add":
    item = input("What should I add to the list?: ")
    print()
    # Check for duplicate
    if item not in myToDoList:
      myToDoList.append(item)
      printList()
      print()
    else:
      print(f"{item} is already in the list")
      print()
  elif menu == "remove":
    item = input("What should I remove from the list?: ")
    print()
    # Check if user really wants to remove item from list
    if item in myToDoList:
      confirm = input(
          f"Are you sure you want to remove {item} from the list? (yes/no): ")
      print()
      if confirm.lower() == "yes":
        myToDoList.remove(item)
        printList()
      else:
        print(f"{item} was not removed from the list")
        printList()
        print()
    else:
      print(f"{item} was not in the list")
      printList()
      print()
  elif menu == "edit":
    item = input("What do you want to edit?: ")
    print()
    if item in myToDoList:
      newItem = input("What do you want to change it to?: ")
      print()
      if newItem not in myToDoList:
        for i in range(len(myToDoList)):
          if myToDoList[i] == item:
            myToDoList[i] = newItem
        printList()
        print()
      else:
        print(f"{newItem} is already in the list")
        printList()
        print()
    else:
      print(f"{item} was not in the list")
      print()
      printList()
      print()
  # Give user option to completely erase list
  elif menu == "erase":
    confirm = input(
        "Are you sure you want to erase the entire list? (yes/no): ")
    print()
    if confirm.lower() == "yes":
      myToDoList.clear()
      print("The list has been erased.")
      print()
    else:
      print("The list was not erased.")
      printList()
      print()
  else:
    print("Invalid input")
    print()
