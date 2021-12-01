import unittest
from EventIT.MapsSist.MapClass import Map
from EventIT.MapsSist.UbicacionClass import Ubicacion
from EventIT.MapsSist.ZonaClass import Zona
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos
from EventIT.EventLib.EventoClass import Evento
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.Estadisticas.Estadisticas import Estadisticas
from EventIT.EventLib.EventManager import EventManger
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios


class TestPrueba(unittest.TestCase):
    def setUp(self):
        self.regDeUsuarios = RegDeUsuarios()
        self.regDeEventos = RegDeEventos(self.regDeUsuarios)
        self.eventManager = EventManger(self.regDeEventos)
        self.datasetANSES = DatasetANSES()

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


        self.listadeubicaciones = crear_ubicaciones()
        self.Zona1 = Zona(self.listadeubicaciones[0], 1, "Zona 1")
        self.Zona2 = Zona(self.listadeubicaciones[1], 2, "Zona 2")
        self.Zona3 = Zona(self.listadeubicaciones[2], 3, "Zona 3")
        self.Zona4 = Zona(self.listadeubicaciones[3], 4, "Zona 4")
        self.Mapa = Map([self.Zona1, self.Zona2, self.Zona3, self.Zona4])


        self.eventManager.alta_tiposDeEvento('Fiesta', self.regDeUsuarios.Get_Admins()['Juan'])
        self.eventManager.alta_tiposDeEvento('Sanitario', self.regDeUsuarios.Get_Admins()['Juan'])
        self.eventManager.alta_tiposDeEvento('Social', self.regDeUsuarios.Get_Admins()['Juan'])
        self.eventManager.alta_tiposDeEvento('Privado', self.regDeUsuarios.Get_Admins()['Juan'])

        self.evento1 = Evento('Fiesta', self.Mapa.search_ubicacion(1,3), 'Evento1')
        self.evento2 = Evento('Sanitario', self.Mapa.search_ubicacion(8,6), 'Evento2')
        self.evento3 = Evento('Social', self.Mapa.search_ubicacion(2,7), 'Evento3')
        self.evento4 = Evento('Privado', self.Mapa.search_ubicacion(5,5), 'Evento4')
        self.regDeEventos.Set_Events(self.evento1, True)
        self.regDeEventos.Set_Events(self.evento2, True)
        self.regDeEventos.Set_Events(self.evento3, True)
        self.regDeEventos.Set_Events(self.evento4, True)

        self.evento1.Set_Attendance(self.regDeUsuarios.Get_Ciudadanos()['Lucas'][0], True)
        self.evento1.Set_Attendance(self.regDeUsuarios.Get_Ciudadanos()['Joaquin'][0], True)
        self.evento2.Set_Attendance(self.regDeUsuarios.Get_Ciudadanos()['Facundo'][0], True)

        self.ciudadano1 = Ciudadano('pepe', 4444, 15151515)
        self.ciudadano2 = Ciudadano('tomas', 5555, 16161616)
        self.ciudadano3 = Ciudadano('Marcos', 6666, 17171717)
        self.ciudadano4 = Ciudadano('Antonio', 7777, 18181818)

        self.regDeUsuarios.Manage_Ciudadanos(self.ciudadano1, True, 'Pepe')
        self.regDeUsuarios.Manage_Ciudadanos(self.ciudadano2, True, 'Tomas')
        self.regDeUsuarios.Manage_Ciudadanos(self.ciudadano3, True, 'Marcos')
        self.regDeUsuarios.Manage_Ciudadanos(self.ciudadano4, True, 'Antonio')

        self.evento3.Set_Attendance(self.ciudadano1, True)
        self.evento1.Set_Attendance(self.ciudadano2, True)
        self.evento2.Set_Attendance(self.ciudadano3, True)
        self.evento4.Set_Attendance(self.ciudadano4, True)

        # self.estadisticas = Estadisticas(self.mapa1, self.datasetANSES, self.regDeEventos)

        # self.rankingString = f"|\tPosicion\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas por zona\t|\tCantidad de personas totales\t|\tPorcentaje de asistentes de la zona\t|\n"
        # for index, evento in enumerate(Estadisticas.calculate_positions_of_the_ranking(self.Mapa, self.datasetANSES, self.regDeEventos, False, False, True)): # arma el ranking en formato string para imprmirlo
        #     self.rankingString += f"|\t\t{index + 1}\t\t|\t\t{evento}\t\t\t|\t{evento.getZona(self.Mapa.getListaDeZonas())}\t|" \
        #                           f"\t\t\t\t{Estadisticas.calculate_number_of_attendees_per_zone_per_event(self.Mapa, self.datasetANSES, self.regDeEventos)[evento]}\t\t\t\t\t|" \
        #                           f"\t\t\t\t{Estadisticas.calculate_total_number_of_attendees(self.Mapa, self.datasetANSES, self.regDeEventos)[evento]}\t\t\t\t\t|" \
        #                           f"\t\t\t\t{Estadisticas.calculate_percentage_of_atendees_of_the_zone(self.Mapa, self.datasetANSES, self.regDeEventos)[evento]}\t\t\t\t\t|\n"
        # print(self.rankingString)

        # print(Estadisticas.calculate_ranking(self.Mapa, self.datasetANSES, self.regDeEventos))

    def test_ranking(self):
        print(Estadisticas.calculate_ranking(map=self.Mapa, datasetANSES=self.datasetANSES, regDeEventos=self.regDeEventos, mayor_cantidad_de_asistentes=True))

    def test_add_events(self):
        self.assertEqual(self.regDeEventos.View_Events(), [self.evento1, self.evento2, self.evento3, self.evento4])

    def test_set_attendance_inscribirse(self):
        self.assertEqual(self.evento1.getListaDeAsistencia(), [self.regDeUsuarios.Get_Ciudadanos()['Lucas'][0], self.regDeUsuarios.Get_Ciudadanos()['Joaquin'][0], self.ciudadano2])

    def test_set_attendance_desinscribirse(self):
        self.evento1.Set_Attendance(self.regDeUsuarios.Get_Ciudadanos()['Lucas'][0], False)
        self.assertEqual(self.evento1.getListaDeAsistencia(), [self.regDeUsuarios.Get_Ciudadanos()['Joaquin'][0], self.ciudadano2])

    def test_calculate_number_of_attendees_per_zone_per_event(self):
        self.assertEqual(Estadisticas.calculate_number_of_attendees_per_zone_per_event(self.Mapa, self.datasetANSES, self.regDeEventos)[self.evento2], 1)

    def test_calculate_total_number_of_attendees(self):
        self.assertEqual(Estadisticas.calculate_total_number_of_attendees(self.regDeEventos)[self.evento1], 3)

    def test_calculate_percentage_of_atendees_of_the_zone(self):
        self.assertEqual(Estadisticas.calculate_percentage_of_atendees_of_the_zone(self.Mapa, self.datasetANSES, self.regDeEventos)[self.evento2], 50)

    def test_calculate_positions_of_the_ranking(self):
        self.assertEqual(Estadisticas.calculate_positions_of_the_ranking(self.Mapa, self.datasetANSES, self.regDeEventos), [self.evento2, self.evento4, self.evento1, self.evento3])
        self.assertEqual(Estadisticas.calculate_positions_of_the_ranking(map=self.Mapa, datasetANSES=self.datasetANSES, regDeEventos=self.regDeEventos, mayor_porcentaje=True), [self.evento4, self.evento2, self.evento1, self.evento3])

if __name__ == '__main__':
    unittest.main()
