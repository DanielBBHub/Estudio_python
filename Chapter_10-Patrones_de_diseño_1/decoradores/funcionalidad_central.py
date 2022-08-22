import socket
from decoradores.log_decorador import LogDecorador
from decoradores.gzip_decorador import GzipSocket

def responder(cliente):
    respuesta = input("Introduzca un valor: ")
    cliente.send(bytes(respuesta, "utf-8"))
    cliente.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2401))
server.listen(1)
try:
    while True:
        cliente, direc = server.accept()
        responder(LogDecorador(cliente))

finally:
    server.close()