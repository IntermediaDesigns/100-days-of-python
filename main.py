while True:
    animal = input("Enter the name of the animal you want to hear: ").lower()
    print()
    if animal == 'frog':
        print("The frog goes 'ribbit'")
    elif animal == 'dog':
        print("The dog says 'woof'")
    elif animal == 'cat':
        print("The cat says 'meow'")
    elif animal == 'cow':
        print("The cow says 'moo'")
    else:
        print("Sorry, I don't know what sound that animal makes.")
    print()
    exit = input("Do you want to exit? (yes/no): ").lower()
    print()
    if exit == 'yes' or exit == 'y':
        print("Exiting the program...")
        break
    elif exit == "no" or exit == "n":
        print("Okay, let's continue.")
        print()
    else:
        print("Invalid input. Please enter 'yes/y' or 'no/n'.")
