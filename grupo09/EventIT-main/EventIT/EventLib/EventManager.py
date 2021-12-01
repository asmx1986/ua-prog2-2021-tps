from tkinter import messagebox

from EventIT.UsersLib.AdminClass import Administrator
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventoClass import Evento

class EventManger:

    def __init__(self, regdeevento: RegDeEventos):
        self.__regdeeventos = regdeevento
        self.__TipoDeEventos = []

    def alta_tiposDeEvento(self, TipoDeEvento, User):
        # El admin da de alta tipos de eventos, para que a la hora de crear eventos solo sean de los tipos de eventos aprobados.
        if isinstance(User,Administrator) and TipoDeEvento not in self.__TipoDeEventos:
            self.__TipoDeEventos.append(TipoDeEvento)

    def darbaja_tipodeevent(self, tipodeevento):
        if tipodeevento in self.__TipoDeEventos:
            self.__TipoDeEventos.remove(tipodeevento)
        else:
            messagebox.showwarning(title= "Type of event", message= "The type of event couldnt be found")

    def ver_tiposDeEvento (self):
        return self.__TipoDeEventos.copy()

    def report_evento(self, tipo, ubicacion, nombre):
        # Se guardan nuevos eventos en lista de eventos del RegDeEventos
        if tipo in self.__TipoDeEventos:
            eventosnames = []
            for evento in self.__regdeeventos.View_Events():
                eventosnames.append(evento.getName())
            if nombre in eventosnames:
                messagebox.showwarning(title= "Name taken", message= "This name is already taken")
            else:
                self.__regdeeventos.Set_Events(Evento(tipo, ubicacion, nombre), True)


    def asistir_evento(self, evento, usuario, invitados= None):
        # Si el evento existe en la lista de eventos, se agrega a la lista de invitados el nuevo invitado.
        if invitados is None:
            if evento in self.__regdeeventos.View_Events():
                evento.Set_Attendance(usuario,True)
        else:
            if evento in self.__regdeeventos.View_Events():
                evento.Set_Attendance(usuario,True)
            for invitado in invitados:
                evento.Set_Attendance(invitado,True)

    def desinscribirse_evento(self, evento, usuario):
        # Si el evento esta en la lista y el usuario figura como invitado, se lo elimina de la lista de invitados.
        if evento in self.__regdeeventos.View_Events() and usuario in evento.getListaDeAsistencia():
            evento.Set_Attendance(usuario,False)
