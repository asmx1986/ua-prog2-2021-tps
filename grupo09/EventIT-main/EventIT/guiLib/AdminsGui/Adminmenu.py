import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.EventLib.EventManager import EventManger
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.MapsSist.MapClass import Map
from EventIT.guiLib.AdminsGui.NewAdminW import New_AdminW
from EventIT.guiLib.AdminsGui.abmW import AbmW
from EventIT.guiLib.AdminsGui.eventmaneW import EventManagerW
from EventIT.guiLib.AdminsGui.CreateSensorW import CreateSensorW

class AdminMenu(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, eventmanager: EventManger, regdeeventos: RegDeEventos,
                 regdesensores: RegDeSensores, mapa: Map, admin: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.admin = admin
        self.regdeusuarios = regdeusuarios
        self.eventmanager = eventmanager
        self.regdeeventos = regdeeventos
        self.regdesensores = regdesensores
        self.mapa = mapa
        self.Create_Widgets()


    def Create_Widgets(self):
        #creacion de widgets
        self.new_adminW_btn = tk.Button(self, text= "New admin", command= lambda: self.Open_Window(New_AdminW))
        self.abmW_btn = tk.Button(self, text= "ABM", command= lambda: self.Open_Window(AbmW))
        self.eventmanageW_btn = tk.Button(self, text= "Event Manager", command= lambda: self.Open_Window(EventManagerW))
        self.CreteSesorW_btn = tk.Button(self, text= "Manage sensors", command= lambda: self.Open_Window(CreateSensorW))




        #impresion de widgets
        self.new_adminW_btn.grid(row= 0, column= 0)
        self.abmW_btn.grid(row= 1, column= 0)
        self.eventmanageW_btn.grid(row= 2, column= 0)
        self.CreteSesorW_btn.grid(row= 3, column= 0)



    def Open_Window(self, window):
        if window == New_AdminW:
            New_AdminW(self.regdeusuarios, self.admin)
        if window == AbmW:
            AbmW(self.regdeusuarios, self.admin)
        if window == EventManagerW:
            EventManagerW(self.eventmanager, self.regdeeventos, self.admin)
        if window == CreateSensorW:
            CreateSensorW(self.regdesensores, self.mapa, self.admin)

