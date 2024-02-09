import math

def hypotenuse(a,b):
  c_squ=a**2+b**2
  c=math.sqrt(c_squ)
  return c

a=float(input("Enter the base:"))
b=float(input("Enter the hight:"))
c=hypotenuse(a, b)
print("The length of the hypotenuse is:", c)
