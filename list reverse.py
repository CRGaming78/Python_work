lst=[]
n=int(input("How many numbers do you want to add in list:"))
for i in range(0,n):
    a=input("Enter the element:")
    lst.append(a)
print("LIST:",lst)
lst2=[]
for i in range(n-1,-1,-1):
    lst2.append(lst[i])
print("Reversed list:",lst2)
#easy way lst.sort(reverse=True) :)