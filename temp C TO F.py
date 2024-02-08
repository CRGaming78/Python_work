def Celsius_to_Faherenheit(F):
    x=(F*9/5)+32
    return(x)

F=float(input("Enter Tenprature in Celsius:"))
x=Celsius_to_Faherenheit(F)
print("Temprature in Faherenheit:",x)