from bankapp.account import Account


class Bank:
    def __init__(self):
        self.accounts = []
        self.__account_number = 10001

    def create_account(self,first_name,last_name,pin):
        if not first_name or first_name.isspace():
            raise ValueError("First name cannot be empty")
        if not last_name or last_name.isspace():
            raise ValueError("Last name cannot be empty")
        if not pin or pin.isspace():
            raise ValueError("Pin cannot be empty")
        self.accounts.append(Account(first_name,last_name,pin,self.__account_number))
        self.__account_number += 1

    def get_size(self):
        return len(self.accounts)

    def get_account_number(self):
        return self.__account_number

    def deposit(self, account_number, amount):
        account = self.find_account_by(account_number)
        account.increase_balance(amount)

    def check_balance(self, account_number, pin):
        account = self.find_account_by(account_number)
        return account.get_balance(pin)


    def find_account_by(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        raise ValueError("Account not found")

    def withdraw(self, account_number,amount,pin):
        account = self.find_account_by(account_number)
        account.decrease_balance(amount,pin)

    def transfer (self,sender_account_number,recipient_account_number,pin,amount):
        account1 = self.find_account_by(sender_account_number)
        account2 = self.find_account_by(recipient_account_number)
        account1.decrease_balance(amount,pin)
        account2.increase_balance(amount)

    def update_pin(self, account_number, old_pin, new_pin):
        account = self.find_account_by(account_number)
        account.update_pin(old_pin, new_pin)








