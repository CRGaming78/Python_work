import random
min=1
max=6
roll_again="y"
while roll_again == "y" or roll_again == "Y":
    print("Rolling the dice...")
    val=random.randint(min, max)
    print("You get... :", val)
    roll_again = input("Roll the dice again? (y/n)..")
