import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.Estadisticas.Estadisticas import Estadisticas
from EventIT.MapsSist.MapClass import Map




class RankingW(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, dataanses: DatasetANSES, regdeeventos: RegDeEventos,mapa: Map, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("1350x400")
        self.wm_resizable(1, 1)
        self.dataanses = dataanses
        self.regdeusuarios = regdeusuarios
        self.regdeeventos =regdeeventos
        self.mapa = mapa
        self.user = user
        self.Create_Widgets()





    def Create_Widgets(self):

        # creacion de widgents
        self.rank_asis_x_zona_btn = tk.Button(self, text= "ranking por zona", command= lambda: self.show_ranking("zona"))
        self.rank_asis_max_btn = tk.Button(self, text= "ranking de asistencia max", command= lambda: self.show_ranking("max"))
        self.rank_asis_porcent_btn = tk.Button(self, text= "ranking por porcentajes", command= lambda: self.show_ranking("porcentaje"))




        # imprecion de widgets
        self.rank_asis_x_zona_btn.grid(row= 0, column= 0)
        self.rank_asis_max_btn.grid(row=1, column=0)
        self.rank_asis_porcent_btn.grid(row= 2, column= 0)

        """       #Experimental
        self.displayinfo = tk.Canvas(self, width= 50, height= 50)
        self.displayinfo.grid(row=0, column= 1)
        scroll = tk.Scrollbar(self.displayinfo)
        scroll.pack(side='right', fill='y')
        self.txtRes= tk.Text(self.displayinfo, width=50, height=50, yscrollcommand=scroll.set)
        self.txtRes.pack(side='left')
        scroll.config(command = self.txtRes.yview)"""


        #CANVAS
        self.displayinfo = tk.Canvas(self, width=1000, height=400, bg="white")
        self.displayinfo.grid(row=0, column= 3, rowspan = 20)

        self.vsb = tk.Scrollbar(self, orient= "vertical")
        self.vsb.grid(row=0, column= 4, rowspan= 20, sticky= "ns")


        self.displayframe = tk.Frame(self.displayinfo, bg="white")

        self.displayinfo.config(yscrollcommand = self.vsb.set)
        self.displayinfo.bind('<Configure>', lambda e: self.displayinfo.config(scrollregion = self.displayinfo.bbox("all")))


        self.displayinfo.create_window((10, 0), window= self.displayframe, anchor="nw")

        self.vsb.config(command= self.displayinfo.yview)





    def show_ranking(self, por):
        if por == "zona":
            ranking = Estadisticas.calculate_ranking(self.mapa, self.dataanses, self.regdeeventos,
                                                    mayor_cantidad_de_asistentes_de_la_zona=True)
        elif por == "max":
            ranking = Estadisticas.calculate_ranking(self.mapa, self.dataanses, self.regdeeventos,
                                                                      mayor_cantidad_de_asistentes=True)
        elif por == "porcentaje":
            ranking = Estadisticas.calculate_ranking(self.mapa, self.dataanses, self.regdeeventos,
                                                                      mayor_porcentaje=True)
        else:
            ranking = ""


        tk.Label(self.displayinfo, text=f"{ranking}").pack()











