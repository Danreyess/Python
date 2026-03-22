class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    def calculate_bonus(self):
        bonus = self.salary * 0.1
        return bonus

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        bonus = self.salary * 0.2
        return bonus

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        bonus = self.salary * 0.3
        return bonus
    def get_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Team: {self.team_size}")