# Nesting

Nesting is where we put an `if` statement within an `if` statement using the power of indenting. The second `if` statement within the first `if` statement must be indented and its print statement needs to be indented one more time.

Pay attention to the vertical lines (as shown with the blue arrows in this image) to ensure your indents line up correctly.

👉 Do you notice the second `if` statement below about `faveCharacter` and how it is indented?

```python
tvShow = input("What is your favorite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
```

I highly doubt your favorite TV shows are Peppa Pig and Paw Patrol. Copy the code above and change it to match your favorite TV shows and characters.

## Common Errors

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error-free. Click on the 👀 Answer to compare your code to the correct code.

### Syntax Error

👉 What is wrong with the code below?

```python
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
else:
  print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")
else:
  print("Nah, Daddy Pig's the greatest")
```

The `else` statement is not indented properly. This `else` statement is referring to `faveCharacter` and therefore, both the above `else` and `print` statements need to be indented one time. Highlight them both and click 'tab' one time.

### Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error-free. Click on the 👀 Answer to compare your code to the correct code.

```python
order = input(What would you like to order: pizza or hamburger? ")
if order = "hamburger":
print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
  print("You got it.")
else: 
    print("No cheese it is.")
elif order == pizza:
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings = "yes"
    print("We will add pepperoni.")
else:
  print"Your pizza will not have pepperoni.")
```

Corrected code:
```python
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")
```

## 👉 Day 7 Challenge: Fake Fan Question Generator

Wanna find out if someone else is a true superfan of the same show, movie or interest as you? Create a program that asks what someone is interested in and includes nested `if` statements to ask annoying follow-up questions to see if someone is the real deal!

Make sure you include multiple `if`/`elif` statements and nested `if` statements too!

The code from today is a good place to get you started.

### My Solution:
![my solution](image.png)