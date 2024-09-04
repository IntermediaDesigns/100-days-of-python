print("Fill in the blank lyrics!")
print("(Type in the blank lyrics and see if you are as cool as me.)")
print()

attempts = 0
while True:
    print("Never going to ______ you up.")
    print()
    word = input("What is the missing word? ")
    print()
    attempts += 1
    if word == "give":
        print(f"Well done! It only took you {attempts} attempts.")
        break
    else:
        print("Nope, try again.")
        print()