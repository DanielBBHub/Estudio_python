from ejemplo_tarea.excepciones import *
from ejemplo_tarea.usuario import Usuario
class Autentificador:
    def __init__(self):
        self.usuarios = {}


    def añadir_usuario(self, nombre, contrasenya):
        # Comprobamos que el nombre de usuario este dentro del diccionario
        if nombre in self.usuarios:
            raise NombreExistente(nombre)

        # Comprobamos que la contrasenya tenga un minimo de caracteres
        if len(contrasenya) < 6:
            raise ContrasenyaDemasiadoCorta(nombre)
        
        # Añadimos el usuario
        self.usuarios[nombre] = Usuario(nombre, contrasenya)

    def login(self, nombre, contrasenya):

        # Comprobamos que existe el usuario
        try:
            usuario = self.usuarios[nombre]
        except KeyError:
            raise NombreInvalido(nombre)
        
        # Comprobamos que existe la contrasenya
        if not usuario.comprobar_contra(contrasenya):
            raise ContrasenyaInvalida(nombre, usuario)

        usuario.logeado = True
        return True

    def usuario_logeado(self, nombre):
        if nombre in self.usuarios:
            return self.usuarios[nombre].logeado
        
        return False

    def logof(self, nombre):
        if nombre in self.usuarios and self.usuarios[nombre].logeado == True:
            usuario = self.usuarios[nombre]
            usuario.logeado = False
            return True

        return False
