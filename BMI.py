a=float(input("Enter your weight: "))
b=float(input("Enter your height(in m):"))
bmi=a/(b*b)
print("BMI:",bmi)
if (bmi<=18.5):
  print("You are underweight.")
elif(bmi<=24.9):
  print("You are in normal weight")
elif(bmi<=29.9):
  print("Your are overweight")
else:
  print("You come under obsity classes")
