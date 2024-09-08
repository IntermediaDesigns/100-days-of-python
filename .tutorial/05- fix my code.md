# Fix My Code

👉 Try and fix this code which is *full* of errors.

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

```python

class animal:
  species = None
  name = None
  sound = None
 
  def __init__(name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}"))

class bird():

 def __init__():
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
print(cow.color)

polly = bird("Green") 
polly.talk()
print(polly.color) 
```

<details> <summary> 👀 Answer </summary>

```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound): # missed the 'self'
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}"))

class bird(animal): # missed the inheritance from animal

 def __init__(self, color): # missed the 'self'
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)
#print(cow.color) # no such property in the animal class.

polly = bird("Green") 
polly.talk()
print(polly.color) 
```


</details>