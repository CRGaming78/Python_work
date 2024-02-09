import random
names=input("Please enter everyones name seperated by comma: ")
names_list=names.split(",")
length=len(names_list)
#print(names_list)
choice=random.randint(0,length-1)
print(f"{names_list[choice]} will pay the bill")
