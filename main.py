print(" 🅱️ 5️⃣ 🎉 ~ BINGO CARD GENERATOR ~ 🎉🅱️ 5️⃣ ")
print()

import random
from tabulate import tabulate


def createCard():
    numbers = random.sample(range(1, 91), 24)
    numbers.sort()
    bingo = [numbers[i * 5:(i + 1) * 5] for i in range(4)]
    bingo.insert(2,
                 [numbers[20], numbers[21], "FREE", numbers[22], numbers[23]])
    return bingo


def prettyPrint(bingo):
    print(
        tabulate(bingo,
                 tablefmt="pipe",
                 headers=["B", "I", "N", "G", "O"],
                 numalign="center",
                 stralign="center"))


def checkWin(bingo):

    for row in bingo:
        if all(cell == "X" or cell == "FREE" for cell in row):
            return True

    for col in range(5):
        if all(bingo[row][col] == "X" or bingo[row][col] == "FREE"
               for row in range(5)):
            return True
    if all(bingo[i][i] == "X" or bingo[i][i] == "FREE" for i in range(5)):
        return True
    if all(bingo[i][4 - i] == "X" or bingo[i][4 - i] == "FREE"
           for i in range(5)):
        return True
    return False


bingo = createCard()
prettyPrint(bingo)

numbers = list(range(1, 91))
while True:
    print()
    number = random.choice(numbers)
    numbers.remove(number)
    print("Computer's Number: ", number)
    print()

    while True:
        try:
            guess = int(input("Enter number: "))
            print()
            if guess != number:
                print(f"Error: Please enter the computer's number ({number}).")
                print()
                continue
            break
        except ValueError:
            print()
            print("Invalid input. Please enter a number.")
            print()

    print()
    found = False
    for i in range(len(bingo)):
        for j in range(len(bingo[i])):
            if bingo[i][j] == guess:
                bingo[i][j] = "X"
                found = True

    if not found:
        print()
        print("Number is not on card.")
        print()
    else:
        prettyPrint(bingo)
        if checkWin(bingo):
            print()
            print("🎉 BINGO!! You have won! 🎉")
            print()
            break
