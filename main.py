import os
import time
import random


class Character:

    def __init__(self):
        self.name = self.generate_name()
        self.title = self.generate_title()
        self.type = self.generate_type()
        self.health = self.generate_health()
        self.strength = self.generate_strength()

    def generate_name(self):
        names = ["Sheila", "Gorath", "Elanor", "Drax", "Luna"]
        return random.choice(names)

    def generate_title(self):
        titles = [
            "the Mighty", "the Brave", "the Wise", "the Cunning",
            "the Fearless"
        ]
        return random.choice(titles)

    def generate_type(self):
        types = ["Human", "Imp", "Wizard", "Elf", "Orc"]
        return random.choice(types)

    def generate_health(self):
        return ((self.roll_dice(6) * self.roll_dice(12)) // 2) + 10

    def generate_strength(self):
        return ((self.roll_dice(6) * self.roll_dice(12)) // 2) + 12

    def roll_dice(self, sides):
        return random.randint(1, sides)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    time.sleep(1.5)


def battle(character1, character2):
    round = 1
    while character1.health > 0 and character2.health > 0:
        clear_screen()
        print(f"⚔️ BATTLE TIME ⚔️\n\nRound {round} begins!")
        print()
        pause()

        roll1 = character1.roll_dice(6)
        roll2 = character2.roll_dice(6)

        if roll1 > roll2:
            damage = abs(character1.strength - character2.strength) + 1
            character2.health -= damage
            print(
                f"Your character {character1.name} wins round {round}\n{character2.name} takes a hit, with {damage} damage"
            )
            print()
        elif roll2 > roll1:
            damage = abs(character2.strength - character1.strength) + 1
            character1.health -= damage
            print(
                f"Your opponent {character2.name} wins round {round}\n{character1.name} takes a hit, with {damage} damage"
            )
            print()
        else:
            print("It's a tie!")
            print()

        pause()
        print(
            f"\n{character1.name} {character1.title}\nYOUR HEALTH: {character1.health}"
        )
        print()
        print(
            f"\n{character2.name} {character2.title}\nOPPONENT HEALTH: {character2.health}"
        )
        print()
        pause()

        round += 1

    if character1.health <= 0:
        print(
            f"\nOh no, your character {character1.name} {character1.title} has died!"
        )
        print()
        print(
            f"{character2.name} {character2.title} destroyed your character {character1.name} {character1.title} in {round} rounds!"
        )
        print()
    else:
        print(f"\nOh no {character2.name} {character2.title} has died!")
        print()
        print(
            f"Your character {character1.name} {character1.title} destroyed {character2.name} {character2.title} in {round} rounds!"
        )
        print()
        print(f"Your name will go down in history as {character1.name} {character1.title} {character1.type}!")
        print()

while True:
    clear_screen()
    print("Character Builder")
    pause()
    print()

    character1 = Character()
    print(
        f"Your character:\nName: {character1.name}\nTitle: {character1.title}\nType: {character1.type}\nHealth: {character1.health}\nStrength: {character1.strength}\n"
    )
    pause()

    choice = input("Do you want to remake your character? (y/n): ").lower()
    print()
    if choice == 'y':
        continue
    else:
        character2 = Character()
        print(
            f"Your opponent:\nName: {character2.name}\nTitle: {character2.title}\nType: {character2.type}\nHealth: {character2.health}\nStrength: {character2.strength}\n"
        )
        print()
        print(f"Your opponent is {character2.name} {character2.title} {character2.type}!")
        print()
        pause()
        print("Let the battle begin!")
        print()
        pause()
        battle(character1, character2)
        choice = input("Do you want to play again? (y/n): ").lower()
        print()
        if choice == 'y':
            continue
        else:
            print("Thanks for playing!")
            break
