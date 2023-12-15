# Write code below 💖
gry = 0
rav = 0
huf = 0
sly = 0

answer = int(input("Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n"))
if answer == 1:
  gry = gry + 1
  rav = rav + 1
elif answer == 2:
  huf = huf + 1
  sly = sly + 1
else:
  print("Wrong input")
answer = int(input("Whem I'm dead, I want people to remember me as: \n 1) The good \n 2) The Great \n 3) The Wise \n 4) The Bold \n"))
if answer == 1:
  huf = huf + 2
elif answer == 2:
  sly = sly + 2
elif answer == 3:
  rav = rav + 2
elif answer == 4:
  gry = gry + 2
else:
  print("Wrong input")

answer = int(input("Which kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum \n"))
if answer == 1:
  sly = sly + 4
elif answer == 2:
  huf = huf + 4
elif answer == 3:
  rav = rav + 4
elif answer == 4:
  gry = gry + 4
else:
  print("Wrong input")

if sly > huf and sly > rav and sly > gry:
  print("Your house is Slytherin!")
elif huf > sly and huf > rav and huf > gry:
  print("Your house is Hufflepuff!")
elif gry > sly and gry > rav and gry > huf:
  print("Your house is Gryffindor!")
elif rav > gry and rav > sly and rav > huf:
  print("Your house is Ravenclaw!")

print(gry,sly,rav,huf)      





