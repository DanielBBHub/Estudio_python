from collections import defaultdict
from contextlib import suppress
import smtplib
from email.mime.text import MIMEText

class ListaCorreos:
    """ Manejador de grupos de direcciones de 
    correo para enviar correos electronicos """

    def __init__(self, archivo_info):
        self.mapeo_correos = defaultdict(set)
        self.archivo_info = archivo_info

    # Se sobreescribe la funcion __enter__() para que el desarrollador no tenga que 
    # cargar manualmente
    def __enter__(self):
        self.cargar_informacion()
        return self

    # Se sobreescribe la funcion __exit__() para que el desarrollador no tenga que 
    # guardar manualmente
    def __exit__(self, type, value, tb):
        self.guardar_informacion()

    def anyadir_a_grupo(self, correo, grupo):
        self.mapeo_correos[correo].add(grupo)

    def direcciones_en_grupo(self, *grupos):
        grupos = set(grupos)
        direcciones = set()

        for dirs, grupo in self.mapeo_correos.items():
            # La sintaxis de grupo & grupos es una sustitucion de la funcion
            # de set() intersection(). Esto equivaldria a grupo.intersect(grupos) 
            if grupo & grupos:
                direcciones.add(dirs)

        return direcciones
    
    def enviar_correo(self, sujeto, mensaje, direccion_desde, *direccion_hacia, host='localhost', port=1025, cabeceras = None):
        # MIMEText nos proporcionara un objeto-diccionario con el que podremos contener un mensaje
        # y el resto de parametros que necesiatmos para un correo 
        correo = MIMEText(mensaje)
        correo["Subject"] = sujeto
        correo["From"] = direccion_desde

        cabeceras = cabeceras if cabeceras else {}

        enviador = smtplib.SMTP(host, port)

        for direccion in direccion_hacia:
            del correo["To"]
            correo["To"] = direccion
            enviador.sendmail(direccion_desde, direccion_hacia, correo.as_string())
        
        enviador.quit()

    def enviar_correos_a_todos(self, sujeto, mensaje, direccion_desde, *grupos, cabeceras = None):
        direcciones_hacia = self.direcciones_en_grupo(*grupos)
        self.enviar_correo(sujeto, mensaje, direccion_desde, *direcciones_hacia, cabeceras=cabeceras)

    # En este metodo se abre un archivo de texto designado en modo escritura y se escriben las
    # direcciones de correo y grupos a los que pertenecen. Se ha escogido el siguiente formato de texto:
    # {direccion grupo1,grupo2,grupo3,...} 
    def guardar_informacion(self):
        with open(self.archivo_info, "w") as archivo:
            for direccion, grupos in self.mapeo_correos.items():
                archivo.write("{} {}\n".format(direccion, ",".join(grupos)))

    # En este metodo, primero se reescribe el diccionario que mapea las direcciones, en caso de que haya habido una
    # llamada anterior a cargar_informacion(). Se añade la libreria suppress para ignorar excepciones que puedan
    # haber en la lectura del archivo. Finalmente el bucle for lee linea por linea el archivo y separa las direcciones
    # y los grupos para, posteriormente, meterlos como llaves y valores de nuestro mapeo de correos respectivamente.
    # *la funcion strip() se llama para no tener en cuenta en nuestro codigo si hay saltos de linea (\n)*  
    def cargar_informacion(self):
        self.mapeo_correos = defaultdict(set)
        with suppress(IOError):
            with open(self.archivo_info) as archivo:
                for linea in archivo:
                    direcciones, grupos = linea.strip().split(" ")
                    grupos = set(grupos.split(","))
                    self.mapeo_correos[direcciones] = grupos
            

