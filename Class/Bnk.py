#Creating a bank acount system
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Money deposited")

    def withdraw(self, amount):
        self.balance -= amount
        print("Money withdrawn")

    def display_balance(self):
        print(f"Money balance {self.balance}")

account = BankAccount("Daniel")


