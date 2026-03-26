class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.__prestado = False

    def ver_info(self):
        print(f"Titulo: {self.titulo}, autor: {self.autor}")



