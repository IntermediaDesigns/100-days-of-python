candy = input("What is your favorite candy? ")
color = input("What is your favorite color? ")
crazy = input("Describe yourself in one word. ")
name = color + " " + candy
villain = crazy + " " + name

if candy == "skittles" and color == "blue" and crazy == "awesome":
    print("You are a superhero named", name, "!")
else: 
    print("You are a villain named", villain, "!")
