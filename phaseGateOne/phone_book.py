def display_phone_book_menu():
    print("""
PhoneBook Menu:
1. Add contact.
2. Remove contact.
3. Find contact by phone number.
4. Find contact by first name.
5. Find contact by last name.
6. Edit contact.
    """)

    option = int(input("> "))
    match option:
        case 1: add_contact()
        case 2: delete_contact()
        case 3: search_contact_by_number()
        case 4: search_contact_by_first_name()
        case 5: search_contact_by_last_name()
        case 6: update_contact()


def add_contact():
    first_name = input("Enter first name: ")
    first_name_list.append(first_name)

    last_name = input("Enter last name: ")
    last_name_list.append(last_name)

    phone_number = input("Enter phone number: ")    
    phone_number_list.append(phone_number)

    email = input("Enter email address: ")
    email_list.append(email)

    print("Contact saved!")
    display_phone_book_menu()


def delete_contact():
    contact_name = input("Enter the name you want to remove: ")
    if contact_name in first_name_list:
        index = first_name_list.index(contact_name)

        first_name_list.pop(index)
        last_name_list.pop(index)
        phone_number_list.pop(index)
        email_list.pop(index)

        print("Contact deleted.")
    else:
        print("Contact does not exist.")
    display_phone_book_menu()


def search_contact_by_number():
    contact_number = input("Enter the phone number you want to find: ")
    if contact_number in phone_number_list:
        index = phone_number_list.index(contact_number)
        print(f"First Name: {first_name_list[index]}\nLast Name: {last_name_list[index]}\nPhone Number: {phone_number_list[index]}\nEmail: {email_list[index]}")
    else:
        print("Contact does not exist.")
    display_phone_book_menu()


def search_contact_by_first_name():
    contact_first_name = input("Enter the first name you want to find: ")
    if contact_first_name in first_name_list:
        index = first_name_list.index(contact_first_name)
        print(f"First Name: {first_name_list[index]}\nLast Name: {last_name_list[index]}\nPhone Number: {phone_number_list[index]}\nEmail: {email_list[index]}")
    else:
        print("Contact does not exist.")
    display_phone_book_menu()


def search_contact_by_last_name():
    contact_last_name = input("Enter the last name you want to find: ")
    if contact_last_name in last_name_list:
        index = last_name_list.index(contact_last_name)
        print(f"First Name: {first_name_list[index]}\nLast Name: {last_name_list[index]}\nPhone Number: {phone_number_list[index]}\nEmail: {email_list[index]}")
    else:
        print("Contact does not exist.")
    display_phone_book_menu()


def update_contact():
    contact_name = input("Enter the name of the contact you want to update: ")
    if contact_name in first_name_list:
        index = first_name_list.index(contact_name)

        new_first_name = input("Enter new first name: ")
        first_name_list[index] = new_first_name

        new_last_name = input("Enter new last name: ")
        last_name_list[index] = new_last_name

        new_phone_number = input("Enter new phone number: ")
        phone_number_list[index] = new_phone_number

        new_email = input("Enter new email address: ")
        email_list[index] = new_email

        print("Contact updated successfully.")
    else:
        print("Contact does not exist.")
    display_phone_book_menu()

first_name_list = []
last_name_list = []
phone_number_list = []
email_list = []

display_phone_book_menu()
