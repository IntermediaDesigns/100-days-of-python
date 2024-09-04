myToDoList = []

def printList():
  print() 
  for item in myToDoList:
    print(item)
  print() 

while True:
  menu = input("View, edit, add, or remove?: ")
  printList()
  if menu == "view":
    printList()
  elif menu == "add":
    item = input("What should I add to the list?: ")
    myToDoList.append(item)
    printList()
  elif menu == "remove":
    item = input("What should I remove from the list?: ")
    if item in myToDoList:
      myToDoList.remove(item)
      printList()
    else:
      print(f"{item} was not in the list")
      printList()
  elif menu == "edit":
    item = input("What do you want to edit?: ")
    printList()
    new = input("What do you want to change it to?: ")
    printList()
    for i in range(0,len(myToDoList)):
      if myToDoList[i]==item:
        myToDoList[i]=new
  else:
    print("Invalid input")