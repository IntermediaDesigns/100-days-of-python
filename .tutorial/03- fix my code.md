# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  newImage = tk.PhotoImage(file="success.png") 
  newImage = newImage.subsample(5) 
  canvas.itemconfig(container, image = newImage) 

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()

canvas = tk.Canvas(window, width = 300, height=150) 


image = tk.PhotoImage(file="theFeels.png") 
image = image.subsample(5)

container = canvas.create_image(150,1,image=image)

```

<details> <summary> 👀 Answer </summary>

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  newImage = tk.PhotoImage(file="success.png") 
   

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage)
button.pack()

canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack() # Didn't pack the canvas

image = tk.PhotoImage(file="theFeels.png") 
image = image.subsample(5)

newImage = newImage.subsample(5) 
canvas.itemconfig(container, image = newImage)
# Needed to create the images in the main program.

container = canvas.create_image(150,1,image=image)


tk.mainloop() # Missed out main loop
```



</details>