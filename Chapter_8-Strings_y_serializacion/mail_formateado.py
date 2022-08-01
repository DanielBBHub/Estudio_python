class EMail:
    def __init__(self, dir_desde, dir_para, sujeto, mensaje):
        self.dir_desde = dir_desde
        self.dir_para = dir_para
        self.sujeto = sujeto
        self._mensaje = mensaje

    def mensaje(self):
        return self._mensaje