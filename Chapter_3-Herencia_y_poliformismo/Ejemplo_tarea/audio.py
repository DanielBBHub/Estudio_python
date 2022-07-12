class Audio:
    def __init__(self, filename):
        # Usamos el polimorfismo para acceder al valor de "ext" de las subclases
        if not filename.endswith(self.ext):
            raise Exception("Formato invalido")
        
        self.filename = filename


class MP3(Audio):
    ext = "mp3"

    def play(self):
        print("Reproduciendo el archivo {} ".format(self.filename))

class Wav(Audio):
    ext = "wav"

    def play(self):
        print("Reproduciendo el archivo {} ".format(self.filename))

class Ogg(Audio):
    ext = "ogg"

    def play(self):
        print("Reproduciendo el archivo {} ".format(self.filename))


class Flac:
    def __init__(self, filename):
        # Usamos el polimorfismo para acceder al valor de "ext" de las subclases
        if not filename.endswith(".flac"):
            raise Exception("Formato invalido")
        
        self.filename = filename
        
        def play(self):
            print("Reproduciendo el archivo {} ".format(self.filename))