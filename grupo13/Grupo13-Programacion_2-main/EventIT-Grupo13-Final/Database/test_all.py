import unittest
from Monitoreo.Manipulacion_csv import getRow
from Usuario.U_Login import Login
from Usuario.U_Ciudadano import Ciudadano
from Monitoreo.M_ABM import ABM
from Monitoreo.M_Evento import Event
from Monitoreo.M_Anses import Anses


def sum1(a, b):
    return a + b


class SimpleTest(unittest.TestCase):
    def test_sum134(self):
        result = sum1(1, 4)
        self.assertEqual(result, 5)

    def test_01_ansesconfimar(self):
        result1 = Anses("ciudadano").confirmCuil('20440000001')
        self.assertEqual(result1, True)

    def test_02_registrarse1(self):
        result1 = Login.register("ciudadano", "Testeo1", 11111111111, 11111111111, "pass")
        self.assertEqual(result1, True)

    def test_03_registrarse2(self):
        result2 = Login.register("ciudadano", "Testeo2", 22222222222, 22222222222, "pass")
        self.assertEqual(result2, True)

    def test_04_chekeo_de_info1(self):
        result2 = Login.getInfo("ciudadano", "Testeo2")
        self.assertEqual(result2, ['Testeo2', '22222222222', '22222222222', '0', 'No'])

    def test_05_chekeo_de_info2(self):
        result2 = Login.getInfo("ciudadano", "Testeo1")
        self.assertEqual(result2, ['Testeo1', '11111111111', '11111111111', '0', 'No'])

    def test_06_solicitudes1(self):
        ciu1 = Ciudadano("Testeo1")
        ciu2 = Ciudadano("Testeo2")
        ciu1.sendFriend_Request(ciu2)
        result = ciu2.getfriend_request()
        self.assertEqual(result, ["Testeo1"])

    def test_07_solicitudes2(self):
        ciu2 = Ciudadano("Testeo2")
        ciu2.rejectFriend_Request("Testeo1")
        result = ciu2.getfriend_request()
        self.assertEqual(result, ['Nada que encontrar...'])

    def test_08_solicitudes3(self):
        ciu1 = Ciudadano("Testeo1")
        result = ciu1.getrejected_requests()
        self.assertEqual(result, 1)

    def test_09_solicitudes4(self):
        ciu1 = Ciudadano("Testeo1")
        ciu2 = Ciudadano("Testeo2")
        ciu1.sendFriend_Request(ciu2)
        ciu2.acceptFriend_Request("Testeo1")
        result = ciu2.getfriends()
        self.assertEqual(result, ["Testeo1"])

    def test_10_solicitudes5(self):
        ciu1 = Ciudadano("Testeo1")
        ciu2 = Ciudadano("Testeo2")
        ciu1.delFriend("Testeo2")
        ciu2.delFriend("Testeo1")
        result = ciu2.getfriends()
        self.assertEqual(result, ['Nada que encontrar...'])

    def test_11_evento1(self):
        Event.addType("Testeo tipo 1")
        Event.addEvent("Testeo evento 1", "Testeo tipo 1", 7, 7, "Unitest")
        Event.reportEvent("Testeo evento 1", 10)
        ABM.setAlta("Testeo evento 1")
        result = getRow("evento", "Testeo evento 1")
        self.assertEqual(result, ['Testeo evento 1', 'Testeo tipo 1', '7', '7', 'Alta', 'Unitest', '10'])

    def test_12_evento2(self):
        ciu1 = Ciudadano("Testeo1")
        ciu2 = Ciudadano("Testeo2")
        ciu1.sendFriend_Request(ciu2)
        ciu2.acceptFriend_Request("Testeo1")
        list = ciu2.getfriends()
        Event.reportEvent("Testeo evento 1", list)
        result = Event.getParticipants("Testeo evento 1")
        self.assertEqual(result, 11)

    def test_13_admin1(self):
        ABM.block("Testeo1")
        result = ABM.getBlock("ciudadano", "Name", 'Testeo1')
        self.assertEqual(result, True)

    def test_14_admin2(self):
        ABM.unblock("Testeo1")
        result = ABM.getBlock("ciudadano", "Name", 'Testeo1')
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
