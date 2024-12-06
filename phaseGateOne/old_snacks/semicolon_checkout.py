from datetime import datetime

def check_out(goods,quantity,price,cashier_name,user_name,user_payment):

	current_date_time = datetime.now()
	formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

	print(f"SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA,LAGOS.\nTEL: 03293828343\nDate:  {formatted_date_time} \nCashier: {cashier_name} \nCustomer Name: {user_name}")

	print("========================================================")
	print ("	ITEM	QTY	PRICE		TOTAL(NGN)")
	print("--------------------------------------------------------")
	sub_total = 0
	
	for index in range(0,len(goods)):
		line_cost = quantity[index] * price[index]
		sub_total += line_cost
 
		print (f"	{goods[index]}	{quantity[index]}	{price[index]}		{line_cost:.2f}")
	
	print("--------------------------------------------------------")
	discount = 0.05 * sub_total
	vat = 0.075 * sub_total 
	bill_total = sub_total + vat - discount

	print(f"			Sub Total:	{sub_total:.2f}\n			Discount:	{discount:.2f}\n			VAT @ 7.5:	{vat:.2f}")

	print("========================================================")
	print(f"			Bill Total:	{bill_total:.2f}")

	print("========================================================")
	print(f"			Amount Paid:	{user_payment:.2f}")
	
	balance = user_payment - bill_total
	
	print(f"			Balance:	{balance:.2f}")

	print("========================================================")
	print("	THANK YOU FOR YOUR PATRONAGE!!!")

	print("========================================================")




def invoice(goods,quantity,price,cashier_name,user_name):

	current_date_time = datetime.now()
	formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

	print(f"SEMICOLON STORES\nMAIN BRANCH\nLOCATION: 312, HERBERT MACAULAY WAY, SABO YABA,LAGOS.\nTEL: 03293828343\nDate:  {formatted_date_time} \nCashier: {cashier_name} \nCustomer Name: {user_name}")

	print("========================================================")
	print ("	ITEM	QTY	PRICE		TOTAL(NGN)")
	print("--------------------------------------------------------")
	sub_total = 0
	
	for index in range(0,len(goods)):
		line_cost = quantity[index] * price[index]
		sub_total += line_cost
 
		print (f"	{goods[index]}	{quantity[index]}	{price[index]}		{line_cost:.2f}")
	
	print("--------------------------------------------------------")
	discount = 0.05 * sub_total
	vat = 0.075 * sub_total 
	bill_total = sub_total + vat - discount

	print(f"			Sub Total:	{sub_total:.2f}\n			Discount:	{discount:.2f}\n			VAT @ 7.5:	{vat:.2f}")

	print("========================================================")
	print(f"			Bill Total:	{bill_total:.2f}")

	print("========================================================")
	print(f"	THIS IS NOT A RECEIPT KINDLY PAY {bill_total:.2f}")	

	print("========================================================")
	


def main_method():
	
	add_more = True
	
	goods = []
	quantity = []
	price = []

	user_name = input("What is the customer's name?: ")

	while add_more:
		goods_bought = input("What did the user buy?: ")
		goods.append(goods_bought)

		pieces_bought = int(input("How many pieces?: "))
		quantity.append(pieces_bought)

		price_per_unit = float(input("How much per unit?: "))
		price.append(price_per_unit)
		
		yes_no = False

		while yes_no == False :
			user_choice = input("Do you want to add more items?yes/no: ")
			if user_choice.lower() == "yes":
				yes_no = True
			
			elif user_choice.lower() == "no":
				yes_no = True
				add_more = False
			else: print("Invalid input!!!")


	cashier_name = input("What is your name?: ")

	print("You will get a 5% discount!!!!!")
	
	print("")

	invoice(goods,quantity,price,cashier_name,user_name)
	
	print("")

	user_payment = float(input("How much did the user give to you?: "))
	print("")
	print("")

	check_out(goods,quantity,price,cashier_name,user_name,user_payment)
main_method()
		

	
	
	

	