class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        print("Aumentando la velocidad")

    def  display_info(self):
        print(f"Brand:{self.brand}, Speed:{self.speed}")

class Car(Vehicle):
    def __init__(self, brand, fuel):
        super().__init__(brand)
        self.fuel = fuel

    def refuel(self, amount):
        self.fuel += amount

class Motocycle(Vehicle):
    def __init__(self, brand, helmet):
        super().__init__(brand)
        self.helmet = helmet

    def display_info(self):
        print(f"Brand:{self.brand}, Speed: {self.speed}Helmet:{self.helmet}")