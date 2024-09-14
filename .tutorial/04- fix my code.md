# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  canvas.itemconfig(container, image = newImage)

def hideImage():
  container.pack_forget()

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()

button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()


canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()

image = tk.PhotoImage(file="theFeels.png") 
image = image.subsample(5)

newImage = tk.PhotoImage(file="success.png") 
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image) 

tk.mainloop()
```

<details> <summary> 👀 Answer </summary>
Oh no! This was a *really* tricky one. di you get it?

Yep, we were tyring to hide the container instead of the canvas.
```python
def hideImage():
  canvas.pack_forget()
```

</details>