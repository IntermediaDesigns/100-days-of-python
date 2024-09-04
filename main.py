import random

greeting = [
    'Hello', 'Hola', 'Bonjour', 'Guten Tag', 'Ciao', 'Olá', 'Privyet',
    'Nǐn hǎo', 'Konnichiwa', 'Anyoung haseyo'
]

print(
    f'{greeting[random.randint(0,9)]}, I am a program that will tell you a greeting in a random language.'
)
