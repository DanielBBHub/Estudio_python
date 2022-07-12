from ejemplo_tarea.excepciones import *

class Autorizador:
    def __init__(self, auth):
        self.auth = auth
        self.permisos = {}

    def anyadir_permisos(self, nombre_permiso):
        # Comprobamos si existe el permiso
        try:
            set_permisos = self.permisos[nombre_permiso]
        # Si no se encuentra la key en el diccionario se crea
        except KeyError:
            self.permisos[nombre_permiso] = set()
        # Si existe el permiso se suelta la excepcion 
        else:
            raise ErrorDePermisos("Los permisos ya existen")

    def permitir_usuario(self, nombre_permiso, nombre_usuario):
        # Comprobamos que exista el permiso
        try:
            set_permisos = self.permisos[nombre_permiso]
        # Si no se encuentra la key lanzamos la excepcion
        except KeyError:
            raise ErrorDePermisos("El permiso no existe")
        else:
            # Si existe comprobamos que el nombre de usuario exista dentro del diccionario de usuarios
            if nombre_usuario not in self.auth.usuarios:
                # Si no se encuentra al usuario se lanza la excepcion
                raise NombreInvalido(nombre_usuario)
            # En caso contrario se añade el usuario al diccionario de permisos de permisos
            set_permisos.add(nombre_usuario)

    def comprobar_permisos(self, nombre_permiso, nombre):
        # Comprobamos que el usuario este logeado, en caso negativo se lanza la excepcion
        if not self.auth.usuario_logeado(nombre):
            raise SinLogear(nombre)
        
        # Comprobamos si el usuario tiene permisos
        try:
            set_permisos = self.permisos[nombre_permiso]

        # Si no se encuentra la key lanzamos la excepcion
        except KeyError:
            raise ErrorDePermisos("No existe el permiso")
        
        # Si tiene permisos
        else:
            if nombre not in set_permisos:
                raise ErrorSinPermisos(nombre)
            else:
                return True


