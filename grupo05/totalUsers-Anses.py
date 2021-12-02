from user import Citizen

class TotalUsers:

     listOfUsers = []
     listOfAdmins = []

import unittest

class Test(unittest.TestCase): #revisar
    def Test_1(self):
        facundo = Citizen(1, 123)
        citizens = [facundo]
        anses = Anses()
        anses.citizens = citizens
        self.assertEqual(True, anses.findCitizen(facundo))
