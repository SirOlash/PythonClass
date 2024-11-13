# 3,10 > 18(3+6+9=18)
def sum_of_multiples():
	first_number = int(input("Enter first number: "))
	second_number = int(input("Enter second number: "))
	sum = 0

	for count in range (first_number,second_number + 1,first_number):
		sum +=count
	print(sum)
sum_of_multiples()
