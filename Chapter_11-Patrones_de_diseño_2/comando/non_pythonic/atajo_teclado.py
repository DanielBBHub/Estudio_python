class AtajoTeclado:
    def __init__(self, llave, modificador):
        self.llave = llave
        self.modificador = modificador

    def keypress(self):
        self.command.execute()