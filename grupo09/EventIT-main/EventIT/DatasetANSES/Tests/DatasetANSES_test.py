import unittest
from EventIT.DatasetANSES.DatasetANSES import DatasetANSES

class TestDatasetANSES(unittest.TestCase):
    def test_make_the_list_of_users(self):
        datasetANSES = DatasetANSES()
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[0].getName(), 'Lucas.Perez')
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getName(), 'Joaquin.Hernandez')
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[0].getTelCell(), 1111)
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getTelCell(), 2222)
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getCuil(), 13131313)
        self.assertEqual(datasetANSES.getListOfUsuariosANSES()[1].getUbicacion().Get_Coordinates(), (17, 17))


if __name__ == '__main__':
    unittest.main()
