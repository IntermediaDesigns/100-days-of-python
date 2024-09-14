# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## There's a huge error message that includes 'KeyError'

👉 Why am I getting this error?


```python
import os

password = os.environ['password'] 

userPass = input("Password > ")

if userPass == password:
  print("Well done")
else:
  print("Better luck next time")
```

<details> <summary> 👀 Answer </summary>

Nothing wrong with your code here. You just haven't created a secret called 'password'.

</details>
