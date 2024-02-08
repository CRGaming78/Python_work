lst1=[]
max=0
#lst1=input("Enter the list without space:")
#lst1=lst1.split(" ")
iput=int(input("Enter the number of elements:"))
for i in range(1,iput+1):
  a=int(input("Enter the element:"))
  lst1.append(a)
for i in lst1:
    if i>max:
        max=i
print("Max value:",max)
