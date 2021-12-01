import tkinter as tk
from tkinter import messagebox

from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventManager import EventManger
from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.MapsSist.MapClass import Map



class MenuSensors(tk.Tk):
    def __init__(self, regdeeventos: RegDeEventos, eventmanager: EventManger, regdesensores: RegDeSensores, mapa: Map):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.regdeeventos = regdeeventos
        self.eventmanager = eventmanager
        self.regdesensores = regdesensores
        self.mapa = mapa
        self.Create_Widgets()

    def Create_Widgets(self):
        #creacion de widgets
        self.nameentry = tk.Entry(self)
        self.nameevententry = tk.Entry(self)

        self.report_btn = tk.Button(self, text= "Report event", command= self.report)


        #impresion de widgets
        self.nameentry.insert(0, "sensor name")
        self.nameentry.grid(row= 0, column= 0)
        self.nameevententry.insert(0, "name of event")
        self.nameevententry.grid(row= 1, column= 0)

        self.report_btn.grid(row= 2, column= 0)


    def report(self):
        nameofsensor = self.nameentry.get()
        sensor = self.regdesensores.Search_sensor(nameofsensor)
        if sensor == False:
            messagebox.showwarning(title= "Not found", message= "Sensor couldnt be found")
        else:
            nameofevent = self.nameevententry.get()
            if self.regdeeventos.Search_events(nameofevent) == False:
                sensor.detected_event(nameofevent, self.regdeeventos, self.eventmanager)
            else:
                messagebox.showwarning(title= "Name in use", message= "This name is already in use for a event")






