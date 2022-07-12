# Creamos una clase EvenOnly para añadir dos condiciones a la clase lista
class EvenOnly(list):

    def append(self, entero):
        # Si no es un entero levantara una excepcion "TypeError"
        if not isinstance(entero, int):
            raise TypeError("Solo pueden añadirse enteros")
        # Si no es un entero par levantara la excepcion "ValueError"
        if not entero % 2:
            raise ValueError("Solo pueden introducirse pares")

        super().append(entero)