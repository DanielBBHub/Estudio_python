class IterableInicial:
    def __init__(self, string):
        self.string = string

    # Definimos un objeto iterable mediante este metodo __iter__(), devolviendo
    # mediante el yield, una instancia de el mismo 
    def __iter__(self):
        yield IterableInicial(self.string)
    