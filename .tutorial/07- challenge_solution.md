# Solution (No Peeking!)
![](https://www.youtube.com/watch?v=nJ5oribx71c)

<details> <summary> 👀 Answer </summary>

```python
import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for rows in scores:
  data = rows.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("The winner is", name, "with", highscore)

```

</details>

- Join our [100 Days Community](https://replit.com/100-days-help)
- Want [live support?](https://replit.com/replit-101)