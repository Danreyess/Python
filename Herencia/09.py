class Deportista:
    def __init__(self, nombre, edad, energia):
        self.__nombre = nombre
        self.__edad = edad
        self.__energia = energia

    #Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_energia(self):
        return self.__energia

    # Setter
    def set_energia(self, valor):
        self.__energia = max(0, valor)

    def entrenar(self, horas):
        if self.__energia > 0:
            total = horas * 10
            self.__energia -= total

    def descansar(self, horas):
        self.__energia  = min(self.__energia + horas * 15, 100)

    def esta_lista(self):
        if self.__energia > 30:
            return True

    def __str__(self):
        return f"{self.__nombre} - {self.__edad} - {self.__energia}"

class Futbolista(Deportista):
    def __init__(self, nombre, edad, energia, goles):
        super().__init__(nombre, edad, energia)
        self.__goles = goles

    def marcar_gol(self):
        self.__goles += 1
        self.set_energia(self.get_energia() - 20)

    def __str__(self):
        return f" {self.get_nombre()} - {self.get_edad()} - {self.get_energia()} - {self.__goles}"

class Nadador(Deportista):
    def __init__(self, nombre, edad, energia, metros_nadados):
        super().__init__(nombre,edad,energia)
        self.__metros_nadados = metros_nadados

    def nadar(self, metros):
        if self.__energia > 0:
            self.__metros_nadados += metros
            self.__energia -= 1 * (metros)

    def __str__(self):
        return f"{self.__nombre} - {self.__edad} - {self.__energia} - {self.__metros_nadados}"



datos_api = [
    {"nombre": "Carlos", "edad": 25, "energia": 100, "tipo": "futbolista", "goles": 0},
    {"nombre": "Ana", "edad": 22, "energia": 100, "tipo": "nadador", "metros": 0}
]