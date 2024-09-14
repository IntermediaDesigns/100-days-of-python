# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Headers Up!

👉 What's the problem here?


```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
  username = request.header["X-Replit-User-Name"]
  return f"Hello {username}"

app.run(host='0.0.0.0', port=81)
```

<details> <summary> 👀 Answer </summary>
  
This is a mistake I make **all** the time, it's `headers` not `header`. This will throw an 'Internal Server Error'.

```python
  username = request.headers["X-Replit-User-Name"]
```
</details>

