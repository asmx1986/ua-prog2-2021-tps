from notificacion import Notification, Notificacion_amistad, Notificacion_Evento
from totalUsers import TotalUsers
from totalSensors import TotalSensors
from ubicacion import Ubicacion
from sensor import  Sensor
from excepciones import TipoInexistente, CoordenadaInvalida, NoTenesAmigos, ValorInvalido, NoExisteLaPersona,UsuarioNoBloqueado, NoExisteElsolicitador
# from TotalUsers_Anses import TotalUsers, Anses
from abc import ABC, abstractmethod
import unittest
from typeOfEvent import Type
from event import Event
from event_administrator import EventAdministrator

z = Ubicacion(1,1)
x = Ubicacion(1.5,0.5)
v = Ubicacion(-1,-1)
s = Sensor("choque",z)
ss = Sensor("incendio",x)
sss = Sensor("recital",v)



class User(ABC):
    def __init__(self, name, password):
        self.name = name
        self.isactive = True
        self.password = password

    def __repr__(self):
        return self.name

    def Activar(self):
        self.isactive = True

    def desactivar(self):
        self.isactive = False


    def reportEvent(self,tipo,ubicacion,nivel):
        a = "No se ha podido reportar el evento"
        try:
            ubicacion.isOk()
            EventAdministrator.isTipo(tipo)
            if 1 <= int(nivel) <= 5:
                evento = Event(tipo,ubicacion,nivel)
                EventAdministrator.addEvent(evento)
                print("Evento reportado")
            else:
                raise ValorInvalido
        except TipoInexistente:
            print(a)
            print(TipoInexistente.msg)
        except CoordenadaInvalida:
            print(a)
            print(CoordenadaInvalida.msg)
        except ValueError:
           print(a)
           print("Las coordenadas a ingresar deben ser numeros.")
        except ValorInvalido:
            print(a)
            print(ValorInvalido.msg)


class Admin(User):

    def __init__(self,name, password,id):
        super().__init__(name,password)

        self.id = id


    def BanCitizen(self, name):
        try:
            usuario_a_bloquear = TotalUsers.userByName(name)
            usuario_a_bloquear.Ban()
            print('Se ha bloqueado al usuario correctamente')


        except NoExisteLaPersona:
            print(NoExisteLaPersona.msg)


    def UnBanCitizen(self, name):
        try:
            usuario_a_desbloquear = TotalUsers.userByName(name)
            TotalUsers.isnotbanned(usuario_a_desbloquear)
            usuario_a_desbloquear.unban()
            TotalUsers.removeBancitizen(usuario_a_desbloquear)
            print(f'{usuario_a_desbloquear} es libre de utilizar su cuenta nuevamente')
        except NoExisteLaPersona:
            print(NoExisteLaPersona.msg)
        except UsuarioNoBloqueado:
            print(UsuarioNoBloqueado.msg)


    def Create_Type_of_Event(self, name):
        type = Type(name)
        EventAdministrator.addTipoDeEvento(type)
        print('Se ha creado el tipo de evento correctamente')



    def CreateAdmin(self, name,password,id):
        try:
            if not TotalUsers.isId(id):
                admin = Admin(name,password,id)
                TotalUsers.addadmin(admin)
                print('Se ha creado el administrador correctamente')
            else:
                raise Exception
        except Exception:
            print("Ese id ya existe")



    def DeleteAdmin(self, id):
        try:
            if TotalUsers.isId(id):
                amdin_a_borrar = TotalUsers.getId(id)
                TotalUsers.listOfAdmins.remove(amdin_a_borrar)
                print('Se ha eliminado el administrador correctamente')
            else:
                raise Exception
        except Exception:
            print("el id no existe")


    def desactivateSensor(self,sensor):
        try:
            TotalSensors.searchActiveSensor(sensor)
            sensor.desactivate()
        except Exception:
            print("el sensor seleccionado o no existe o no esta activado")



    def activateSensor(self,sensor):
        try:
            TotalSensors.searchDesactiveSensor(sensor)
            sensor.activate()
        except Exception:
            print("el sensor seleccionado o no existe o no esta activado")

    def addSensor(self,tipo,ubicacion):
        try:
            ubicacion.isOk()
            EventAdministrator.isTipo(tipo)
            sensor = Sensor(tipo,ubicacion)
            TotalSensors.addSensor(sensor)
            print("Sensor creado con éxito")
        except TipoInexistente:
            print(TipoInexistente.msg)
        except CoordenadaInvalida:
            print(CoordenadaInvalida.msg)
        except ValueError:
           print("Las coordenadas a ingresar deben ser numeros.")





class Citizen(User):

    listFriends = []
    timesBlocked = 0
    notificationEvents = []
    notificationRequests= []
    isActive = True
    isBanned = False

    def __init__(self,name, passwrord, cuilNumber,phoneNumber):
        super().__init__(name,passwrord)
        self.phoneNumber = phoneNumber
        self.cuil = cuilNumber


    def getInvitations(self):
        return self.notificationEvents

    def getNotifications(self):
        return self.notificationRequests

    def unban(self):
        if self.isBanned:
            self.isBanned = False

    def getBanned(self):
        return self.isBanned

    def __toBan(self):
        if self.timesBlocked == 5:
            self.isBanned = True
            TotalUsers.addbannedUser(self)
            #agregar que lo saque si isActive == True

    def Ban(self):
        self.isBanned = True
        TotalUsers.addbannedUser(self)

    def addRequest(self,request):
        self.notificationRequests.append(request)

    def addRequestEvent(self,request):
        self.notificationEvents.append(request)


    def sendRequest(self, citizen, sender):
        notificacion = Notificacion_amistad(sender)
        citizen.notificationRequests.append(notificacion)
        print("Se ha enviado la solicitud con exito")


    def denyRequest(self, notificacion):
        solicitador = notificacion.getSender()
        for noti in self.notificationRequests:
            if noti.sender == solicitador:
                self.notificationRequests.remove(noti)
                print('Se ha rechazado la solicitud con exito')

                solicitador.timesBlocked += 1
                solicitador.__toBan()

        raise NoExisteElsolicitador

    def notifyFriend(cls, friend, event):
        notifiaction = Notificacion_Evento(friend, event)
        friend.addRequestEvent(notifiaction)


    def acceptRequest(self, notificacion):
        solicitador = notificacion.getSender()
        for noti in self.notificationRequests:
            if noti.sender == solicitador:
                self.listFriends.append(solicitador)
                self.notificationRequests.remove(noti)
                solicitador.listFriends.append(self)
                print('Ha aceptado a su amigo')


class TestAdmin(unittest.TestCase):
    def test_bancitizen(self):
        santi = Citizen("santiago",1,1,'h')
        pedro = Citizen("pedro",2,2,'g')
        santi.sendRequest(pedro,santi)
        self.assertEqual(santi,pedro.notificationRequests[0].getSender())



    def test_identificadordeadmin(self):
        administrador = Admin("facundo",123,4)
        administrador.CreateAdmin("tomas",33,4)
        self.assertEqual(4, administrador.id)


    def test_banCitizen(self):
        administrador = Admin("Ernesto", "godeto",'18')
        santi = Citizen('santi','1234', '2','santi')
        pepe = Citizen('pepe','23141235','1','pepe')
        TotalUsers.addUser(santi)
        TotalUsers.addUser(pepe)
        print(TotalUsers.listOfUsers)
        self.assertEqual('Se ha bloqueado al usuario correctamente',administrador.BanCitizen("2"))
        print(TotalUsers.listOfUsers)
