end_msg = "stop it"

msg = input("SIS: Hey how's it going?\n> ")

while msg != end_msg:
  print(f"SIS: {msg}")
  msg = input("> ")
else:
  print("SIS: Haha okay ")