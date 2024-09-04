print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
 print("Welcome Mark! You have successfully logged in.")
elif username == "suzanne":
 print("Welcome Suzanne! You have successfully logged in.")
else:
 print("Sorry, you are unable to log in. Please try again.")