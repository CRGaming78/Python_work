'''def fibonacci(n):
  a,b=0,1
  for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

num=int(input("Enter the no. of terms:"))
fibonacci(num)'''
#upar wala faster hai
def fibonacci(n):
  if n<=1:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter the no. of terms:"))
for i in range(num):
  print(fibonacci(i),end=" ")

