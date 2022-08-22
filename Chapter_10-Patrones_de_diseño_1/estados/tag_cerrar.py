from estados import nodo_hijo
class TagCerrar:
    def procesar(self, resto_string, parser):
        # Se localiza el principio y el final del tag que se cierra y 
        # se recogen los indices
        i_comienzo_tag = resto_string.find("<")
        i_final_tag = resto_string.find(">")
        # Con este assert se quiere comprobar que es consistente el string,
        # es decir, que la segunda posicion cuente con la barra  
        assert resto_string[i_comienzo_tag + 1] == "/"
        # Se extrae el nombe del tag
        tag = resto_string[i_comienzo_tag + 2 : i_final_tag]
        tag = tag.capitalize()
        # Con este segundo assert se comprueba que este tag que se ha obtenido y
        # el tag previamente obtenido en TagAbrir son el mismo 
        assert tag == parser.nodo_actual.tag
        # Se reestablece el nodo anterior (el padre) para posibilitar añadir mas
        # hijos en el camino
        parser.nodo_actual = parser.nodo_actual.padre
        # Se vuelve al estado "NodoHijo"
        parser.estado = nodo_hijo.NodoHijo()
        return resto_string[i_final_tag +1:].strip()