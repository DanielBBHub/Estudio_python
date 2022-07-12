from Ejemplo_tarea.calificador_notas import Calificador
from Ejemplo_tarea.estadisticas import Estadisticas
from Ejemplo_tarea.tarea_introduccion import IntroduccionPython
import statistics

calificador = Calificador()
itp_id = calificador.registro(IntroduccionPython)
stat_id = calificador.registro(Estadisticas)

calificador.empezar_tarea("Daniel", itp_id)

print("Leccion de Daniel: ", calificador.obtener_tarea("Daniel"))

print("Comprobacion de Daniel: ",
    calificador.comprobar_tarea("Daniel", "a=1 ; b='hola'"),)

print("Comprobacion segunda de Daniel: ",
    calificador.comprobar_tarea("Daniel", "a = 1\n b ='hola'"),)

print(calificador.resumen("Daniel"))

calificador.empezar_tarea("Daniel", stat_id   )

print("Leccion de Daniel: ", calificador.obtener_tarea("Daniel"))

print("Comprobacion de Daniel: ",
    calificador.comprobar_tarea("Daniel", "mediana=5.25"))

print("Comprobacion segunda de Daniel: ",
    calificador.comprobar_tarea("Daniel", "mediana=statistics.mean([1, 5, 18, -3])"),)

print(calificador.resumen("Daniel"))                                                         