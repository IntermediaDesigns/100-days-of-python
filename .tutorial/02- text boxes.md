# Adding Text
## Let's Talk About Text Baby

We can add text boxes to our windows using the entirely obvious `text` command.

👉 Here's the code you need in isolation:
```python

text = tk.Text(window ,height=1, width = 50)
# Three arguments, name of the window to place the text box in, height & width.
text.pack()

```

👉 And here it is in context.

```python
window = tk.Tk()
window.title("Hello World") 
window.geometry("300x300") 

label = 0

def updateLabel():
  global label
  label += 1 
  hello["text"] = label 
  

hello = tk.Label(text = label) 
hello.pack() 

button = tk.Button(text = "Click me!", command = updateLabel) 
button.pack()

text = tk.Text(window ,height=1, width = 50)
text.pack()

tk.mainloop()
```
This gives us a window with a text box like this:
![](resources/02_textBox1.png)

## It All Adds Up

Let's make our program add the number in the text box to the number in the label when the button is pressed.

👉 To do this, we need to change the `updateLabel` subroutine.  Here's the code in isolation:
```python
def updateLabel():
  global label
  number = text.get("1.0","end") # Gets the number from the text box (starting at the first position and going to the end.) and stores in the number variable
  number = int(number) #Casts to an integer. I've done this on a separate line to prevent the line above getting too complex, but you can combine the two.
  label += number # Adds the number from the text box to the one in the label.
  hello["text"] = label 
```

### Try it out!