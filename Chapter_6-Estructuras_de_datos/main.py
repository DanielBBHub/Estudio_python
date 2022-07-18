tupla1 = "hola", 18, 17.46, 24
tupla2 = ("hola", 18, 17.46, 24)

import datetime
from operator import itemgetter
from xml.dom.pulldom import CHARACTERS
def medio(tupla, fecha):
    simbolo, actual, bajo, alto = tupla
    return (((alto + bajo) / 2), fecha)

valor_medio, fecha = medio(tupla2, datetime.date(2022, 7, 11))

print("\n--------------[Obtencion de valores de una tupla]--------------\n")
print("Valor medio tupla: " + str(valor_medio) + " : " +str(fecha))

print("Desmempaquetando: " + str(tupla1[2]))
print("Desmempaquetando: " + str(tupla1[:3]))

# Para usar las tuplas con nombre debemos primero importar la libreria 
from collections import namedtuple
Stock = namedtuple("Stock", ["simbolo", "actual", "bajo", "alto"])
stock = Stock("hola", 18, 17.46, 24)

print("Tupla con nombre: " + str(stock.simbolo) + " : " + str(stock.alto))

# Para usar las dataclasses debemos primero importar la libreria 
from dataclasses import make_dataclass
Stock = make_dataclass("Stock",[ "simbolo", "actual", "bajo", "alto"])
stock = Stock("hola", 18, 17.46, 24)

print("\n--------------[Obtencion de valores de una dataclass]--------------\n")
print("Dataclass: " + str(stock))
stock.simbolo = "FB"
print("Simbolo de la dataclass modificado: " + stock.simbolo)

# Importamos "Any"para no tener que especificar siempre que tipo de dato tenemos que introducir
from typing import Any
from dataclasses import dataclass

@dataclass
class StockDecorado:
    nombre: str
    actual: Any
    bajo: float
    alto: float

stock2 = StockDecorado("Twitter", 18, 17.46, 24 )
print("Dataclass decorada: " + str(stock2))

diccionario = dict()
diccionario["llave"] = 12

print("\n--------------[Obtencion de valores de un diccionario]--------------\n")
diccionario2 = { "llave" : 24}
print("Obteniendo un valor por llave: " + str(diccionario["llave"]))
print("Obteniendo un valor por llave (metodo): " + str(diccionario2.get("llave")))

print("\n--------------[Uso de setdefault() para dar valores a un diccionario]--------------\n")
diccionario.setdefault("ancla", 25)
print("Valor por defecto: " + str(diccionario.get("ancla")))

diccionario_stocks = {
    "GOOG" : (127.5, 124.2, 123.5),
    "MSTF" : (147.5, 128.2, 153.5)
}

# En est bucle for "stock" es la llave que identifica a los "values" que se encuentran 
# dentro de los items del diccionario
print("\n--------------[Obtencion de valores de un diccionario en bucle for]--------------\n")
for stock, values in diccionario_stocks.items():
    print(f"{stock} ultimo valor es {values[0]} ")

diccionario_stocks["GOOG"] = (147.5, 128.2, 153.5)
diccionario_stocks["MSTF"] = (127.5, 124.2, 123.5)
print("\n--------------[Obtencion de valores de un diccionario en bucle for despues de cambiarlos]--------------\n")
for stock, values in diccionario_stocks.items():
    print(f"{stock} ultimo valor es {values[0]} ")


print("\n--------------[Uso de diccionarios para guardar objetos (existan o no llaves)]--------------\n")
frase = "Me follo a knekro y me vuelvo a follar a knekro"

# Usamos un diccionario para guardar las palabras que hay en una frase, como llaves, y las 
# veces que estas aparecen en ella
def word_frecuency(frase):
    frecuencias = {}
    frase = frase.split(" ")
    for palabra in frase:
        frecuencia = frecuencias.setdefault(palabra, 0)
        frecuencias[palabra] = frecuencia + 1
    return frecuencias
print("Contar cuantas veces se repiten las palabras en una frase: {}".format(str(word_frecuency(frase))))



# Usamos un diccionario para guardar las palabras que hay en una frase, como llaves, y las 
# veces que estas aparecen en ella. En este caso usamos el defaultdic para evitar comprobar 
# cada vez que exista la llave a la que queremos sumar el valor
from collections import defaultdict
def word_frecuency_defaultdict(frase):
    frecuencias = defaultdict(int)
    frase = frase.split(" ")
    for palabra in frase:
        frecuencias[palabra] += 1
    return frecuencias
print("Contar cuantas veces se repiten las palabras en una frase (objeto defaultdict): {}".format(str(word_frecuency_defaultdict(frase))))


num_objetos = 0

def tuple_counter():
    global num_objetos
    num_objetos += 1
    return (num_objetos, [])

d = defaultdict(tuple_counter)
d["a"][1].append("Hola")
d["b"][1].append("mundo")

print(d)

print("\n--------------[Uso del objeto Counter para guardar como llaves objetos evaluados y nº de apariciones como valor]--------------\n")
from collections import Counter
def word_frecuency_counter(frase):
    frase = frase.split(" ")
    return Counter(frase)

contador = word_frecuency_counter(frase)
print("Contar cuantas veces se repiten las palabras en una frase (objeto Counter): {}".format(str(contador)))
print("Las palabras que mas se repiten son:")
for i in range(3):
    # La funcion "most_common(n)" enseña en orden las llaves con mayor valor, siendo n 
    # la longitud de la lista que quieres que devuelva
    print(contador.most_common(3)[i])

import string
CHARACTERES = list(string.ascii_letters) + [" "]

print("\n--------------[Uso de listas para guardar y ordenar valores]-------------- \n")
# Funcion que crea una lista y guarda tuplas en cada posicion, tantas como letrs en el abecedario,
# para llevar la cuenta de cuantas veces ha aparecido cada una en una frase 
def letters_frequency(frase):
    frecuencias = [(c, 0) for c in CHARACTERES]
    for letra in frase:
        indice = CHARACTERES.index(letra)
        frecuencias[indice] = (letra, frecuencias[indice][1] +1)
    return frecuencias

print("Ejemplo que no se ha de seguir con listas: " + str(letters_frequency(frase)))

from lista_ordenada import ListaOrdenada

a = ListaOrdenada('a', 4, True)
b = ListaOrdenada('b', 3, True)
c = ListaOrdenada('c', 2, True)
d = ListaOrdenada('d', 1, True)
e = ListaOrdenada('e', 0, True)

lista_de_listas = [a, b, c, d, e]
print("Probando el funcionamiento de __repr__(): " + str(lista_de_listas) )
lista_de_listas.sort()
print("Probando el funcionamiento de __lt__(): " + str(lista_de_listas))
for i in lista_de_listas:
    i.num_ordenado = False
lista_de_listas.sort()
print("Probando el funcionamiento de __lt__() (cambiando el valor de num_ordenado): " + str(lista_de_listas))

lista_strings = ["hol", "AYUDA", "Hola"]
lista_strings.sort()
print("Ordenando una lista de strings: " + str(lista_strings))

def funcion_para_ordenar(obj):
    return len(obj)

lista_strings.sort(key=funcion_para_ordenar)
print("Ordenando una lista de strings pasandole un argumento a sort (longitud): " + str(lista_strings))

lista_strings.sort(reverse=True ,key=funcion_para_ordenar)
print("Ordenando una lista de strings pasandole un argumento a sort (revertida, longitud): " + str(lista_strings))

import operator
lista_tuplas = [('h', 4), ('n', 6), ('o', 5), ('p', 1)]
# itemgetter() recibe un numero n de arugmentos y aplica una funcion sobre ese numero de elementos
lista_tuplas.sort(key=operator.itemgetter(1))
print("Ordenando una lista de tuplas: " + str(lista_tuplas))

GUITARRISTAS = [
    {'nombre':'Timo', 'apellido':'Tolski', 'banda':'Stratovarius'},
    {'nombre':'Eric', 'apellido':'Clapton', 'banda':'Cream'},
    {'nombre':'Eddie', 'apellido':'Van Halen', 'banda':'Van Halen'},
    ]
GUITARRISTAS.sort(key=operator.itemgetter('apellido', 'nombre'))
print("Comprobando itemgetter() en un diccionario: " + str(GUITARRISTAS))

print("\n--------------[Uso de sets para guardar valores]-------------- \n")

libreria_canciones = [
    ("She dont give a fo", "Duki"),
    ("Goteo", "Duki"),
    ("Llorando en la limo", "C. Tangana"),
    ("Mala mujer", "C. Tangana"),
    ("Jugador 9", "Soto Asa"),
    ("Tana", "Soto Asa"),
    ("Venenno", "Delaosa"),
    ("Fellas / Again", "Saske")
]

artistas1 = set()
for cancion, artista in libreria_canciones:
    artistas1.add(artista)

print("Set de artistas: " + str(artistas1))

artistas2 = {
    "Easy.S",
    "El Virtual",
    "Delaosa",
    "Carrion"
}


print("Todos los artistas: \n set1-2: [" + str(artistas1.union(artistas2)) + "] \n set2-1: [" + str(artistas2.union(artistas1)) + " ]")
print("Artistas en comun: \n set1-2: [" + str(artistas1.intersection(artistas2)) + "] \n set2-1: [" + str(artistas2.intersection(artistas1)) + " ]")
print("Unos u otros artistas, pero no los dos sets completos: " + str(artistas1.symmetric_difference(artistas2)))

union = artistas1.union(artistas2)
space_hammu = {
    "Raggio", 
    "Delaossa", 
    "Easy.S", 
    "Carrion", 
    "Saske", 
    "J.Moods",
    "Kas Rules"  
}
print("Diferencia entre sets: " + str(union.difference(space_hammu)))
print("Diferencia equivale a un operador - : " + str(union - space_hammu))

print("\n--------------[Ejemplo tarea recolector URLs]-------------- \n")
from ejemplo_tarea.recolector_urls import RecolectorDeLinks

# Para comprobar el ejemplo has de ejecutar "python -m http.server" en una cmd dentro del
# directorio /ejemplo_tarea para poder acceder a los archivos html
recolector = RecolectorDeLinks("http://localhost:8000/")
recolector.recoger_links()
