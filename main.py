import os

admin_password = os.environ['admin']
user_password = os.environ['user']
admin_username = os.environ['adminName']
user_username = os.environ['userName']

username = input("Username > ")
print()
password = input("Password > ")
print()

if username == admin_username and password == admin_password:
  print("Welcome Admin")
  print()
elif username == user_username and password == user_password:
  print("Welcome User")
  print()
else:
  print("Incorrect, please try again.")

