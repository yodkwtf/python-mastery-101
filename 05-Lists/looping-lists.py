colors = ["red", "purple", "magenta", "crimson"]
numbers = list(range(1,5))

# forloop
for num in numbers:
  print(num*num)

# while loop
i = 0
while i < len(colors):
  print(f"Color {i+1}: {colors[i]}")
  i+=1
