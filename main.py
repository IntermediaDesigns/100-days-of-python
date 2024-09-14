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