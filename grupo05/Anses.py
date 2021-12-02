import csv
from ubicacion import Ubicacion
from admin_zones import  Admin_zones

class Anses:
    @classmethod
    def GetZone(cls, location):
        with open("zonas.csv") as csv_file:
            zonas = csv.reader(csv_file, delimiter = ",")
            for row in zonas:
                zona = row[0]
                Xi = int(row[1])
                Xf = int(row[2])
                Yi = int(row[3])
                Yf = int(row[4])
                if Xi <= float(location.getX()) < Xf and Yi <= float(location.getY()) < Yf:
                    Admin_zones.addZone(zona)
                    return zona


    @classmethod
    def existPerson(cls,cuil):
        with open("personas.csv") as csv_file:
            personas = csv.reader(csv_file, delimiter = ",")
            for row in personas:
                if row[2] == cuil:
                    return True
            return False


import unittest

class Test(unittest.TestCase):

    def test_existPerson(self):
        self.assertEqual(True, Anses.existPerson(20443626027))

