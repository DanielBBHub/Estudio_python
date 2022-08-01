print("\n--------------[Manipulacion de strings]--------------\n")
a = 'hola'
b = "k ase"
c = """ string multilinea
    lesgooo con la ligel """

e = ("Tres" "Strings" "Juntos")

print("Cuenta de la letra o dentro de: {}: ".format(c) + str(c.count('o')))

print("Busqueda de la letra 'l' dentro de: {} indice[".format(a) + str(a.find('l')) + "]")

print("Usando la funcion split() para separar la frase {} ".format(c) + str(c.split(' ')) )

print("Usando join() para juntar # con {} ".format(c.split(' ')) + '#'.join(c.split(' ')) )

print("Usando partition() en la frase {} ".format(e) + str(e.partition("s")) )

print("\n--------------[Formateo de strings]--------------\n")
nombre = "Garou Estelar"
actividad = "perder con Saitama\n"
string_formateado = f"Hola, {nombre} ultimamente no deja de {actividad} "
print( "Uso del formateo de strings: " + string_formateado)

nombre_clase = "Mondongo"
codigo_python = "print('mondongo ssj3')"
# Esta plantilla contiene el programa en python mas simple que contenga el programa en java
# mas simple que contenga el programa en python mas simple 
plantilla = f""" 
            public class {nombre_clase}{{

                public static void main(String[] arg){{

                    System.out.println( "{codigo_python}" );

                }}

            }} """

print("Uso del formateo para crear plantillas:\n " + plantilla)

emails = ("a@gmail.com", "b@gmail.com" )
mensaje = {
    "sujeto":"Tienes un nuevo correo",
    "mensaje":"¡Hay un nuevo correo esperando a que lo abras!"
}

string_formateado = f""" 
De: <{emails[0]}>
Para: <{emails[1]}>
Sujeto: {mensaje['sujeto']}
{mensaje['mensaje']}\n """

print("String formateado utilizando tupla y diccionario: " + string_formateado)

mensaje['emails'] = emails
string_formateado = f""" 
De: <{mensaje['emails'][0]}>
Para: <{mensaje['emails'][1]}>
Sujeto: {mensaje['sujeto']}
{mensaje['mensaje']}\n """
print("String formateado utilizando un diccionario: " + string_formateado)

from ast import pattern
from math import prod

from mail_formateado import EMail
mail = EMail(emails[0],emails[1],mensaje["sujeto"],mensaje["mensaje"])
string_formateado = f""" 
De: <{mail.dir_desde}>
Para: <{mail.dir_para}>
Sujeto: {mail.sujeto}
{mail.mensaje()}\n """
print("String formateado utilizando una clase: " + string_formateado )

subtotal = 12.32
impuesto = subtotal * 0.07
total = subtotal + impuesto
# En el caso de hacer calculos matematicos con floats, como el total de una compra,
# pueden darse casos en el que de como resultado un num con indefinidos decimales
# *para hacer calculos realmente precisos deberiamos utilizar decimal.Decimal()*  
print("Sub: €{0} Imp: €{1} Total: {total} ".format(subtotal, impuesto, total = total) )

# Para evitar este caso podemos añadir mas informacion dentro de las llaves, como en el siguiente
# caso: en el 0.2f influyen varias cosas como el 0, para valores <1 se muestra un 0 a la izquierda del
# punto deciml, . para enseñar un punto decimal, n (2) para enseñar una cantidad n (2) de decimales 
# despues del punto, f como el valor de entrada (float en este caso)
print("Sub: €{0:0.2f} Imp: €{1:0.2f} Total: {total:0.2f} ".format(subtotal, impuesto, total = total) )

comanda = [("hamburgesa", 2, 5), ("patatas", 3.5, 1), ("refresco", 1.75, 3)]
print("PRODUCTO  CANTIDAD  PRECIO  SUBTOTAL ")
for producto, precio, cantidad in comanda:
    subtotal = precio * cantidad
    print( 
        # En este caso tenemos varias cosas interesantes en el string formateado
        # 10s (s: tipo string, 10: cantidad de caracteres que ocupara)
        # ^9d (d: tipo entero, 9: cantidad de caracteres que ocupara, ^: alineacion central)
        # <8.2f (f: tipo float, 8: cantidad de espacio caracteres, .: punto decimal, 2: cantidad de decimales, <: alineacion a la izq)
        # >7.2f (f: tipo float, 7: cantidad de espacio para caracteres, .: punto decimal, 2: cantidad de decimales, >: alineacion a la drch)
        f"{producto:10s}{cantidad:^9d}"
        f"€{precio:<8.2f}€{subtotal:>7.2f}"
    )

# Si se quieren añadir mas tipos de inputs, se pueden usar los siguientes:
# o(para octales), X(para hexadecimales), n(separadores de enteros), %(para crear porcentajes a partir de floats)


import datetime
print( "{:%Y-%m-%d %I:%M%p} ".format(datetime.datetime.now()))

print("\n--------------[Encoder y decoder]--------------\n")
# La b, como la f de los f-string, nos da a entender que estamos definiendo un byte, mientras que la x
# especifica que los siguientes dos caracteres van a representar un byte usando hexadecimales   
caracteres_bytes = b'\x63\x6c\x69\x63\x68\xe9'
# Este print renderiza los bytes a ASCII, mientras que el ultimo hexadecimal que escapa a ASCII
print("Caracteres en bytes: " + str(caracteres_bytes))
# Este print decodea y devuelve un string Unicode
print("Caracteres decodeados: " + caracteres_bytes.decode("latin-1"))
print("Caracteres decodeados sin especificar decoder: " + b'\x63\x6c\x69\x63\x68'.decode())


caracteres_unicode = "cliché"
print("'{}' transformado mediante diferentes encoders: ".format(caracteres_unicode) )
# Los tres primeros encodes mapean diferentes valores hexadecimales a los bytes con tilde
print("UTF-8 - " + str(caracteres_unicode.encode("UTF-8")))#b'clich\xc3\xa9'
print("latin-1 - " + str(caracteres_unicode.encode("latin-1")))#b'clich\xe9'
print("CP437 - " + str(caracteres_unicode.encode("CP437")))#b'clich\x82'
# Este ultimo encode no es capaz de mapear la tilde. Este metodo puede recibir un segundo argumento
# para manejar los caracteres que no se encuentren mappeados: 
# "strict" levantara expeciones cuando se desconozca el codigo hex, "repalce" lo reemplazara por un ?,
# "ignore" simplemente lo ignorara y xmlcharrefreplace crea una entidad xml representando el caracter unicode
print("ASCII - " + str(caracteres_unicode.encode("ascii","xmlcharrefreplace")))
print("Sin encoder especificado - " + str(caracteres_unicode.encode()))

print("\n--------------[Bytearray]--------------\n")

byte = bytearray(b"abcefghi")
byte[4:6] = b"\x15\xa3"
print("Objeto bytearray: " + str(byte))

byte2 = bytearray(b"abcdef")
byte2[3] = ord(b"g")
byte2[4] = 68
print("Objeto bytearray: " + str(byte2))

print("\n--------------[Expresiones regulares (REGEX)]--------------\n")

# Libreria de la que extraemos funciones de expresiones regulares
import re
lista_matches = [("hola mundo", "hola mundo"), ("hola mu","hola mundo" ),  
("hola mundo", "^hola mun$"), ("hola mun", "^hola mun$"), ("hola mu do", "^hola mu.do$"),
("hopa muxdo","ho[lp]a mu[nx]do"), ("hora muGdo","ho[a-z]a mu[a-zA-Z]do"),
("Free 2 play","[A-Z]ree [a-z0-9] play"), ("Tree b play","[A-Z]ree [a-z0-9] play"),
("0.05","0\.[0-9][0-9]"), (" f2","\s[a-s]\d"), ("hollllllla","hol*a"), ("hoa","hol*a"),
(" tn5","\s\w*[l-z]\d"), ("Que dise mi niño cohone.","[A-Z][a-z]* [a-z]+\.*"),("10.05","\d+\.\d+"),
("25.555","\d?\.\d+"),("ACABACABACAB","(ACAB){3}"),("Come mas verduras.","[A-Z][a-z]*( [a-z]+)*\.$")]
tiempo_empezar = datetime.datetime.now()
for string, patron in lista_matches:
    match = re.match(patron, string)

    if match:
        plantilla = "{}: '{}' coincide con el patron '{}' "

    else: 
        plantilla = "{}: '{}' no coincide con el patron '{}' "
    print(plantilla.format(datetime.datetime.now() - tiempo_empezar,string, patron))

patron = "^([a-zA-Z.]+)@([a-z.]*\.[a-z]+)$"
string_a_buscar = "algun.usuario@gmail.com"
match = re.match(patron,string_a_buscar)
if match:
    print("\nNombre y dominio de correo obtenido: " + match.groups()[0] + " : " + match.groups()[1])

print("\n")
print("Find all sin grupos: re.findall("'a.'", "'abcdefgh'")=" + str(re.findall("a.", "abcdefgh")))
print("Find all con un grupo: re.findall("'a(.)'", "'abcdefgh'")=" + str(re.findall("a(.)", "abcdefgh")))
print("Find all con dos grupos: re.findall("'(a)(.)'", "'abcdefgh'")=" + str(re.findall("(a)(.)", "abcdefgh")))
print("Find all con grupos anidados: re.findall("'((a)(.))'", "'abcdefgh'")=" +str(re.findall("((a)(.))", "abcdefgh")))

print("\n--------------[Caminos de Filesystem]--------------\n")
import os
camino = os.path.abspath(os.sep.join(['.', 'subdir','subsubdir','file.ext'] ))
print(camino)

import pathlib
camino_pathlib = (pathlib.Path(".") / "subdir" / "subsubdir" / "file.ext").absolute()
print(camino_pathlib)

def contar_lineas_codigo(dir_path):
    # Variable con la que llevaremos cuenta de las lineas de codigo
    # lcf (lineas codigo fuente) 
    lcf = 0
    # Gracias al metodo iterdir() iteramos todos los diferentes directorios que haya 
    for camino in dir_path.iterdir():
        # Si el directorio empieza con "." se pasa al siguiente
        if camino.name.startswith("."):
            continue
        # Si se encuentra otro posible directorio se vuelve a llamar a la funcion 
        if os.path.isdir(camino):
            lcf += contar_lineas_codigo(camino)
            continue
        # Si no acaba con ".py" se pasa al siguiente
        if camino.suffix != ".py":
            continue
        # Aprovechando la sintaxis with, abrimos el archivo y separamos las lineas de este en una
        # lista y contabilizamos todas aquellas que no empiezan con # (lineas comentadas) 
        with camino.open() as archivo:
            for linea in archivo:
                lineas = linea.split("\n")
                for linea in lineas:
                    if linea and not linea.startswith("#"):
                        lcf += 1

    return lcf

# Asignamos a esta variable el path del directorio actual, para que empieze a revisar
camino_raiz = pathlib.Path(".")
#print(f"Hay {contar_lineas_codigo(camino_raiz)} lineas de codigo")

print("\n--------------[Serializacion de objetos]--------------\n")

import pickle
informacion_serializable = ["una lista", "conteniendo", 5, "valores incluyendo otra lista",["lista","interior"] ]

# Crea un archivo con la lista anterior
with open("archivo_pickle", 'wb') as archivo:
    pickle.dump(informacion_serializable, archivo)

# Carga la lista del archivo que hemos creado
with open("archivo_pickle", 'rb') as archivo:
    informacion_cargada = pickle.load(archivo)

print("Informacion cargada mediante libreria pickle: " + str(informacion_cargada))
assert informacion_cargada == informacion_serializable

from refrescar_enlace import EnlaceRefrescado
er = EnlaceRefrescado("https://www.wordreference.com")

#er_serial = pickle.dumps(er)
#er_serial = pickle.loads(er_serial)

print("\n--------------[Caso de uso (escritura de archivos HTML dinamica)]--------------\n")
from ejemplo_tarea.manejador_plantillas import MotorPlantillas

motor = MotorPlantillas("ejemplo_tarea/index.html", "ejemplo_tarea/generado.html","ejemplo_tarea/parse_text.json")
motor.procesar()