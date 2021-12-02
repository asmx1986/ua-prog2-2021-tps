import csv
from typeOfEvent import Type
from ubicacion import Ubicacion
import csv
from typeOfEvent import Type
from ubicacion import Ubicacion
from event import Event
from excepciones import TipoInexistente, EventoNoEncontrado

class EventAdministrator:

    actualEvents = []
    tipos_de_eventos = []

    @classmethod
    def addTipoDeEvento(cls,tipo):
        cls.tipos_de_eventos.append(tipo)


    @classmethod
    def addEvent(cls,event):
        cls.actualEvents.append(event)

    @classmethod
    def RemoveEvent(cls,event):
        cls.actualEvents.remove(event)

    @classmethod
    def findEvent(cls, event):
        for evento in cls.actualEvents:
            if evento.type == event:
                return event
        else:
            raise EventoNoEncontrado

    @classmethod
    def isTipo(cls, tipo):
        for tipo_de_evento in cls.tipos_de_eventos:
            if tipo == tipo_de_evento.name:
                return True
        else:
            raise TipoInexistente

import unittest

class Test(unittest.TestCase):

    def test_zona(self):
        type = Type("seguridad")
        Ubicacion = (1,3)
        event = Event(type,Ubicacion,3)
        EventAdministrator.addEvent(event)
        EventAdministrator.filterByZone()
        self.assertEqual("Tigre", event.zone)
