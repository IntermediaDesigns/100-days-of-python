import os
import base64
import time
import datetime
import hashlib
from replit import db


def create_user():
    while True:
        username = input("Create a username: ")
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        password = input("Create a password: ")
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
        confirm_password = input("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue
        salt = os.urandom(32)
        hashed_password = hashlib.pbkdf2_hmac('sha256',
                                              password.encode('utf-8'), salt,
                                              100000)
        db['user'] = {
            'username': username,
            'salt': base64.b64encode(salt).decode('utf-8'),
            'hashed_password':
            base64.b64encode(hashed_password).decode('utf-8')
        }
        print("User created successfully!")
        return username


def verify_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_data = db.get('user')
    if not user_data or username != user_data['username']:
        return False
    salt = base64.b64decode(user_data['salt'])
    stored_password = base64.b64decode(user_data['hashed_password'])
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),
                                          salt, 100000)
    return hashed_password == stored_password


def add_entry():
    time.sleep(1)
    os.system("clear")
    timestamp = datetime.datetime.now()
    print(f"Diary entry for {timestamp}")
    print()
    entry = input("> ")
    db[timestamp.isoformat()] = entry
    print("\nEntry added successfully!")
    time.sleep(1)
    os.system("clear")


def view_entries():
    keys = list(db.keys())
    keys.remove('user')
    if not keys:
        print("No entries to display.")
        time.sleep(1)
        return
    keys.sort(reverse=True)
    index = 0
    while True:
        os.system("clear")
        if 0 <= index < len(keys):
            key = keys[index]
            entry_date = datetime.datetime.fromisoformat(key)
            print(f"Entry {index + 1} of {len(keys)}")
            print()
            print(f"Date: {entry_date.strftime('%Y-%m-%d %H:%M:%S')}")
            print()
            print(f"Content: {db[key]}\n")
        print("View options:")
        print()
        print("1: View by date")
        print("2: Next entry")
        print("3: Previous entry")
        print("4: Return to menu")
        choice = input("> ")
        if choice == "1":
            date_input = input("Enter date (YYYY-MM-DD): ")
            print()
            try:
                target_date = datetime.datetime.strptime(
                    date_input, "%Y-%m-%d").date()
                found_entries = False
                for i, key in enumerate(keys):
                    entry_date = datetime.datetime.fromisoformat(key).date()
                    if entry_date == target_date:
                        index = i
                        found_entries = True
                        break
                if not found_entries:
                    print("No entries found for that date.")
                    time.sleep(1)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                time.sleep(1)
        elif choice == "2":
            if index < len(keys) - 1:
                index += 1
            else:
                print("This is the oldest entry.")
                time.sleep(1)
        elif choice == "3":
            if index > 0:
                index -= 1
            else:
                print("This is the most recent entry.")
                time.sleep(1)
        elif choice == "4":
            break
        else:
            print("Invalid option")
            time.sleep(1)
    print("Returning to menu...")
    time.sleep(1)


print(" 📖 Private Diary 📖 ")
print()

if len(db) == 0:
    print("Welcome to your new diary!")
    print()
    username = create_user()
else:
    while True:
        if verify_user():
            print("Access granted.")
            print()
            time.sleep(1)
            break
        else:
            print("Incorrect username or password. Please try again.")
            print()
            time.sleep(1)
            os.system("clear")
            print(" 📖 Private Diary 📖 ")
            print()

while True:
    os.system("clear")
    print(" 📖 Private Diary 📖 ")
    print()
    menu = input("1: Add\n2: View\n3: Close Diary\n> ")
    print()
    if menu == "1":
        add_entry()
    elif menu == "2":
        view_entries()
    elif menu == "3":
        break
    else:
        print("Invalid option")
        time.sleep(1)

print("Diary closed.")
