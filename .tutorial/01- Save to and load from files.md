# Save to and Load From Files

There are some things that *primary* storage in the RAM does better. 

For example, it's easy to access, amend, or remove a piece of data held in a list (in the RAM).

Holding data in *secondary* storage in a file makes this more difficult. Or does it?

With Python, there's more than meets the eye.

## 


👉 The program below lets me add & remove events and dates into a diary system.
It adds the name & date of an event to the 2D list.  Or it searches for an existing name & date and removes it.

```python
myEvents = []

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)
```
Manually saving and loading from this program to a file each time would be a massive faff. Instead, we can set up an auto-save by writing the save code at the end of our infinite loop.

## Auto-Save



👉 At the bottom of the code, we are going to add an autosave **just before the loop repeats**.

*Make sure this new code matches the indent for the while loop, so it is part of the loop.*


```python
myEvents = []

def prettyPrint():
  print()
  for row in myEvents:
    print(f"{row[0] :^15} {row[1] :^15}")
  print()

while True:
  menu = input("1: Add, 2: Remove\n")

  if menu == "1":
    event = input("What event?: ").capitalize()
    date = input("What date?: ")
    row = [event,date]
    myEvents.append(row)
    prettyPrint()

  else:
    criteria = input("What event do you want to remove?: ").title()
    for row in myEvents:
      if criteria in row:
        myEvents.remove(row)

  ########### THIS IS THE NEW BIT ########
  f = open("calendar.txt", "w") # Permissions set to 'w' because we are deleting the file and replacing it with the whole 2D list every time.
  f.write(str(myEvents)) # Need to cast the list to a single string
  f.close()
  #########################################
```

### 🐞 There is a potential problem with this system. Try running the program a few times and add events to the calendar.
