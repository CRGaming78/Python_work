def greatest_of_two(a,b):
  if a>b:
    return a
  elif a<b:
    return b
  else:
    return "Numbers are equal"

def greatest_of_three(a,b,c):
  if a>b and a>c:
    return a
  elif b>a and b>c:
    return b
  else:
    return c

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
greatest_two=greatest_of_two(num1, num2)
greatest_three=greatest_of_three(num1, num2, num3)
print("Greatest of two:", greatest_two)
print("Greatest of three:", greatest_three)
