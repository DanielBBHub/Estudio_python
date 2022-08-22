class Inventario:
    def __init__(self):
        self.observadores = []
        self._producto = None
        self._cantidad = 0

    def attach(self, observador):
        self.observadores.append(observador)

    @property
    def producto(self):
        return self._producto 

    @producto.setter
    def producto(self, valor):
        self._producto = valor
        self._update_observadores()

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor):
        self._cantidad = valor
        self._update_observadores()

    def _update_observadores(self):
        for observador in self.observadores:
            print("\nActualizando los observadores")
            observador()
