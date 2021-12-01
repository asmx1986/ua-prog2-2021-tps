from EventIT.MapsSist.MapClass import Map
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.EventLib.RegDeEventosClass import RegDeEventos


class Estadisticas:
    @classmethod
    def calculate_number_of_attendees_per_zone_per_event(cls, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        """Calcula la cantidad de asistentes que asistieron a un evento y que viven en la misma zona donde se realizo el evento"""
        lista_de_zonas = map.getListaDeZonas()
        lista_de_eventos = regDeEventos.View_Events()
        cantidad_de_asistentes_x_zona_x_evento = dict({})
        for evento in lista_de_eventos:
            cantidad_de_asistentes_x_zona_x_evento[evento] = 0
        for evento in lista_de_eventos:
            for asistente in evento.getListaDeAsistencia():
                if evento.getZona(lista_de_zonas) == datasetANSES.searchUser(int(asistente.Get_Telefono()), int(asistente.Get_Cuil())).getZona(lista_de_zonas): #compara la zona del evento con la zona del asistente obtenida en el datasetANSES
                    cantidad_de_asistentes_x_zona_x_evento[evento] += 1
        return cantidad_de_asistentes_x_zona_x_evento

    @classmethod
    def calculate_total_number_of_attendees(cls, regDeEventos: RegDeEventos):
        lista_de_eventos = regDeEventos.View_Events()
        cantidad_de_asistentes_totales_x_evento = dict({})
        for evento in lista_de_eventos:
            cantidad_de_asistentes_totales_x_evento[evento] = len(evento.getListaDeAsistencia())
        return cantidad_de_asistentes_totales_x_evento

    @classmethod
    def calculate_percentage_of_atendees_of_the_zone(cls, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        lista_de_eventos = regDeEventos.View_Events()
        porcentaje_de_asistentes_de_la_zona_por_evento =dict({})
        for evento in lista_de_eventos:
            if cls.calculate_total_number_of_attendees(regDeEventos)[evento] != 0:
                porcentaje_de_asistentes_de_la_zona_por_evento[evento] = round((cls.calculate_number_of_attendees_per_zone_per_event(map, datasetANSES, regDeEventos)[evento]/cls.calculate_total_number_of_attendees(regDeEventos)[evento]) * 100, 1)
            else:
                porcentaje_de_asistentes_de_la_zona_por_evento[evento] = 0.0
        return porcentaje_de_asistentes_de_la_zona_por_evento

    @classmethod
    def calculate_positions_of_the_ranking(cls,  map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos, mayor_cantidad_de_asistentes_de_la_zona: bool = False, mayor_cantidad_de_asistentes: bool = False, mayor_porcentaje: bool = False):
        """Calcula el ranking de eventos en orden descendente segun el parametro que elija"""
        ranking = regDeEventos.View_Events()
        if mayor_cantidad_de_asistentes_de_la_zona or not (mayor_cantidad_de_asistentes_de_la_zona or mayor_cantidad_de_asistentes or mayor_porcentaje):
            ranking.sort(key=lambda x:cls.calculate_number_of_attendees_per_zone_per_event(map, datasetANSES, regDeEventos)[x], reverse=True)# Ordena la lista de eventos poniendo en primer lugar al evento con mas asistentes de la zona
            return ranking
        elif mayor_cantidad_de_asistentes:
            ranking.sort(key=lambda x:cls.calculate_total_number_of_attendees(regDeEventos)[x], reverse=True)# Ordena la lista de eventos poniendo en primer lugar al evento con mas asistentes de la zona
            return ranking
        elif mayor_porcentaje:
            ranking.sort(key=lambda x:cls.calculate_percentage_of_atendees_of_the_zone(map, datasetANSES, regDeEventos)[x], reverse=True)# Ordena la lista de eventos poniendo en primer lugar al evento con mas asistentes de la zona
            return ranking

    @classmethod
    def calculate_ranking(cls, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos, mayor_cantidad_de_asistentes_de_la_zona: bool = False, mayor_cantidad_de_asistentes: bool = False, mayor_porcentaje: bool = False):
        rankingString = f"|\t\tPosicion\t\t|\tNombre del evento\t|\tZona\t|\tCantidad de personas por zona\t|\tCantidad de personas totales\t|\tPorcentaje de asistentes de la zona\t|\t\t\n"
        for index, evento in enumerate(Estadisticas.calculate_positions_of_the_ranking(map, datasetANSES, regDeEventos, mayor_cantidad_de_asistentes_de_la_zona, mayor_cantidad_de_asistentes, mayor_porcentaje)): # arma el ranking en formato string para imprmirlo
            rankingString += f"|\t\t{index + 1}\t\t|\t\t{evento}\t\t|\t{evento.getZona(map.getListaDeZonas())}\t|" \
                                  f"\t\t\t{Estadisticas.calculate_number_of_attendees_per_zone_per_event(map, datasetANSES, regDeEventos)[evento]}\t\t|" \
                                  f"\t\t\t{Estadisticas.calculate_total_number_of_attendees(regDeEventos)[evento]}\t\t|" \
                                  f"\t\t\t{Estadisticas.calculate_percentage_of_atendees_of_the_zone(map, datasetANSES, regDeEventos)[evento]}%\t\t|\t\t\n"
        return rankingString



    @classmethod
    def calculate_event_attendance_maximums(cls, map: Map, datasetANSES: DatasetANSES, regDeEventos: RegDeEventos):
        """Calcula el evneto con mas asistentes en el momento (picos de asistencia)"""
        return cls.calculate_positions_of_the_ranking(map, datasetANSES, regDeEventos, mayor_cantidad_de_asistentes=True)[0]

