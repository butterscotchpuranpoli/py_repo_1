# Bank Account (Inheritance)

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Inheriting from the Account class to create a SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.deposit(interest)

# Creating instances of Account and SavingsAccount
my_account = Account(account_number="A12345", balance=1000)
my_savings = SavingsAccount(account_number="S67890", balance=2000, interest_rate=5)

# Performing transactions
my_account.deposit(500)
my_account.withdraw(200)

my_savings.add_interest()
print("Savings Balance (after interest):", my_savings.balance)
