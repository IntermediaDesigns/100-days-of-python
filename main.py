score1 = 0
score2 = 0

while True:
    print("Let's play Rock, Paper, Scissors!")
    print()
    print("Use 'R' for Rock, 'P' for Paper, and 'S' for Scissors.")
    print()

    player1 = input("Player 1, enter your choice: ").upper()
    print()
    player2 = input("Player 2, enter your choice: ").upper()
    print()

    if player1 == 'R' and player2 == 'R':
        print("It's a tie! Both players chose Rock.")
    elif player1 == 'R' and player2 == 'P':
        print("Player 2 wins! Paper covers Rock.")
        score2 += 1
    elif player1 == 'R' and player2 == 'S':
        print("Player 1 wins! Rock crushes Scissors.")
        score1 += 1
    elif player1 == 'P' and player2 == 'R':
        print("Player 1 wins! Paper covers Rock.")
        score1 += 1
    elif player1 == 'P' and player2 == 'P':
        print("It's a tie! Both players chose Paper.")
    elif player1 == 'P' and player2 == 'S':
        print("Player 2 wins! Scissors cut Paper.")
        score2 += 1
    elif player1 == 'S' and player2 == 'R':
        print("Player 2 wins! Rock crushes Scissors.")
        score2 += 1
    elif player1 == 'S' and player2 == 'P':
        print("Player 1 wins! Scissors cut Paper.")
        score1 += 1
    elif player1 == 'S' and player2 == 'S':
        print("It's a tie! Both players chose Scissors.")
        print()
    else:
        print("Invalid input. Please use 'R', 'P', or 'S'.")
        print()
        continue
    print()
    print(f"Score: Player 1 = {score1}, Player 2 = {score2}")
    print()

    if score1 == 3:
        print("Player 1 wins the game!")
        print()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'no' or play_again == 'n':
            break
        elif play_again == 'yes' or play_again == 'y':
            score1 = 0
            score2 = 0
            continue
        else:
            print("Invalid input. Please enter 'y', 'yes' or 'n', 'no'.")
            continue
    elif score2 == 3:
        print("Player 2 wins the game!")
        print()
        play_again = input("Do you want to play again? (y/yes/n/no): ").lower()
        if play_again == 'no' or play_again == 'n':
            break
        elif play_again == 'yes' or play_again == 'y':
            score1 = 0
            score2 = 0
            continue
        else:
            print("Invalid input. Please enter 'yes', 'y', or 'no', 'n'.")
            continue
print()
print("Thanks for playing!")
