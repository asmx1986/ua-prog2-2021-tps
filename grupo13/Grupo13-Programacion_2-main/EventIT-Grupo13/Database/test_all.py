import unittest

from Usuario.U_Login import Login
from Usuario.U_Ciudadano import Ciudadano
from Monitoreo.M_ABM import ABM
from Monitoreo.M_Evento import Evento
from Usuario.U_Administrador import Admin
from Monitoreo.M_Anses import Anses


def sum1(a, b):
    return a + b


class SimpleTest(unittest.TestCase):
    def test_sum134(self):
        result = sum1(1, 4)
        self.assertEqual(result, 5)

    def test_ansesconfimar(self):
        result1 = Anses("ciudadano").confirmarCuil('20440000001')
        self.assertEqual(result1, True)

    def test_chekeo_de_info(self):
        result2 = Login.getInfo("ciudadano", "Facu")
        self.assertEqual(result2, ['Facu', '20440000001', '15123456', '1', '1', 'n', '0'])

    def test_solicitudes1(self):
        ciu1 = Ciudadano(20440000001, 15123456, "mimama")
        ciu2 = Ciudadano(20440000011, 15123457, "ayuda")
        ciu3 = Ciudadano(20441010101, 15101010, "siu")
        ciu1.enviarSolicitud(ciu2)
        result = ciu2.getSolicitud()
        self.assertEqual(result, [20440000001])

    def test_solicitudes2(self):
        ciu1 = Ciudadano(20440000001, 15123456, "mimama")
        ciu2 = Ciudadano(20440000011, 15123457, "ayuda")
        ciu3 = Ciudadano(20441010101, 15101010, "siu")
        ciu2.enviarSolicitud(ciu1)
        result = ciu1.getSolicitud()
        self.assertEqual(result, [20440000011])

    def test_solicitudes3(self):
        ciu1 = Ciudadano(20440000001, 15123456, "mimama")
        ciu2 = Ciudadano(20440000011, 15123457, "ayuda")
        ciu3 = Ciudadano(20441010101, 15101010, "siu")
        ciu2.enviarSolicitud(ciu1)
        ciu3.enviarSolicitud(ciu1)
        result = ciu1.getSolicitud()
        self.assertEqual(result, [20440000011, 20441010101])

    def test_solicitudes4(self):
        ciu1 = Ciudadano(20440000001, 15123456, "mimama")
        ciu2 = Ciudadano(20440000011, 15123457, "ayuda")
        ciu3 = Ciudadano(20441010101, 15101010, "siu")
        ciu1.enviarSolicitud(ciu2)
        ciu3.enviarSolicitud(ciu2)
        ciu2.aceptarSolictud(0)
        ciu2.aceptarSolictud(0)
        result = ciu2.getAmigos()
        self.assertEqual(result, [20440000001, 20441010101])

    def test_evento1(self):
        ciu1 = Ciudadano(20440000001, 15123456, "mimama")
        g = Evento("Plaza", "c", "3")
        ciu1.reportarEvento(g)
        result = g.getNumParticipantes()
        self.assertEqual(result, 1)

    def test_evento2(self):
        ciu1 = Ciudadano(20440000001, 15123456, "mimama")
        ciu2 = Ciudadano(20440000011, 15123457, "ayuda")
        g = Evento("Plaza", "c", "3")
        ciu2.reportarEvento(g)
        ciu1.reportarEvento(g)
        result = g.getNumParticipantes()
        self.assertEqual(result, 2)

    def test_sensor1(self):
        a = Evento("Prueba", "a", "1")
        result = a.getTipo()
        self.assertEqual(result, "Prueba")

    def test_sensor2(self):
        a = Evento("Concierto", "a", "1")
        result = a.getTipo()
        self.assertEqual(result, "Concierto")

    def test_zadmin(self):
        Admin(99999999999, 3777392328, "patas").Bloquear("Facu")
        bloc = ABM.getBlock("ciudadano", "Nombre", "Facu")
        self.assertEqual(bloc, True)

    def test_registro(self):
        Anses("ciudadano").agregarCuil("99999999911")
        ABM.agregarUsuario("Hola", "contra", 99999999911, 3777393939, "1", "7")
        Ciudadano(99999999911, 3777393939, "contra")

    def test_zsolicitudes5(self):
        ciu = Ciudadano(20440000001, 15123456, "mimama")
        ciu2 = Ciudadano(20440000011, 15123457, "ayuda")
        ciu3 = Ciudadano(20441010101, 15101010, "siu")
        ciu.enviarSolicitud(ciu2)
        ciu3.enviarSolicitud(ciu2)
        ciu3.enviarSolicitud(ciu2)
        ciu3.enviarSolicitud(ciu2)
        ciu3.enviarSolicitud(ciu2)
        ciu3.enviarSolicitud(ciu2)
        ciu2.aceptarSolictud(0)
        ciu2.rechazarSolicitud(0, ciu3)
        ciu2.rechazarSolicitud(0, ciu3)
        ciu2.rechazarSolicitud(0, ciu3)
        ciu2.rechazarSolicitud(0, ciu3)
        ciu2.rechazarSolicitud(0, ciu3)
        ciu3.getRechazadas()
        result = ABM.getBlock("ciudadano", "Cuil", 20441010101)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
