# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## What Is Recursion?

👉 What's the problem here?

```python
def reverse(value):

  for i in range(value):
    print("💯", end="") 
    
  print() 
  reverse(value - 1)
reverse(10)
```

<details> <summary> 👀 Answer </summary>

There is no ending condition. It will repeat until it eats up **all** of the machine's resources until there's no more RAM left!  Then, it crashes.

Python has a limit to the amount of recursion. If it didn't, then you'd have unleashed a RAM eating monster!

```python
def reverse(value):
  if value <= 0:
    print("Done!")
    return
  else: 
    for i in range(value):
      print("💯", end="") 
      
    print() 
    reverse(value - 1)
    
reverse(10)
```

</details>

