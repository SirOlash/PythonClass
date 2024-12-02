user_input = int(input("Enter an integer between 0-1000: "))

sum = 0
while user_input > 0:
	last_number = user_input % 10
	sum += last_number
	user_input //= 10

print(f"{sum}")