from event import Event
from event_administrator import EventAdministrator

class Ranking:



    @classmethod
    def getRanking(cls):
        eventos = EventAdministrator.actualEvents
        eventos_por_nivel = sorted(eventos, key = lambda event:int(event.level) ,reverse= True)
        return eventos_por_nivel

    @classmethod
    def getZones(cls):
        listOfZones = []
        for event in EventAdministrator.actualEvents:
            if event.getZone() not in listOfZones:
                listOfZones.append(event.getZone())
        return listOfZones

    @classmethod
    def getFinalRanking(cls):
        zonas = []
        for zone in cls.getZones():
            eventos_por_nivel_por_zona = []
            for event in cls.getRanking():
                if event.getZone() == zone:
                    eventos_por_nivel_por_zona.append(event)
            zonas.append([zone,eventos_por_nivel_por_zona])
        return zonas

    @classmethod
    def GetStatistics(cls):
        for element in Ranking.getFinalRanking():
            print(f'Zona: {element[0]},  Eventos: {element[1]}')





