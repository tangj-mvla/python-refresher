import unittest
from bank import Bank


class bankTest(unittest.TestCase):
    def test_withdraw(self):
        bank = Bank("Hello", 1)
        bank.deposit(1000)
        self.assertEqual(bank.withdraw(500), 500)
        self.assertEqual(bank.withdraw(1000), "Unavailable Funds")
        self.assertEqual(bank.withdraw(-100), "Unable to remove negative amounts")

    def test_deposit(self):
        bank = Bank("Hello", 1)
        bank.deposit(1000)
        self.assertEqual(bank.deposit(500), 1500)
        self.assertEqual(bank.deposit(-100), "Unable to add negative values")

    def test_currentBalance(self):
        bank = Bank("Hello", 1)
        bank.deposit(1000)
        print(bank.get_balance())
        self.assertEqual(bank.get_balance(), 1000)


if __name__ == "__main__":
    unittest.main()
