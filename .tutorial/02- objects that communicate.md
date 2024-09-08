# More Methods 

Subroutines inside an object are called **methods**.

👉 Let's create a `talk` method inside the `animal` class.  This can then be used by both our `dog` and `cow` objects.


```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}"))
```

👉 Now I can use the `talk()` method for each object.  

```python
class animal:
  species = None
  name = None
  sound = None
  # Sets the characteristics

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}")) 
  # 'self' means 'use the identifier given to the object that is accessing this method'. So If I use it with dog it will become 'dog.talk()' etc.

dog = animal("Brian", "Canine", "Woof")
dog.talk()

cow = animal("Ermintrude", "Bo Taurus", "Moo")
cow.talk()
```

### Try it out!