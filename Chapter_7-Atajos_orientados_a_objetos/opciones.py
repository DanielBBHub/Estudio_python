class Opciones:
   # Se declara un diccionario con las opciones por defecto para la clase
   opciones_por_defecto = {
      'puerto':21,
      'host':'localhost',
      'usuario':None,
      'contrasenya':None,
      'debug':False
   }
   
   def __init__(self, **argumento_kw):
      """  En el constructor se asignara al diccionario opciones el que se ha declarado previamente
       con lo que no se quedara nunca vacio. Si en el momento de instanciar el objeto se quiere especificar
       las opciones del mismo, se actualizara el diccionario con los argumentos introducidos arbitrariamente
       como palabras clave """
      #self.opciones = dict(Opciones.opciones_por_defecto)
      #self.opciones.update(argumento_kw)

      # Otra forma de rellenar el diccionario de opciones sera mediante el desempaquetado de argumentos.
      # como se de desempaquetan de izq a drch, se rellenara el diccionario con las opciones por defecto
      # y, si ha habido algun cambio se actualizara con el diccionario que se ha recogido como argumento del
      # constructor  
      self.opciones = {**Opciones.opciones_por_defecto, **argumento_kw }

   def __getitem__(self, key):
      return self.opciones[key]