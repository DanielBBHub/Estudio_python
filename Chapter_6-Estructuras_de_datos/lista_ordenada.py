from functools import total_ordering

@total_ordering
class ListaOrdenada:
    def __init__(self, string, num, num_ordenado):
        self.string = string
        self.num = num
        self.num_ordenado = num_ordenado

    def __lt__(self, objeto):
        if self.num_ordenado:
            return self.num < objeto.num
        return self.string < objeto.string

    def __repr__(self):
        return f"{self.string}:{self.num}"

    def __eq__(self, objeto):
        return all((
            self.string == objeto.string,
            self.num == objeto.num,
            self.num_ordenado == objeto.num_ordenado
        ))