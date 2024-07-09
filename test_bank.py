import unittest
from bank import Bank


class bankTest(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Hello", 1)

    def test_setup(self):
        self.assertEqual(self.bank.get_name(), "Hello")
        self.assertEqual(self.bank.get_number(), 1)
        self.assertEqual(self.bank.get_balance(), 0)

    def test_withdraw(self):
        # bank = Bank("Hello", 1)
        self.bank.deposit(1000)
        self.assertEqual(self.bank.withdraw(500), 500)
        self.assertNotEqual(self.bank.withdraw(100), 500)
        self.assertEqual(self.bank.withdraw(1000), "Unavailable Funds")
        self.assertEqual(self.bank.withdraw(-100), "Unable to remove negative amounts")

    def test_deposit(self):
        # bank = Bank("Hello", 1)
        self.bank.deposit(1000)
        self.assertEqual(self.bank.deposit(500), 1500)
        self.assertEqual(self.bank.deposit(-100), "Unable to add negative values")

    def test_currentBalance(self):
        # bank = Bank("Hello", 1)
        self.bank.deposit(1000)
        print(self.bank.get_balance())
        self.assertEqual(self.bank.get_balance(), 1000)


if __name__ == "__main__":
    unittest.main()
