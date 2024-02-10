lst=[]
n=int(input("How many numbers do you want to add in list:"))
for i in range(0,n):
    a=int(input("Enter the element:"))
    lst.append(a)
print("LIST:",lst)
print("Even number in list:")
for i in range(1,n):
    a=lst[i]
    if a%2==0:
        print(lst[i])
