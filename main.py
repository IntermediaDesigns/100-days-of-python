import os
import time
import datetime
from replit import db

print(" 📖 Private Diary 📖 ")
print()
correct_password = "secretpassword"
while True:
    password_entered = input("Enter password: ")
    print()
    if password_entered == correct_password:
        print("Access granted.")
        print()
        time.sleep(1)
        break
    else:
        print("Incorrect password. Please try again.")
        time.sleep(1)
        os.system("clear")
        print("Private Diary")
        print()


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
            try:
                target_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
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


while True:
    print(" 📖 Private Diary 📖 ")
    print()
    os.system("clear")
    menu = input("1: Add\n2: View\n3: Close Diary\n> ")
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
