from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.EventLib.EventoClass import Evento
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.MapsSist.GraficarMapa import Graficar_Mapa





#creo un mapa con 4 zonas de 10x10
if __name__ == "__main__":
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

    evento1 = Evento("fiesta", listadeubicaciones[0][2], "L")
    evento1.Set_Attendance("enrique", True)

    evento2 = Evento("fiesta", listadeubicaciones[0][20], "L")
    evento2.Set_Attendance("e", True)
    evento2.Set_Attendance("g", True)
    evento2.Set_Attendance("r", True)


    evento3 = Evento("fiesta", listadeubicaciones[1][2], "L")
    evento3.Set_Attendance("m", True)
    evento3.Set_Attendance("h", True)

    evento4 = Evento("fiesta", listadeubicaciones[1][3], "L")
    evento5 = Evento("fiesta", listadeubicaciones[2][2], "L")
    evento6 = Evento("fiesta", listadeubicaciones[2][3], "L")
    evento7 = Evento("fiesta", listadeubicaciones[2][4], "L")
    evento8 = Evento("fiesta", listadeubicaciones[3][2], "L")
    evento9 = Evento("fiesta", listadeubicaciones[3][3], "L")
    evento10 = Evento("fiesta", listadeubicaciones[3][4], "L")

    regdeeventos = RegDeEventos()
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


    Graficar_Mapa.graficar(Mapa, regdeeventos)
