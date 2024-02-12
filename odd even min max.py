a=[]
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    b=int(input("Enter the element:"))
    a.append(b)
print("Smallest value in list:",min(a))
print("Maximum value in list:",max(a))
even,odd=[],[]
for i in range(0,n):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
print("Even number in list:",even)
print("Odd number in list:",odd)
