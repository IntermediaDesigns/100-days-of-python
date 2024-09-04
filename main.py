from getpass import getpass as get_choice

while True:
  print("Let's play Rock, Paper, Scissors!")
  print()
  print("Use 'R' for Rock, 'P' for Paper, and 'S' for Scissors.")
  print()
  
  player1 = input("Player 1, enter your choice: ").upper()
  player2 = input("Player 2, enter your choice: ").upper()
  
  if player1 == 'R' and player2 == 'R':
      print("It's a tie! Both players chose Rock.")
  elif player1 == 'R' and player2 == 'P':
      print("Player 2 wins! Paper covers Rock.")
  elif player1 == 'R' and player2 == 'S':
      print("Player 1 wins! Rock crushes Scissors.")
  elif player1 == 'P' and player2 == 'R':
      print("Player 1 wins! Paper covers Rock.")
  elif player1 == 'P' and player2 == 'P':
      print("It's a tie! Both players chose Paper.")
  elif player1 == 'P' and player2 == 'S':
      print("Player 2 wins! Scissors cut Paper.")
  elif player1 == 'S' and player2 == 'R':
      print("Player 2 wins! Rock crushes Scissors.")
  elif player1 == 'S' and player2 == 'P':
      print("Player 1 wins! Scissors cut Paper.")
  elif player1 == 'S' and player2 == 'S':
      print("It's a tie! Both players chose Scissors.")
  else:
      print("Invalid input. Please use 'R', 'P', or 'S'.")
  
  game_over = input("Do you want to play again? (y/yes/n/no): ").lower()
  if game_over == 'y' or game_over == 'yes':
      print("Great! Let's play again!")
  else:
      print("Thanks for playing!")
      break
  
  