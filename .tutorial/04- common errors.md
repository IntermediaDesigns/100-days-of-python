# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## InKeyRect

👉 What's the problem here?


```python
from replit import db

value = db["key"]
```

<details> <summary> 👀 Answer </summary>

The key 'key' doesn't exist in the database. Let's use a `try except` to catch it. 

`pass` is a line of code that tells the program ' don't worry about this just yet, no need to do anything'. 

I've used it here to avoid crashing the program by leaving a blank line after `except`.  I'd probably return to this later and replace the pass with a proper error message.

```python
from replit import db

try:
  value = db["key"]
except:
  pass
```

</details>

## Where's The Data?

👉 What is the problem here?
```python
from replit import db

keys = db.keys
for key in keys:
  print(key)
```

<details> <summary> 👀 Answer </summary>

The code would output the names of all the keys, but not the data.

We'll change the print statement a little and include the 'Get key value' from the database menu. I've used a nice little fString technique here too.

```python
from replit import db

keys = db.keys()
for key in keys:
  print(f"{key}: {db[key]}")
```
</details>

