from datetime import datetime
class Evento():
    def __init__(self,nombre,ano,mes,dia,hora,minuto,tipo_de_evento,cantidad_maxima_de_personas,vectorX,vectorY):
        self.nombre = nombre
        self.fecha = datetime(ano,mes,dia,hora,minuto,0,0)
        self.tipo_de_evento = tipo_de_evento
        self.cantidad_de_personas = 1
        self.cantidad_maxima_de_personas = cantidad_maxima_de_personas
        self.estaLleno = False
        self.x = vectorX
        self.y = vectorY
    def checkSiEstaLleno(self):
        if self.cantidad_de_personas >= self.cantidad_maxima_de_personas:
            self.estaLleno = True
        else:
            pass
    def setCantidadDePersonas(self,personas):
        self.cantidad_de_personas = personas
        return self.cantidad_de_personas
    def setEstaLleno(self,estaLLeno):
        self.estaLleno = estaLLeno
        return self.estaLleno
    def booleanNumericoEstaLleno(self):
        if self.estaLleno == True:
            return 1
        else:
            return 0
    def eventoAEscribir(self):
        return [str(self.nombre),str(self.fecha),str(self.tipo_de_evento),str(self.cantidad_de_personas),str(self.cantidad_maxima_de_personas),str(self.booleanNumericoEstaLleno()),str(self.x),str(self.y)]
    def verificarSiEstaLleno(self):
        if(self.cantidad_de_personas >= self.cantidad_maxima_de_personas):
            self.estaLleno = True
            return ("Este evento está en su capacidad maxima")
        else:
            pass
