def fav_colors(**args):
  print(args)
  for key,val in args.items():
    print(f"{key}'s fav color is {val}")

fav_colors(durgesh="red", john="black", tanu="pink")