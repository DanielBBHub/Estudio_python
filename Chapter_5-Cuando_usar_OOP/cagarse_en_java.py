class Color:
    def __init__(self, rgb, nombre):
        self.color = rgb
        self._nombre = nombre

    def _set_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise Exception("Nombre invalido")
        self._nombre = nuevo_nombre
    
    def _get_nombre(self):
        return self._nombre

    def _del_nombre(self):
        del self._nombre

    name = property(_get_nombre, _set_nombre, _del_nombre, "Esto es el nombre del color de la clase")