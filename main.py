print(" 🌟Dave's Dodgy Pizzas🌟 ")
print()

try:
  with open("orders.txt", "r") as f:
    orderList = eval(f.read())
except FileNotFoundError:
  orderList = []

while True:
  try:
    quantity = int(input("How many pizzas? > "))
    break
  except:
    print("You must input a numerical character, try again.")

size = input("What size? > ").lower()
name = input("Name please > ")
print()

if size == "small" or size == "s" or size == "sm":
  price = quantity * 10
elif size == "medium" or size == "m" or size == "med":
  price = quantity * 12
elif size == "large" or size == "l" or size == "lg":
  price = quantity * 14

cost = round((price), 2)
row = [name, quantity, size, cost]
orderList.append(row)
f = open("orders.txt", "w")
f.write(str(orderList))
f.close()

print(f"Thanks {name}, your pizzas will cost ${cost}.")
