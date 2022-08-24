class Guardar:
    def __init__(self, documento):
        self.documento = documento

    def execute(self):
        self.document.save()