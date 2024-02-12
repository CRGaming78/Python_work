def swap(lst,pos1,pos2):
    temp=lst[pos1]
    lst[pos1]=lst[pos2]
    lst[pos2]=temp
    return lst
    
a=[]
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    b=input("Enter the element:")
    a.append(b)
pos1=int(input("Enter the pos to change:"))
pos2=int(input("Enter the pos where you want to put the value:"))
print(swap(a,pos1-1,pos2-1))
