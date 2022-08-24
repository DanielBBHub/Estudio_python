class FormateadorDivisaFrancia:
    def formatear_divisa(self, base, cent):
        base, cent = (str(x) for x in (base, cent))
        if len(cent) == 0:
            cent = "00"
        
        elif len(cent) == 1:
            cent = "0" + cent

        elif len(cent) == 2:
            cent = cent

        digitos = []

        for index, valor in enumerate(reversed(base)):
            if index and not index % 3:
                digitos.append(" ")
            
            digitos.append(valor)
            base = "".join(reversed(digitos))
        return "{0}€ {1}cent.".format(base, cent)

class FormateadorDivisaUsa:
     def formatear_divisa(self, base, cent):
        base, cent = (str(x) for x in (base, cent))
        if len(cent) == 0:
            cent = "00"
        
        elif len(cent) == 1:
            cent = "0" + cent

        elif len(cent) == 2:
            cent = cent

        digitos = []

        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digitos.append(",")
            
            digitos.append(c)
            base = "".join(reversed(digitos))
        return "${0}.{1}".format(base, cent)