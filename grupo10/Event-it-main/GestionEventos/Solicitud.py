import datetime


class Solicitud():
    def __init__(self,CUILSender,CUILReceiver, NombreEvento):
        self.CUILSender = CUILSender
        self.CUILReceiver = CUILReceiver
        self.NombreEvento = NombreEvento
        self.fechaDeEnvio = datetime.datetime.now()

    def solicitudAEscrbir(self):
        return [str(self.CUILSender), str(self.CUILReceiver), str(self.NombreEvento), str(self.fechaDeEnvio)]