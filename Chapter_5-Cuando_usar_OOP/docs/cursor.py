
class Cursor:
    def __init__(self, doc):
        self.doc = doc
        self.pos = 0

    def forward(self):
        self.pos += 1

    def back(self):
        self.pos -= 1

    def home(self):
        while self.doc.caracteres[self.pos - 1].caracter != "\n":
            self.pos -= 1
            
            if self.pos == 0:
                break
        print("Pos despues de home(): " + str(self.pos))

    def end(self):
        while(self.pos < len(self.doc.caracteres) and self.doc.caracteres[self.pos].caracter != "\n"):
            self.pos += 1

        print("Pos despues de end(): " + str(self.pos))