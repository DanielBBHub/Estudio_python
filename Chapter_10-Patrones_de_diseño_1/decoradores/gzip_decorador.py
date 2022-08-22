import gzip
import imp
from io import BytesIO

class GzipSocket:

    def __init__(self, socket):
        self.socket = socket

    def send(self, datos):
        buf = BytesIO()
        archivo_zip = gzip.GzipFile(fileobj=buf, mode='w')
        archivo_zip.write(datos)
        archivo_zip.close()
        self.socket.send(buf.getvalue())

    def close(self):
        self.socket.close()

    