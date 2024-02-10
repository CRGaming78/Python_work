def flatten_list(nested_list):
    flat_list=[]
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

lst=[[1,2,3],[4,5,6,7],[8,9]]
'''n=int(input("How many numbers do you want to add in list:"))
for i in range(0,n):
    a=input("Enter the element:")
    lst.append(a)'''
flat_list=flatten_list(lst)
print(flat_list)
