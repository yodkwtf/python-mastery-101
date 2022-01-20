def fav_colors(a, b, **kwargs):
  print(a, b, kwargs)
  for key,val in kwargs.items():
    print(f"{key}'s fav color is {val}")

fav_colors("purple", "pink", durgesh="red", john="black", tanu="pink")