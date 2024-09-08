# Inheritance


Inheritance means that we can take the template from `animal` and break it down into sub-classes that use all the attributes and methods from that class, but also add their own attributes.

This is useful when we're thinking about animals as we can start breaking the animal kingdom apart by species.


When I create the sub-class, I use the name of its parent class as a parameter. This means 'get all the features of animal and use them here too'.

Here, I'm creating a sub-class of `bird`, which inherits from `animal`.

👉 I can then create the 'bird specific' features inside the bird sub-class.

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

##### The New Bit ##########

class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"

    # This automatically sets the information for each bird when it is created.


polly = bird() # Instantiates a new bird which gets it's details from the sub-class.

polly.talk() # polly uses the `talk()` method from the animal class 
  
```


👉 Let's add a specific color to the bird class.

```python
class bird(animal):

  def __init__(self, color):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class


polly = bird("Green") # Sets polly's colour to 'Green'
polly.talk()
print(polly.color) # Prints polly's color
```

### We can use inheritance to create a generic class (like 'character') and then sub-divide it into different types (player, enemy, boss etc.)



