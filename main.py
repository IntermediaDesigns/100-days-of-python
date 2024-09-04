import random

def rollDice(sides):
  return random.randint(1,sides)

def characterHealth():
  return rollDice(6) * rollDice(8)

def generateCharacter():
  name = input("Name your warrior: ")
  health = characterHealth()
  print()
  print(f"Their health is: {health}hp")
  print()

print("⚔️ Character Stats Generator ⚔️")
print()

while True:
  generateCharacter()
  while True:
    again = input("Generate stats for another character? (yes/no): ").lower()
    print()
    if again in ["yes", "y", "no", "n"]:
      break
    else:
      print("Invalid input. Please enter 'yes' or 'no'.")
      print()
  if again == "no" or again == "n":
    print("Thanks for playing!")
    break