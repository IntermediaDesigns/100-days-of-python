# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## Attribute Error

👉 Why is there a 'hello.pack()' attribute error?


```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label).grid(row=0, column=1)
hello.pack()

text = tk.Text(window ,height=1, width = 50).grid(row=1, column=1)

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

<details> <summary> 👀 Answer </summary>

`pack` doesn't work with `grid`. You have to decide to use one or the other.

</details>

## Another Attribute Error

👉 Why am I getting a 'NoneType' attribute error when I click a button?  My program was working, but now it isn't.
```python
text = tk.Text(window ,height=1, width = 50).grid(row=1, column=1)
```

<details> <summary> 👀 Answer </summary>

'Getting' the data from the text box worked nicely with `pack`, but not with `grid`.

The `grid` method is directly on the `text` object creation line of code. This causes issues when the `updateLabel` subroutine tries to `get` the contents of the text box.

Wherever I've used `grid` with the text box and the label, I need to split this out onto a separate line. This is because I want to manipulate this data later. I don't need to do it with the buttons because I don't need to manipulate that data.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label)
hello.grid(row=0, column=1) # New line here

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) # New line here

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```


</details>

