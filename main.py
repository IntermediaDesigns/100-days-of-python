names = []

def printList():
  print("List of names:")
  print()
  for i in names:
    print(i)
  print()

while True:
  firstName = input("First Name: ").strip().capitalize()
  print()
  lastName = input("Last Name: ").strip().capitalize()
  print()

  name = f"{firstName} {lastName}"

  if name not in names:
    names.append(name)
    print(f"Added {name} to list.")
    print()
    printList()

    item = input("Add another name to list? (yes/no): ").strip().lower()
    print()
    if item == "yes" or item == "y":
      continue
    else:
      break

  else:
    print("ERROR: Duplicate name in list.")
    print()
