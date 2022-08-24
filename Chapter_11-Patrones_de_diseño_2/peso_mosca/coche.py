class Coche:
    def __init__(self, modelo, color, num_serie):
        self.modelo = modelo
        self.color = color
        self.serie = num_serie

    def get_num_serie(self):
        return self.modelo.comprobar_num_serie(self.serial)