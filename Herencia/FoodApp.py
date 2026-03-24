class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.estado = "pendiente"
        self.__total = 0
        self.productos = []

    def agregar_producto(self, nombre, precio):
        self.productos.append(f"nombre: {nombre}, precio: {precio}")
        self.__total += precio

    def ver_total(self):
        return self.__total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

class PedidoDelivery(Pedido):
    def __init__(self, cliente, direccion):
        super().__init__(cliente)
        self.direccion = direccion
        self.costo_envio = 5

    def ver_total(self):
        total = super().ver_total()
        return total + self.costo_envio

    def entregar(self):
        self.estado = "Entregado"


pedidos_data = [
    {"cliente": "Dani", "direccion": "Toronto"},
    {"cliente": "Ana", "direccion": "Mississauga"}
]

pedidos = []

for data in pedidos_data:
    pedido = PedidoDelivery(data["cliente"], data["direccion"])
    pedidos.append(pedido)

#Simulacion
pedidos[0].agregar_producto("Pizza",15)
pedidos[0].agregar_producto("Soda", 3)

print("Total: ", pedidos[0].ver_total())
pedidos[0].entregar()