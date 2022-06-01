import termcolor
from colorama import init

init()

# prints out the docs of the object passed
# help(termcolor)

text = termcolor.colored("Hi There", color="yellow", on_color="on_cyan", attrs=["blink"])

print(text)