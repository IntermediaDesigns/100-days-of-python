# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python
import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) 
 
  
  for row in reader: 
    print (", ".join(row["Net Total"]))
    total += row["Net Total"] 

print(f"Total: {total}") 
```

<details> <summary> 👀 Answer </summary>

```python
import csv # Imports the csv library

with open("January.csv") as file: 
  reader = csv.DictReader(file) 
 
  
  for row in reader: 
    print (row["Net Total"]) # removed join
    total += float(row["Net Total"] ) #cast to float

print(f"Total: {total}") 
```



</details>