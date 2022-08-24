class CalculadoraEdad:
    def __init__(self, cumpleanyos):
        self.anyo, self.mes, self.dia = (int(x) for x in cumpleanyos.split("-"))
        

    def calcular_edad(self, fecha):
        anyo, mes, dia = (int(x) for x in fecha.split("-"))
        edad = anyo - self.anyo
        if (mes, dia) < (self.mes, self.dia):
            edad -= 1

        return edad