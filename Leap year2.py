Year=int(input("Enter the Year you want to check: "))
if Year%4==0:
  if Year%100==0:
    if Year%400==0:
      print("Leap Year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")
