class ObservadorConsola:
    def __init__(self, inventario):
        self.inventario = inventario

    def __call__(self):
        print(self.inventario.producto)
        print(self.inventario.cantidad)