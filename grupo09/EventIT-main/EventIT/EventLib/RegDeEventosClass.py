from EventIT.EventLib.EventoClass import Evento
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
import os
import tkinter as tk
from tkinter import messagebox


class RegDeEventos:
    def __init__(self, regDeUsuarios: RegDeUsuarios):
        self.__Eventos: list[Evento] = []
        self.__regDeUsuarios = regDeUsuarios
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_eventos.txt'
        with open(path,'r') as f:
            for index, linea in enumerate(f.readlines()):
                tipo = linea.split('/')[0]
                ubicacionString = linea.split('/')[1][1:-1]
                latitud = int(ubicacionString.split(',')[0])
                longitud = int(ubicacionString.split(',')[1])
                ubicacion = Ubicacion(latitud, longitud)
                name = linea.split('/')[2]
                self.__Eventos.append(Evento(tipo, ubicacion, name))
                listaDeAsistentes = list(map(lambda x:regDeUsuarios.searchCitizen(cuil=int(x)), list(filter(lambda x:x!='', list(linea.split('/')[3][1:-2].split(','))))))
                [self.__Eventos[index].Set_Attendance(asistente, True) for asistente in listaDeAsistentes]
            f.close()

    def __repr__(self):
        return 'RegDeEventos'

    def Set_Events(self, evento: Evento, add: bool):
        """Permite inscribirse o desinscribirse de un evento.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo"""
        cuils_de_asistentes = list(map(lambda x:x.Get_Cuil(), evento.getListaDeAsistencia()))
        event_line = f'{evento.getTipo()}/{evento.getUbicacion()}/{evento.getName()}/{cuils_de_asistentes}\n'
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_eventos.txt'
        if add:
            self.__Eventos.append(evento)
            with open(path,'a') as f: # agregar texto sin sobreescribir
                f.write(event_line)
                f.close()
        else:
            try:
                self.__Eventos.remove(evento)
                with open(path,'r') as f: # codigo para borrar usuarios
                    lineas = f.readlines()
                    with open(path,'w') as f:
                        f.write('')
                        f.close()
                    for linea in lineas:
                        if linea != event_line:
                            with open(path,'a') as f:
                                f.write(linea)
                                f.close()
                    f.close()
            except ValueError:
                alert = tk.messagebox.showwarning(title="Event not found", text="El evento que desea eliminar no existe.")

    def View_Events(self)-> list[Evento]:
        return self.__Eventos.copy()

    def Search_events(self, name):
        for evento in self.__Eventos:
            if evento.getName() == name:
                return evento
        return False

