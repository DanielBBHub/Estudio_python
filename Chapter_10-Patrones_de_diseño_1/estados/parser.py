from estados import primer_tag
class Parser:
    def __init__(self, string):
        self.string = string
        # Nodo con el que empieza el string
        self.raiz = None
        # Nodo actual en la ejecucion
        self.nodo_actual = None
        
        self.estado = primer_tag.PrimerTag()

    # Con la funcion procesar se pasara el resto del string al estado siguiente para que
    # se siga procesando  
    def procesar(self, resto_string):
        
        resto = self.estado.procesar(resto_string, self)
        if resto:
            self.procesar(resto)

    def start(self):
        self.procesar(self.string)