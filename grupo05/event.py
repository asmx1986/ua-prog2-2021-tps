from typeOfEvent import Type
from Anses import Anses
from ubicacion import Ubicacion
from datetime import  datetime
class Event:
    #activness = True
    fecha = datetime.now()

    def __init__(self, type,location,level):
        self.type = type
        self.location = location
        self.level = level
        self.zone = Anses.GetZone(self.location)

    def __repr__(self):
        return f"Evento de tipo: {self.type}, de nivel: {self.level}"


    def getZone(self):
        return self.zone

import unittest

class Test(unittest.TestCase):

     def test_getZone(self):
         ubicacion = Ubicacion(2,8)
         choque = Event("accidente", ubicacion ,1)
         self.assertEqual("Tigre", choque.getZone())
