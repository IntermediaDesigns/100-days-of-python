import requests
import json
import os

if not os.path.exists('profile_pics'):
  os.makedirs('profile_pics')

for _ in range(10):
  result = requests.get("https://randomuser.me/api/")
  user = result.json()

  for person in user['results']:
    first_name = person["name"]["first"]
    last_name = person["name"]["last"]
    name = f"{first_name} {last_name}"
    print(name)
    profile_pic_url = person["picture"]["medium"]

    pic_result = requests.get(profile_pic_url)

    with open(f"profile_pics/{first_name}_{last_name}.jpg", 'wb') as file:
      file.write(pic_result.content)

print("Profile pictures saved successfully!")
