class Atleta:
    def __init__(self, nombre, id_fiscal):
        self.nombre = nombre
        self.__id_fiscal = id_fiscal

    def obtener_nombre(self):
        return self.nombre

class CorredorGravel(Atleta):
    def __init__(self, nombre, id_fiscal, datos_bici):
        super().__init__(nombre, id_fiscal)
        self.bicicleta = datos_bici
        self.tiempos = []

    def registrar_lap(self, segundos):
        self.tiempos.append(segundos)

    def promedio_velocidad(self):
        if not self.tiempos:
            return 0
        total = sum(self.tiempos)
        return total / len(self.tiempos)

# 1. Creamos el diccionario de la bici
bici_luis = {"marca": "Canyon", "modelo": "Grizl CF SL 7"}

# 2. Creamos al corredor
corredor = CorredorGravel("Luis Daniel", "ID-MEX-99", bici_luis)

# 3. Registramos tiempos (Laps en el Don Valley)
corredor.registrar_lap(300)
corredor.registrar_lap(320)

# 4. RESULTADOS
print(f"Atleta: {corredor.obtener_nombre()}")
print(f"Bicicleta: {corredor.bicicleta['modelo']}")
print(f"Promedio de tiempo: {corredor.promedio_velocidad()} segundos")

# 5. EL TEST DE ENCAPSULAMIENTO (Esto debe fallar)
try:
    print(corredor.__id_fiscal)
except AttributeError:
    print("¡Éxito! El ID Fiscal está protegido y no es accesible desde fuera.")