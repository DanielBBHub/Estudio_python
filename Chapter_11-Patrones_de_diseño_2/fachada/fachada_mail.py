import smtplib
import imaplib

class FachadaMail:
    def __init__(self, host, usuario, passw):
        self.host = host
        self.usuario = usuario
        self.passw = passw

    def enviar_mail(self, hacia, sujeto, mensaje):
        if not "@" in self.usuario:
            desde_mail = "{0}@{1}".format(self.usuario, self.host)
        else:
            desde_mail = self.usuario
        
        mensaje = (
            "Desde: {0}\r\n" "Para: {1}\r\n " "Sujeto: {2}\r\n\r\n{3} ".format(desde_mail, hacia, sujeto, mensaje)
        )
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.usuario, self.passw)
        smtp.sendmail(desde_mail, [hacia], mensaje)

    def get_mensajes(self):
        entrada = imaplib.IMAP4(self.host)
        entrada.login(
            bytes(self.usuario, "utf-8"), bytes(self.passw, "utf-8")
            )
        entrada.select()
        x, info = entrada.search(None, "All")
        mensajes = []
        for num in info[0].split():
            x, mensaje = entrada.fetch(num, "(RFC822)")
            mensajes.append(mensaje[0][1])
        return mensajes