import unittest

from bankapp.bank import Bank


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_that_you_can_create_account(self):
        self.bank.create_account("John","Doe","correctpin")
        self.assertEqual(1,self.bank.get_size())
        self.bank.create_account("Jo","Do","correctpin")
        self.assertEqual(2,self.bank.get_size())

    def test_that_you_can_find_account_by_account_number(self):
        self.bank.create_account("John","Doe","correctpin")
        account = self.bank.find_account_by(10001)
        self.assertIsNotNone(account)
        self.assertEqual("John",account.get_first_name())

    def  test_that_you_can_deposit_money(self):
        self.bank.create_account("John","Doe","correctpin")
        self.bank.deposit(10001,1000)
        self.assertEqual(1000,self.bank.check_balance(10001,"correctpin"))

    def test_that_if_you_deposit_1000_withdraw_500_balance_is_500(self):
        self.bank.create_account("John","Doe","correctpin")
        self.bank.deposit(10001,1000)
        self.bank.withdraw(10001,500,"correctpin")
        self.assertEqual(500,self.bank.check_balance(10001,"correctpin"))

    def test_that_you_can_transfer_from_one_account_to_another_account(self):
        self.bank.create_account("John","Doe","correctpin")
        self.bank.create_account("James","york","correctpin")
        self.bank.deposit(10001,1000)
        self.bank.transfer(10001,10002,"correctpin",500)
        self.assertEqual(500,self.bank.check_balance(10001,"correctpin"))
        self.assertEqual(500,self.bank.check_balance(10002,"correctpin"))

    def test_that_you_can_update_pin(self):
        self.bank.create_account("John","Doe","correctpin")
        self.bank.deposit(10001,1000)
        self.bank.withdraw(10001,200,"correctpin")
        self.bank.updatepin(10001,"correctpin","newpin")
        self.bank.withdraw(10001,300,"newpin")


if __name__ == '__main__':
    unittest.main()
