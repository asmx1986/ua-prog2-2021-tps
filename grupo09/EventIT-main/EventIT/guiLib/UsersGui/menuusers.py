import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.MapsSist.GraficarMapa import Graficar_Mapa
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.MapsSist.MapClass import Map
from EventIT.EventLib.EventManager import EventManger
from EventIT.guiLib.UsersGui.RankingW import RankingW
from EventIT.guiLib.UsersGui.FriendshipW import FrienshipW
from EventIT.guiLib.UsersGui.ReportW import ReportW


class MenuUsers(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, data_anses: DatasetANSES, regdeeventos: RegDeEventos,
                 eventmanager: EventManger, mapa: Map, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.dataanses = data_anses
        self.regdeusuarios = regdeusuarios
        self.regdeeventos = regdeeventos
        self.eventmanager = eventmanager
        self.mapa = mapa
        self.user = user
        self.Create_Widgets()



    def Open_Window(self, window):
        if window == RankingW:
            RankingW(self.regdeusuarios, self.dataanses, self.regdeeventos ,self.mapa, self.user)
        if window == FrienshipW:
            FrienshipW(self.regdeusuarios, self.user)
        if window == ReportW:
            ReportW(self.regdeusuarios, self.dataanses, self.regdeeventos, self.eventmanager, self.mapa, self.user)



    def Create_Widgets(self):
        #creacion de widgets
        self.rank_btn = tk.Button(self, text="Ranking", command= lambda: self.Open_Window(RankingW))
        self.frien_btn = tk.Button(self, text="Friend", command= lambda: self.Open_Window(FrienshipW))
        self.map_of_events_btn = tk.Button(self, text= "map", command= lambda: Graficar_Mapa.graficar(self.mapa, self.regdeeventos))
        self.report_btn = tk.Button(self, text= "Report Event", command= lambda: self.Open_Window(ReportW))




        #impresion de widgets
        self.rank_btn.grid(row = 0, column = 0)
        self.frien_btn.grid(row = 1, column = 0)
        self.map_of_events_btn.grid(row= 2, column = 0)
        self.report_btn.grid(row= 3, column= 0)



