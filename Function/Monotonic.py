def isMonotonic(A):
    x,y=[],[]
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x==A or y==A):
        return True
    return False

a=[]
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    b=input("Enter the element:")
    a.append(b)
print(isMonotonic(a))
