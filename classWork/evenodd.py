number = int(input("Enter a number: "))

even = 0
odd = 0
def get_even(number):
	for count in range(1,number):
		if number % 2 == 0:
			return even+1
	odd+1
print(get_even(number))