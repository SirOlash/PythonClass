def is_prime(number):
	for index in range (2,number):
		if number % index == 0:
			return false
	return true  

def prime_number(number):
	primes = []
	for number in range (1,21):
		if is_prime(number):
			primes.append(number)
	# print("Prime numbers from 0 to 20:",primes)

is_prime(number)

"""def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_1():
    primes = []
    for number in range(21):
        if is_prime(number):
            primes.append(number)
    print("Prime numbers from 0 to 20:", primes)

# Example usage
prime_numbers_1()"""

	
	