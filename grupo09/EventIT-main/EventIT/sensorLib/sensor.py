from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.EventLib.EventoClass import Evento
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventManager import EventManger
import tkinter as tk
from tkinter import messagebox


class Sensor:
    def __init__(self, ubicacion, tipo, name):
        self.__ubicacion: Ubicacion = ubicacion
        self.__tipo: str = tipo
        self.__name = name

    def get_name(self):
        return self.__name

    def get_ubicacion(self):
        return self.__ubicacion

    def get_tipo(self):
        return self.__tipo

    def detected_event(self, nombre, regdeeventos: RegDeEventos, eventManager: EventManger):
        if self.__tipo in eventManager.ver_tiposDeEvento():
                regdeeventos.Set_Events(Evento(self.__tipo, self.__ubicacion, nombre), True)
        else:
            tk.messagebox.showwarning(title="Type of event not alowd", message="The event type should be abled by the administrators")
