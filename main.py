def login():
  correct_username = "david"
  correct_password = "baldies4life"
  while True:
    username = input("What is your username?: ")
    print()
    password = input("What is your password?: ")
    print()
    if username == correct_username and password == correct_password:
      print("Welcome to Replit!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      print()
login()
