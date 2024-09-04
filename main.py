import os
import time
import random

def generate_name():
  names = ["Sheila", "Gorath", "Elanor", "Drax", "Luna"]
  return random.choice(names)

def generate_title():
  titles = ["the Mighty", "the Brave", "the Wise", "the Cunning", "the Fearless"]
  return random.choice(titles)

def generate_type():
  types = ["Human", "Imp", "Wizard", "Elf", "Orc"]
  return random.choice(types) 

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def pause():
  time.sleep(1)

def roll_dice(sides):
  return random.randint(1, sides)

def generate_health():
  return ((roll_dice(6) * roll_dice(12)) // 2) + 10

def generate_strength():
  return ((roll_dice(6) * roll_dice(12)) // 2) + 12

while True:
  clear_screen()
  print("Character Builder")
  pause()
  print()
  name = generate_name()
  title = generate_title()
  type = generate_type()
  health = generate_health()
  strength = generate_strength()

  print(f"Name your character:\n{name}")
  pause()
  print()
  print(f"Title:\n{title}")
  pause()
  print()
  print(f"Character type:\n{type}")
  pause()
  print()
  print(f"Health: {health}\nStrength: {strength}\n")
  pause()
  print()
  print(f"May your name go down in history as {name} {title} {type}! ")
  pause()
  print()

  choice = input("Do you want to create another character? (y/n): ").lower()
  if choice != 'y':
    break