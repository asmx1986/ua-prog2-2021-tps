from event import Event
from event_administrator import EventAdministrator
from Anses import Anses
from totalSensors import TotalSensors
from ubicacion import  Ubicacion

class Sensor:
    def __init__(self, Type_of_event,location):
        self.type_of_event = Type_of_event
        self.location = location
        self.zone = Anses.GetZone(location)
        self.isActive = True

    def __repr__(self):
        return f"sensor de: {self.type_of_event}, ubicación en coordenadas: {self.location}"

    def activate(self):
        self.isActive = True
        TotalSensors.ActivateSensor(self)

    def desactivate(self):
        self.isActive = False
        TotalSensors.DesactiveSensor(self)

    def reportEvent(self,nivel):
        evento = Event(self.type_of_event,self.location,nivel)
        EventAdministrator.addEvent(evento)


