"""prompt user to enter a number from 0 - 1000
save the number as "user_input"
make a while loop that runs provided the user input is greater than 0
calculate last number by user_input % 10 in the loop
then add the value to sum which is originaly zero
then use a floor division to divide the user input by 10
this goes on till the user input is less than 0"""



user_input = int(input("Enter an integer between 0-1000: "))

sum = 0
while user_input > 0:
	last_number = user_input % 10
	sum += last_number
	user_input //= 10

print(f"{sum}")