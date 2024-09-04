# 👉 Day 26 Challenge

Play a song from this repl and build a menu to go with it. Make it look like an iPod!

When you run the code below, it should open the Output tool which will have a checkbox with a headphones icon in the bottom right corner. Select this checkbox to hear the sound. (It may be behind the video.)

- Use a `while true` loop to create a title for a music player. 
- Allow the user to select to play a song and use subroutine called 'play' when they select the song.
- Give the user the option to exit the program.
- The title should pop up and pause along with the menu options.
- If the user chooses anything else, start again by clearing the screen.
  
Use this code to get started:

```python
import os
import time

import pygame

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('audio.wav')
sound.play()

def pause():
  pygame.mixer.pause()
  
pause()

def play():
  # Play the sound
  pygame.mixer.unpause()
  while True:
    # Start taking user input and doing something with it
    input()

while True:
  # clear the screen 

  # Show the menu

  # take user's input

  # check whether you should call the play() subroutine depending on user's input
  if True:
    play()
```

Here is an example:

```
🎵 MyPOD Music Player

Press 1 to Play
Press 2 to Exit

Press anything else to see the menu again.
```

<details> <summary> 💡 Hints </summary>

- Import your libraries first.
- With the sample code above, think about what code can be added to pause and play the audio.
- What command do you need to use to return (hint, hint) to the main menu (subroutine)?
- Create a `while True` loop that clears the code and pauses the code. What libraries would you need for these things to happen?
- You may also need `if` statements within your loop.


</details>