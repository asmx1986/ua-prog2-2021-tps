class Contactos:
    def __init__(self):
        """Solicitudes recibidas y invitaciones enviadas"""
        self.enviadas = []
        self.recibidas = []
        self.bff = []

    def getEnviadas(self):
        return self.enviadas

    def getRecibidas(self):
        return self.recibidas

    def getAmigos(self):
        return self.bff

    def setRecibidas(self,contacto):
        print( "Contactos setRecibidas agrega a", contacto )
        self.recibidas.append(contacto)

    def setEnviadas(self,contacto):
        print( "Contactos setEnviadas agrega a", contacto )
        self.enviadas.append(contacto)

    def removeEnviadas(self,contactos):
        print( "Contactos removeEnviadas a", contactos )
        self.enviadas.remove(contactos)

    def removeRecibidas(self,contacto):
        print( "Contactos removeRecibidas de", contacto )
        self.recibidas.remove(contacto)
