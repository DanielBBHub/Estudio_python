class IteradorInicial:
    def __init__(self, string):
        self.palabras = [w.capitalize() for w in string.string.split()]
        # Declaramos la variable que nos ayudara a llevar la cuenta de cuantos
        # elementos hemos revisado del objeto iterable 
        self.indice = 0

    # Mediante la llamada a next(iterador) llamamos al siguiente metodo para
    # que el objeto siga iterando al iterable  
    def __next__(self):
        if self.indice == len(self.palabras):
            raise StopIteration()

        palabra = self.palabras[self.indice]
        self.indice += 1
        return palabra

    def __iter__(self):
        return self