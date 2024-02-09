lst1=[]
sum=0
iput=int(input("Enter the number of elements:"))
for i in range(1,iput+1):
  a=int(input("Enter the element:"))
  sum+=a
  lst1.append(a)
print(lst1)
print("Sum:",sum)
print(sum/iput)
