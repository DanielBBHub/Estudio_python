import datetime
import time

# Esta clase es meramente un contenedor para el evento. Esta pensada para que no sea accedida, si no creada desde la clase Cronometro
class EventoTimeado:
    def __init__(self, tiempo_final, cb):
        self.tiempo_final = tiempo_final
        self.callback = cb
    
    def listo(self):
        return self.tiempo_final <= datetime.datetime.now()


class Cronometro:
    def __init__(self):
        self.eventos = []

    # Esta funcion crea un tiempo que tiene que esperarse para ejecutar una funcion, en base al argumento 
    # "retraso", y crea un evento pasandole la variable tiempo_final y un callback que tambien ha recibido
    # como argumento de entrada 
    def llamar_despues(self, retraso, cb):
        # La funcion timedelta() de Python se usa generalmente para calcular diferencias en fechas. Tambien se puede 
        # usar para manipular fechas. Es una de las formas mas faciles. Tiene la siguiente sintaxis:
        # datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)  
        tiempo_final = datetime.datetime.now() + datetime.timedelta(
            seconds=retraso
        )
        # El callback que se introduzca debera tener un argumento de entrada
        self.eventos.append(EventoTimeado(tiempo_final, cb))


    def correr(self):
        while True:
            eventos_listos = (evento for evento in self.eventos if evento.listo())
            for evento in eventos_listos:
                evento.callback(self)
                self.eventos.remove(evento)

            time.sleep(0.5)


