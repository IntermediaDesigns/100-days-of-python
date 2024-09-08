# Keys and Dictionaries

I'm a comuter scientist and I *love* a good database. 

One of the most powerful things we can do is assign more than just one piece of data to a key. We could assign a whole list, or a dictionary.

👉 This example uses 'david' as the key, and a dictionary as the value. Look at how we can use this to store all of the user data in one key location.

```python
from replit import db

db["david"] = {"username": "dmorgan", "password":"baldy1"}
```

List all the keys:

```python
from replit import db

keys = db.keys()
print(keys)
```

## Individual Elements
👉 Now I can access individual elements in the dictionary in the normal way.

```python
from replit import db

value = db["david"]
print(value["password"])
```

### Try it out!