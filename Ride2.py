ht=int(input("Enter your height="))
baby=150
child=250
adult=500
if ht >=4:
  print("you can ride")
  age=int(input("enter your age"))
  if age<=12:
    print("you have to pay",baby)
    d=input("Do you want a photograph(Y/N)? ")
    if (d=='Y' | d=='y'):
      print("Total will be:",baby+50)
  if age<=18:
    print("you have to pay",child)
    d=input("Do you want a photograph(Y/N)? ")
    if (d=='Y' | d=='y'):
      print("Total will be:",child+50)
  else:
    print("you have to pay",adult)
    d=input("Do you want a photograph(Y/N)? ")
    if (d=='Y' | d=='y'):
      print("Total will be:",adult+50)
else:
  print("You cannot ride")
