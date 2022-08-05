class FiltroGuiones:
    def __init__(self, secuencia):
        self.secuencia = secuencia

    def __iter__(self):
        return self

    def __next__(self):
        linea = self.secuencia.readline()
        while linea and '-' not in linea:
            linea = self.secuencia.readline()
        if not linea:
            raise StopIteration
        return linea.replace("-", "@")