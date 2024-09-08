print("🌟 Generic RPG 🌟")
print()


class Character:

    def __init__(self, name, health, magic_points):
        self.name = name
        self.health = health
        self.magic_points = magic_points

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Magic Points: {self.magic_points}")


class Player(Character):

    def __init__(self, name, health, magic_points, lives):
        super().__init__(name, health, magic_points)
        self.lives = lives

    def is_alive(self):
        return self.lives > 0

    def print_info(self):
        super().print_info()
        print(f"Lives: {self.lives}")
        print(f"Alive?: {'Yes' if self.is_alive() else 'No'}")


class Enemy(Character):

    def __init__(self, name, health, magic_points, enemy_type, strength):
        super().__init__(name, health, magic_points)
        self.type = enemy_type
        self.strength = strength

    def print_info(self):
        super().print_info()
        print(f"Type: {self.type}")
        print(f"Strength: {self.strength}")


class Orc(Enemy):

    def __init__(self, name, health, magic_points, strength, speed):
        super().__init__(name, health, magic_points, "Orc", strength)
        self.speed = speed

    def print_info(self):
        super().print_info()
        print(f"Speed: {self.speed}")


class Vampire(Enemy):

    def __init__(self, name, health, magic_points, strength, is_day):
        super().__init__(name, health, magic_points, "Vampire", strength)
        self.is_day = is_day

    def print_info(self):
        super().print_info()
        print(f"Day/Night?: {'Day' if self.is_day else 'Night'}")


player = Player("David", 100, 50, 3)
vampire1 = Vampire("Boris", 45, 70, 3, False)
vampire2 = Vampire("Rishi", 70, 10, 75, True)
orc1 = Orc("Bill", 60, 5, 75, 90)
orc2 = Orc("Ted", 75, 40, 80, 45)
orc3 = Orc("Station", 35, 40, 49, 50)

characters = [player, vampire1, vampire2, orc1, orc2, orc3]
for character in characters:
    character.print_info()
    print()
