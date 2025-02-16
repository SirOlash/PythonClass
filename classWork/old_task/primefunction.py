number = int(input("Enter a number: "))
# number = 8
def get_prime(number):
	for count in range(2,number):
		if number % count == 0:
			return False
	
	return True

result = get_prime(number)
print(get_prime(number))	