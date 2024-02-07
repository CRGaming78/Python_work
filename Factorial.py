c=int(input("Enter a number:"))
factorial=1
if(c<0):
  print("Error, factorial can't be negative.")
elif(c==0|c==1):
  print("Factorial of",c,"is",1)
elif(c>=2):
  for i in range(2,c+1):
    factorial=factorial*i
  print("Factorial:",factorial)
else:
  print("Error")
