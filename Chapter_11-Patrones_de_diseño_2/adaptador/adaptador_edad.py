import datetime
from adaptador import calculadora_edad as calc
class AdaptadorFecha:
    def _str_fecha(self, fecha):
        return fecha.strftime("%Y-%m-%d")

    def __init__(self, cumpleanyos):
        cumpleanyos = self._str_fecha(cumpleanyos)
        self.calculadora = calc.CalculadoraEdad(cumpleanyos)

    def get_edad(self, fecha):
        fecha = self._str_fecha(fecha)
        return self.calculadora.calcular_edad(fecha)