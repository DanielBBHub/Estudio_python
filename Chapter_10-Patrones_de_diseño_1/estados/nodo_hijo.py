from estados import nodo_texto, tag_abrir, tag_cerrar

class NodoHijo:
    # Como hemos dicho, este nodo hijo servira para pasar entre estados, 
    # esto se hara dependiendo del principio del string que reciba
    def procesar(self, resto_string, parser):
        desmontado = resto_string.strip()
        # En el caso de que el string que recibamos comience de esta manera significara
        # que es la parte que cierra el tag (PJ: <\html>) 
        if desmontado.startswith("</"):
            parser.estado = tag_cerrar.TagCerrar()
        # En el caso de que el string que recibamos comience de esta manera significara
        # que es la parte que abre el tag (PJ: <html>) 
        elif desmontado.startswith("<"):
            parser.estado = tag_abrir.TagAbrir()
        # En el caso de que no comience de ninguna de las maneras anteriores
        # significara que lo que hay en esta parte del string es solo texto 
        else:
            parser.estado = nodo_texto.NodoTexto()
        
        return desmontado