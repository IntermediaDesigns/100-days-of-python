# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## No Replacement Image

👉 Why is it not showing the new image when I click the button?


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
canvas.pack()

image = tk.PhotoImage(file="theFeels.png") 
image = image.subsample(5)

container = canvas.create_image(150,1,image=image)


tk.mainloop()
```

<details> <summary> 👀 Answer </summary>

All the images should be defined in the main body of the code, not in the subroutine.  If they're in the subroutine, the variables are **local** - they only exist inside the subroutine. So they can't be accessed by the rest of the program.

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
# Moved from the sub to the main program

container = canvas.create_image(150,1,image=image)


tk.mainloop()
```

</details>


