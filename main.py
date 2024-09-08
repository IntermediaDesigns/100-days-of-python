import os
import time
import datetime
from replit import db

def addTweet():
    tweet = input("Enter your tweet: ")
    timestamp = datetime.datetime.now()
    key = f"mes{timestamp}"
    db[key] = tweet
    time.sleep(1)
    os.system("clear")

def viewTweet():
    matches = db.prefix("mes")
    matches = matches[::-1]
    counter = 0

    if not matches:
        print("No tweets found.")
        time.sleep(1)
        os.system("clear")
        return

    for i in matches:
        print(db[i])
        print()
        time.sleep(0.3)
        counter += 1
        if counter % 10 == 0:
            carryOn = input("Next 10?: ")
            if carryOn.lower() == "no":
                break
    time.sleep(1)
    os.system("clear")

while True:
    print("Someone is wrong on Twitter!")
    print()
    menu = input("1: Add Tweet\n2: View Tweets\n3: Quit> ")
    print()
    if menu == "1":
        addTweet()
        print()
    elif menu == "2":
        viewTweet()
        print()
    elif menu == "3":
        break
    else:
        print("Invalid input. Please try again.")
        time.sleep(1)
        os.system("clear")
    
    print()