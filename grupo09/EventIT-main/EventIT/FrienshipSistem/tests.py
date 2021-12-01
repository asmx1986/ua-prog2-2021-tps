import unittest
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.FrienshipSistem.FrienshipSist import Frienship_System
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.RegUsr = RegDeUsuarios()
        self.Juan = Ciudadano("juan",111,123)
        self.tom = Ciudadano("TOM",000,999)
        self.Marco = Ciudadano("Marco",100,987)

        self.RegUsr.Manage_Ciudadanos(self.Juan,True,'JUAN')
        self.RegUsr.Manage_Ciudadanos(self.tom,True,"tom")
        self.RegUsr.Manage_Ciudadanos(self.Marco, True,"Marco")


    def test_enviar_solicitud(self):
        Frienship_System.EnviarSolicitud(self.RegUsr, 123,999,111,000)
        self.assertEqual(self.RegUsr.Get_Ciudadanos(),{"Marco": [self.Marco, 0], 'JUAN': [self.Juan, 0], 'tom': [self.tom, 0]})
        self.assertEqual(self.tom.Get_ListaDeSolicitudes(),[self.Juan])


    def test_aceptar_y_rechazar(self):
        Frienship_System.EnviarSolicitud(self.RegUsr, 123,999,111,000)#Juan le envia a Tomas
        Frienship_System.EnviarSolicitud(self.RegUsr, CuilSolicitante= 999, CuilDestinatario=987)#Tomas le envia a Marco

        Frienship_System.AceptarSolicitud(self.RegUsr, CelSolicitante=111, CelDestinatario=000)#Tomas acepta a Juan
        Frienship_System.RechazarSolicitud(self.RegUsr, CuilSolicitante=999, CuilDestinatario=987)#Marco rechaza a Tomas

        self.assertEqual(self.Juan.Get_ContactosDeInteres(),[self.tom])
        self.assertEqual(self.tom.Get_ContactosDeInteres(),[self.Juan])
        self.assertEqual(self.tom.Get_ListaDeRechazos(),[self.Marco])
        self.assertEqual(self.tom.Get_ListaDeSolicitudes(),[])
        self.assertEqual(self.Marco.Get_ContactosDeInteres(),[])




if __name__ == '__main__':
    unittest.main()
