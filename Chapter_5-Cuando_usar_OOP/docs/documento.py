from docs.cursor import Cursor
from docs.caracter import Caracter
class Documento:
    def __init__(self):
        self.caracteres = []
        self.cursor = Cursor(self)
        self.nombre_archivo = ""

    def insert(self, caracter):
        if not hasattr(caracter, 'caracter'):
            caracter = Caracter(caracter)
        self.caracteres.insert(self.cursor.pos, caracter)
        self.cursor.pos += 1

    def delete(self):
        del self.caracteres[self.cursor.pos]

    def save(self):
        with open(self.nombre_archivo, "w") as archivo:

            archivo.write(''.join(map(str,self.caracteres)))

    @property
    def string(self):
        return "".join(str(caracter) for caracter in self.caracteres)