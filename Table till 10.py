def multi(a):
    for c in range(1,a+1):
        print("\n")
        for i in range(1,11):
            b=c*i
            print(c,"*",i,"=",b)
    return

a=int(input("Enter a number for table till:"))
multi(a)