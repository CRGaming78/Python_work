def pos(lst,num,size):
    pos=0
    for i in range(0,size+1):
        pos+=1
        if num==lst[i]:
            return pos
    return

a=[]
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    b=input("Enter the element:")
    a.append(b)
num=input("Enter the element to search:")
print(a)
search=pos(a,num,n)
print("\n",search)
