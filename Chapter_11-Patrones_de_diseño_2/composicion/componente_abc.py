class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mover(self, nuevo_path):
        nuevo_directorio = get_path(nuevo_path)
        del self.padre.hijo[self.nombre]
        nuevo_directorio.hijo[self.nombre] = self
        self.padre = nuevo_directorio

    def borrar(self):
        del self.padre.hijo[self.nombre]


class Directorio(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = {}

    def añadir_hijo(self, hijo):
        hijo.parent = self
        self.hijos[hijo.nombre] = hijo

    def copiar(self, nuevo_path):
        pass

class Archivo(Componente):
    def __init__(self, nombre, contenidos):
        super().__init__(nombre)
        self.contenidos = contenidos

    def copiar(self, nuevo_path):
        pass



raiz = Directorio("")
def get_path(path):
    nombres = path.split("/")[1:]
    nodo = raiz
    for nombre in nombres:
        nodo = nodo.hijos[nombre]
    
    return nodo