class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id_prod = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Formato CSV para facilitar el guardado en texto
        return f"{self.id_prod},{self.nombre},{self.cantidad},{self.precio}"