import uuid
from Ejemplo_tarea.abstract import Tarea
from Ejemplo_tarea.corrector import CorrectorTarea

#Clase para manejar las tareas que puede hacer un estudiante
class Calificador:
    # Creamos dos diccionarios para guardar las tareas y los estudiantes
    def __init__(self):
        self.calificadores_estudiantes = {}
        self.calificadores_tarea = {}

    # Creamos un metodo que recibe una clase 'tarea' por parametro
    def registro(self, tarea):
        # Comprobamos que la clase que se ha recibido sea una subclase de la nuestra 'Tarea' 
        if not issubclass(tarea, Tarea):
            raise RuntimeError( "Tu clase no tiene los metodos necesarios" )

        # Generamos un uuid (Universally unique identifier), el cual representa un numero 
        # random extremadamente largo, con el objetivo de evitar coincidencias con otros IDs
        id = uuid.uuid4()
        # Utilizamos el ID generado para indexar las clases recibidas
        self.calificadores_tarea[id] = tarea
        # Devolvemos el ID generado
        return id

    def empezar_tarea(self, estudiante, id):
        self.calificadores_estudiantes[estudiante] = CorrectorTarea(estudiante, 
        self.calificadores_tarea[id])

    def obtener_tarea(self, estudiante):
        tarea = self.calificadores_estudiantes[estudiante]
        return tarea.leccion()

    def comprobar_tarea(self, estudiante, code):
        tarea = self.calificadores_estudiantes[estudiante]
        return tarea.comprobar_codigo(code)

    def resumen(self, estudiante):
        clasificador = self.calificadores_estudiantes[estudiante]
        return f"""
        {estudiante} ha realizado los siguientes intentos en la siguiente tarea:

        intentos: {clasificador.intentos}
        correctos: {clasificador.aciertos}
        superados: {clasificador.aciertos > 0}
        """
