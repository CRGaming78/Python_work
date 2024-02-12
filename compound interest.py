principal=float(input("Enter the principal amount:"))
rate=float(input("Enter the rate of interest:"))
time=float(input("Enter the time in years:"))
roi=rate/100
amount=principal*(1+roi)**time
ci=a-p
print("Total Amount:",amount)
print("Compound interest is ",ci)
