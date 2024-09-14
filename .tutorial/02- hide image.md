# Hiding Images

Here's our image code from Day 67.

```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  canvas.itemconfig(container, image = newImage)

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()


canvas = tk.Canvas(window, width = 300, height=150) 
canvas.pack()
image = tk.PhotoImage(file="theFeels.png") 
image = image.subsample(5)

newImage = tk.PhotoImage(file="success.png") 
newImage = newImage.subsample(5) 

container = canvas.create_image(150,1,image=image) 

tk.mainloop()
```

👉 I'm going to add a second button called 'button2' that will hide the image.  Actually, what we're *really* doing is hiding the canvas. Here's the isolated code for that.
```python
button2 = tk.Button(text = "Hide Image!", command=hideImage) 
button2.pack()
```
##
👉 Next I need to create the `hideImage` sub **above** the button creation. The isolated code is:

```python
def hideImage():
  canvas.pack_forget()
```
##
👉 Now, here are those code snippets as part of the whole program: 
```python
import tkinter as tk

window = tk.Tk()
window.title("Hello World") 
window.geometry("300x200") 

def changeImage():
  canvas.itemconfig(container, image = newImage)

#### NEW SUBROUTINE ######
def hideImage():
  canvas.pack_forget()

hello = tk.Label(text = "Hello World") 
hello.pack() 

button = tk.Button(text = "Click me!", command=changeImage) 
button.pack()

#### NEW BUTTON ######
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

### Try it out!