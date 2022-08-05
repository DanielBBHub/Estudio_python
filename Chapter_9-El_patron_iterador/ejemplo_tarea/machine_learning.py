from collections import Counter
import csv
from random import randint


archivo_dataset = 'ejemplo_tarea/colors.csv'
dataset_alternativo = 'ejemplo_tarea/colors2.csv'


def hex_a_rgb(hex_color):
    # Se recogen los nums hexadecimales y se transforman a una tupla con los nums rgb correspondientes
    # Esta expresion generadora devuelve tres indices mediante la llamada a range() (1, 3, 5), que seran  
    # los indices de las posiciones que queramos convertir, sin importarnos el indice 0 ya que sera una #
    # Para cada uno de los tres valores de la tupla obtendra tres parejas del hex entre i - i+2 
    # (PJ: #12abfe -> 1:12 3:ab 5:fe). Despues se convertiran a enteros debido al casteo con int(). El 16 como
    # segundo argumento en esta llamada indica que utilicemos base 16 (hexadecimal) para la conversion     
    return tuple(int(hex_color[i : i + 2], 16) for i in range(1, 6, 2))

def cargar_colores(archivo):
    with open(archivo) as dataset:
        # El metodo reader() del objeto csv devuelve un iterador sobre las
        # lineas del archivo.  
        lineas = csv.reader(dataset)
        for linea in lineas:
            # Los valores devueltos por el iterador son una lista de strings con el
            # nombre del color y el num hexadecimal que lo representa (PJ: ["Green", "#6edd13"])
            etiqueta, color_hex = linea
            # Se devuelve una tupla con el color en rgb y el nombre de este con la sintaxis yield
            yield (hex_a_rgb(color_hex), etiqueta)

def generar_colores(contador = 100):
    for i in range(contador):
        yield (randint(0, 255), randint(0, 255), randint(0,255))

def calcular_distancia_colores(color1, color2):
    # zip() es una funcion "built-in" que nos ayuda con la iteracion paralela de objetos. Este metodo
    # recibe iterables (tuplas de RBG) y devuelve un iterador con tuplas de cada uno de los iterables
    # ( en este caso devolveria esta lista [(r1,r2), (g1,g2), (b1,b2)])    
    canales = zip(color1, color2)
    cuadrado_distancia = 0
    for c1, c2 in canales:
        cuadrado_distancia = (c1-c2) ** 2
    return cuadrado_distancia

def vecino_mas_proximo(colores_modelo, colores_objetivo, num_vecinos=5):
    # Se cargan los colores modelo (el dataset) en una lista para no andar cargandolos continuamente
    colores_modelo = list(colores_modelo)
    # La variable colores_objetivo es el producto de la funcion generadora "generar_colores()"
    for objetivo in colores_objetivo:
        # La expresion generadora llama a calcular_distancia_colores(), realizando el calculo para cada uno de 
        # los colores (en colores_modelo) y su objetivo. Calculada la distancia se mete en una tupla con el color en
        # cuestion y se ordena mediante sorted() por su primer elemento (las distancias), para luego ser devuelto el
        # objetivo y las vecinos mas proximos (los 5 primeros) por un yield  
        colores_mas_cercanos = sorted(
            ((calcular_distancia_colores(color[0], objetivo), color) for color in colores_modelo)
        )
        yield objetivo, colores_mas_cercanos[:5]

def nombrar_colores(colores_modelo, colores_objetivo, num_vecinos=5):
    # Se crea otro generador para continuar la cadena. Este desempaquetara la tupla recibida en la tupla del
    # color objetivo y 5 vecinos mas proximos 
    for objetivo, vecino_cercano in vecino_mas_proximo(colores_modelo, colores_objetivo, num_vecinos=5):
        print(objetivo," : " ,vecino_cercano)
        # Utilizamos el objeto counter para ordenar de manera descendiente los nombres de los vecinos mas 
        # cercanos al color objetivo 
        suposicion_nombre = Counter(cercano[1] for cercano in vecino_cercano).most_common()[0][0]
        # El yield devolvera un resultado tal que: (91, 158, 250), "Azul"
        yield objetivo, suposicion_nombre

def escribir_resultados(colores, archivo_res = "nombre_colores_generado.csv"):
    with open(archivo_res, 'w') as archivo_res:
        # Se define un objeto que nos ayude a escribir en el archivo generado con el formato de 
        # valores separados por comas (CSV)
        escritor_csv = csv.writer(archivo_res)
        for (r, g, b), nombre in colores:
            escritor_csv.writerow([nombre, f"#{r:02x}{g:02x}{b:02x}"])

def procesar_colores(dataset=dataset_alternativo):
    modelo_colores = cargar_colores(dataset)
    colores = nombrar_colores(modelo_colores, generar_colores(), 5)
    escribir_resultados(colores)