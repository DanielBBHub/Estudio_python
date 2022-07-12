from urllib.request import urlopen, Request

class WebPage:
    def __init__(self, link):
        self.url = link
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Recogiendo una nueva pagina")
            # Esta linea es para añadir a la peticion un "user-agent", para que 
            # el buscador no rechaze la conexion por script
            req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
            # Llamamos a "urlopen()" para abrir y leer el link introducido
            self._content = urlopen(req).read()
        return self._content