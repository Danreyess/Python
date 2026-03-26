class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Fondos insuficientes o monto invalido")

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def __str__(self):
        return f"Cuenta bancaria: {self.__saldo}, Titular: {self.__titular}"


class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        self.__tasa_interes = 0.05

    def aplicar_interes(self):
        self.depositar(self.get_saldo() * self.__tasa_interes)


class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)
        self.__limite_sobregiro = -300

    def retirar(self, monto):
        saldo_actual = self.get_saldo()

        if saldo_actual - monto >= self.__limite_sobregiro:
            super().retirar(monto)
        else:
            print("Limite de sobregiro excedido")



# Simulando datos de una API
datos_api = [
    {"titular": "Juan Pérez", "saldo": 1000, "tipo": "corriente"},
    {"titular": "María López", "saldo": 5000, "tipo": "ahorros"},
]

# Factory function
def crear_cuenta(data):
    if data["tipo"] == "ahorros":
        return CuentaAhorros(data["titular"], data["saldo"])
    elif data["tipo"] == "corriente":
        return CuentaCorriente(data["titular"], data["saldo"])

# Crear objetos
cuentas = [crear_cuenta(data) for data in datos_api]

# Usar los objetos
for cuenta in cuentas:
    print(cuenta)
    cuenta.retirar(200)
    print(f"Saldo después de retiro: {cuenta.get_saldo()}")
    print("---")