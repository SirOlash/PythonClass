import unittest
from bankapp.account import Account

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account = Account("John","Doe","CorrectPin",10001)

    def test_that_account_balance_is_zero_by_default(self):
        self.assertEqual(0,self.account.get_balance("CorrectPin"))

    def test_that_account_balance_can_be_increased(self):
        self.account.increase_balance(1000)
        self.assertEqual(1000,self.account.get_balance("CorrectPin"))

    def test_that_account_balance_cannot_be_increased_with_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.increase_balance(-1000)
        self.assertEqual(0,self.account.get_balance("CorrectPin"))


    def test_that_account_balance_can_be_decreased(self):
        self.account.increase_balance(1000)
        self.account.decrease_balance(500,"CorrectPin")
        self.assertEqual(500,self.account.get_balance("CorrectPin"))

    def test_that_you_cant_remove_more_than_your_balance(self):
        self.account.increase_balance(1000)
        with self.assertRaises(ValueError):
            self.account.decrease_balance(1500,"CorrectPin")
        self.assertEqual(1000,self.account.get_balance("CorrectPin"))

    def test_that_you_can_update_pin(self):
        self.account.increase_balance(1000)
        self.account.decrease_balance(500,"CorrectPin")
        self.account.update_pin("CorrectPin","NewPin")
        self.account.decrease_balance(200,"NewPin")
        self.assertEqual(300,self.account.get_balance("NewPin"))



if __name__ == '__main__':
    unittest.main()
