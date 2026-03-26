class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Salario: {self.salario}")

    def calcular_bono(self):
        return self.salario  * 0.10

class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def calcular_bono(self):
        return self.salario * 0.20

class Manager(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)
        self.equipo = []

    def agregar_miembro(self, nombre):
        self.equipo.append(nombre)

    def calcular_bono(self):
        return self.salario * 0.30


empleados_data = [
    {"nombre": "Dani", "salario": 3000, "tipo": "dev", "lenguaje": "Python"},
    {"nombre": "Ana", "salario": 4000, "tipo": "manager"}
]

empleados = []

for data in empleados_data:
    if data["tipo"] == "dev":
        emp = Desarrollador(data["nombre"], data["salario"], data["lenguaje"])
    else:
        emp = Manager(data["nombre"], data["salario"])

    empleados.append(emp)

for emp in empleados:
    emp.mostrar_info()

    bono = emp.calcular_bono()
    print(f"Bono: {bono}")

    if isinstance(emp, Manager):
        emp.agregar_miembro("Carlos")
        emp.agregar_miembro("Ana")
        print(f"Equipo actualizado: {emp.equipo}")
