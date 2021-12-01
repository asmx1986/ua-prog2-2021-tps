from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.sensorLib.RegDeSensores import RegDeSensores
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.guiLib.Maingui import App
from EventIT.EventLib.EventManager import EventManger
# from EventIT.sensorLib.sensor import Sensor



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


if __name__ == "__main__":
    regdeusuarios = RegDeUsuarios()
    dataAnses= DatasetANSES()
    regdeeventos = RegDeEventos(regdeusuarios)
    admin = Administrator("ADMIN")
    eventmanager  = EventManger(regdeeventos)
    regdesensores = RegDeSensores()




    listadeubicaciones = crear_ubicaciones()
    Zona1 = Zona(listadeubicaciones[0], 1, "Zona 1")
    Zona2 = Zona(listadeubicaciones[1], 2, "Zona 2")
    Zona3 = Zona(listadeubicaciones[2], 3, "Zona 3")
    Zona4 = Zona(listadeubicaciones[3], 4, "Zona 4")
    Mapa = Map([Zona1, Zona2, Zona3, Zona4])






    # sensor1 = Sensor(Mapa.search_ubicacion(1,1), "fiesta", "sensor1,1")
    # regdesensores.Set_Sensors(sensor1, True)
    eventmanager.alta_tiposDeEvento("Fiesta", admin)
    eventmanager.alta_tiposDeEvento("Sanitario", admin)
    eventmanager.alta_tiposDeEvento("Privado", admin)
    eventmanager.alta_tiposDeEvento("Social", admin)








    #mainMenu
    application = App(regdeusuarios, dataAnses, regdeeventos, eventmanager, regdesensores, Mapa)



    application.mainloop()


