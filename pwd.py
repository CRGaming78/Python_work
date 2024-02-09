import random
len_char=int(input("Enter the no. leters:"))
len_num=int(input("Enter the no. of numbers:"))
len_spc=int(input("Enter the no. of symbloles:"))
length=len_char+len_num+len_spc
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = lowercase_letters.upper()
letters=lowercase_letters+uppercase_letters
digits = "0123456789"
symbols = "!@#$%^&*()"
password=[]
for i in range(1,len_char+1):
    char=random.choice(letters)
    password.append(char)
for i in range(1,len_num+1):
    num=random.choice(digits)
    password.append(num)
for i in range(1,len_spc+1):
    sym=random.choice(symbols)
    password.append(sym)
print("" + "".join(password))
