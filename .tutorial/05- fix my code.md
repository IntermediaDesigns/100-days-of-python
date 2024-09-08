# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python

keys = db.key

for key in keys
print(key)
```

<details> <summary> 👀 Answer </summary>

```python
from replit import db # no import

keys = db.keys() # missing 's' from 'key', missing brackets
for key in keys: #missing colon
  print(f"{key}: {db[key]}") # Not indented. Only outputted the key.
```
*You will still get an 'attribution error' if you have not defined 'key'.*
</details>