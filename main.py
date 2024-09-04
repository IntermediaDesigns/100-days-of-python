print(" 🌟 HIGH SCORE TABLE 🌟 ")
print()
while True:
  initials = input("Input your initials > ")
  print()
  score = input("Input your score > ")
  print()
  user_input = initials + " " + score
  initials, score = user_input.split()
  f = open("high.score", "a+")
  f.write(f"{initials} {score}\n")
  f.close()
  print("Added to high score table.")
  print()
  again = input("Add another? y/n? ")
  print()
  if again.lower() == "y" or again.lower() == "yes":
    continue
  else:
    break
