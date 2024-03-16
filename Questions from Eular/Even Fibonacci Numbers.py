first_num1=0
second_num1=1
fibonacci1=0
even_sum1=0
for i in range(0,100):
	fibonacci1=first_num1+second_num1
	first_num1=second_num1
	second_num1=fibonacci1
	if fibonacci1%2==0:
		even_sum1+=fibonacci1
print ("Sum of Even Fibonacci Numbers \nWhich are less than 100 is",even_sum1)

#**** Warning your pc may crash ****
first_num2=0
second_num2=1
fibonacci2=0
even_sum2=0
for i in range(0,4000000):
	fibonacci2=first_num2+second_num2
	first_num2=second_num2
	second_num2=fibonacci2
	if fibonacci2%2==0:
		even_sum2+=fibonacci2
print ("Sum of Even Fibonacci Numbers \nWhich are less than 4 million is",even_sum2)