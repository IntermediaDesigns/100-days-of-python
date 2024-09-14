# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=X6YgX8HpsAc)

<details> <summary> 👀 Answer </summary>

```python
import os

while True:
  username = input("Username: ")
  password = input("Password: ")
  if username == os.environ['adminUsername'] and password == os.environ['adminPassword']:
    print("Welcome Admin")
    break
  elif username ==  os.environ['username'] and password == os.environ['password']:
    print("Welcome Normy")
    break
  else:
    print("Try again")

```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Join our [Discord](https://replit.com/discord)
- Want [live support?](https://replit.com/replit-101)