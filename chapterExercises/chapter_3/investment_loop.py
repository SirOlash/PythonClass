rate = 7/100
total = 0
number_of_years=int(input("Enter the amount of years: "))
principal=float(input("Enter your investment amount: "))




for count in range(1,number_of_years+1):
	
	amount_on_deposit = (principal * (1 + rate)**number_of_years) - principal
	total += amount_on_deposit

	print(f"The amount on deposit after {count} year is {total:.2f}")

