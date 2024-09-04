import random

print(" 🌟 Idea Storage 🌟 ")
print()
while True:
  menu = input("Add an idea or see a random idea? add or r. > ").lower()
  print()
  if menu == "add":
    f = open("my.ideas", "a+")
    idea = input("Input your idea. > ")
    f.write(f"{idea}\n")
    f.close()
    print()
    print("Nice! Your idea has been stored.")
    print()
    print()
  elif menu == "r":
    f = open("my.ideas", "r")
    ideas = f.read().split("\n")
    f.close()
    ideas.remove("")
    idea = random.choice(ideas)
    print(idea)
    print()

  done = input("Are you done? y/n > ")
  print()
  if done == "y":
    break
  else:
    continue