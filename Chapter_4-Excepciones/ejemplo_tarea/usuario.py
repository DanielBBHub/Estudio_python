import hashlib

class Usuario:
    def __init__(self, nombre, contrasenya):
        """Se deberia cifrar la contraseña antes de introducirla en 
        el objeto usuario"""
        self.nombre = nombre
        self.contra = self._encrypt_pw(contrasenya)
        self.logeado = False


    def _encrypt_pw(self, contrasenya):
        """Encriptar la contraseña con el nombre de usario y devolver el sha"""
        hash_string = self.nombre + contrasenya
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()


    def comprobar_contra(self, contrasenya):
        """Devolver True si la contraseña es valida para este usuario"""
        encriptado = self._encrypt_pw(contrasenya)
        return encriptado == self.contra