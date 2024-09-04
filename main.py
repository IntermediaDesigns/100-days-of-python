myBill = float(input("What is the bill total?: "))
tip = input("Select tip percentage (15, 18, or 20): ")
if tip not in ['15', '18', '20']:
    print("Invalid tip percentage selected. Please select from 15, 18, or 20.")
    exit()

tip = int(tip)

numberOfPeople = int(input("How many people?: "))
answer = round(myBill * (1 + tip / 100) / numberOfPeople, 2)
print("Your total including tip is: ", answer)