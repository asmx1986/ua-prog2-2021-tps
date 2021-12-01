import tkinter as tk
from tkinter.messagebox import  showwarning

from EventIT.UsersLib.AdminClass import Administrator
from EventIT.EventLib.EventManager import EventManger
from EventIT.EventLib.RegDeEventosClass import RegDeEventos


class EventManagerW(tk.Tk):
    def __init__(self, eventmanager: EventManger, regdeeventos: RegDeEventos, admin: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"450x300+{550}+{150}")
        self.wm_resizable(1, 1)
        self.eventmanager = eventmanager
        self.regdeeventos = regdeeventos
        self.admin = admin
        self.Create_Widgets()

    def Create_Widgets(self):
        #Creacion de widgets
        self.tipoevent = tk.Entry(self)

        self.altatipo = tk.Button(self, text= "New type of event", command= lambda: self.change_typeofevents(True))
        self.bajatipo = tk.Button(self, text= "Delete type of event", command= lambda: self.change_typeofevents(False))

        self.show = tk.Button(self, text= "Type of events" ,command= self.show)


        self.event_ent = tk.Entry(self)
        self.eliminate_btn = tk.Button(self, text = "eliminate event", command= self.eliminate_event)



        #Impresion de widgets
        self.tipoevent.insert(0, "Type of event")
        self.tipoevent.grid(row= 0, column= 0)

        self.altatipo.grid(row= 1, column= 0)
        self.bajatipo.grid(row= 2, column= 0)

        self.show.grid(row= 3, column= 0)

        self.event_ent.insert(0, "event")
        self.event_ent.grid(row= 4, column= 0)
        self.eliminate_btn.grid(row=  5, column= 0)

        #CANVAS
        self.displayinfo = tk.Canvas(self, width=100, height=400, bg="white")
        self.displayinfo.grid(row=0, column= 3, rowspan = 20)

        self.vsb = tk.Scrollbar(self, orient= "vertical")
        self.vsb.grid(row=0, column= 4, rowspan= 20, sticky= "ns")


        self.displayframe = tk.Frame(self.displayinfo, bg="white")

        self.displayinfo.config(yscrollcommand = self.vsb.set)
        self.displayinfo.bind('<Configure>', lambda e: self.displayinfo.config(scrollregion = self.displayinfo.bbox("all")))


        self.displayinfo.create_window((10, 0), window= self.displayframe, anchor="nw")

        self.vsb.config(command= self.displayinfo.yview)


    def change_typeofevents(self, bool):
        tipo = self.tipoevent.get()
        if bool:
            self.eventmanager.alta_tiposDeEvento(tipo, self.admin)
        else:
            self.eventmanager.darbaja_tipodeevent(tipo)

    def show(self):
        tk.Label(self.displayinfo, text= "----------").pack()
        for tipo in self.eventmanager.ver_tiposDeEvento():
            tk.Label(self.displayinfo, text= f"type: {tipo}").pack()

    def eliminate_event(self):
        eventname = self.event_ent.get()
        evento = self.regdeeventos.Search_events(eventname)
        if evento == False:
            showwarning(title= "Event not found", message= "A event with this name couldt be found.")
        else:
            self.regdeeventos.Set_Events(evento, False)




