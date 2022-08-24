from statistics import mode
import weakref

class ModeloCoche:
    _modelos = weakref.WeakValueDictionary()

    def __new__(cls, nombre_modelo, *args, **kwargs):
        modelo = cls._modelos.get(nombre_modelo)
        if not modelo:
            modelo = super().__new__(cls)
            cls._modelos[nombre_modelo] = modelo
        
        return modelo

    def __init__(self,
                nombre_modelo,
                ac = False,
                control_cruzero = False,
                llantas_aleacion = False,
                cargador_usb = False):
            
        if not hasattr(self, "iniciado"):
            self.nombre_modelo = nombre_modelo
            self.ac = ac
            self.control_cruzero = control_cruzero
            self.llantas_aleacion = llantas_aleacion
            self.usb = cargador_usb
            self.iniciado = True

    def comprobar_num_serie(self, num_serie):
        print("Perdona, pero en estos momentos no podemos comprobar "
             "el numero de serie {0} de {1} ".format(num_serie, self.nombre_modelo))

    