# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import datetime

today = datetime.today() 

holiday = datetime.date(year = 2022, day = 20) 

if holiday < today: 
  print("Coming soon")
elif holiday > today: 
  print("Hope you enjoyed it")
else:
  print("HOLIDAY TIME!")
```

<details> <summary> 👀 Answer </summary>

```python
import datetime

today = datetime.date.today() # Missed the .date 

holiday = datetime.date(year = 2022, month = 10, day = 20) # Missed the month

if holiday > today: # Logic error, checked if the holiday had passed
  print("Coming soon")
elif holiday < today:  # Logic error, checked if the holiday was in the future
  print("Hope you enjoyed it")
else:
  print("HOLIDAY TIME!")
```


</details>