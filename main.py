print(" 🌟 Palindrome Checker 🌟 ")
print()


def palindrome(word):
  if len(word) <= 1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])


while True:
  word = input("Input a word > ").lower()
  print()

  if palindrome(word):
    print(f"{word} is a palindrome. Yay!")
    print()
  else:
    print(f"{word} is not a palindrome. Try again.")
    print()
  again = input("Do you want to try again? > ").lower()
  print()
  if again == "yes" or again == "y":
    continue
  else:
    print("Thanks for playing!")
    break
