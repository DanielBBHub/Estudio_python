print("\n--------------[Funcion len()]--------------\n")
lista_numeros = [1, 2, 3, 4]
print("Longitud de una lista: " + str(lista_numeros) + " : " + str(len(lista_numeros)) )

print("\n--------------[Funcion reversed()]--------------\n")
lista_invertida = []

for numero in reversed(lista_numeros):
   lista_invertida.append(numero)
print("Lista invertida: " + str(lista_numeros) + " : " + str(lista_invertida) )

print("\n--------------[Funcion enumerate()]--------------\n")
lista_palabras = ["Duki", "She", "Don't", "Give", "A", "Fo"]

for indice, palabra in enumerate(lista_palabras):
   print("\n" +"Tupla devuelta en esta iteracion: ")
   print(f" {indice + 1}: {palabra}", end="")

print("\n--------------[Funcion all() y any()]--------------\n")
lista_strings_vacia = ["Hola", "", ""]
print("Evaluacion de lista de strings utilizando any(): " + str(all(lista_strings_vacia)) )

lista_nums_con_ceros = [0, 0, 0, 0]
print("Evaluacion lista de nums con cero utilizando any(): " + str(any(lista_nums_con_ceros)) )

lista_palabras = ["Duki", "She", "Don't", "Give", "A", "Fo"]
print("Evaluacion de lista de strings utilizando all(): " + str(all(lista_palabras)) )

lista_vacia = [False, None]
print("Evaluacion de lista utilizando all(): " + str(all(lista_vacia)) )


print("\n--------------[Funciones __enter__ y __exit__]--------------\n")

import random, string
from typing import Dict
from juntador_strings import JuntarStrings
with JuntarStrings() as juntador:
   for i in range(15):
      juntador.append(random.choice(string.ascii_letters))

print("Resultado del uso del juntador de strings en sitaxis 'with': " + juntador.res)

print("\n--------------[Funciones con argumentos keyword]--------------\n")
x='hola'
def metodo_con_argumentoskw(x, y='kw_por_defecto', *, a, b=False ):
   print(x, y, a, str(b) + "\n")

metodo_con_argumentoskw(x, a='aloja', b=False)

# NO HACER
num = 5
def funcion_con_kw(numero = num):
   print(numero)

num = 6
funcion_con_kw(8) #8
funcion_con_kw() #5
funcion_con_kw(num) #6

from opciones import Opciones

opciones2 = Opciones()
print("\nRecuperacion de los parametros por defecto como palabras clave:" )
print("Debug (?): " + str(opciones2['debug']))
print("Nombre de usuario: " + str(opciones2['usuario']))
print("Contraseña de usuario: " + str(opciones2['contrasenya']))

opciones = Opciones(usuario='DanielB', contrasenya='dandadan', debug=True)
print("\nRecuperacion de los parametros introducidos arbitariamente como palabras clave:" )
print("Debug (?): " + str(opciones['debug']))
print("Nombre de usuario: " + str(opciones['usuario']))
print("Contraseña de usuario: " + str(opciones['contrasenya']))

print("\n--------------[Desempaquetando argumentos]--------------\n")
def mostrar_argumentos(a1, a2, a3='TRES'):
   print(a1, a2, a3)

primeros_argumentos = range(3)
segundos_argumentos = {
   'a1':'UNO',
   'a2':'DOS'
}
print("Desmepaquetando una sequencia: " )
mostrar_argumentos(*primeros_argumentos)
print("Desempaquetando un diccionario: ")
mostrar_argumentos(**segundos_argumentos)

opciones = Opciones(usuario='DanielBB')
print("\nRecuperacion de los parametros introducidos como palabras clave y desempaquetados:" )
print("Debug (?): " + str(opciones['debug']))
print("Nombre de usuario: " + str(opciones['usuario']))
print("Contraseña de usuario: " + str(opciones['contrasenya']))

print("\n--------------[Funciones como objetos]--------------\n")
def mi_funcion_con_descripcion():
   print("Esta funcion ha sido llamada")

mi_funcion_con_descripcion.description = "Una funcion de jugete"

def mi_segunda_funcion_con_descripcion():
   print("La segunda funcion ha sido llamada")

mi_segunda_funcion_con_descripcion.description = "Otra funciond de jugete"

def una_ultima_funcion(funcion):
   print("\nLa descripcion: ", end=" ")
   print(funcion.description)
   print("El nombre: ", end=" ")
   print(funcion.__name__)
   print("La clase: ", end=" ")
   print(funcion.__class__)
   print("Ahora llamaremos a la funcion que se ha recibido")
   funcion()

una_ultima_funcion(mi_funcion_con_descripcion)
una_ultima_funcion(mi_segunda_funcion_con_descripcion)

import datetime
import time
import eventos_por_tiempo

# Se crea una funcion que de formato al mensaje que queramos introducir
# añadiendole el tiempo en el que se esta ejecutando 
def formatear_tiempo(mensaje, *argumentos):
   ahora = datetime.datetime.now()
   print(f"{ahora:%I:%M:%S}: {mensaje} ")

# Se declaran tres funciones sencillas que serviran como callbacks
def uno(Cronometro):
   formatear_tiempo("Primera llamada")

def dos(Cronometro):
   formatear_tiempo("Segunda llamada")

def tres(Cronometro):
   formatear_tiempo("Tercera llamada")

# Se declara un objeto repetidor para hacer visible que los metodos son funciones 
# adjuntas a una clase 
class Repetidor:
   def __init__(self):
      self.cuenta = 0

   # La funcion repetidor llamara recursivamente a la funcion llamar_despues()
   # del objeto cronometro, que se ejecutara indefinidamente. Mostrara por pantalla
   # la cantidad de veces que se ha llamado a la funcion  
   def repetidor(self, cronometro):
      formatear_tiempo(f"repetir {self.cuenta}")
      self.cuenta += 1
      cronometro.llamar_despues(5, self.repetidor)

cronometro = eventos_por_tiempo.Cronometro()
# Esta llamada ira primero
cronometro.llamar_despues(1, uno)
# Esta llamada ira segunda
cronometro.llamar_despues(2, uno)
# Esta llamada casi inmediatamente despues de la llamada anterior
cronometro.llamar_despues(2, dos)
# Esta llamada ira quinta
cronometro.llamar_despues(4, dos)
# Esta llamada ira quarta
cronometro.llamar_despues(3, tres)
# Esta llamada ira sexta
cronometro.llamar_despues(6, tres)
repetidor = Repetidor()
# Habra llamadas indefinidamente con una diferencia de 5s entre ellas
cronometro.llamar_despues(5, repetidor.repetidor)
print("\n")
""" formatear_tiempo("Empezando")
cronometro.correr() """

# Se declara una clase sencilla con un metodo print()
class A:
   def print(self):
      print("Soy parte de la clase 'A'")

# Se declara otro metodo, con el que sustituiremos uno de los metodos
# de la clase declarada previamente 
def print_falso():
   print("No soy parte de la clase 'A'")

def print_falso2(self):
   print("Soy parte de todas las instancias de 'A'")

# Cambiando el metodo print de una instancia de la clase A
a = A()
a.print()
a.print = print_falso
a.print()

# Cambiando el metodo print de todas las instancias de la clase A
A.print = print_falso2
a = A()
a2 = A()
a.print()
a2.print()

# En esta definicion de la clase repetidor hemos cambiado el metodo repetir()
# por __call__() y cambiado el callback por el objeto mismo para que sea llamable
# y utilizar la funcionalidad del metodo __call__() implementado  
class Repetidor2:
   def __init__(self):
      self.cuenta = 0

   def __call__(self, cronometro):
      formatear_tiempo(f"repetir {self.cuenta} ")
      self.cuenta += 1
      cronometro.llamar_despues(5, self)

crono2 = eventos_por_tiempo.Cronometro()

# En esta llamada hacemos lo mismo pasando una instancia de Repetidor2 como callback
# Es importante destacar que unicamente se esta creando una instancia de la clase Repetidor2,
# para llamar al metodo __call__() tendriamos que escribir Repetidor2()() 
# (esto demuestra que no estas entendiendo la abstraccion que aporta el metodo __call__ 
# y deberias darle una segunda pensada)  
crono2.llamar_despues(5, Repetidor2())
print("\n")
""" formatear_tiempo("Empezando")
crono2.correr() """

print("\n--------------[Caso de uso (sistema de envio de correo automatizado)]--------------\n")
from ejemplo_tarea.lista_correos import ListaCorreos

with ListaCorreos('correos_y_grupos.db') as l:
   print("Escribiendo correos y grupos: " + str(l.mapeo_correos))
   print("\nEnviando correo")
   l.enviar_correos_a_todos("Prueba automatizada de correo","A la que te da esta haha anda tira", "ElGuason@gmail.com", 
                  "amigos", "trolls", cabeceras={"Replay-To" : "JoukerInternasional@gmail.com"})

   

# Se ha comentado esta llamada por que es redundante ya que se ha implementado en la clase
# ListaCorreos 
""" l.enviar_correo("Un sujeto modelo", "Los contenidos del mensaje", 
              "desde_paris_con_amor@gmail.com", "hacia_madrid@gmail.com", "hacia_burgos@gmail.com") """

# Se han comentado estas lineas ya que estan guardadas las direcciones y los grupos a
# las que estas pertenecen en el archivo "correos_y_grupos.db". Si se quiere añadir una 
# direccion a un grupo aqui esta lasintaxis necesaria para ello. Se ha de modificar el 
# campo del correo y grupo y hacerla llamada a guardar_informacion() para poder utilizar 
# estos datos en una futura ocasion   
""" 
print("Añadiendo a grupos: " )
l.anyadir_a_grupo("MiPollaConCebolla@gmail.com", "amigos")
print("Correo:'MiPollaConCebolla@gmail.com',Grupo:'amigos'" )

l.anyadir_a_grupo("MiPollaConCebolla@gmail.com", "trolls")
print("Correo:'MiPollaConCebolla@gmail.com',Grupo:'trolls'" )

l.anyadir_a_grupo("AgachateYConocelo@gmail.com", "trolls")
print("Correo:'AgachateYConocelo@gmail.com',Grupo:'trolls'" )

l.anyadir_a_grupo("GoooozGente@gmail.com", "streamers")
print("Correo:'GoooozGente@gmail.com',Grupo:'streamers'" )

l.anyadir_a_grupo("GoooozGente@gmail.com", "amigos")
print("Correo:'GoooozGente@gmail.com',Grupo:'amigos'" )

l.guardar_informacion()
print("Guardando la informacion...\n") 

print(l.mapeo_correos)
"""

