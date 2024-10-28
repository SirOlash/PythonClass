integer = int(input("Enter a three digit integer: "))

last_number = integer % 10
first_number = integer // 100
first_two = integer // 10
middle_number = first_two % 10

if last_number == first_number:
	print(integer," is a palindrome")

else:print(integer, " is not a palindrome")

