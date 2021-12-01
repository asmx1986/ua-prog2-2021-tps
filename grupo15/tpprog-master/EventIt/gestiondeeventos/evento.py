class Evento:
    def __init__(self,tipo,x,y):
        self.tipo = tipo
        self.x = x
        self.y = y


    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getTipo(self):
        return self.tipo

    def getZona(self):
        return self.zona

    def __repr__(self):
        return f"Evento de tipo:{self.tipo}|En coordenadas: ({self.x},{self.y})"
