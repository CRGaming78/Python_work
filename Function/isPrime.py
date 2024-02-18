def isPrime(num):
    if num==0:
        return False
    elif num==1:
        return False
    else:
        for i in range(2,int(num/2)+1):
            if (num%i)==0:
                return False 
        else:
            return True

num=int(input("Enter a number:"))
print(isPrime(num))