class ExcepcionConPropiedades(Exception):
    
    def __init__(self, balance, cantidad_total):
        super().__init__(f"La cuenta no dispone de los fondos suficientes")
        self.balance = balance
        self.cantidad = cantidad_total

    def deuda(self):
        return self.cantidad - self.balance