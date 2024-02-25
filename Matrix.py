#matrix 3x3 
import numpy

def print_mat(result):
    for r in result:
        print(r)

matrix1=[]
print("Enter Value for Matrix 1:\n")
for i in range(3):
    row=[]
    for j in range(3):
        number=int(input(f"Enter number for row {i+1}, column {j+1}: "))
        row.append(number)
    matrix1.append(row)
matrix2=[]
print("Enter Value for Matrix 2:\n")
for i in range(3):
    row=[]
    for j in range(3):
        number=int(input(f"Enter number for row {i+1}, column {j+1}: "))
        row.append(number)
    matrix2.append(row)

print("\n","-"*5,"MENU","-"*5)
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
n=int(input("Enter the number from menu: "))
result=[]
if n==1:
    result=numpy.add(matrix1,matrix2)
    print_mat(result)
elif n==2:
    result=numpy.subtract(matrix1,matrix2)
    print_mat(result)
elif n==3:
    result=numpy.dot(matrix1,matrix2)
    print_mat(result)
else:
    print("Invaild input.")
