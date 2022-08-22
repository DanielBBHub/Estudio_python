from PIL import Image

class EstrategiaBaldosa:

    def hacer_fondo(self, img, tamaño_escritorio):
        imagen_entrada = Image.open(img)
        imagen_salida = Image.new("RGB", tamaño_escritorio)
        num_baldosas = [
            o // i + 1 for o, i in zip(imagen_salida.size, imagen_entrada.size)
        ]
        for x in range(num_baldosas[0]):
            for y in range(num_baldosas[1]):
                imagen_salida.paste(
                    imagen_entrada,
                    (
                        imagen_entrada.size[0] * x,
                        imagen_entrada.size[1] * y,
                        imagen_entrada.size[0] * (x + 1),
                        imagen_entrada.size[1] * (y + 1)
                    ),
                )
        return imagen_salida