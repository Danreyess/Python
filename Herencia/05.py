import random

class Sensor:
    def __init__(self,id_sensor, ubicacion):
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion

    def leer_datos(self):
        n1 = random.uniform(0,100)
        return n1

class SensorPro(Sensor):
    def __init__(self,id_sensor, ubicacion, umbral_alerta):
        super().__init__(id_sensor, ubicacion)
        self.umbral_alerta = umbral_alerta

    def leer_datos(self):
        valor = super().leer_datos()
        if valor > self.umbral_alerta:
            print(f"Alerta en {self.ubicacion}")
            return valor

