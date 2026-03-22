#Encapsulacion/Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

#Herencia/Inheritance
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Miauu")

#Polimorfismo/Polymorphism

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

#Abstraccion/Abstraction
#Mostrar solo lo importante, ocultar lo complejo
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass