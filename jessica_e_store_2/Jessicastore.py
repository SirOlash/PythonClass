def jessica_store_main_menu():
	shopping = True

	while shopping:
		user_choice = int(input("Welcome to Jessica's E-Store!\n1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit\n>>>"))

		match user_choice:
			case 1: View_products()
			case 2: pass
			case 3: pass
			case 4: pass
			case 5: pass
			case 6: shopping = False

def View_products():
	user_choice_2 = int(input("These are the products!!!\n1. Laptop - $1000\n2. Phone - $500\n3. Headphones - $100\n>>>"))
	
	match user_choice_2:
 		case 1: pass
print (jessica_store_main_menu())	




	
