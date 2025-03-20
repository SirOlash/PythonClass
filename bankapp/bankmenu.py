import re
import time

from bankapp.bank import Bank


class BankMenu:
    def __init__(self):
        self.bank = Bank()

    def main(self ):
        self.main_menu()

    def main_menu(self):
        while True:
            print(""""
            Welcome to GTB Bank
            1. Create Account
            2. Deposit
            3. Withdrawal
            4. Transfer
            5. Check Balance
            6. Change Pin 
            7. Exit
            """"")
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    self.create_account()
                    break
                case 2:
                    self.deposit()
                    break
                case 3:
                    self.withdrawal()
                    break
                case 4:
                    self.transfer()
                    break
                case 5:
                    self.check_balance()
                    break
                case 6:
                    self.change_password()
                    break
                case 7:
                    print("Thank you for using GTB Bank")
                    exit()
                case _:print("invalid choice")


    def deposit(self):
        account_number = int(input("Enter your account number: "))
        try:
            self.bank.find_account_by(account_number)
            amount = int(input("Enter the amount to be deposited: "))
            self.bank.deposit(account_number,amount)
            self.loading_screen("Please Wait")
            print(f"You just deposited NGN{amount} to Account Number:{account_number}")

        except ValueError as e:
            print(e)

        finally:
            self.main_menu()

    def withdrawal(self):
        account_number = int(input("Enter your account number: "))
        try:
            self.bank.find_account_by(account_number)
            amount = int(input("Enter the amount to be withdrawn: "))
            password = self.valid_password("Enter your password: ")
            self.bank.withdraw(account_number,amount,password)
            self.loading_screen("Please Wait")
            print(f"You just withdrawn NGN{amount} to Account Number:{account_number}")

        except ValueError as e:
            print(e)

        finally:
            self.main_menu()

    def transfer(self):
        sender_account_number = int(input("Enter your account number: "))
        receiver_account_number = int(input("Enter your account number: "))
        if sender_account_number == receiver_account_number:
            print("You cannot transfer to the same account")
            self.main_menu()
        try:
            self.bank.find_account_by(sender_account_number)
            self.bank.find_account_by(receiver_account_number)
            amount = int(input("Enter the amount to be transferred: "))
            password = self.valid_password("Enter your password: ")
            self.bank.transfer(sender_account_number,receiver_account_number,amount,password)
            self.loading_screen("transferring")
            print(f"You have successfully transferred NGN{amount} to Account Number:{sender_account_number}")

        except ValueError as e:
            print(e)

        finally:
            self.main_menu()

    def check_balance(self):
        account_number = int(input("Enter your account number: "))
        try:
            self.bank.find_account_by(account_number)
            password = self.valid_password("Enter your password: ")
            balance = self.bank.check_balance(account_number,password)
            print(f"Your balance is: {balance}")

        except ValueError as e:
            print(e)
        finally:
            self.main_menu()

    def change_password(self):
        account_number = int(input("Enter your account number: "))
        try:
            self.bank.find_account_by(account_number)
            old_password = self.valid_password("Enter your old password: ")
            new_password = self.valid_password("Enter your new password: ")
            self.bank.update_pin(account_number,old_password,new_password)
            self.loading_screen("changing password")
            print(f"You have successfully changed your password: {new_password}")
        except ValueError as e:
            print(e)
        finally:
            self.main_menu()


    def create_account(self):
        try:
            first_name = self.valid_name("Enter your first name: ")
            last_name = self.valid_name("Enter your last name: ")
            password = self.valid_password("Enter your password: ")
            account = self.bank.create_account(first_name, last_name, password)
            self.loading_screen("Creating Account please wait")
            print(f"Account with account number: {account.get_account_number()} has been created")
            print()
        except ValueError as e:
            print(e)
        finally:
            self.main_menu()

    @staticmethod
    def valid_password(prompt):
        while True:
            user_input = input(prompt)
            if re.fullmatch(r'[A-Z][a-z\d]{8,}',user_input):
                return user_input
            else:
                print("Password must contain at least 8 alphabet,numbers and starts with a capital letter")


    @staticmethod
    def valid_name(prompt):
        while True:
            user_input = input(prompt).strip()
            if re.fullmatch(r'^[A-Z][a-z]+',user_input):
                return user_input

            else:
                print("Enter a valid input")


    @staticmethod
    def loading_screen(message):
        print(message, end='')
        for index in range(1, 6):
            print(">", end='')
            time.sleep(1)
        print()

if __name__ == "__main__":
    bank_menu = BankMenu()
    bank_menu.main()