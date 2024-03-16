l_palindrome=0
for i in range(1000,100,-1):
	for j in range(1000,100,-1):
		if i*j>l_palindrome:
			if str(i*j)[::-1]==str(i*j):
				l_palindrome=i*j
				break
			else:
				continue
		break

print ("Larges Palindrome in 3 digit:",l_palindrome)