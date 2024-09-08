# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

👉 What's the problem here?


```python
import datetime

today = datetime.today()

print(today)
```

<details> <summary> 👀 Answer </summary>

Missed the `date` function from the second line.

```python
import datetime

today = datetime.date.today()

print(today)
```

</details>


👉 What is the problem here?
```python
import datetime

today = datetime.date(day = 1, year = 2023)

print(today)
```

<details> <summary> 👀 Answer </summary>

Missed the month.

```python
import datetime

today = datetime.date(day = 1, month = 10, year = 2023)

print(today)
```


</details>

