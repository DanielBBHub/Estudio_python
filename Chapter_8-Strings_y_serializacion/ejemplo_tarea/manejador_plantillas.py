from argparse import ArgumentError
import re
import json
from pathlib import Path

REGEX = re.compile(
    # Se usa la r (raw string) para poder partir la regex en dos lineas
    # y asi mejorar la lectura de esta. Se estan buscando substrings como los siguientes:
    # /** include header.html **/ 
    r'/\*\*\s*(include|variable|loopover|endloop|loopvar)'
    r'\s*([^*]*)\s*\*\*/'
)

class MotorPlantillas:

    def __init__(self, archivo_in, archivo_out, archivo_contexto):
        # En el constructor se han asignado los valores del archivo que usaremos
        # como plantilla (en este caso index.html) 
        self.plantilla = open(archivo_in).read()
        # Se recoge el path del directorio en el que estamos trabajando para coger
        # los recursos que sean necesarios 
        self.dir_trabajo = Path(archivo_in).absolute().parent
        self.pos = 0
        # Se declara el archivo que sera modificado con la inclusion de la informacion
        # que obtengamos del archivo JSON 
        self.archivo_salida = open(archivo_out, 'w')
        # Abrimos el archivo JSON para parsear en un diccionario toda la informacion que este alberga
        with open(archivo_contexto) as archivo_contexto:
            self.contexto = json.load(archivo_contexto)

    def procesar(self):
        # Se llama a la funcion search() para que empieze a buscar en index.html
        # los diferentes strings que coincidan con el patron 
        match = REGEX.search(self.plantilla, pos=self.pos)
        # Mientras haya habido un match
        while match:
            # Se escribira en el archivo generado.html la informacion de la plantilla
            self.archivo_salida.write(self.plantilla[self.pos:match.start()])
            # Se recoge la informacion del emparejamiento dentro de las variables
            # "accion", que sera el string que decida que funcion de procesar_ sera la
            # que se ejecute, mientras que argument sera el trozo de informacion que tendremos
            # que buscar dentro del archivo JSON   
            accion, argument = match.groups()
            nombre_metodo = 'procesar_{}'.format(accion)
            # Se llama a la funcion getattr() para realizar la accion necesaria, en este ejemplo
            # seran: inrustar header-> incrustar menu->  incrustar el menu-> introducir nombre->
            # introducir mediante bucle la lista de libros-> incrustar footer 
            getattr(self, nombre_metodo)(match, argument)
            # Se vuelve a llamar a search() para continuar la escritura del archivo
            match = REGEX.search(self.plantilla, pos = self.pos)
        # En el caso de que la ultima llamada a search() no haya devuelto nada, simplemente
        # se escribe el resto de la plantilla, desde donde se ha quedado hasta el final 
        self.archivo_salida.write(self.plantilla[self.pos:])    

    def procesar_include(self, match, argumento):
        # Para incrustar los archivos html dentro del archivo generado se declara esta funcion,
        # la cual busca en el directorio de trabajo un archivo con un nombre que coincida con el
        # argumento recibido  
        with (self.dir_trabajo / argumento ).open() as archivo_include:
            # Una vez abierto, se escribe en el archivo generado
            self.archivo_salida.write(archivo_include.read())
            self.pos = match.end()

    def procesar_variable(self, match, argumento):
        # Se busca el valor de la variable que se requiere y se escribe en el archivo generado,
        # se declara que, en caso de que no exista, se devuelva un string vacio 
        self.archivo_salida.write(self.contexto.get(argumento, ''))
        self.pos = match.end()

    def procesar_loopover(self, match, argumento):
        # Se declara esta funcion para establecer las variables:
        # indice_bucle, lista_bucle y pos_bucle que utilizaremos para iterar la
        # informacion convertida del objeto JSON. Se declara que, en caso de que no exista, 
        # se devuelva una lista vacia  
        self.indice_bucle = 0
        self.lista_bucle = self.contexto.get(argumento, [])
        self.pos = self.pos_bucle = match.end()

    def procesar_loopvar(self, match, argumento):
        # Se declara esta funcion para iterar la lista con la informacion recibida y a su vez
        # escribirla en el archivo generado
        self.archivo_salida.write(self.lista_bucle[self.indice_bucle])
        self.pos = match.end()

    def procesar_endloop(self, match, argumento):
        # Se declara esta funcion para, primero, comprobar si quedan mas posiciones en la lista 
        # a iterar y, en caso afirmativo añadir 1 a la posicion del bucle, segundo, en caso de
        # que se haya llegado al final de la iteracion, desdefinir las variables para el bucle y
        # situar la posicion al final del bucle    
        self.indice_bucle += 1
        if self.indice_bucle >= len(self.lista_bucle):
            self.pos = match.end()
            del self.indice_bucle
            del self.lista_bucle
            del self.pos_bucle
        else:
            self.pos = self.pos_bucle

    