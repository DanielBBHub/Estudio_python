class ObjetosMenu:
    def __init__(self, menu_name, nombre_objeto):
        self.menu = menu_name
        self.objeto = nombre_objeto

    def click(self):
        self.command.execute()