class Contacto:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @property
    def nombre_completo(self):
        return ("{} {} ".format(self.nombre, self.apellido) )