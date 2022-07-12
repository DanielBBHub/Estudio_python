import abc

class OddContainer:
    def __contains__(self, x):
        # The isinstance() function returns True if the specified object is of the specified type, otherwise False.
        # If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
        if not isinstance(x, int) or not x % 2:
            return False

        return True


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def play(self):
        pass

    @abc.abstractproperty
    def ext(self):
        pass

#[------------------------------COPY-PASTE--------------------------------------------]
    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented
#[------------------------------COPY-PASTE--------------------------------------------]

#Definimos una clase abstracta para el ejercicio en concreto
class Tarea(metaclass=abc.ABCMeta):
    #Definimos dos metodos abstractos para esta clase: 
    # El primero el de 'leccion' para obtener el nombre del usuario
    @abc.abstractclassmethod
    def leccion(self, student):
        pass

    # El segundo para hacer la comprobación del ejercicio
    @abc.abstractclassmethod
    def comprobar_codigo(self, code):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Tarea:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented