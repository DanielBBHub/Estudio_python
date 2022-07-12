from collections.abc import Container
from Ejemplo_tarea.contact import Contact
from Ejemplo_tarea.supplier import Suplier
from Ejemplo_tarea.audio import MP3, Ogg
from Ejemplo_tarea.abstract import OddContainer

#Creamos un objeto con cada clase que hemos creado
c = Contact("Antonio Orozco", "antonio@gmail.com")
s = Suplier("David Bisbal", "david_bisbal@gmail.com")

#Comprobamos que se ha guardado la informacion
""" print(c.name + " : " + c.email)
print(s.name + " : " + s.email)
 """

#Ejecutamos el metodo order de la clase Suplier
""" s.order("Tomatico con macarrones")
 """
#Creamos dos contactos mas con nombres parecidos
c2 = Contact("Antonio Orozco 2", "antonio2@gmail.com")
c3 = Contact("Antonio Orozco 3", "antonio3@gmail.com")

""" res = Contact.all_contacts.buscar("Antonio")
for r in res:
    print("Contacto: ")
    print(r.name) """


mp3 = MP3("mi_archivo.mp3")
ogg = Ogg("mi_archivo.ogg")

""" mp3.play()
ogg.play() """

#Creamos un objeto de la clase abstracta OddContainer
odd_container = OddContainer()

""" print("Instancia: " + str(isinstance(odd_container, Container)))
print("Subclase: " + str(issubclass(OddContainer, Container)))

print("Comprobacion de __contains__: " )
print( 1 in odd_container)
print(2 in odd_container) """

