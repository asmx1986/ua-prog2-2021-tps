import tkinter as tk
from tkinter import messagebox
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.EventLib.EventManager import EventManger
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.MapsSist.MapClass import Map
from EventIT.guiLib.AdminsGui.Adminmenu import AdminMenu

class LogAdmin(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, eventmanager: EventManger, regdeeventos: RegDeEventos,
                 regdesensores: RegDeSensores, mapa: Map):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.regdeusuarios = regdeusuarios
        self.eventmanager = eventmanager
        self.regdeeventos =regdeeventos
        self.regdesensores = regdesensores
        self.mapa = mapa
        self.Create_Widgets()


    def Create_Widgets(self):
        #creacion de widgets
        self.title = tk.Label(self, text="Log Admin")
        self.admin_input = tk.Entry(self)
        self.log_btn = tk.Button(self, text = "log", command = self.Log_in_admin)



        #impresion de widgets
        centerW = 150

        self.title.grid(row= 0, column= centerW)
        self.admin_input.insert(0, "key name")
        self.admin_input.grid(row= 1, column= 0)
        self.log_btn.grid(row= 2, column= 0)

    def Log_in_admin(self):
        key_admin = self.admin_input.get()
        if key_admin in self.regdeusuarios.Get_Admins():
            self.admin = self.regdeusuarios.Get_Admins()[key_admin]
            self.Open_Window(AdminMenu)
        else:
            alert = tk.messagebox.showwarning(title = "key name not found", message = "key name couldt be found, thy again")

    def Open_Window(self, window):
        if window == AdminMenu:
            AdminMenu(self.regdeusuarios, self.eventmanager, self.regdeeventos, self.regdesensores, self.mapa, self.admin)
        self.withdraw()
