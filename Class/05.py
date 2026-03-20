
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying")

    def increase_grade(self, points):
        self.grade += points

    def show_info(self):
        print(f"{self.name} grade {self.grade} ")

s1 = Student("Daniel", 5)
s1.study()
s1.increase_grade(10)
s1.show_info()


#Bank acount
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"You've been deposited ${amount}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"You've been withdrawn ${amount}")

    def show_balance(self):
        print(f"{self.owner} balance is ${self.balance}")

acc = BankAccount("Daniel", 1000)
acc.deposit(100)
acc.withdraw(200)
acc.show_balance()


