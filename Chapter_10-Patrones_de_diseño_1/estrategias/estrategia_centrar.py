from PIL import Image

class EstrategiaCentrar:
    def hacer_fondo(self, img, tamaño_escritorio):
        imagen_entrada = Image.open(img)
        imagen_salida = Image.new("RGB", tamaño_escritorio)
        izq = (imagen_salida.size[0] - imagen_entrada.size[0]) // 2
        arriba = (imagen_salida.size[1] - imagen_entrada.size[1]) // 2
        imagen_salida.paste(
            imagen_entrada,
            (izq, arriba, izq + imagen_entrada.size[0], arriba + imagen_entrada.size[1]),
        )
        return imagen_salida