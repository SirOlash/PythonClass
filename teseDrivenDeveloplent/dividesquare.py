import math
def get_division_or_square (number):
	if number % 5 == 0:
		square_root = round((math.sqrt(number)),2)
		return square_root

	elif number % 5 != 0:
		remainder = round((number % 5),2)
		return remainder

	elif type (number) is not int :
		return "invalid"
	elif number < 0 :
		return "invalid"
		
	#raise TypeError



def get_future_investment (investment,monthly,month):
	future_investment_amount = investment * (1 + monthly/100)**month
	future_investment_amount = round(future_investment_amount,2)

	return future_investment_amount
