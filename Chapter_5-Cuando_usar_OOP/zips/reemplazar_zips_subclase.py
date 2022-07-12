import sys
import shutil
import zipfile
from pathlib import Path
from zips.procesar_zips_superclase import ProcesadorZip

class ReemplazadorZip(ProcesadorZip):
    """ Creamos una clase para preocuparnos del reemplazo de arhchivos de texto a primer nivel en archivos
    comprimidos en zip """

    def __init__(self, nombre_archivo, string_busqueda, string_intercambiar):
        super().__init__(nombre_archivo) 
        self.buscar = string_busqueda
        self.reemplazar = string_intercambiar

    # Funcion que revisara los archivos que haya en el directorio temporal
    def procesar_archivos(self):
        """ Realiza una busqueda entre los archivos descomprimidos de un zip
        e intercambia el contenido de self.buscar por el de self.reemplazar """
        # Para cada archivo que haya dentro del directorio
        for nombre_archivo in self.directorio_temp.iterdir():
            with nombre_archivo.open() as file:
                # Se lee el contenido y se almacena en una variable
                print("Leyendo: {}".format(nombre_archivo))
                contenidos = file.read()
            
            # Se reemplaza el contenido con "replace()", pasandole el string que se quiere cambiar 
            # y el string con el que se quiere reemplazar
            contenidos = contenidos.replace(self.buscar, self.reemplazar)

            # Finalmente se escribe en un archivo los nuevos contenidos
            with nombre_archivo.open("w") as file:
                nombre_archivo.write_text(contenidos)

# Con estas dos lineas implementamos la funcionalidad de ejecutar la funcionalidad desde la consola del interpretador 
if __name__ == "__main__":
    ProcesadorZip(*sys.argv[1:4]).procesar_zip
