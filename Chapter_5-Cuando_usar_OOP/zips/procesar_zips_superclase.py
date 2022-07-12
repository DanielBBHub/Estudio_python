import sys
import shutil
import zipfile
from pathlib import Path

class ProcesadorZip:
    """ Creamos una clase para preocuparnos del procesado de zips en general """

    def __init__(self, nombre_zip):
        self.nombre_zip = nombre_zip
        self.directorio_temp = Path(f"unzipped-{nombre_zip[:-4]}")

    # Funcion para llamar a la funcionalidad completa del objeto
    def procesar_zip(self):
        self.extraer_archivos()
        self.procesar_archivos()
        self.comprimir_archivos()

    # Funcion que se ocupara de la extraccion del archivo zip
    def extraer_archivos(self):
        # Se crea un archivo temporal en el que guardar el archivo que vaya a crearse
        self.directorio_temp.mkdir()

        # Con el zip en cuestion ubicado, se vierte el contenido de este dentro del 
        # nuevo directorio que se ha creado
        with zipfile.ZipFile(self.nombre_zip) as zip:
            print("Entrando a: {}".format(self.nombre_zip))
            zip.extractall(self.directorio_temp)

    # Funcion que comprimira de nuevo el archivo modificado
    def comprimir_archivos(self):
        with zipfile.ZipFile(self.nombre_zip,"w") as file:
            
            for nombre_archivo in self.directorio_temp.iterdir():
                print("Comprimiendo: {}".format(nombre_archivo))
                file.write(nombre_archivo, nombre_archivo.name)
        # Eliminar un directorio en base a una direccion: (self.directorio_temp)
        shutil.rmtree(self.directorio_temp)

# Con estas dos lineas implementamos la funcionalidad de ejecutar la funcionalidad desde la consola del interpretador 
if __name__ == "__main__":
    ProcesadorZip(*sys.argv[1:4]).procesar_zip
