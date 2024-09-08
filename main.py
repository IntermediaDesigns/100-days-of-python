print(" 🌟 Factorial Finder 🌟 ")
print()


def factorial(value):
  if value == 1:
    return 1
  else:
    return value * factorial(value - 1)


while True:
  print()
  num = int(input("Input a number > "))
  print()
  print(f"The factorial of {num} is {factorial(num)}")
