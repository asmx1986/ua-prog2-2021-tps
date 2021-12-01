import unittest
from EventIT.UserManagementLib.CreateProfileClass import CreateProfile
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios


class TestCreateNewProfile(unittest.TestCase):
    def setUp(self):
        self.regdeusuarios = RegDeUsuarios()
        self.datasetanses = DatasetANSES()

    def test_valid_user(self):
        value = CreateProfile.ValidarUsuario("43807968", "1150042603", self.datasetanses)
        self.assertEqual(value, True)

    def test_add_user_to_reg(self):
        CreateProfile.Create_Profile("user", "Juan","1150042603", "43807968", self.regdeusuarios, self.datasetanses)
        self.assertEqual(len(self.regdeusuarios.Get_Ciudadanos()), 1)







