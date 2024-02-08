x=float(input("Enter first number:"))
y=float(input("Enter secound number:"))
z=float(input("Enter Third Number:"))
if x>=y:
    if x>=z:
        print(x,"is the largest number")
    else:
        print(z,"is the larges number")
else:
    if y>=z:
        print(y,"is the largest number")
    else:
        print(z,"is the larges number")