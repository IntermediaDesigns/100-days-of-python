print("Let's test your knowledge with a math facts game!")
print()

multiply = int(input("Enter a number: "))
print()
correct_answers = 0
message_counter = 1

for i in range(1, 11):
  answer = int(input(f"What is {i} x {multiply}? "))
  print()
  if answer == i * multiply:
    if message_counter == 1:
      print("Great job!")
    elif message_counter == 2:
      print("Well done!")
    elif message_counter == 3:
      print("You're on fire!")
    elif message_counter == 4:
      print("Keep it up!")
    else:
      print("Nice work!")
      message_counter = 0
    print()
    correct_answers += 1
    message_counter += 1
  else:
    print(f"Sorry, that's incorrect. The correct answer is {i * multiply}.")
    print()
print(f"You got {correct_answers} out of 10 correct!")

if correct_answers == 10:
  print()
  print("🎉 Congratulations! You got all 10 math facts correct! 🎉")
