def print_in_color(word, color):
    color_codes = {
        "purple": "\033[035m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[036m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    if color in color_codes:
        print(color_codes[color], word, sep="", end="")
        print(color_codes["reset"])
    else:
        print("Invalid color")

print("Super Subroutine")
print("with my")
print_in_color("colorful ", "purple")
print_in_color("text ", "cyan")
print_in_color("printer", "yellow")
