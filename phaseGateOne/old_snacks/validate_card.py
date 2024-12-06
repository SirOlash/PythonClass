def main():
    while True:
        credit_card_number = input("Hello, Kindly Enter card details to verify: ")
        
        if 13 <= len(credit_card_number) <= 16:
            break
        else:
            print("Enter a valid Credit Card Number!!!!")

    print("******************************************")
    print("** Credit Card Type: ", get_card_type(credit_card_number))
    print("** Credit Card Number: ", credit_card_number)
    print("** Credit Card Digit Length: ", len(credit_card_number))
    print("** Credit Card Validity Status: ", validate_card(credit_card_number))
    print("******************************************")


def get_card_type(credit_card_number):
   
    if credit_card_number.startswith("4"):
        return "Visa Card"
    elif credit_card_number.startswith("5"):
        return "MasterCard"
    elif credit_card_number.startswith("37"):
        return "American Express Card"
    elif credit_card_number.startswith("6"):
        return "Discover Card"
    else:
        return "Invalid Card"


def validate_card(credit_card_number):
   
    even_sum = 0
    odd_sum = 0


    for index in range(len(credit_card_number)):
        digit = int(credit_card_number[-(index + 1)])  
        
        if index % 2 == 0:  # Odd-positioned digits (1-based index)
            odd_sum += digit
        else: 
            doubled = digit * 2
            if doubled > 9:  
                doubled = (doubled % 10) + (doubled // 10)
            even_sum += doubled

    total_sum = odd_sum + even_sum
    return "Valid" if total_sum % 10 == 0 else "Invalid"


main()
