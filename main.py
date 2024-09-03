movie = input("What is your favorite movie? ")

if movie.lower() == "the godfather":
  director = input("Who directed The Godfather? ")
  if director.lower() == "francis ford coppola":
    print("Correct! You're a true superfan of The Godfather!")
  else:
    print("Sorry, that's not correct. Better luck next time!")

elif movie.lower() == "pulp fiction":
  actor = input("Who plays Vincent Vega in Pulp Fiction? ")
  if actor.lower() == "john travolta":
    print("Correct! You're a true superfan of Pulp Fiction!")
  else:
    print("Sorry, that's not correct. Better luck next time!")

elif movie.lower() == "the dark knight":
  joker = input("Who plays the Joker in The Dark Knight? ")
  if joker.lower() == "heath ledger":
    print("Correct! You're a true superfan of The Dark Knight!")
  else:
    print("Sorry, that's not correct. Better luck next time!")

else:
  print("Sorry, I don't know that movie. Better luck next time!")