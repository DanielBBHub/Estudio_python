from prueba_excepciones import Pruebas
p = Pruebas()

""" try:
    p.call_exceptor()
except:
    print("--------------Primera prueba---------------")
    print("He recogido una escepcion")
    print("Y he ejecutado este codigo") """


""" print("--------------Segunda prueba---------------")
p.division_jajas(0)
print("--------------Tercera prueba---------------")
p.division_jajas(50)
print("--------------Cuarta prueba---------------")
p.division_jajas("Dos palabras") """

""" for val in (0, "hola", 50.00, 13):
    print("--------------Prueba con valor: {} ---------------".format(val), end=" ")
    print(p.division_jajas2(val)) """

""" for val in (0, "hola", 50.00, 13):
    print("--------------Prueba con valor: {} ---------------".format(val), end=" ")
    print(p.division_jajas3(val)) """


""" try:
    raise ValueError("Esto es el argumento")
except ValueError as error:
    print("Este es el argumento del error recogido: {}".format(error)) """

import random
escepciones = [ValueError, TypeError, IndexError, None]

""" try:
    eleccion_escepcion = random.choice(escepciones)
    print("Levantando la escepcion: {}".format(eleccion_escepcion))
    if eleccion_escepcion:
        raise eleccion_escepcion("Un error")
except ValueError:
    print("Recogido un ValueError")
except TypeError:
    print("Recogido un TypeError")
except Exception as error:
    print("Recogido cualquier otro error: %s" %
    # Recogo el nombre de la clase del error mediante metodos y propiedades privadas de este
    (error.__class__.__name__))
else:
    print("Este codigo se ejecuta si no hay ningun error")
finally:
    print("Este codigo se ejecuta siempre") """

from nueva_excepcion import EscepcionDePrueba

#raise EscepcionDePrueba("Estas quajao niño, que haces Knekrin")


from excepcion_con_propiedades import ExcepcionConPropiedades

try:
    raise ExcepcionConPropiedades(25, 50)
except ExcepcionConPropiedades as e:
    print("Lo sentimos pero la cantidad a retirar es mayor que el balance por: " f"${e.deuda()}" )

from ejemplo_tarea.autentificador import Autentificador
from ejemplo_tarea.autorizador import Autorizador

auth = Autentificador()
autorizador = Autorizador(auth)

auth.añadir_usuario("Joe Mama", "joemamapass")
autorizador.anyadir_permisos("pintar")
#auth.login("Joe Mama", "joemamapass")
#autorizador.permitir_usuario("pintar","Joe Mama" )
autorizador.comprobar_permisos("pintar", "Joe Mama")