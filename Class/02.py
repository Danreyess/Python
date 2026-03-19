# class car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def drive(self):
#         print(f"The {self.color} {self.brand} car is driving.")
#
# my_car = car("Toyota", "Blue")
#
# my_car.drive()


# class Student:
#     def __init__(self, name, age, career):
#         self.name = name
#         self.age = age
#         self.career = career
#
#     def introduce(self):
#         print(f"Hi, I'm {self.name}, I am {self.age} years old and I study {self.career}.")
#
# student1 = Student("Daniel", 25, "Data Science")
# student2 = Student("Luis", 25, "Data Analitic")
# student1.introduce()
# student2.introduce()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def showBalance(self):
        print(self.balance)

account1 = BankAccount("Luis", 1500)
account1.deposit(100)
account1.showBalance()

