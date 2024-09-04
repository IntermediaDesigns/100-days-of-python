import os
import time
import pygame

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('audio.wav')
is_paused = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    global is_paused
    pygame.mixer.pause()
    is_paused = True

def play():
    global is_paused
    if is_paused:
        pygame.mixer.unpause()
        is_paused = False
    else:
        sound.stop()
        sound.play()

def show_menu():
    print("🎵 MyPOD Music Player\n")
    print("Press 1 to Play")
    print("Press 2 to Pause")
    print("Press 3 to Exit\n")
    print("Press anything else to see the menu again.")

while True:
    clear_screen()
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        play()
        time.sleep(1)  
    elif choice == "2":
        pause()
        time.sleep(1)  
    elif choice == "3":
        print("Exiting the music player...")
        break  
    else:
        if sound:
            print("Audio file loaded successfully.")
        else:
            print("Error loading audio file.")

        continue