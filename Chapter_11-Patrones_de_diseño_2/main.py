print("\n--------------[Patron de diseño: Patron adaptador]--------------\n")
from datetime import datetime
from re import T
from adaptador import calculadora_edad, adaptador_edad, fecha_herencia 

cumple = fecha_herencia.FechaHerencia(2000, 4, 11)
hoy = fecha_herencia.FechaHerencia.today()

# Calculo con el objeto de fecha modificado
calc = calculadora_edad.CalculadoraEdad(cumple)
res = calc.calcular_edad(hoy) 
print("Tu edad es la siguiente: {}".format(res))

# Calculo con el adaptador de la calculadora
edad_adaptada = adaptador_edad.AdaptadorFecha(datetime(2000, 4, 11))
res = edad_adaptada.get_edad(hoy)
print("Tu edad es la siguiente: {}".format(res))

print("\n--------------[Patron de diseño: Patron fachada]--------------\n")


print("\n--------------[Patron de diseño: Patron peso-mosca]--------------\n")
from peso_mosca import coche, modelo_coche
import gc

dx = modelo_coche.ModeloCoche("FIT DX")
lx = modelo_coche.ModeloCoche("FIT LX", True, True, True)

coche1 = coche.Coche(dx, "Azul", "123456")
coche2 = coche.Coche(lx, "Rojo", "789123")

print("Comprobacion del id de los modelos creados: " + str(id(dx)) + " : " + str(id(lx)))

del lx 
del coche2
gc.collect()

lx = modelo_coche.ModeloCoche("FIT LX", ac = True, control_cruzero = True, llantas_aleacion = True)
lxid2 = str(id(lx))
lx = modelo_coche.ModeloCoche("FIT LX")
lxid1 = str(id(lx))


# Comprobamos que despues de crear dos instancias con el mismo identificador
# no se llenan dos espacios de memoria distintos 
print("Comprobacion del id de los modelos creados (ambos iguales): {0} : {1} ".format(lxid1, lxid2))
print("¿Son los modelos iguales? " + str(lxid1 == lxid2) + " ¿Tienen aire acondicionado? " + str(lx.ac))
print("\n")
# La lista con las diferentes instancias de modelos es comun
for modelo in dx._modelos:

    print("Lista modelos instancia dx: " + str(modelo))
for modelo in lx._modelos:

    print("Lista modelos instancia lx: " + str(modelo))

print("\n--------------[Patron de diseño: Patron comando]--------------\n")
from comando.non_pythonic import ventana, documento, guardar, salir, barra_herramientas, atajo_teclado, objetos_menu

# Definimos los receptores
ventana1 = ventana.Ventana()
documento1 = documento.Documento("doc_texto.txt")

# Definimos los comandos
com_guardar = guardar.Guardar(documento1)
com_salir = salir.Salir(ventana1)

# Se asigna los comandos a los invocadores 
boton_guardar = barra_herramientas.BarraHerramientas("guardar", "icono_guardar.png")
boton_guardar.command = com_guardar
atajo_guardar = atajo_teclado.AtajoTeclado("s", "ctrl")

boton_salir = objetos_menu.ObjetosMenu("Archivo", "Salir")
boton_salir.command = com_salir


print("\n--------------[Patron de diseño: Patron fabrica abstracta]--------------\n")
from fabrica_abstracta import fabrica_formateadora
codigo_pais = "FR"

fabrica_formateo = fabrica_formateadora.mapeo_fabrica.get(codigo_pais)()
formateo_fecha = fabrica_formateo.crear_formateador_fecha()
fecha = formateo_fecha.formatear_fecha(2022, 8, 24)
print("Fecha obtenida por el formateador FR: {} ".format(fecha))

formateo_divisa = fabrica_formateo.crear_formateador_divisa()
divisa = formateo_divisa.formatear_divisa(1553, 99)
print("Divisa obtenida por el formateador FR: {} ".format(divisa))

print("\n--------------[Patron de diseño: Patron compuesto]--------------\n")
from composicion import componente_abc

directorio1 = componente_abc.Directorio("Directorio1")
directorio2 = componente_abc.Directorio("Directorio2")

componente_abc.raiz.añadir_hijo(directorio1)
componente_abc.raiz.añadir_hijo(directorio2)

directorio11 = componente_abc.Directorio("Directorio11")
directorio1.añadir_hijo(directorio11)

archivo1 = componente_abc.Archivo("archivo1", "contenidos")
directorio11.añadir_hijo(archivo1)

archivo2 = componente_abc.Archivo("archivo2", "contenidos")
directorio2.añadir_hijo(archivo2)

archivo3 = componente_abc.Archivo("archivo3", "contenidos")
directorio1.añadir_hijo(archivo1)
print("[")
for llave, hijo in directorio1.hijos.items():
    print(str(llave) )
    
print("]")

print("[")
for llave, hijo in directorio2.hijos.items():
    print(str(llave))

print("]")