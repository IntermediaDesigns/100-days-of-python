print("🌟 Website Rating 🌟")
print()
website_name = input("Input the website name: ")
print()
url = input("Input the URL: ")
print()
description = input("Input your description: ")
print()
rating = input("Input the a star rating out of 5: ")
print()

website_rating = {"name": website_name, "url": url, "description": description, "rating": rating}
print()
print(" ~ Website Rating Information ~ ")
print()

for name, value in website_rating.items():
  print(f"{name}: {value}")
  print()
if rating == "5":
  print("⭐️⭐️⭐️⭐️⭐️")
  print()
elif rating == "4":
  print("⭐️⭐️⭐️⭐️")
  print()
elif rating == "3":
  print("⭐️⭐️⭐️")
  print()
elif rating == "2":
  print("⭐️⭐️")
  print()
elif rating == "1":
  print("⭐️")
  print()
else:
  print("No rating")
  print()
