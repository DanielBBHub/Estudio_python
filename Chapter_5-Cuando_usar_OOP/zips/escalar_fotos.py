from PIL import Image
import sys
from procesar_zips_superclase import ProcesadorZip

class EscalarImagenesEnZip(ProcesadorZip):
    def procesar_archivos(self):
        """ Escalar todas las imagenes a un tamaño de 640x480 """
        for nombre_archivo in self.directorio_temp.iterdir():
            imagen = Image.open(str(nombre_archivo))
            escalado = imagen.resize((640,480))
            escalado.save(nombre_archivo)

# Con estas dos lineas implementamos la funcionalidad de ejecutar la funcionalidad desde la consola del interpretador 
if __name__ == "__main__":
    ProcesadorZip(*sys.argv[1:4]).procesar_zip