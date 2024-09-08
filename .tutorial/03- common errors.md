# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## No Such File

👉 Why am I getting a 'no such file' error?

```python
f = open("calendar.txt","r") 
myEvents = eval(f.read())
f.close()
```

<details> <summary> 👀 Answer </summary>

Well friends, this happens when the file does not exist yet.  The auto-load code below tries to open the file and if it can't find it, it crashes.  There **has to be** a 'calendar.txt' file for it to work.

This fix is a temporary one because we'll learn how to sort this properly in tomorrow's lesson.

For today, we'll just comment out the auto-load code to give the auto-save the chance to create the file.

```python
#f = open("calendar.txt","r") 
#myEvents = eval(f.read())
#f.close()
```

Once the file has been created, remove the comments to enable auto-load.

</details>

