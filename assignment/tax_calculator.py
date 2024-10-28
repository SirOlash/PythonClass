citizen =input("Enter your name: ")

earnings = float(input("Enter your earnings in USD: "))

if earnings > 30000:
	tax = 0.2 * earnings;
	print("Hello ",citizen, ",Your tax is ", tax)

else: 
	tax = 0.15 * earnings
	print("Hello ",citizen, ",Your tax is ", tax)	
 
