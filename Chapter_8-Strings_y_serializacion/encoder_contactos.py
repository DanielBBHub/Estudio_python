import json
import contacto
class EncoderContactos(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, contacto.Contacto):
            return {
                "es_contacto": True,
                "nombre":obj.nombre,
                "apellido":obj.apellido,
                "nombre_completo": obj.nombre_completo
            }
        return super().default(obj)