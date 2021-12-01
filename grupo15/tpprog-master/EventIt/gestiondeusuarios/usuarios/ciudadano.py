import csv
from gestiondeeventos.contactos import Contactos
from gestiondeeventos.evento import Evento
from gestiondeusuarios.atributosUsuarios.telefono import Telefono
from gestiondeusuarios.atributosUsuarios.cuil import Cuil
from gestiondeusuarios.atributosUsuarios.password import Password

class Ciudadano:
    def __init__(self, telefono, cuil, password):
        self.telefono = Telefono(telefono)
        self.cuil = Cuil(cuil)
        self.password = Password(password)
        self.estado=True
        self.rechazos=0
        self.contactos = Contactos()
        self.eventos=[]

    def Enviarinvitacion(self,enviarAContacto):
        if (self.__block()):
            print( "Ciudadano", self, "llama a setRecibidas con", enviarAContacto )
            enviarAContacto.contactos.setRecibidas(self)
            self.contactos.setEnviadas(enviarAContacto)
        else:
            raise ValueError("Usuario Bloqueado, pida auditoria")

    def rechazarInvitacion(self,ciudadano):
        """Se fija en la lista de invitaciones si esta la invitacion y si no esta salta error"""
        if (self.__block()):
            print( "Ciudadano rechazarInvitacion",self,"rechaza invitacion de",ciudadano)
            #if (ciudadano in self.contactos.getRecibidas()) and (self in ciudadano.contactos.getEnviadas()):
            if (self in ciudadano.contactos.getEnviadas()) and (ciudadano in self.contactos.getRecibidas()):
                self.contactos.removeRecibidas(ciudadano)
                ciudadano.contactos.removeEnviadas(self)
                ciudadano.setRechazo()
            else:
                raise ValueError("Este ciudadano no te ha enviado una solicitud")

    def aceptarInvitacion(self,ciudadano):
        if (self.__block()):
            if (ciudadano in self.contactos.getRecibidas()) and (self in ciudadano.contactos.getEnviadas()):
                self.contactos.removeRecibidas(ciudadano)
                ciudadano.contactos.removeEnviadas(self)
                self.contactos.getAmigos().append(ciudadano)
                ciudadano.contactos.getAmigos().append(self)
            else:
                raise ValueError("Este ciudadano no te ha enviado una solicitud")
        else:
            raise ValueError("Usuario Bloqueado, pida auditoria")

    def asistirEvento(self,tipo,x,y):
        """Crear evento,appendearlo en un lugar que sea eventos activos"""
        if (self.__block()):
            self.eventos.append(Evento(tipo,x,y))
        else:
            raise ValueError("Usuario bloqueado, pida auditoria al 0800 999 1507")

    def pedirAuditoria(self):
        if self.estado == False:
            with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataUsuarios\ciudadanosBloqueados.csv","a",newline='') as archivo:
                writer = csv.writer(archivo)
                writer.writerow([str(self.cuil),str(self.telefono)])
                archivo.close()
        else:
            raise ValueError("Usted no es un usuario bloqueado")

    def __block(self):
        if self.rechazos >= 5:
            self.estado = False
            return self.estado
        else:
            return self.estado

    def __repr__(self):
        return str(f"Cuil: {self.cuil}|Telefono: {self.telefono}")

    def getCuil(self):
        return str(self.cuil)

    def getTelefono(self):
        return self.telefono

    def getContrasena(self):
        return str(self.password)

    def setEstado(self,estado:bool):
        self.estado = estado

    def setRechazos(self):
        self.rechazos=0

    def getstate(self):
        return self.estado

    def getEventos(self):
        return self.eventos

    def setRechazo(self):
        self.rechazos +=1

