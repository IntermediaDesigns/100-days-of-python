import random


def hangman():
	listOfWords = [
	    "twitter", "python", "coding", "software", "react", "developer",
	    "javascript"
	]
	wordChosen = random.choice(listOfWords)
	guessedLetters = []
	attempts = 6
	hangmanParts = ['🙂', '👕', '🫲', '👖', '🫱', '💪']

	print("🌟Hangman🌟")
	print()
	wordGuessed = ["_"] * len(wordChosen)
	print()

	while attempts > 0 and "_" in wordGuessed:
		print((" ".join(wordGuessed)))
		print()
		print(f"You have {attempts} attempts remaining.")
		print()

		guess = input("\nPlease guess a letter: ")
		print()

		if guess in guessedLetters:
			print("You already guessed this letter. Try again.")
			print()
		elif guess not in wordChosen:
			print("Nope, not in there.")
			print()
			attempts -= 1
			guessedLetters.append(guess)
			print(' '.join(hangmanParts[:6 - attempts]))
		else:
			print("Correct!")
			print()
			for i in range(len(wordChosen)):
				if wordChosen[i] == guess:
					wordGuessed[i] = guess
			guessedLetters.append(guess)

	if "_" not in wordGuessed:
		print("🥳 You won with", attempts, "lives left. The word was", wordChosen,
		      ".")
		print()
	else:
		print("😢 Hangman!! You lost! The word was", wordChosen, ".")
		print()


hangman()
