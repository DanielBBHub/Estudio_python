#Clase para monitorizar el numero de intentos del usuario
class CorrectorTarea:
    def __init__(self, estudiante, ClaseTarea):
        self.tarea = ClaseTarea()
        self.tarea.nombre_estudiante = estudiante
        self.intentos = 0
        self.aciertos = 0
        
    def comprobar_codigo(self, code):
        self.intentos += 1
        res = self.tarea.comprobar_codigo(code)
        if res:
            self.aciertos += 1

        return res

    def leccion(self):
        return self.tarea.leccion()