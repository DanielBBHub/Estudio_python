#Contener una lista con los contactos 
class ContactList(list):

    def buscar(self, name):
        "Devolver los contactos que coincidad con el name introducido"

        #Comprehension para introducir los contactos que coincidan con el nombre en la lista de contactos
        contactos_res = [ contact for contact in self
            if name in contact.name]
        return contactos_res

class Contact: 
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        #Asignamos el nombre y el mail a la variable de la clase, creando una unica instancia
        Contact.all_contacts.append(self)


#Creamos una clase que nos permita guardar un tlf en caso de que sea un amigo cercano
#-----------------¡¡Override!!---------------
class Friend(Contact):
    def __init__(self, name, email, phone):
        #De la siguiente manera añadiremos el contacto de un amigo a la lista 
        # que hay en el objeto contact de la que hereda
        super.__init__(name, email)
        self.phone = phone