class Caracter:
    def __init__(self, caracter, negrita=False, cursiva=False, subrayado=False):
        assert len(caracter) == 1
        self.caracter = caracter
        self.negrita = negrita
        self.cursiva = cursiva
        self.subrayado = subrayado

    # Metodo de manipulacion de strings. Normalmente saca el nombre de la clase 
    # y la direccion de memoria. Lo hemos sustituido por este metodo 
    # que añade un caracter especial delante de cada caracter si la propiedad es True
    def __str__(self):
        negrita = "*" if self.negrita else ''
        cursiva = "/" if self.cursiva else ''
        subrayado = "_" if self.subrayado else ''
        return negrita + cursiva + subrayado + self.caracter