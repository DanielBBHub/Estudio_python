from threading import Timer
import datetime
from urllib.request import Request, urlopen


class EnlaceRefrescado:
    """ Clase con la que podemos refrescar una pagina web cada 3600 segundos
    para comprobar si todavia sigue operativa """

    def __init__(self, url):
        self.url = url
        self.contenido = ''
        self.ultima_act = None
        self.peticion = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        self.update()

    def update(self):
        self.contenido = urlopen(self.peticion).read()
        self.ultima_act = datetime.datetime.now()
        print(str(self.ultima_act))
        self.horario()

    def horario(self):
        self.cronometro = Timer(3600, self.update)
        self.cronometro.setDaemon(True)
        self.cronometro.start()

    # Si probamos a "picklear" una instancia de este objeto sin la definicion de este metodo como esta
    # nos dara un error, ya que tenemos el atributo cronometro (instancia de Timer), el cual no es serializable.
    # La libreria pickle llama a __dict__() para guardar el mappeo de los valores y asi serializar el objeto, pero
    # antes llama al metodo __getstate__(), el cual hemos modificado para eliminar la instancia del Timer  
    def __getstate__(self):
        nuevo_estado = self.__dict__.copy()
        if 'cronometro' in nuevo_estado:
            del nuevo_estado['cronometro']
        return nuevo_estado 

    # Definimos el siguiente metodo por que, en el caso de serializar el objeto, se eliminaria la instancia del Timer,
    # con lo que con la siguiente definicion lo reinstanciariamos 
    def __setstate__(self, info):
        self.__dict__ = info 
        self.horario()