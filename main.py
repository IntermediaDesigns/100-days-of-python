print("Remember, every day is a new opportunity to achieve your goals and make your dreams come true. Stay motivated! 💪🏻")
print()
day = input("What day of the week is it? ")
if day.lower() == "monday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("The only way to achieve the impossible is to believe it is possible.")
  else:
    print("Okay, have a great day!")

elif day.lower() == "tuesday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("The only limit to our realization of tomorrow will be our doubts of today.")
  else:
    print("Okay, have a great day!")

elif day.lower() == "wednesday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("Believe you can and you’re halfway there.")
  else:
    print("Okay, have a great day!")

elif day.lower() == "thursday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("The future belongs to those who believe in the beauty of their dreams.")
  else:
    print("Okay, have a great day!")

elif day.lower() == "friday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("The only thing standing between you and your goal is the story you keep telling yourself as to why you can’t achieve it.")
  else:
    print("Okay, have a great day!")

elif day.lower() == "saturday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("The only place where success comes before work is in the dictionary.")
  else:
    print("Okay, have a great day!")

elif day.lower() == "sunday":
  positive = input("Do you want a positive quote for the day? ")
  if positive.lower() == "yes":
    print("The biggest risk is not taking any risk. In a world that’s changing really quickly, the only strategy that is guaranteed to fail is not taking risks.")
  else:
    print("Okay, have a great day!")

else:
  print()
  print("That is not a day of the week. Please try again.")
