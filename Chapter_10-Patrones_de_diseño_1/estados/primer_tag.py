from estados import nodos
from estados import nodo_hijo

class PrimerTag:
    # El objetivo de este estado es devolver el string del archivo xml desde un punto 
    # en el que ya se haya procesado el primer tag
    def procesar(self, resto_string, parser):
        i_comienzo_tag = resto_string.find("<")
        i_final_tag = resto_string.find(">")
        # Se extrae el nombe del tag
        tag = resto_string[i_comienzo_tag + 1 : i_final_tag].capitalize()
        # Se asigna al nodo raiz del parser
        raiz = nodos.Nodo(tag)
        # Se asigna el nodo tambien a la raiz del parser
        parser.raiz = parser.nodo_actual = raiz
        # Se cambia de estado del parser al de NodoHijo
        parser.estado = nodo_hijo.NodoHijo()
        return resto_string[i_final_tag + 1 : ]