from estados import nodos, nodo_hijo
class TagAbrir:
    def procesar(self, resto_string, parser):
        # Se localiza el principio y el final del tag de apertura y 
        # se recogen los indices
        i_comienzo_tag = resto_string.find("<")
        i_final_tag = resto_string.find(">")
        # Se recoge el tag que se esta leyendo desmepaquetandolo en 
        # base a los indices que se han obtenido 
        tag = resto_string[i_comienzo_tag + 1 : i_final_tag]
        tag = tag.capitalize()
        # Se instancia un nodo, al que se le pasa el tag recogido y el nodo 
        # actual del parser para que apunte a el como su padre
        nodo = nodos.Nodo(tag, parser.nodo_actual)
        # Se añade a la lista de hijos el nodo recien creado
        parser.nodo_actual.hijos.append(nodo)
        # Y se apunta como el ultimo nodo que se ha usado para el parser
        parser.nodo_actual = nodo
        # Se vuelve al estado "NodoHijo"
        parser.estado = nodo_hijo.NodoHijo()
        # Finalmente se devuelve el resto del string sin tratar
        return resto_string[i_final_tag +1:]
