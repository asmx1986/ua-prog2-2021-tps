from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.UsersLib.CitizenClass import Ciudadano
import os
import tkinter as tk
from tkinter import messagebox


class Evento:
    def __init__(self, tipo, ubicacion: Ubicacion, nombre):
        self.__Tipo = tipo
        self.__Ubicacion = ubicacion
        self.__ListaAsistentes = []
        self.__nombre = nombre

    def __repr__(self):
        return self.__nombre

    def getTipo(self):
        return self.__Tipo

    def getUbicacion(self):
        return self.__Ubicacion

    def getListaDeAsistencia(self):
        return self.__ListaAsistentes.copy()

    def getZona(self, lista_de_zonas):
        for zona in lista_de_zonas:
            if self.__Ubicacion.Get_Coordinates() in list(map(lambda x:x.Get_Coordinates(), zona.Get_Ubicaciones())): #la idea es ver si esa ubicacion es parte de la zona PROBAR
                return zona

    def getName(self):
        return self.__nombre

    def Set_Attendance(self, ciudadano: Ciudadano, inscribirse: bool):
        """Permite inscribirse o desinscribirse de un evento.\n
            inscribirse = True, para inscribirse.\n
            inscribirse = False, para desinscribirse"""
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_eventos.txt'
        with open(path,'r') as f:
            replacement = ""
            # using the for loop
            for line in f:
                line = line.strip()
                # if self es igual al evento de la linea:
                name = line.split('/')[2]
                if self.getName() == name:
                    oldList = self.getListaDeAsistencia()
                    oldListCuils = list(map(lambda x:x.Get_Cuil(), oldList))
                    newList = self.getListaDeAsistencia()
                    if inscribirse:
                        newList.append(ciudadano)
                    else:
                        try:
                            newList.remove(ciudadano)
                        except ValueError:
                            pass
                    newListCuils = list(map(lambda x:x.Get_Cuil(), newList))
                    changes = line.replace(str(oldListCuils), str(newListCuils))
                    replacement = replacement + changes + "\n"
                else:
                    replacement = replacement + line + "\n"
            f.close()
        # opening the file in write mode
        with open(path,'w') as f:
            f.write(replacement)
            f.close()

        if inscribirse:
            self.__ListaAsistentes.append(ciudadano)
        else:
            try:
                self.__ListaAsistentes.remove(ciudadano)
            except ValueError:
                alert = tk.messagebox.showwarning(title="Error al desinscribirse", text="Para poder desinscribirse, antes debe pertenecer a la lista de asistentes")
