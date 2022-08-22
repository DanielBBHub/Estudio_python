from PIL import Image

class EstrategiaEscalado:
    def hacer_fondo(self, img, tamaño_escritorio):
        imagen_entrada = Image.open(img)
        imagen_salida = imagen_entrada.resize(tamaño_escritorio)
        return imagen_salida
        