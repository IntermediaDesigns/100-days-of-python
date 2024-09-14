import requests
import json
from replit import db

def get_random_joke():
    try:
        result = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
        result.raise_for_status()
        joke = result.json()
        return joke["id"], joke["joke"]
    except requests.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None, None

def save_joke(joke_id):
    if "saved_jokes" not in db:
        db["saved_jokes"] = []
    if joke_id not in db["saved_jokes"]:
        db["saved_jokes"].append(joke_id)
        print("Joke saved successfully!")
        print()
    else:
        print("This joke is already saved.")
        print()

def display_saved_jokes():
    if "saved_jokes" not in db or len(db["saved_jokes"]) == 0:
        print("No jokes saved yet.")
        return

    print("Saved jokes:")
    for joke_id in db["saved_jokes"]:
        try:
            result = requests.get(f"https://icanhazdadjoke.com/j/{joke_id}", headers={"Accept":"application/json"})
            result.raise_for_status()
            joke = result.json()
            print(f"- {joke['joke']}")
        except requests.RequestException as e:
            print(f"Error fetching joke {joke_id}: {e}")

def main():
    while True:
        joke_id, joke_text = get_random_joke()
        if joke_id is None:
            continue

        print("\nHere's a random joke for you:")
        print()
        print(joke_text)

        save = input("\nDo you want to save this joke? (y/n): ").lower()
        print()
        if save == "y":
            save_joke(joke_id)

        view_saved = input("Do you want to see your saved jokes? (y/n): ").lower()
        print()
        if view_saved == "y":
            display_saved_jokes()

        again = input("\nDo you want another joke? (y/n): ").lower()
        print()
        if again != "y":
            break

    print("Thanks for using the Dad Joke program!")

if __name__ == "__main__":
    main()