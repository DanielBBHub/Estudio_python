class BarraHerramientas:
    def __init__(self, nombre, icono):
        self.nombre = nombre
        self.icono = icono

    def click(self):
        self.command.execute()