# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## A Cow Of Many Colors?

👉 What's wrong here?


```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

class bird(animal):

 def __init__(self):
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

- cow was created using the `animal` class. The `color` attribute only belongs to bird objects. Inheritance only works one way.
- `talk` was not defined so `polly.talk()` should be removed.

</details>

## A strong Sense Of Self

👉 What is the problem here?
```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = color # Only applies to the bird sub class


cow = animal("Ermintrude", "Bo Taurus", "Moo")
print(cow.sound)



```

<details> <summary> 👀 Answer </summary>

A mistake like this will throw an error like: 'takes 3 positional arguments but 4 were given'.  

It will look weird because there are only 3 parameters in the brackets of the animal class's `init` method.

However, instantiating an object also creates an invisible extra argument, called 'self', so you have to include that as the first argument in the parameters of the `init`.

```python
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
    self.name = name
    self.species = species
    self.sound = sound
    self.color = color

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "green"


cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
print(cow.sound)



```


</details>

