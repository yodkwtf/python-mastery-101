def colorize(text,color):
  colors = ["red", "blue", "green", "yellow"]

  #! check if color is string and raise custom error if it isn't
  if type(color) is not str:
    raise TypeError("color should be a string")

  #! check if color is acceptable & raise error if not
  if color not in colors:
    raise ValueError(f"{color} is not a valid color")

  #! check if text is string and raise error if it isn't
  if type(text) is not str:
    raise TypeError("text should be a string")

  # print if correct
  print(f"Prints {text} in {color}")



## calling to test
colorize("hello world", "blue")
# colorize(45, "blue")
colorize("hey", "orange")