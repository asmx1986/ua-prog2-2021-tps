import tkinter as tk
from tkinter import messagebox

from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.sensorLib.sensor import Sensor
from EventIT.MapsSist.MapClass import Map
from EventIT.UsersLib.AdminClass import Administrator


class CreateSensorW(tk.Tk):
    def __init__(self, regdesensores: RegDeSensores, mapa: Map, admin: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(1, 1)
        self.regdesensores = regdesensores
        self.mapa = mapa
        self.admin = admin
        self.Create_Widgets()





    def Create_Widgets(self):
        # creacion de widgents
        self.nameentry = tk.Entry(self)
        self.ubicacionentry = tk.Entry(self)
        self.tipoentry = tk.Entry(self)

        self.createS_btn = tk.Button(self, text= "New senor", command= lambda: self.create_delate_sensor(True))
        self.dismissS_btn = tk.Button(self, text= "Dismiss", command= lambda: self.create_delate_sensor(False))

        self.text = tk.Label(self, text= "Dismiss use only the name of the sensor")


        # imprecion de widgets
        self.nameentry.insert(0, "Name")
        self.nameentry.grid(row= 0, column= 0)
        self.ubicacionentry.insert(0, "latitude,longitude")
        self.ubicacionentry.grid(row= 1, column= 0)
        self.tipoentry.insert(0, "Type")
        self.tipoentry.grid(row= 2, column= 0)

        self.createS_btn.grid(row= 3, column= 0)
        self.dismissS_btn.grid(row= 4, column= 0)

        self.text.grid(row= 5, column= 0)

    def create_delate_sensor(self, bool):
        name = self.nameentry.get()
        if bool:
            try:
                coordenadasstr = self.ubicacionentry.get()
                if coordenadasstr.find(",") == -1:
                    messagebox.showwarning(title= "Syntax error", message= "Remember to divide latitude and longitude by: ,\n latitude,longitude")
                else:
                    (lat, lon) = coordenadasstr.split(",")
                    ubicacion = self.mapa.search_ubicacion(int(lat), int(lon))
                    if ubicacion != False:
                        tipo = self.tipoentry.get()
                        self.regdesensores.Set_Sensors(Sensor(ubicacion, tipo, name), True)
                    else:
                        messagebox.showwarning(title= "Not location", message= "We couldnt found a location with those valuese")
            except ValueError:
                messagebox.showwarning(title= "Wrong values", message= "only numbers should be in latitude, longitude")
        else:
            sensor = self.regdesensores.Search_sensor(name)
            if sensor != False:
                self.regdesensores.Set_Sensors(sensor, False)
            else:
                messagebox.showwarning(title= "Sensor not found", message= "We couldnt found a senor with that name")

