import imp
from importlib.resources import path
from unittest.mock import patch
from urllib.request import Request, urlopen
from urllib.parse import urlparse

class RecolectorDeLinks:
    def __init__(self, url):
        # La url se formara con el protocolo HTTP combinado con la parte netloc de la direccion 
        # web que se le ha pasado
        self.url = "http://" + urlparse(url).netloc

        # Declaramos un diccionario donde guardaremos una relacion de pagina visitada - links recogidos
        self.links_recogidos = {}

        # Declaramos un set para guardar las llaves para el diccionario de enlaces recogidos
        self.links_visitados = set()

        
    def recoger_links(self, path="/"):
        # Se compone la url completa con la que se va a realizar la peticion combinando la url que 
        # se ha formado en el  __init__() y el path introducido como argumento
        url_completa = self.url + path

        # Se crea un objeto "Request()" para poder acceder a todas las paginas web sin ningun 
        # problema *a veces el servidor deniega la conexion al intentar acceder a el mediante el 
        # modulo urllib.request, con lo que has de añadirle una cabecera*  
        peticion = Request(url_completa, headers={'User-Agent': 'Mozilla/5.0'})
        self.links_visitados.add(url_completa)

        # Se realiza la peticion al servidor HTTP y se guarda la pagina como un solo string dentro de 
        # la variable "pagina" 
        pagina = str(urlopen(peticion).read())
        # Separamos el string que hemos guardado y transformamos la variable de str a una lista, en la que 
        # guardaremos las cadenas separadas por cada dobles comillas que haya en esta  
        pagina = pagina.split('"')
        links = []

        # Recorremos la lista que hemos creado en base a la pagina para recoger toda cadena que este terminada en
        # .html o en .com para guardar todos los enlaces posibles con ese formato 
        for link in pagina:
            if link.__contains__('.html') or link.__contains__('.com'):
                # En el caso de que el string las contenga la añadimos a la lista de enlaces
                links.append(link)

        # Normalizamos los enlaces recibidos con comprehension llamando a nuestra funcion "normalizar_urls()"
        links = {self.normalizar_urls(path, link) for link in links}
        # Guardamos los enlaces recogidos en la pagina, con forma de tupla, en base al enlace
        # recibido para la peticion
        self.links_recogidos[url_completa] = links

        # Recorremos la lista de enlaces y creamos por defecto indices en el diccionario de enlaces recogidos
        # con los enlaces visitados y un set() con los enlaces recogidos de este que hemos visitado 
        for link in links:
            self.links_recogidos.setdefault(link, set())

        # Se discierne entre los enlaces que hemos recogido y aquellos que no hemos visitado mediante una 
        # diferencia de sets
        links_no_visitados = links.difference(self.links_visitados)
        print(links_no_visitados)

        # Se declara un bucle para crear peticiones recursivamente llamando a la funcion "recoger_links()" en 
        # base a los links que no hemos visitado aun 
        for link in links_no_visitados:
            if link.startswith(self.url):
                print("Link a recoger: " + link )
                self.recoger_links(urlparse(link).path)
      
        print("Enlaces recogidos: " + str(self.links_recogidos) + "\n")
        print("Enlaces visitados: " + str(self.links_visitados) + "\n")             


    def normalizar_urls(self, path, link):
        if link.startswith("http://"):
            return link

        elif link.startswith("https://"):
            return link

        elif link.startswith("/"):
            return path + link

        else:
            return self.url + path.rpartition('/')[0] + '/' + link

    