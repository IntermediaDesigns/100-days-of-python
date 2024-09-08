# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=QzqlfMBDZdw)

<details> <summary> 👀 Answer </summary>

```python

from replit import db
import datetime, os, time

def addTweet():
  tweet = input("🐥 > ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")

def viewTweet():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%10==0):
      carryOn = input("Next 10?: ")
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")


while True:
  print("Tweeter")
  menu = input("1: Add Tweet\n2: View Tweets\n> ")
  if menu == "1":
    addTweet()
  else:
    viewTweet()
  


```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Join our [Discord](https://replit.com/discord)
- Want [live support?](https://replit.com/replit-101)