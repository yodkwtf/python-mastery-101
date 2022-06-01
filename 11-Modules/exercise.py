from termcolor import colored
from pyfiglet import figlet_format
COLORS = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
message = input("> What do you want to print? ")
color = input("> What color you want? ")
if color not in COLORS:
    color = 'cyan'

ascii_art = figlet_format(message, font="slant")
colored_art = colored(ascii_art, color=color)
print(colored_art)
