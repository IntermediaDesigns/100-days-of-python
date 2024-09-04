color_codes = {
    "red": "\033[0;31m",
    "green": "\033[92m",
    "purple": "\033[035m",
    "yellow": "\033[1;33m",
    "blue": "\033[0;34m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}

def print_in_color(word, color):
    if color in color_codes:
        print(color_codes[color], word, sep="", end="")
        print(color_codes["reset"])
    else:
        print("Invalid color")
        
music_app = "Music App"

interface1_no_color = f"=== {music_app} ===".center(50)

interface1 = interface1_no_color.replace("==", f"{color_codes['red']}={color_codes['white']}={color_codes['blue']}=").replace("==", f"{color_codes['white']}{color_codes['blue']}=").replace("Music App", f"{color_codes['yellow']}Music App")

interText1 = "🔥▶️ \tRadio Gaga"
interText2 = "Queen"

prev = "PREV"
next = "NEXT"
pause = "PAUSE"

print("Interface 1")
print()
print(interface1)
print()
print_in_color(f"{interText1: <0}", "white")
print_in_color(f"{interText2: >13}", "yellow")
print()
print_in_color(f"{prev: <20}", "white")
print_in_color(f"{next: >10}", "green")
print_in_color(f"{pause: >17}", "purple")
print()
print()

print("Interface 2")
print()

interface2 = "WELCOME TO"
interText2 = "--    ARMBOOK    --"
interText3 = "Definitely not a rip off of"
interText4 = "a certain other social"
interText5 = "networking site."

interText6 = "Honest."

interText7 = "Username:"
interText8 = "Password:"

print_in_color(f"{interface2:^50}", "white")
print_in_color(f"{interText2:^50}", "blue")
print()
print_in_color(f"{interText3:>43}", "yellow")
print_in_color(f"{interText4:>43}", "yellow")
print_in_color(f"{interText5:>43}", "yellow")
print()
print_in_color(f"{interText6:^50}", "red")
print()
print_in_color(f"{interText7:^50}", "white")
print_in_color(f"{interText8:^50}", "white")