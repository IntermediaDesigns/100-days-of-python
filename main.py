from replit import db
import random
import time
import hashlib

def add_user():
    username = input("Username: > ")
    password = input("Password: > ")
    salt = ''.join([str(random.randint(0, 9)) for _ in range(4)])
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    db[username] = {"salt": salt, "password": hashed_password}
    print("\nDetails stored.")
    time.sleep(.5) 
    print("\033[H\033[J")  

def login():
    username = input("Username: > ")
    password = input("Password: > ")

    if username not in db:
        print("\nUser not found.")
        return

    user_data = db[username]
    salt = user_data["salt"]
    stored_hash = user_data["password"]

    input_hash = hashlib.sha256((password + salt).encode()).hexdigest()

    if input_hash == stored_hash:
        print("\nLogin successful")
        time.sleep(.5)
        print("\033[H\033[J")
    else:
        print("\nIncorrect password.")
        time.sleep(.5)
        print("\033[H\033[J")

def main():
    while True:
        print("\n🌟 Login System 🌟")
        print("\n1: Add User, 2: Login, 3: Exit")
        
        choice = input("> ")
        print()

        if choice == "1":
            add_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()