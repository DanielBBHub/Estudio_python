import time 

print("\n--------------[Patron de diseño: Patron decorador]--------------\n")
import decoradores.funciones_decoradas as func

@func.llamadas_log
def test1(a, b, c):
    print("\tLlamado test1")

def test2(a, b):
    print("\tLlamado test2")

def test3(a, b):
    print("\tLlamado test3")
    time.sleep(1)

test2 = func.llamadas_log(test2)
test3 = func.llamadas_log(test3)

test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)


print("\n--------------[Patron de diseño: Patron observador]--------------\n")
from observadores.inventario import Inventario
from observadores.observador_consola import ObservadorConsola

inv = Inventario()
obs1 = ObservadorConsola(inv)
obs2 = ObservadorConsola(inv)
inv.attach(obs1)
inv.attach(obs2)
inv.producto = "Dildo de goma"
inv.cantidad = 5

print("\n--------------[Patron de diseño: Patron estrategia]--------------\n")



print("\n--------------[Patron de diseño: Patron estados]--------------\n")
from estados.parser import  Parser
with open("estados/ejemplo_xml.xml") as archivo_xml:
    contenidos = archivo_xml.read()
    p = Parser(contenidos)
    p.start()

    nodos = [p.raiz]
    while nodos:
        nodo = nodos.pop(0)
        print(nodo)
        nodos = nodo.hijos + nodos

print("\n--------------[Patron de diseño: Patron estados]--------------\n")
from singleton import un_unico
singleton1 = un_unico.UnUnico()
singleton2 = un_unico.UnUnico()

# Comprobamos mediante un assert que estos dos objetos sean iguales
assert singleton1 == singleton2
# Para despues comprobar mediante un print que ambos objetos apuntan al mismo
# espacio de memoria, confirmando que son el mismo 
print(singleton1)
print(singleton2)