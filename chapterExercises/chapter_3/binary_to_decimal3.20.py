binary_number = int(input("Enter binary number"))

position = 1
decimal = 0

while binary_number > 0:
	last_number = binary_number % 10
	decimal += last_number * position
	position *= 2
	binary_number //= 10 
print (decimal)

