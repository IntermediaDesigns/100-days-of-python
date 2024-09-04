letters = ["r", "g", "b", "p", "y"]

response = input("What sentence do you want to rainbow-ize?\n")
print()

for letter in response:
  if letter.lower() in letters:
    if letter.lower() == "r":
      print("\033[31m", end="")
    elif letter.lower() == "g":
      print("\033[32m", end="")
    elif letter.lower() == "b":
      print("\033[34m", end="")
    elif letter.lower() == "p":
      print("\033[35m", end="")
    elif letter.lower() == "y":
      print("\033[33m", end="")
  print(letter, end="")
  print("\033[0m", end="")