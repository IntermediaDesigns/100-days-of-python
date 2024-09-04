print(" 👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾 ")
print()
beast_name = input("Input your beast's name > ")
print()
beast_type = input("Input your beast's type > ")
print()
beast_special_move = input("Input your beast's special move > ")
print()
beast_starting_hp = input("Input your beast's starting HP > ")
print()
beast_starting_mp = input("Input your beast's starting MP > ")
print()

beast_dict = {"Name": beast_name, "Type": beast_type, "Special move" : beast_special_move, "Starting HP": beast_starting_hp, "Starting MP": beast_starting_mp}
print()
if beast_type == "earth":
  print("\033[32m", end="")
  print()
elif beast_type == "fire":
  print("\033[31m", end="")
  print()
elif beast_type == "air":
  print("\033[37m", end="")
  print()
elif beast_type == "water":
  print("\033[34m", end="")
  print()
elif beast_type == "spirit":
  print("\033[35m", end="")
  print()
else:
  print("\033[33m", end="")
  print()

for key, value in beast_dict.items():
  print(f"{key}: {value}")
print()
print(f"Your beast is called {beast_name}. It is an {beast_type} beast with a special move of {beast_special_move}.")
