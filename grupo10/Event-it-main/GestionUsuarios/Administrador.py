from GestionUsuarios.Ciudadano import Ciudadano
from Anses.Anses import leerTiposDeEvento
from Anses.Anses import escribirTipoDeEvento

class Administrador():

    def __init__(self, usuario, contrasena, accesoAABM):
        self.usuario = usuario
        self.contrasena = contrasena
        self.accesoAABM = accesoAABM
    def booleanNumericoAccesoAABM(self):
        if self.accesoAABM == True:
            return 1
        else:
            return 0
    def adminAEscribir(self):
        return [str(self.usuario),str(self.contrasena),self.booleanNumericoAccesoAABM()]
    def desbloquearCiudadano(self,Ciudadano):
        Ciudadano.estaBloqueado = False
        Ciudadano.solicitudesRechazadas = 0
        return ("El ciudadano se ha desbloqueado")
    def bloquearCiudadano(self,Ciudadano):
        Ciudadano.estaBloqueado = True
        return("El ciudadano se ha bloqueado")
    def crearTipoDeEvento(self):
        tipoNuevo=str(input("ingrese el evento en minuscula: "))
        listaTiposEventos=[]
        leerTiposDeEvento(listaTiposEventos)
        indiceLista = 0
        estariaRepetido = False
        while indiceLista < len(listaTiposEventos):
            if tipoNuevo == listaTiposEventos[indiceLista]:
                estariaRepetido = True
                indiceLista = indiceLista + len(listaTiposEventos)
            else:
                indiceLista = indiceLista + 1
        if estariaRepetido == True:
            print("Este tipo de evento ya fue creado previamente.")
        else:
            escribirTipoDeEvento(tipoNuevo)
            print("se ha guardado el tipo de evento")