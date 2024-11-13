largest = 0
second_largest = 0

for _ in range(1, 11):	
	number =int(input("Enter a number: "))
	if number > largest:
		second_largest = largest
		largest = number
	elif number > second_largest: 
		second_largest = number

print(f"The largest number is {largest}\nThe second largest number is {second_largest}")
