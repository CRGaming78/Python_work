name=input("Enter your Name:")
sap_id=input("Enter your SAP ID:")
dob=input("Enter your Date of Birth:")
program=input("Enter your learning program:")
sem=input("Enter you semester:")
python=float(input("Enter your python marks:"))
chem=float(input("Enter your Chemistry marks:"))
eng=float(input("Enter your English marks:"))
phy=float(input("Enter your physics marks:"))
PDS=float(input("Enter your PDS marks:"))
percentage=(python+chem+eng+phy+PDS)/5
CGPA=percentage/10
print("\n\nStudent details:")
print("NAME: ",name)
print("SAP ID: ",sap_id)
print("DATE OF BIRTH: ",dob)
print("PROGRAM ENTERED: ",program)
print("SEMESTER: ",sem)
print("Marks:")
print("PDS:",PDS)
print("Python:",python)
print("Chemistry:",chem)
print("English:",eng)
print("Physics:",phy)
print("Percentage:",percentage)
print("CGPA:",CGPA)
if CGPA<=3.4:
    print("Grade:F")
elif CGPA<=5.0:
    print("Grade:C+")
elif CGPA<=6:
    print("Grade:B")
elif CGPA<=7:
    print("Grade:B+")
elif CGPA<=8:
    print("Grade:A")
elif CGPA<=9:
    print("Grade:A+")
else:
    print("Grade:O")

