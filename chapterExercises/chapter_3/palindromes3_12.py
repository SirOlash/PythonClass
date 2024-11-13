number = int(input("Enter an integer: "))

if number//10000 <= 9 and number // 1000 != 0:
	first_number = number // 10000
	second_number = (number //1000)%10
	third_number =  (number //100)%10 
	fourth_number =  (number //10)%10
	fifth_number = number % 10
	
	if first_number == fifth_number and second_number == fourth_number:
		print (number, "is a Palindrome")
	else: print(number, "is not a Palindrome")  
else:print("Enter a 5 digit number")
	
	