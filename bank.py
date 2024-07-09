class Bank:
    def __init__(self, name, number):
        self.balance = 0
        self.name = name
        self.number = number

    def withdraw(self, amount):
        if amount < 0:
            return "Unable to remove negative amounts"
        if amount > self.balance:
            return "Unavailable Funds"
        self.balance = self.balance - amount
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            return "Unable to add negative values"
        self.balance = self.balance + amount
        return self.balance

    def get_balance(self):
        return self.balance
