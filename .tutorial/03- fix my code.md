# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
password = environ['password'] 

userPass = input("Password > ")

if userPass == password:
  print("Well done")
else:
print("Better luck next time")
```

<details> <summary> 👀 Answer </summary>

```python
import os # No import

password = os.environ['password'] #Missed the os before environ

userPass = input("Password > ")

if userPass == password:
  print("Well done")
else:
  print("Better luck next time") # Indent error, just to keep you on your toes!
```
</details>