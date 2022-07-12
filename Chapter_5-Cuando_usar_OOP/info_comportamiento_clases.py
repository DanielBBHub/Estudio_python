cuadrado = [(5,2),(5,9),(6,8),(9,5)]

import math
def distancia(p1, p2):
    return math.sqrt(abs((p1[0] - p2[0])**2 - (p1[1] - p2[1])**2))


def perimetro(poligono):
    perimetro = 0
    puntos = poligono + [poligono[0]]
    for i in range(len(poligono)):
        perimetro += distancia(puntos[i], puntos[i+1])
    return perimetro


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self, p2):
        return math.sqrt(abs((self.x - p2.x)**2 - (self.y - p2.y)**2))


class Poligono:
    def __init__(self):
        self.vertices = []

    def __init__(self, puntos=None):
        puntos = puntos if puntos else []
        self.vertices = []
        for punto in puntos:
            if isinstance(puntos, tuple):
                punto = Punto(*punto)


    def anyadir_vertice(self, punto):
        self.vertices.append(punto)

    def calcular_perimetro(self):
        perimetro = 0
        puntos = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimetro += puntos[i].calcular_distancia(puntos[i+1])
        return perimetro

class PoligonoV2(Poligono):
    # Constructor que acepta una lista de tuplas como argumento
    def __init__(self, puntos=None):
        # Si hay una lista la guarda, si no inicializa una vacia
        puntos = puntos if puntos else []
        self.vertices = []
        # Se recorre la lista
        for punto in puntos:
            # Si es una instancia de tupla se convierte a objeto Punto y 
            # se agrega a la lista de vertices
            if isinstance(puntos, tuple):
                punto = Punto(*punto)
                self.vertices.append(punto)

    def anyadir_vertice(self, punto):
        self.vertices.append(punto)

    def calcular_perimetro(self):
        perimetro = 0
        puntos = self.vertices + [self.vertices[0]]
        for i in range(len(self.vertices)):
            perimetro += puntos[i].calcular_distancia(puntos[i+1])
        return perimetro