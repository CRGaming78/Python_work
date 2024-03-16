'''f1=open("File1.txt","r+")
data=f1.read()
print(f1.tell())
print(data)
note=input("Enter any note to add to the file: ")
f1.write(note)
f1.seek(0)
data=f1.read()
print(data)
f1.close()'''
import os
def read(f,file_name):
   f.seek(0)# using as a backup
   print(f"Data from {file_name} is {f.read()}")

dec=input("Do you want to crete file? (y/n): ")
if dec =='y' or dec =='Y':
    file_name=input("Enter the new file name with the extension:")
    f=open(file_name,"x")
else:
    file_name=input("Enter the name of the file with the extension: ")
while(True):
    f=open(file_name,"r+")
    content=f.read()
    try:
        print("\n\n------ File MENU ------\n")
        print("1. Print the data")
        print("2. Write into file")
        print("3. Rename the file")
        print("4. Delete the file")
        print("5. Size of the file")
        print("6. exit")
        c=int(input("Enter the number from the menu: "))
        if c==1:
            read(f,file_name)
        elif c==2:
            data=input("Enter any sentance to add to the file: ")
            f.write(data)
            read(f,file_name)
        elif c==3:
            new_name=input("Enter the new name with the extension: ")
            os.rename(file_name,new_name)
            file_name=new_name
        elif c==4:
            os.remove(file_name)
            print("File has been Removed.")
            dec=input("Do you want to add new name(y) or exit(n)?\n")
            if (dec=='y' or dec=='Y'):
                file_name=input("Enter the name of the file with the extension: ")
            else:
                exit(0)
        elif c==5:
            size=os.path.getsize(file_name)
            print(f"Size of {file_name} is {size}")
        elif c==6:
            print("Exiting...")
            exit(0)
        else:
            print("Wrong input")
    except Exception as e:
        print(f"{e} Invaild Input!!")
