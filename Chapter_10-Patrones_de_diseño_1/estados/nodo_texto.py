from estados import nodo_hijo
class NodoTexto:
    # El objetivo de este estado es recoger el texto que exista entre los tags de apertura y
    # de cierre 
    def procesar(self, resto_string, parser):
        # Se recoge el indice de cuando empieza el tag de cerrar
        i_comienzo_tag = resto_string.find("<")
        # Se desempaqueta el texto que haya previo al tag de cerrar
        texto = resto_string[: i_comienzo_tag ]
        # Se asigna el texto obtenido al nodo actual
        parser.nodo_actual.texto = texto
        # Se devuelve el estado a "NodoHijo"
        parser.estado = nodo_hijo.NodoHijo()
        return resto_string[i_comienzo_tag:]
        