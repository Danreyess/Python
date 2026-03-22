class Experimento:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.finalizado = False
        self.resultados = []

    def agregar_resultado(self, numero):
        if self.finalizado == False:
            self.resultados.append(numero)

    def obtener_promedio(self):
        if not self.resultados:
            return 0
        
        suma_total = 0
        for res in self.resultados:
            suma_total += res #Vamos sumando cada numero uno por uno

        #Una vez que el ciclo For termina, hacemos la division final
        promedio = suma_total / len(self.resultados)
        return promedio


    def finalizar(self):
        self.finalizado = True


