import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 2401))
print("Recibido: {0}".format(cliente.recv(1024)))
cliente.close()