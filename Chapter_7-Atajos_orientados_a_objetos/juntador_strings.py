# Declaracion de una clase para demostrar la personalizacion de __enter__ y __exit__
class JuntarStrings(list):
   # Dentro de esta funcion podemos declarar cualquier funcionalidad de preparacion para el objeto,
   # en este caso ninguna, antes de que este devuelva el objeto que sera asignado a "juntador" 
   def __enter__(self):
      return self
   # Dentro de esta funcion podemos declarar cualquier funcionalidad que queramos ejecutar una vez el
   # codigo que haya dentro de la sintaxis with haya terminado de ejecutarse. En este caso asignara
   # un string concatenado a la variable self.res
   def __exit__(self, tipo, valor, traceback):
      self.res = "".join(self)
