# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## 

👉 Why am I getting an attribute error when I try to `pack_forget` the container?


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
The container is not directly in the window, so it can't be hidden. The canvas is. That's what we have to hide.

```python
def hideImage():
  canvas.pack_forget()
```

</details>

