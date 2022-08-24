class FormateadorFechaUSA:
    def formatear_fecha(self, anyo, mes, dia):
        a, m, d = (str(x) for x in (anyo, mes, dia))
        a = "20" + a if len(a) == 2 else a
        m = "0" + m if len(m) == 1 else m
        d = "0" + d if len(d) == 1 else d
        return "{0}-{1}-{2}".format(m, d, a)


class FormatoadorFechaFrancia:
    def formatear_fecha(self, anyo, mes, dia):
        a, m, d = (str(x) for x in (anyo, mes, dia))
        a = "20" + a if len(a) == 2 else a
        m = "0" + m if len(m) == 1 else m
        d = "0" + d if len(d) == 1 else d
        return "{0}/{1}/{2}".format(d, m, a)