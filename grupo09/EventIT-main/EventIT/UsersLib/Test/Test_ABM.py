import unittest

from EventIT.UsersLib.ABM import ABM
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.UsersLib.AdminClass import Administrator


class Test_Modificar(unittest.TestCase):
    def test_modificar_nombre(self): 
        ciudadano_1 = Ciudadano("Juan", 1, 2)
        ABM.modificar_name("Pedro", ciudadano_1)
        self.assertEqual("Pedro", ciudadano_1.Get_Name())

    def test_modificar_tel(self):
        ciudadano_1 = Ciudadano("Daniel", 1, 1234)  # Aca es un int, eso probablemente de un error, tenerlo en cuenta, no da error.
        ABM.modificar_tel(2, ciudadano_1)  # Aca se modifica el telefono
        self.assertEqual(2, ciudadano_1.Get_Telefono())

        ciudadano_2 = Ciudadano("Pedro", 4, 1234)
        ABM.modificar_tel(1, ciudadano_2)
        self.assertEqual(1, ciudadano_2.Get_Telefono())

    def test_modificar_cuil(self): # Pasa
        ciudadano_1 = Ciudadano("Francisco", 1112345678, 4321)
        ABM.modificar_cuil(1234, ciudadano_1)  # Aca se modifica el cuil
        self.assertEqual(1234, ciudadano_1.Get_Cuil())
        
# ------------------------------------
# ------------------------------------

class Test_ABM_bloq_desbloq(unittest.TestCase): 
    def test_bloq(self):
        self.reg_de_usuarios = RegDeUsuarios()
        self.ciudadano_1 = Ciudadano("Adrian", 3, 1234)
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_1, True, "Adrian")
        self.reg_de_usuarios.estado_de_bloqueo(True, "Adrian")

        ABM.bloquear_desbloquear(True, self.reg_de_usuarios, "Adrian")
        self.assertEqual(self.reg_de_usuarios.Get_Ciudadanos()["Adrian"][1], True)
        
    def test_desbloq(self):
        self.reg_de_usuarios = RegDeUsuarios()
        self.ciudadano_1 = Ciudadano("Oliver", 8, 1912)
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_1, True, "Oliver")
        self.reg_de_usuarios.estado_de_bloqueo(False, "Oliver") # Con esto condiciono que quiero desbloquear a Oliver

        ABM.bloquear_desbloquear(False, self.reg_de_usuarios, "Oliver")
        self.assertEqual(self.reg_de_usuarios.Get_Ciudadanos()["Oliver"][1], False) 

# ------------------------------------
# ------------------------------------

class test_dar_baja_o_alta(unittest.TestCase):
    def test_dar_de_baja_a_ciudadanos(self):
        self.reg_de_usuarios = RegDeUsuarios() # Cuando se agrega el self. se le puede aplicar cada metodo que tiene la clase a la cual hace referencia.
        self.ciudadano_1 = Ciudadano("Roberto", 1,1234)
        self.ciudadano_2 = Ciudadano("Bruno", 2, 4321)
        self.ciudadano_3 = Ciudadano("Pablo", 3, 3214)

        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_1, True, "Roberto") # Acá los agrego
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_2, True, "Bruno")
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_3, True, "Pablo")

        ABM.dar_baja("Roberto", 1, 1234, self.reg_de_usuarios)
        ABM.dar_baja("Pablo", 3, 3214, self.reg_de_usuarios)

        self.assertEqual(len(self.reg_de_usuarios.Get_Ciudadanos()), 1)
        
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_1, True, "Roberto") # Acá los agrego
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_2, True, "Bruno")
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_3, True, "Pablo")

        ABM.dar_baja("Roberto", 1, 1234, self.reg_de_usuarios)

        self.assertEqual(len(self.reg_de_usuarios.Get_Ciudadanos()), 2) # Me quedan Bruno y Pablo (2 ciudadanos)

        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_1, True, "Roberto") # Acá los agrego
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_2, True, "Bruno")
        self.reg_de_usuarios.Manage_Ciudadanos(self.ciudadano_3, True, "Pablo")

        ABM.dar_baja("Roberto", 1, 1234, self.reg_de_usuarios) # Acá los doy de baja a los tres ciudadanos
        ABM.dar_baja("Bruno", 2, 4321, self.reg_de_usuarios)
        ABM.dar_baja("Pablo", 3, 3214, self.reg_de_usuarios)

        self.assertEqual(len(self.reg_de_usuarios.Get_Ciudadanos()), 0) # Acá elimina los dos ciudadanos que tengo, por lo que deberian ser 0 ciudadanos.

    def test_dar_alta(self):
        self.reg_de_usuarios =  RegDeUsuarios()
        self.ciudadano_1 = Ciudadano("Roberto", 1,1234)
        self.ciudadano_2 = Ciudadano("Bruno", 2, 4321)
        self.ciudadano_3 = Ciudadano("Pablo", 3, 3214)
        ABM.dar_alta("Roberto",1, 1234, self.reg_de_usuarios)
        ABM.dar_alta("Bruno", 2, 4321, self.reg_de_usuarios)
        ABM.dar_alta("Pablo", 3, 3214, self.reg_de_usuarios)

        self.assertEqual(len(self.reg_de_usuarios.Get_Ciudadanos()), 3)

        admin1 = Administrator('Tomas')
        ABM.agregar_admin('Tomas', self.reg_de_usuarios, admin1)
        self.assertEqual(self.reg_de_usuarios.Get_Admins()['Tomas'].Get_Name(), 'Tomas')


if __name__=='__main__':
    unittest.main()
