class Nodo:
    def __init__(self, tag, padre=None):
        self.padre = padre
        self.tag = tag
        self.hijos = []
        self.texto = ""

    def __str__(self):
        if self.texto:
            return self.tag + ": " + self.texto
        else:
            return self.tag