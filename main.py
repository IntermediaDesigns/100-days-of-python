print(" 🌟 Shop $$ Tracker 🌟 ")
print()

import csv

total = 0

# Read the CSV file in
with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)

    # Multiply the cost by the quantity and add to total
    for row in reader:
        item_total = float(row["Cost"]) * int(row["Quantity"])
        total += item_total

# Print the total money the shop made in a day
print(f"Your shop made ${total:,.2f} dollars today.")