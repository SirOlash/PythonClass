factorial = 1
number = int(input("Enter a number:  "))

for count in range(number, 0, -1):
	factorial *= count 	
print (factorial)