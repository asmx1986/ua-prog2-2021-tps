import csv
import pandas as pd

from gestiondeusuarios.usuarios.ciudadano import Ciudadano

class Administrador:

    def bloquearCiudadano(self,ciudadano):
        if ciudadano.getstate() == True:
            ciudadano.setEstado(False)
        else:
            raise ValueError("Este ciudadano ya esta deshabilitado")

    def crearEvento(self,tipo,x,y):
        """Crear base de datos"""
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataEventos\eventosdeAlta.csv","a",newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([tipo,x,y])
            archivo.close()


    def desbloquearCiudadano(self,ciudadano):
        ciudadano.setEstado(True)
        ciudadano.setRechazos()

        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataUsuarios\ciudadanosBloqueados.csv","r+") as archivo:
            df = pd.read_csv(archivo)
            index = df.index
            condition = df["cuil"] == ciudadano.getCuil()
            cuil= index[condition]
            df.drop(cuil)
