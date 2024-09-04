heading = "30 Days Down"
print(heading)
print()

for days in range(1,31):
  user_input = input(f"Day {days}: ")
  sentence = f"You thought Day {days} was {user_input}."
  spaces = (len(heading) - len(sentence)) // 2
  print()
  print(" " * spaces + sentence)
  print()
