import random
from tabulate import tabulate

def ran():
  number = random.randint(1, 90)
  return number

numbers = []
for i in range(15):
  numbers.append(ran())
numbers.sort()

bingo = [[numbers[0], numbers[1], numbers[2], numbers[3], numbers[4]],
         [numbers[5], numbers[6], "BINGO", numbers[7], numbers[8]],
         [numbers[9], numbers[10], numbers[11], numbers[12], numbers[13], " "]]

print(" 🅱️ 5️⃣ 🎉 ~ BINGO CARD GENERATOR ~ 🎉🅱️ 5️⃣ ")
print()

def prettyPrint():
  print(
      tabulate(bingo,
               tablefmt="pipe",
               headers=["B", "I", "N", "G", "O"],
               numalign="center",
               stralign="center"))


prettyPrint()
