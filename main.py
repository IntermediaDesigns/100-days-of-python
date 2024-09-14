import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Guess Who?")
window.geometry("400x400")


def showImage():
    person = text.get("1.0", "end").strip().lower()
    newImage = None
    try:
        if person in ['charlotte', 'gerald', 'katie', 'mo']:
            newImage = ImageTk.PhotoImage(
                Image.open(f"Guess Who/{person}.jpg"))
            canvas.itemconfig(container, image=newImage)
            canvas.image = newImage
            warning.pack_forget()
            canvas.pack()
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        canvas.pack_forget()
        warning.pack()


hello = tk.Label(text="Guess Who?")
hello.pack()

text = tk.Text(window, height=1, width=30)
text.pack()

button = tk.Button(text="Find", command=showImage)
button.pack()

canvas = tk.Canvas(window, width=400, height=281)
canvas.pack()

warning = tk.Label(text="Image not found")
container = canvas.create_image(200, 140, image=None)

tk.mainloop()
