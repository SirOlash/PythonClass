integer = int(input("Enter an integer: "))

while integer > 0:
	last_number = integer % 10 
	integer //= 10  
	print (last_number,end=" ")
