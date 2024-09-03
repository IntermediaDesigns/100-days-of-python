# If Statements

These statements are a bit like asking a question. You are telling the computer: if something is true, then do this specific block of code. Double equals (`==`) is asking the computer to compare if these two things are exactly the same.

In the code below, I am asking if the variable `myName` is the same as the string `David`.

```python
myName = input("What's your name?: ")
if myName == "David":
```

But that doesn't print anything? To create a print statement related to the input from the if statement, you must go to the next line and indent once (Luckily, Replit does this for you, but be careful!) so it is all a part of the code we run.

👉 Copy this code and see what happens.

```python
myName = input("What's your name?: ")
if myName == "David":
  print("Welcome Dude!")
```

## What is else?

If the condition is not met with the if statement, then we want the computer to do the else part instead. Likewise, if the condition is met in the if statement, then the else bit is ignored by the computer. The else statement must be the first thing unindented after the if statement and in line with it (Replit helps you out here too!)

👉 Copy this code and give it a go. Watch those indents!

```python
myName = input("What's your name?: ")
if myName == "David":
 print("Welcome Dude!")
 print("You're just the baldest dude I've ever seen")
else:
 print("Who on earth are you?!")
```

## Common Errors

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error-free. Click on the 👀 Answer to compare your code to the correct code.

### Syntax Error

👉 What is wrong with this code below?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs = "cat":
  print("Meow")
else:
  print("Woof")
```

Our if statement must include `==` so it should read:
```python
if catsOrDogs == "cat":
```

### Syntax Error...again

👉 What is wrong with this code?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat"
  print("Meow")
else:
  print("Woof")
```

Our if statement is missing the `:`.

### Indentation Error

👉 Do you see the error here?

```python
catsOrDogs = input("Are you a cat person? Or a dog person?: ")
if catsOrDogs == "cat":
  print("Meow")
else:
print("Woof")
```

As soon as you see a colon, the next line should be indented one more than the line above it.

## Fix My Code

👉 Try and fix this code which is full of errors.

First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error-free. Click on the 👀 Answer to compare your code to the correct code.

```python
drink = input("Do you prefer coffee or tea?)
if drink = "coffee"
  print("Tea is better.")
    else:
  print("Excellent choice.")
```

Corrected code:
```python
drink = input("Do you prefer coffee or tea?")
if drink == "coffee":
  print("Tea is better.")
else:
  print("Excellent choice.")
```

## 👉 Day 5 Challenge: "Which character are you?" Generator

You will need to:

1. Ask your users a series of questions that identify if they're one of the characters in the world you have created.
2. Add multiple if statements to check the result of each question.
3. Make sure to have a final print if they haven't selected any of the characters so far.

### Example

Marvel Movie Character Creator
--
```plaintext
Do you like 'hanging around'?: No
Then you're not Spider-man
Do you have a 'gravelly' voice?: No
Aww, then you're not Korg
Do you often feel 'Marvelous'?: Yes
Aha! You're Captain Marvel! Hi!
```

### My Solution:

![my solution](image.png)


