class LogDecorador:
    def __init__(self, socket):
        self.socket = socket

    def send(self, datos):
        print(
            "Enviando {0} a {1}".format(datos, self.socket.getpeername()[0])
        )
        self.socket.send(datos)

    def close(self):
        self.socket.close()