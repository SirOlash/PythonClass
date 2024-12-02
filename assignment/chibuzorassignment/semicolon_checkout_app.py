def main():
    print(" SEMICOLON STORE! \nMAIN BRANCH \nLOCATION: 312, HERBERT MACAULAY SABO YABA, LAGOS. \nTEL: 08083484717 \nDate : 02-Dec-24 10:48:11 pm\nCashier; Cashier's Name")
    

    cart = []
    vat_rate = 7.5
    discount_rate = 0.1 
    adding_products = True
 
    while adding_products:
        product_name = input("What did the user buy? (or type 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        customer_name = (input("What is the customer's name?: "))
        product_quantity = int(input("How many pieces?: "))
        product_price = float(input("How much per unit?: "))
               
        
        cart.append({
            "name": customer_name,
            "name": product_name,
            "price": product_price,
            "quantity": product_quantity,
            "total": product_price * product_quantity,
	    
        })

    subtotal = sum(item["total"] for item in cart)

   
    discount = subtotal * discount_rate if subtotal > 100 else 0

    vat = subtotal * (vat_rate / 100)

    total = subtotal - discount + vat
    
    print("\n=======================================")
    print("ITEM\tQTY \tPRICE \tTOTAL(NGN)")
    print("_")
    for item in cart:
        print(f"{item['name']} \t(x{item['quantity']}): \t{item['price']} \t{item['total']:.2f}")
    print("")

    print(f"\nSubtotal: {subtotal:.2f}")
    print(f"Discount: -{discount:.2f}")
    print(f"VAT 7.5%: {vat:.2f}")
    print("=======================================")
    print(f"Bill Total: {total:.2f}")
    print("=======================================")
    print("\nTHIS IS NOT A RECEIPT KINDLY PAY!", total)


    


if _name_ == "_main_":
    main()