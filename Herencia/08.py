class Videojuego:
    def __init__(self, nombre, vida, ataque):
        self.__nombre = nombre
        self.__vida = vida
        self.__ataque = ataque

    def recibir_damage(self, cantidad):
        self.__vida = max(0, self.__vida - cantidad)

    def esta_vivo(self):
        if self.__vida > 0:
            return True

    def __str__(self):
        return f"Nombre: {self.__nombre} Vida: {self.__vida}"

class Guerrero(Videojuego):
    def __init__(self, nombre, vida, ataque, armadura):
        super().__init__(nombre, vida, ataque)
        self.__armadura = armadura

    def recibir_damage(self, cantidad):
        damage_real = max(0, cantidad - self.__armadura)
        super().recibir_damage(damage_real)

class Mago(Videojuego):
    def __init__(self, nombre, vida, ataque, mana):
        super().__init__(nombre, vida, ataque)
        self.__mana = mana

    def lanzar_hechizos(self):
        new_damage = self.__ataque * 2
        self.__mana += -20




