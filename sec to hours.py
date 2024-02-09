seconds=int(input("Enter the total no. of seconds:"))
hours=seconds//3600
remaining_sec=seconds%3600
minutes=remaining_sec//60
remaining_sec=remaining_sec%60
print("The time is:", hours, "hours,", minutes, "minutes,", remaining_sec, "seconds.")
