# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## It's outputting a blank at the end?

👉 What's wrong with this code


```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  print(contents)
  
  if contents == "":
    break
```
<details> <summary> 👀 Answer </summary>

- The print goes after the break (but not inside the selection branch).

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break

  print(contents)
  
```

</details>

## Make it stop! MAKE IT STOP!

👉 What is the problem here?
```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  print(contents)
  
```

<details> <summary> 👀 Answer </summary>

Somebody forgot to break the while loop. no dessert for you....

```python
f = open("filenames.list","r")
while True:
  contents = f.readline().strip()
  
  if contents == "":
    break

  print(contents)

```


</details>

