first_number = int(input("Enter first number: "))

second_number = int(input("Enter second number: "))

third_number = int(input("Enter third number: "))

if first_number > second_number and first_number > third_number :
	print("Number is in decreasing order")

elif third_number > second_number and third_number > first_number :
	print("Number is in increasing order")

else: print("Number isn't in an order")