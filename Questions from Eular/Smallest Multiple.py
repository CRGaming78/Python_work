
#? I have used euclid Algorithm to find the lcm also called smallest multiple
#* This method much more efficient
def gcd(n1,n2):
	remainder=1
	while remainder!=0:
		remainder=n1%n2
		n1=n2
		n2=remainder
	return n1

#* lcm=(number1*number2)/GCD(number1,number2)
def lcm(n1,n2):
	return (n1*n2)/gcd(n1,n2)

l = lcm(2,3) # loading lcm with starting value
#? lcm of three numbers n1,n2,n3 is
#* lcm(lcm(n1,n2),n3)
for i in range(4,21):
	l = lcm(l,i)

print ("LCM:",l)