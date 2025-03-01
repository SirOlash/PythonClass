import re
from unittest import case

import bcrypt

# user_name = input("Enter your name: ")
# password = input("Enter your password: ")
#
# hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#
# print("username: ", user_name)
# print("password:", hashed_password)


USER_DETAILS = 'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_to_file(username, hashed_password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f'{username}:{hashed_password.decode('utf-8')}\n')

def register_user():
    # while True:
    #     user_name = input("Enter your name: ")
    #
    #     if not user_name:
    #         print("Username can't be empty")
    #         continue
    #     break

    while True:
        email = input("Enter your email: ")
        if re.fullmatch(r'[A-Za-z]+@[a-z]+[.][a-z]+\.[a-z]*', email):
            break
        # if not email:
        else:
            print("Enter a valid email")
            continue


    while True:
        password = input("Enter your password: ")
        if not password:
            print("Password can't be empty")
            continue
        break

    save_to_file(email,hash_password(password))

def validate_user(username, password):
    try:
        with open(USER_DETAILS, "r") as file:
           # details = file.read()
            for line in file:
                stored_username,stored_password = line.strip().split(':')
                if username == stored_username:
                    return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))

    except FileNotFoundError:
        print("File not found")

def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if validate_user(username, password):
        print("Login successful")

    else:
        print("Invalid username or password")

def main():
   print( """""
   1 to register_user
   2 to login user
   3 to exit.""""")
   choice = input("Enter your choice: ")

   match choice:
    case "1":
        register_user()
    case "2":
        login_user()
    case "3":
        print("Thank you!")


main()
