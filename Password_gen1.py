import string
import random
length=int(input("Enter the length of the password: "))
characterList = ""
while(True):
  characterList += string.ascii_letters
  characterList += string.digits
  characterList += string.punctuation
  break
password=[]
for i in range(length):
    randomchar=random.choice(characterList)
    password.append(randomchar)
print("" + "".join(password))
