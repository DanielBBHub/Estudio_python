from pickle import TRUE
from info_comportamiento_clases import *
from cagarse_en_java import Color
""" cuadrado = Poligono()
cuadrado.anyadir_vertice(Punto(1,1))
cuadrado.anyadir_vertice(Punto(1,2))
cuadrado.anyadir_vertice(Punto(2,2))
cuadrado.anyadir_vertice(Punto(2,1))
print("Solucion usando programacion orientada a objetos:")
#print(cuadrado.calcular_perimetro())

print("Solucion usando programacion con lista de tuplas:")
cuadrado = [(1,1),(1,2),(2,2),(2,1)]
#print(perimetro(cuadrado))

c = Color("#0000ff", "rojo brillante")
print("Prueba con el metodo semi-privado (obtener nombre)")
print(c._get_nombre())
print("Prueba con el atributo-propiedad (obtener nombre)")
print(c.name)

print("Prueba con el metodo semi-privado (cambiar nombre)")
c._set_nombre("verde")
print(c._get_nombre())
print("Prueba con el atributo-propiedad (cambiar nombre)")
c.name = "amarillo"
print(c.name)

#help(Color) """

import time
from web import WebPage
""" 
# Cargamos la url de la pagina que queramos acceder a la clase que hemos creado
web = WebPage("https://www.google.com/search?client=opera&q=google&sourceid=opera&ie=UTF-8&oe=UTF-8")
# Para ver la diferencia de tiempo guardamos el tiempo en el que empieza a ejecutar el codigo
tiempo_ahora = time.time()
# Llamamos a la funcion para que abra la página
contenido1 = web.content
# Sacamos por pantalla el tiempo que ha tardado en cargar la página
print(time.time() - tiempo_ahora)
# Volvemos a guardar el tiempo
tiempo_ahora = time.time()
# Volvemos a llamar a la funcion para cargar la pagina
contenido2 = web.content
# Volvemos a comprobar el tiempo que tarda en cargar la pagina
print(time.time() - tiempo_ahora)
# Comprobamos que ambos contenidos de las variables son los mismos
print(contenido1 == contenido2) """

from zips.reemplazar_zips_subclase import ReemplazadorZip
""" ree = ReemplazadorZip("texto_a_cambiar.zip","OLE", "ALOJA")
ree.encontrar_reemplazar_zip() """

from docs.documento import Documento
import string
from docs.caracter import Caracter

# Creamos un objeto documento
doc = Documento()
# Le añadimos un nombre
doc.nombre_archivo = "Knekrin tercero del mundo lesgo.txt"
# Insertamos en la lista de caracteres el abecedario completo
for i in list(string.ascii_lowercase):
    doc.insert(i)

# Volvemos 4 posiciones atras con el cursor
for i in range(4):
    doc.cursor.back()

# Borramos el caracter, lo sustituimos por una K y hacemos un salto de linea
doc.delete()
doc.insert(Caracter("K", negrita=True, subrayado=True))
doc.insert("\n")

# Vamos al principio de la linea e insertamos un "[*"
doc.cursor.home()
doc.insert("[")
doc.insert("*")

# Vamos al final de la linea e insertamos un "*]"
doc.cursor.end()
doc.insert("*")
doc.insert("]")
print(doc.string)
doc.save()

# Para comprobar el contenido, primero abrimos el archivo y lo guardamos en "contenido_archivo"
contenido_archivo = open("Knekrin tercero del mundo lesgo.txt", "r").read()
print("El archivo contiene el siguiente mensaje: ( " + contenido_archivo + " )")
# Tambien lo sacamos a partir de la lista de caracteres de la clase Documento
print("La propiedad string nos devuelve: [ {} ]".format(doc.string))
