def add():
    item = input("Input the item to add: > ")
    print()
    quantity = int(input("Input the quantity: > "))
    print()

    if quantity <= 0:
        print("Invalid quantity. Please enter a number greater than 0.")
        print()
        return

    try:
        with open("inventory.txt", "r") as f:
            items = f.read().splitlines()
    except FileNotFoundError:
        items = []

    item_found = False
    for i, existing_item in enumerate(items):
        existing_quantity, existing_name = existing_item.split(" x ")
        if existing_name == item:
            new_quantity = int(existing_quantity) + quantity
            items[i] = f"{new_quantity} x {item}"
            item_found = True
            break

    if not item_found:
        items.append(f"{quantity} x {item}")

    with open("inventory.txt", "w") as f:
        f.write("\n".join(items))

    print(f"{quantity} x {item} has been added to your inventory.")
    print()


def view():
    try:
        with open("inventory.txt", "r") as f:
            items = f.read().splitlines()
        print("📜 Inventory 📜")
        print()
        for item in items:
            print(item)
            print()
            print()
    except FileNotFoundError:
        print("Inventory is empty or file not found.")
        print()


def remove():
    view()
    item_to_remove = input("Input the item to remove: > ")
    print()

    while True:
        try:
            quantity_to_remove = int(input("Input the quantity to remove: > "))
            print()
            if quantity_to_remove <= 0:
                print(
                    "Invalid quantity. Please enter a number greater than 0.")
                print()
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            print()

    try:
        with open("inventory.txt", "r") as f:
            items = f.read().splitlines()
        updated_items = []
        item_found = False
        for item in items:
            quantity, name = item.split(" x ")
            if name == item_to_remove:
                item_found = True
                new_quantity = int(quantity) - quantity_to_remove
                if new_quantity > 0:
                    updated_items.append(f"{new_quantity} x {name}")
                elif new_quantity == 0:
                    print(f"All {name} have been removed from your inventory.")
                    print()
                else:
                    print(
                        f"Error: Trying to remove more {name} than available.")
                    print()
                    updated_items.append(item)
            else:
                updated_items.append(item)
        if item_found:
            with open("inventory.txt", "w") as f:
                f.write("\n".join(updated_items))
            print(
                f"{quantity_to_remove} x {item_to_remove} has been removed from your inventory."
            )
            print()
        else:
            print(f"{item_to_remove} is not in your inventory.")
        print()
    except FileNotFoundError:
        print("Inventory is empty or file not found.")
        print()


print(" 🌟 RPG Inventory 🌟 ")
print()

while True:
    try:
        menu = input("1: Add  2: View  3: Remove  4: Quit > ")
        print()
        print()
        if menu == "1":
            add()
        elif menu == "2":
            view()
        elif menu == "3":
            remove()
        elif menu == "4":
            break
        else:
            print("Invalid input. Please try again.")
            print()
    except Exception as err:
        print("Error: ", err)
        print()

print("Thank you for using RPG Inventory!")
