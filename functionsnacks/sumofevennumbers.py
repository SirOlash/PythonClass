def sum_of_even_numbers():
	number =int(input("Enter a number: "))
	sum = 0
	for count in range(0,number+1,2):
		
		sum+=count	
	print (sum)
sum_of_even_numbers()