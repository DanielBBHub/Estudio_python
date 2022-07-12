class AuthExcepcions(Exception):
    #Requiere nombre de usuario y un objeto Usuario
    def __init__(self, nombre, usuario = None):
        super().__init__(nombre, usuario)
        self.nombre = nombre
        self.usuario = usuario


class NombreExistente(AuthExcepcions):
    pass


class ContrasenyaDemasiadoCorta(AuthExcepcions):
    pass

class NombreInvalido(AuthExcepcions):
    pass

class ContrasenyaInvalida(AuthExcepcions):
    pass

class ErrorDePermisos(Exception):
    pass

class SinLogear(AuthExcepcions):
    pass

class ErrorSinPermisos(AuthExcepcions):
    pass