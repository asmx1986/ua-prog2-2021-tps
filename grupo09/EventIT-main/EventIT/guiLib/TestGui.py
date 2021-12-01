from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.guiLib.Maingui import App
from EventIT.EventLib.EventoClass import Evento
from EventIT.EventLib.EventManager import EventManger
from EventIT.sensorLib.sensor import Sensor


if __name__ == "__main__":
    regdeusuarios = RegDeUsuarios()
    dataAnses= DatasetANSES()
    regdeeventos = RegDeEventos()
    regdeusuarios.Manage_Ciudadanos(Ciudadano("ADMIN", 1,1),True,"ADMIN")
    admin = Administrator("ADMIN")
    regdeusuarios.Manage_Admins(admin, True,"ADMIN")
    eventmanager  = EventManger(regdeeventos)
    regdesensores = RegDeSensores()


    def crear_ubicaciones():
        ParaZona1 = []
        ParaZona2 = []
        ParaZona3 = []
        ParaZona4 = []
        x_origen = 0
        x = 0
        y = 0
        cantidad_en_fila = 0
        cantidad_en_y = 0
        while cantidad_en_y <= 20:
            while cantidad_en_fila <= 20:
                if x <= 10 and y <= 10:
                    ParaZona1.append(Ubicacion(x, y))
                elif 10< x <= 20 and y <= 10:
                    ParaZona2.append(Ubicacion(x,y))
                elif x <= 10 and 10 < y <= 20:
                    ParaZona3.append(Ubicacion(x, y))
                else:
                    ParaZona4.append(Ubicacion(x,y))

                x += 1
                cantidad_en_fila += 1
            cantidad_en_fila = 0
            cantidad_en_y += 1
            x = x_origen
            y += 1

        return [ParaZona1, ParaZona2, ParaZona3, ParaZona4]

    listadeubicaciones = crear_ubicaciones()
    Zona1 = Zona(listadeubicaciones[0], 1, "Zona 1")
    Zona2 = Zona(listadeubicaciones[1], 2, "Zona 2")
    Zona3 = Zona(listadeubicaciones[2], 3, "Zona 3")
    Zona4 = Zona(listadeubicaciones[3], 4, "Zona 4")
    Mapa = Map([Zona1, Zona2, Zona3, Zona4])





    evento1 = Evento("fiesta", listadeubicaciones[0][2], "Evento 1")
    evento2 = Evento("fiesta", listadeubicaciones[0][20], "Evento 2")
    evento3 = Evento("fiesta", listadeubicaciones[1][2], "4")
    evento4 = Evento("fiesta", listadeubicaciones[1][3], "5")
    evento5 = Evento("fiesta", listadeubicaciones[2][2], "6")
    evento6 = Evento("fiesta", listadeubicaciones[2][3], "7")
    evento7 = Evento("fiesta", listadeubicaciones[2][4], "8")
    evento8 = Evento("fiesta", listadeubicaciones[3][2], "9")
    evento9 = Evento("fiesta", listadeubicaciones[3][3], "3")
    evento10 = Evento("fiesta", listadeubicaciones[3][4], "10")

    


    regdeeventos.Set_Events(evento1, True)
    regdeeventos.Set_Events(evento2, True)
    regdeeventos.Set_Events(evento3, True)
    regdeeventos.Set_Events(evento4, True)
    regdeeventos.Set_Events(evento5, True)
    regdeeventos.Set_Events(evento6, True)
    regdeeventos.Set_Events(evento7, True)
    regdeeventos.Set_Events(evento8, True)
    regdeeventos.Set_Events(evento9, True)
    regdeeventos.Set_Events(evento10, True)

    sensor1 = Sensor(Mapa.search_ubicacion(1,1), "fiesta", "sensor1,1")
    regdesensores.Set_Sensors(sensor1, True)
    eventmanager.alta_tiposDeEvento("fiesta", admin)








    #mainMenu
    application = App(regdeusuarios, dataAnses, regdeeventos, eventmanager, regdesensores, Mapa)



    application.mainloop()


