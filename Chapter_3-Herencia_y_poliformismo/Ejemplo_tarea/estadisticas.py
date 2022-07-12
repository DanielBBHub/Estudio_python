from Ejemplo_tarea.abstract import Tarea

#Clase con tarea para obtener la media de un vector de numeros
class Estadisticas(Tarea):
    def leccion(self):
        return (
            "Buen trabajo, "
            + self.nombre_estudiante
            + ". Ahora calcula la media de los siguientes numeros"
            + "1, 5, 18, -3 y asigna el resultado a la variable 'mediana' "
        )

    def comprobar_codigo(self, code):
        import statistics
        code = "import statistics\n " + code

        variables_locales = {}
        variables_globales = {}
        exec(code, variables_globales, variables_locales)

        return variables_locales.get("mediana") == statistics.mean([1, 5, 18, -3])