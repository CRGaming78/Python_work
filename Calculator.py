a=float(input("Enter a number:"))
b=float(input("Enter 2nd number:"))
print("Menu")
print("1.addition")
print("2.Sub")
print("3.Multi")
print("4.Divide")
x=int(input("Enter the no. from menu:"))
if(x==1):
  print("Added number:",a+b)
elif(x==2):
  print("Sub number:",a-b)
elif(x==3):
  print("Multiplied number:",a*b)
elif(x==4):
  print("Divided number:",a/b)
else:
  print("Wrong number entered.")
