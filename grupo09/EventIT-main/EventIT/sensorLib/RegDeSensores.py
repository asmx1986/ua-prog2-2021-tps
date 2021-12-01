from EventIT.sensorLib.sensor import Sensor
from EventIT.MapsSist.UbicacionClass import Ubicacion
import os
import tkinter as tk
from tkinter import messagebox



class RegDeSensores:
    def __init__(self):
        self.__sensores: list[Sensor] = []
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_sensores.txt'
        with open(path,'r') as f:
            for linea in f.readlines():
                name = linea.split('/')[0]
                tipo = linea.split('/')[1]
                ubicacionString = linea.split('/')[2][1:-1]
                latitud = int(ubicacionString.split(',')[0])
                longitud = int(ubicacionString.split(',')[1])
                ubicacion = Ubicacion(latitud, longitud)
                self.__sensores.append(Sensor(ubicacion, tipo, name))
            f.close()

    def __repr__(self):
        return 'RegDeSensores'

    def Set_Sensors(self, sensor: Sensor, add: bool):
        """Permite inscribirse o desinscribirse de un evento.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        sensor_line = (f'{sensor.get_name()}/{sensor.get_tipo()}/{sensor.get_ubicacion()}/\n')
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_sensores.txt'
        if add:
            if sensor.get_name() not in list(map(lambda x:x.get_name(), self.__sensores)):
                self.__sensores.append(sensor)
                with open(path,'a') as f: # agregar texto sin sobreescribir
                    f.write(sensor_line)
                    f.close()
            else:
                tk.messagebox.showwarning(title="Sensor invalido", message= "El sensor que intenta agregar ya se encuentra en el registro")
        else:
            try:
                self.__sensores.remove(sensor)
                with open(path,'r') as f: # codigo para borrar usuarios
                    lineas = f.readlines()
                    with open(path,'w') as f:
                        f.write('')
                        f.close()
                    for linea in lineas:
                        if linea != sensor_line:
                            with open(path,'a') as f:
                                f.write(linea)
                                f.close()
                    f.close()
            except KeyError:
                alert = tk.messagebox.showwarning(title="Sensor not found", text="El sensor wue intenta eliminar no existe.")


    def View_Sensors(self)-> list[Sensor]:
        return self.__sensores.copy()

    def Search_sensor(self, name):
        for sensor in self.__sensores:
            if sensor.get_name() == name:
                return sensor
        return False

