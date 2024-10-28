integer = int(input("Enter a number from 0-1000:"))

last_number = integer%10
first_two = integer//10

if first_two == 0:
	print(f"The sum is {last_number}")
if first_two != 0:
	middle_number = first_two % 10
	first_number = first_two//10
	if first_number == 0:
		sum_of_two = middle_number + last_number;
		print(f"The sum is {sum_of_two}")
	if first_number != 0:
		sum_of_three = first_number + middle_number + last_number
		print(f"The sum is {sum_of_three}")