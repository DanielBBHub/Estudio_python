
#Clase con tarea para crear un codigo simple con dos variables (int, string)
class IntroduccionPython:
    def leccion(self):
        return f"""
        Hola, {self.nombre_estudiante}. Define dos variables, un entero a con valor '1' 
        y un string b con valor 'hola'
        """

    def comprobar_codigo(self, code):
        return code == "a = 1\n b ='hola'"