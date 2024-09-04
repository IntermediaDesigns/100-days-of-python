import random

print(" 🌟 Top Trumps 🌟 ")
print()
print("Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator")
print()


def random_number():
  number = random.randint(1, 100)
  return number


morgan = {
    "Intelligence": random_number(),
    "Handsomeness": random_number(),
    "L33t c0ding skillz": random_number(),
    "Baldness level": random_number()
}
colley = {
    "Intelligence": random_number(),
    "Handsomeness": random_number(),
    "L33t c0ding skillz": random_number(),
    "Baldness level": random_number()
}

stats = [
    "Intelligence", "Handsomeness", "L33t c0ding skillz", "Baldness level"
]

while True:
  card = input("Choose your card: 1 - Mr. Morgan 2 - Mr. Colley ")
  print()
  stat = input(
      "Choose your stat: 1. Intelligence 2. Handsomeness 3. L33t c0ding skillz 4. Baldness level "
  )
  print()

  if card == "1":
    print("Mr. Morgan has a", stats[int(stat) - 1], "stat of",
          morgan[stats[int(stat) - 1]])
    print()
    print("Mr. Colley has a", stats[int(stat) - 1], "stat of",
          colley[stats[int(stat) - 1]])
    print()
    if morgan[stats[int(stat) - 1]] > colley[stats[int(stat) - 1]]:
      print("************* Mr. Morgan wins! *************")
      print()
    else:
      print("************* Mr. Colley wins! *************")
      print()
  elif card == "2":
    print("Mr. Colley has a", stats[int(stat) - 1], "stat of",
          colley[stats[int(stat) - 1]])
    print()
    print("Mr. Morgan has a", stats[int(stat) - 1], "stat of",
          morgan[stats[int(stat) - 1]])
    print()
    if morgan[stats[int(stat) - 1]] > colley[stats[int(stat) - 1]]:
      print("************* Mr. Morgan wins! *************")
      print()
    else:
      print("************* Mr. Colley wins! *************")
      print()
  else:
    print("Invalid input")
    print()

  again = input("Again? y/n > ").lower()
  print()
  if again == "y" or again == "yes":
    continue
  else:
    break
