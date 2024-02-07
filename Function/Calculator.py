def addition(a,b):
    x=a+b
    return(x)

def sub(a,b):
    x=a-b
    return(x)

def multi(a,b):
    x=a*b
    return(x)

def div(a,b):
    x=a/b
    return(x)

a=float(input("Enter a number (A):"))
b=float(input("Enter second number (B):"))
print("What do you want to do:-")
print("1:addition")
print("2:Subtration")
print("3:Multiply")
print("4:Divide")
c=int(input("Enter the number:"))
if c==1:
    x=addition(a,b)
    print("Added number:",x)
elif c==2:
    x=sub(a,b)
    print("Subratacted number:",x)
elif c==3:
    x=multi(a,b)
    print("Mutliplied number:",x)
elif c==4:
    x=div(a,b)
    print("Divivded number:",x)
else:
    print("Invaild number entered")