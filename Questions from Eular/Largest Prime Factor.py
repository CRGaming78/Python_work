num2=600851475143
i2=2 #*prime number starts from 2

while i2<num2:
	if num2%i2==0:
		num2=num2/i2
		i2-=1
	i2+=1
print(f"largest prime factor of the number of 600851475143 is {num2}")