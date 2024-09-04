print(" 👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾 ")
print()

mokedex = {}

while True:
  beast_name = input("Input your beast's name > ")
  print()
  beast_type = input("Input your beast's type > ").lower()
  print()
  beast_special_move = input("Input your beast's special move > ")
  print()
  beast_starting_hp = input("Input your beast's starting HP > ")
  print()
  beast_starting_mp = input("Input your beast's starting MP > ")
  print()

  beast_dict = {
      "Name": beast_name,
      "Type": beast_type,
      "Special move": beast_special_move,
      "Starting HP": beast_starting_hp,
      "Starting MP": beast_starting_mp
  }

  mokedex[beast_name] = beast_dict

  if beast_type == "earth":
    print("\033[32m", end="")
  elif beast_type == "fire":
    print("\033[31m", end="")
  elif beast_type == "air":
    print("\033[37m", end="")
  elif beast_type == "water":
    print("\033[34m", end="")
  elif beast_type == "spirit":
    print("\033[35m", end="")
  else:
    print("\033[33m", end="")

  print(
      f"\n{beast_name}: | Type: {beast_type} | Special move: {beast_special_move} | Starting HP: {beast_starting_hp} | Starting MP: {beast_starting_mp}"
  )
  print()
  print(
      f"Your beast is called {beast_name}. It is an {beast_type} beast with a special move of {beast_special_move}."
  )
  print("\033[0m", end="")
  print()

  another = input("Add another beast? y/n > ")
  print()
  if another.lower() != "yes" and another.lower() != "y":
    break
