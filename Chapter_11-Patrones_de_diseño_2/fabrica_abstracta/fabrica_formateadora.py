from .formateadores import formateador_divisa, formateador_fecha

class FabricaFormateadoresUSA:
    def crear_formateador_fecha(self):
        return formateador_fecha.FormateadorFechaUSA()

    def crear_formateador_divisa(self):
        return formateador_divisa.FormateadorDivisaUsa()



class FabricaFormateadoresFrancia:
    def crear_formateador_fecha(self):
        return formateador_fecha.FormatoadorFechaFrancia()

    def crear_formateador_divisa(self):
        return formateador_divisa.FormateadorDivisaFrancia()



mapeo_fabrica = {"US": FabricaFormateadoresUSA, "FR": FabricaFormateadoresFrancia}
