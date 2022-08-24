class Documento:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.contenidos = "This file cannot be modified"

    def save(self):
        with open(self.filename, "w") as archivo:
            archivo.write(self.contents)