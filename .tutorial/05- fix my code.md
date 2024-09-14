# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

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

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) # New line here

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = .Button(text = "Another Button", command = updateLabel).grid(row=2, column=1)

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```

<details> <summary> 👀 Answer </summary>

```python
import tkinter as tk # No import

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

global label
  number = text.get("1.0","end") 
  number = int(number) 
  label += number
  hello["text"] = label 
  

hello = tk.Label(text = label)
hello.grid(row=0, column=1) # Needs grid on a new line.

text = tk.Text(window ,height=1, width = 50)
text.grid(row=1, column=1) 

button = tk.Button(text = "Click me!", command = updateLabel).grid(row=2, column=0)

button = tk.Button(text = "Another Button", command = updateLabel).grid(row=2, column=1) # Missed the '.tk'

button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

tk.mainloop()
```




</details>