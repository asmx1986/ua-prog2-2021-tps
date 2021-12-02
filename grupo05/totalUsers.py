from excepciones import NoExisteLaPersona, UsuarioBloqueado, UsuarioNoBloqueado
#from user import Admin,Citizen

class TotalUsers:

    listOfUsers = []
    listOfAdmins = []
    usuarios_bloqueados = []

    @classmethod
    def isId(cls,id):
        for admin in cls.listOfAdmins:
            if admin.id == id:
                return True
        return False


    @classmethod
    def isbanned(cls,name):
        for user in cls.usuarios_bloqueados:
            if user.name == name:
                raise UsuarioBloqueado

    @classmethod
    def isnotbanned(cls,usuario):
        for user in cls.usuarios_bloqueados:
            if user == usuario:
                return True
        raise UsuarioNoBloqueado

    @classmethod
    def removeBancitizen(cls,user):
        for citizen in cls.usuarios_bloqueados:
            if citizen == user:
                cls.usuarios_bloqueados.remove(citizen)



    @classmethod
    def isUser(cls,cuil):
        for user in cls.listOfUsers:
            if user.cuil == cuil:
                return True
            else:
                raise Exception

    @classmethod
    def userByName(cls, name):
        a = 0
        for user in cls.listOfUsers:
            if user.name == name:
                a = 1
                return user
        if a == 0:
            raise NoExisteLaPersona




    @classmethod
    def getId(cls,id):
        for admin in cls.listOfAdmins:
            if admin.id == id:
                return admin

    @classmethod
    def getUser(cls,cuil):
        for user in cls.listOfUsers:
            if user.cuil == cuil:
                return user
        else:
            raise Exception

    @classmethod
    def addUser(cls,user):
        cls.listOfUsers.append(user)

    @classmethod
    def addadmin(cls,admin):
        cls.listOfAdmins.append(admin)

    @classmethod
    def addbannedUser(cls,user):
        cls.usuarios_bloqueados.append(user)


import unittest

class Test(unittest.TestCase):

    def test_getUser(self):
        administrador = Admin("Ernesto", "godeto",'18')
        santi = Citizen('santi','1234', '2','santi')
        pepe = Citizen('pepe','23141235','1','pepe')
        TotalUsers.listOfUsers.append(santi)
        TotalUsers.listOfUsers.append(pepe)
        TotalUsers.listOfAdmins.append(administrador)
        self.assertEqual(santi, TotalUsers.getUser("2"))



    def test_isUSer(self):
        administrador = Admin("Ernesto", "godeto",'18')
        santi = Citizen('santi','1234', '2','santi')
        pepe = Citizen('pepe','23141235','1','pepe')
        TotalUsers.listOfUsers.append(santi)
        TotalUsers.listOfUsers.append(pepe)
        TotalUsers.listOfAdmins.append(administrador)
        self.assertEqual(True, TotalUsers.isUser("2"))
