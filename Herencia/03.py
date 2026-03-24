class Bicicleta:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 #Atributo privado

    def ver_odometro(self):
        print(f"Odometro: {self.__kilometraje} km")

    def recorrer(self, kms):
        if kms > 0:
            self.__kilometraje += kms
        else:
            print("Los kilometros deben ser positivos")

class EBike(Bicicleta):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.nivel_bateria = 100

    def cargar(self):
        self.nivel_bateria = 100

    def recorrer(self, kms):
        super().recorrer(kms) #Usamos la logica del padre
        self.nivel_bateria -= kms

        if self.nivel_bateria < 0:
            self.nivel_bateria = 0


#Script principal
flota_data = [
    {"marca": "Canyon", "modelo": "Grizl"},
    {"marca": "Trek", "modelo": "Allant"},
    {"marca": "Specialized", "modelo": "Turbo Vado"}
]

flota = []

#Crear objetos a partir de diccionarios
for data in flota_data:
    bici = EBike(data["marca"], data["modelo"])
    flota.append(bici)

#Usar una bici
flota[0].recorrer(20)

#Mostrar estado
flota[0].ver_odometro()
print(f"Bateria: {flota[0].nivel_bateria}%")
