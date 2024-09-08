# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
myEvents = []

f = open("calendar.txt","r")
myEvents = eval(f.read())
f.close()

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
        myevents.remove(row)

  
f = open("calendar.txt", "w") 
f.write(str(myEvents)) 
f.close()
```

<details> <summary> 👀 Answer </summary>

```python
myEvents = []

# Will crash on first run if file doesn't exist
#f = open("calendar.txt","r") 
#myEvents = eval(f.read())
#f.close() # Forgot to close the file


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
        myEvents.remove(row) # List identifier wasn't correct

  # Lines below weren't indented to make them part of the loop.
  f = open("calendar.txt", "w") 
  f.write(str(myEvents)) 
  f.close()
```



</details>