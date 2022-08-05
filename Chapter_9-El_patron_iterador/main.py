import datetime
from iterable_plantilla import IterableInicial
from iterador_plantilla import IteradorInicial

print("\n--------------[Bucle con iterador]--------------\n")
lista_palabras = 'Me follo a Knekro y me lo vuelvo a follar'.split()
# Ejemplo basico de un bucle sobre un iterador
iterable = IterableInicial('Me follo a Knekro y me lo vuelvo a follar')
iterator = IteradorInicial(iterable)
while True:
    try:
        item = next(iterator)
        # Hacer algo con el objeto
        print("Bucle WHILE: " + item)
    except StopIteration:
        break

for palabra in lista_palabras:
    print("Bucle FOR: " + str(palabra))

print("\n--------------[Uso de comprehension (List)]--------------\n")

string_nums = ["15", "0", "32","20"]
lista_enteros = [int(num) for num in string_nums]
print("Casteo de numeros str -> int: " + str(string_nums) + " : " + str(lista_enteros))

lista_enteros_pares = [int(num) for num in string_nums if int(num) % 2 == 0]
print("Casteo de numeros pares str -> int: " + str(string_nums) + " : " + str(lista_enteros_pares))

# El siguiente ejemplo es uno de como puede llegar uno a abusar de una herramienta,
# haciendo dificil de leer y mantener el codigo que se escribe 

archivo = "apuntes.txt"
with open(archivo) as archivotxt:
    cabecera = archivotxt.readline().strip().split("\t")
    tiempo_empezar = datetime.datetime.now()
    print(tiempo_empezar)
    contenidos = [ 
        dict(zip(cabecera, linea.strip().split("\t")))
        for linea in archivotxt
    ]
print("Comprehension dict: " + str(datetime.datetime.now() - tiempo_empezar))
""" for contenido in contenidos:
    print(contenido) """

print("\n--------------[Uso de comprehension (Set y Dict)]--------------\n")

from collections import namedtuple
Libro = namedtuple("Libro", "autor titulo genero")
libros = [
    Libro("Nassim Taleb", "El cisne negro: El impacto de lo altamente improbable", "literario"),
    Libro("Dostoiesvky", "El idiota", "novela"),
    Libro("Turner", "El ladron", "fantasia"),
    Libro("Rothfuss", "El temor de un hombre sabio", "fantasia")
]

libros_de_fantasia = {libro.autor for libro in libros if libro.genero == "fantasia"}
print("Comprehension en set: " + str(libros_de_fantasia))

libros_de_fantasia = {libro.autor: (libro.titulo, libro.genero) for libro in libros if libro.genero == "fantasia"}
print("Comprehension en dict: " + str(libros_de_fantasia))


print("\n--------------[Uso de expresiones generadoras]--------------\n")


with open(archivo) as archivotxt:
    with open("archivos_generados/res_exp_generadora.txt", 'w') as archivo_generado:
        tiempo_empezar = datetime.datetime.now()
        print(tiempo_empezar)
        lineas_con_guiones = (linea for linea in archivotxt if '-' in linea)
        for linea_nueva in lineas_con_guiones:
            archivo_generado.write(linea_nueva)

print("Expresion generadora: " + str(datetime.datetime.now() - tiempo_empezar))

print("\n--------------[Uso de generadores]--------------\n")

from filtro_guiones import FiltroGuiones
with open(archivo) as archivotxt:
    with open("archivos_generados/res_generador.txt", 'w') as archivo_generado:
        tiempo_empezar = datetime.datetime.now()
        print(tiempo_empezar)
        filtro = FiltroGuiones(archivotxt)
        for linea in filtro:
            archivo_generado.write(linea)
print("Expresion generadora: " + str(datetime.datetime.now() - tiempo_empezar))

def cambiar_guiones_secuencia(secuencia):
    for linea in secuencia:
        if '-' in linea:
            yield linea.replace('-', '@')

with open(archivo) as archivotxt:
    with open("archivos_generados/res_func_generador.txt", 'w') as archivo_generado:
        tiempo_empezar = datetime.datetime.now()
        print("\n" + str(tiempo_empezar))
        filtro = cambiar_guiones_secuencia(archivotxt)
        for linea in filtro:
            archivo_generado.write(linea)
print("Expresion generadora: " + str(datetime.datetime.now() - tiempo_empezar))

def cambiar_guiones_archivo(archivo):
    with open(archivo) as archivotxt:
        yield from(
             linea.replace('-', '@') for linea in archivotxt if '-' in linea
        )

filtro = cambiar_guiones_archivo(archivo)
with open('archivos_generados/res_fun_generadora.txt', 'w') as generado:
    for linea in filtro:
        generado.write(linea)

# ------------------------------------- Clases --------------------------
# Para poner a prueba las funciones generadoras se ha aplicado en un problema clasico
# de caminar un arbol, con lo que se define  
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

class Carpeta(Archivo):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = []


raiz = Carpeta("")
etc = Carpeta("etc")
raiz.hijos.append(etc)
etc.hijos.append(Archivo("passwd"))
etc.hijos.append(Archivo("grupos"))
httpd = Carpeta("httpd")
etc.hijos.append(httpd)
httpd.hijos.append(Archivo("http.config"))
var = Carpeta("var")
raiz.hijos.append(var)
log = Carpeta("log")
var.hijos.append(log)
log.hijos.append(Archivo("mensajes"))
log.hijos.append(Archivo("kernel"))

def caminar_arbol(archivo):
    if isinstance(archivo, Carpeta):
        yield archivo.nombre + "/"
        for f in archivo.hijos:
            yield from caminar_arbol(f)
    else:
        yield archivo.nombre

lista_archivos = []
lista_archivos = caminar_arbol(raiz)
for archivo in lista_archivos:
    print("Arbol caminado: " + str(archivo))


print("\n--------------[Corrutinas]--------------\n")

# Como hemos visto anteriormente, aun que estemos definiendo una funcion, en el momento
# que Python detecte una sintaxis yield, se tomara las molestias de envolverla en un objeto
def calcular():
    resultado = 0
    while True:
        incremento = yield resultado
        resultado += incremento

# Se definen dos objetos 
barcelona = calcular()
madrid = calcular()
# Cuando llamamos a next() hace lo mismo que cualquier generador, ejecuta linea por linea
# hasta que encuentra un yield, devolviendo el valor y pausando la ejecucion hasta que se vuelve
# ha llamar a next() y continua el trabajo desde donde se dejo la ultima vez. Es importante 
# aclarar que hemos de llamar a next una vez por cada individuo, ya que si no no podremos utilizar
# send 
# "barcelona.send(1)
# TypeError: can't send non-None value to a just-started generator"
print("Inicializando objetos {} : {}".format(next(barcelona),next(madrid)))
# Esta es la parte interesante, ya que el metodo send() hace exactamente lo mismo que yield ademas
# de poder introducir argumentos desde fuera del generador para el empleo de este. Este valor es lo que
# se le asignara a la parte izquierda del yield en la funcion (en este caso a incremento)  
barcelona.send(1)
barcelona.send(1)
madrid.send(1)

print("Resultado del partido: " + str(barcelona.send(0)) + " : " + str(madrid.send(0)))

import re
# Este es un uso de corrutina, el cual unicamente se encarga de iterar las lineas del archivo
# en busca de coincidencias con la expresion regular 
def emparejar_regex(archivo, regex):
    # Abrimos el archivo de logs
    with open(archivo) as logs:
        # Leemos todas las lineas
        lineas = logs.readlines()
    # Para poder detectar primero si hay un error antes de pasarnos las lineas que queremos
    # obtener iteramos las lineas en orden invertido 
    for linea in reversed(lineas):
        # Pasamos el emparejador de regex linea por linea
        match = re.match(regex, linea)
        # Si encontramos alguna coincidencia asignamos el valor ala variable regex y creamos
        # la corrutina mediante el yield 
        if match:
            # Se ejecuta el yield y se para la rutina hasta que se vuelva a comenzar con un send()
            regex = yield match.groups()[0]

# Este es un uso de un generador, el cual utiliza una corrutina para obtener el numero de serie de
# un dispositivo, es decir, decide que lineas son importantes para encontrar dicho numero 
def obtener_numero_serie(archivo):
    # Definimos la regex para detectar las lineas de error
    ERROR_RE = "XFS ERROR (\[sd[a-z]\])"
    # Ejecutamos el emparejador sobre el archivo de logs en base a nuestra regex
    matcher = emparejar_regex(archivo, ERROR_RE)
    # Inicializamos el objeto asignado a matcher y recogemos el codigo de dispositivo
    # con el error 
    dispositivo = next(matcher)
    print("Dispositivo " + str(dispositivo))

    while True:
        try:
            # Definimos otra regex para encontrar el bus donde se encuentra el num de serie
            bus = matcher.send(
                "(sd \S+) {}.*".format(re.escape(dispositivo))
            )
            print("\nBUS " + str(bus))
            # Enviamos una nueva regex para que, ahora, recoga el num de serie del dispositivo
            serial = matcher.send("{} \(SERIAL=([^)]*)\)".format(bus))
            print("SERIAL " + str(serial))
            # Se devuelve el serial
            yield serial
            # Y se comienza a buscar otra vez un mensaje de error
            dispositivo = matcher.send(ERROR_RE)
            print("\nDispositivo " + str(dispositivo))
        # Una vez se han acabado las lineas que iterar se levanta la excepcion
        except StopIteration:
            # Se cierra el emparejador (la corrutina) y se para el bucle while
            matcher.close()
            return


with open("archivos_generados/num_serie_logs.txt", 'w') as nums_serie:
    nums_serie.write("Numero de serie de dispositivo defectuoso:\n")
    for numero_serie in obtener_numero_serie("kernel_logs.txt"):    
        print(numero_serie)
        nums_serie.write(numero_serie + "\n")


print("\n--------------[Caso de uso (Machine Learning)]--------------\n")
from ejemplo_tarea import machine_learning as mm

mm.procesar_colores()