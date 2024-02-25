def login():
    while(True):
        # print(track)
        try:
            print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. Exit library\n""")
            us_in=int(input("Enter your choice: "))
            if us_in==1:  # listing
                Delhilibrary.displayAvailableBooks()
            elif us_in==2:  # borrow
                Delhilibrary.borrowBook(
                    input("Enter your name: "),student.requestBook())
            elif us_in==3:  # return
                Delhilibrary.returnBook(student.returnBook())
            elif us_in==4:  # donate
                Delhilibrary.donateBook(student.donateBook())
            elif us_in==5:  # track
                for i in track:
                    for key, value in i.items():
                        holder=key
                        book=value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track)==0:
                    print("NO BOOKS ARE ISSUED!. \n")
            elif us_in==6: #exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" ♦-- "+book)
        print("\n")

    def borrowBook(self,name,bookname):
        if bookname not in self.books:
            print(f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED : THANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("BOOK RETURNED : THANK YOU! \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)

class Student():
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book=input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name=input("Enter your name: ")
        self.book=input("Enter name of the book you want to return: ")
        if {name:self.book}in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("Okay! you want to doante book!")
        self.book = input("Enter name of the book you want to donate: ")
        return self.book

if __name__=="__main__":
    Delhilibrary = Library(["Book of disquiet", "Psychology of money", "48 laws of power", "indian", "Baghatgita", "General relativity"])
    login_de=open(r"D:\Login_details.csv","r+") #login details
    student=Student()
    track=[]
    print("\t♦♦♦♦♦♦♦ WELCOME TO THE <name> LIBRARY ♦♦♦♦♦♦♦\n")
    while (True):
        l=login_de.readlines()
        print("\n1- Login to Library\n2- Create a new Library Account\n3- Guest Login to Library\n4- Exit")
        cho=int(input("Enter your choice: "))
        try:
            if cho==1:
                us_name=input("Enter your Name: ")
                us_pwd=input("Enter your password: ")
                check=us_name+":"+us_pwd+"\n"
                login_susses=-1
                for i in l:
                    if i==check:
                        print("Login Sussesfully")
                        login_susses=1
                if login_susses==-1:
                    print("Account not found")
                    break
                else:
                    login_de.close()
                    login()
            elif cho==2:
                cr_name=input("Enter your name: ")
                cr_pwd=input("Enter your password: ")
                cr_enter=cr_name+":"+cr_pwd+"\n"
                login.write(cr_enter)
                print("Thank you for Creating an account")
            elif cho==3:
                login()
            elif cho==4:
                print("Thank you for using my program :D")
                login_de.close()
                exit()
            else:
                print("Invaild number entered.")
        except Exception as e:              #catch errors
            print(f"{e}---> INVALID INPUT! \n")