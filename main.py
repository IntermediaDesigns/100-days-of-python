print("Let's build an infinity dice!")
print()
def rollDice(sides):
  import random
  roll = random.randint(1,sides)
  print("You rolled", roll)
  
sides = int(input("How many sides?: "))
print()
while True:
  rollDice(sides)
  print()
  again = input("Roll again? ")
  if again == "yes" or again == "y":
    print()
    continue
  else:
    print()
    print(f"Thanks for playing! You rolled {sides} sided dice!")
    break
