class UnUnico:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        # Cuando se llama a __new__() (UnUnico()), se comprueba si la variable _singleton tiene
        # asignado ya un valor, en caso negativo se crea una instancia, se le asigna y se devuelve,
        # por otro lado, si si existe unicamente se devuelve  
        if not cls._singleton:
            cls._singleton = super(UnUnico, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

