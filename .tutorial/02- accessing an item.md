# Accessing a Single Item

To access a single item in a 2D dictionary, we use **two square brackets** just like with a 2D list.

👉 This example stores users' data about their 100 Days Of Code progress. Note how I've set each one up as a 1D dictionary before storing them all in a 2D dictionary.


```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress)
```

##

👉 To access one item, I use two square brackets `[]`. So to see only Erica's results, I would add: 

```python
print(courseProgress["Erica"])
# The bracket contains the key that references the sub dictionary. 
```
##
👉 What if we only want to see how many days Erica has completed?

```python
john = {"daysCompleted": 46, "streak": 22}
janet = {"daysCompleted": 21, "streak": 21}
erica = {"daysCompleted": 75, "streak": 6}

courseProgress = {"John":john, "Janet":janet, "Erica":erica}

print(courseProgress["Erica"]["daysCompleted"])
# The first bracket contains the key that references the sub dictionary. The second bracket contains the key that references the sub item. This will output '75'.
```

### Try it out and go deeper into dictionaries!