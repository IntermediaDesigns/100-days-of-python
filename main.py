print("Let's play a game! Guess the Number!")
print()
print("Guess a number between 1 and 1,000,000 and I will tell you if you are too low or too high.")
print()
print("Let's play!")
print()

fixed_number = 327013
attempt = 1

while True:
    user_input = input("Pick a number between 1 and 1,000,000: ")
    # Remove commas from the input string
    user_input_without_commas = user_input.replace(",", "")
    # Convert the string to an integer
    user_guess = int(user_input_without_commas)

    if user_guess < 0:
        print("Now we'll never know what the answer is …")
        exit()
    elif user_guess < fixed_number:
        print("Too low.")
        attempt += 1
    elif user_guess > fixed_number:
        print("Too high.")
        attempt += 1
    else:
        print()
        print(f"Congratulations! You're a winner! 🎉 You guessed the number in {attempt} attempts.")
        break
