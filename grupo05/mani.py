from totalUsers import TotalUsers
from user import User, Citizen, Admin
from Anses import Anses
from event_administrator import EventAdministrator
from notificacion import Notificacion_amistad, Notificacion_Evento
from totalSensors import TotalSensors
from ubicacion import Ubicacion
from sensor import Sensor
from ranking import Ranking
from excepciones import NivelInvalido, EventoNoEncontrado, NoExisteLaPersona, NoTenesAmigos, UsuarioBloqueado, NoExisteElsolicitador
import grafico
from event import Event
from typeOfEvent import Type



def Menu():
    a = input(f'Bienvenido a EventTlT \nComo desea ingresar\n1.Como Usuario|2.Como Admin|3.Ingresar como sensor|4.Cerrar Sesion|5.Ver mapa\nElija una opcion: ')
    if a == '1':
        return Usuario()
    elif a == '2':
        return admin()
    elif a =='3':
        return ingresarComoSensor()
    elif a == '4':
        print("Tablero de estadísticas de eventos:")
        print("")
        Ranking.GetStatistics()
        print("")
        print('Muchas Gracias por utilizar nuestra plataforma')
    elif a == "5":
        grafico.mapa()
        return Menu()
    else:
        print('El valor ingresado no corresponde a ninguna accion')
        return Menu()

def admin():
    i = input("Ingrese su ID: ")
    pp = input ("Ingrese su contraseña: ")
    a = 0
    for persona in TotalUsers.listOfAdmins:
        if persona.id == i:
            if persona.password == pp:
                a = 1
                print("Ha ingresado correctamente como administrador")
                return adminMenu(persona)
            else:
                a = 1
                print ("Su contrasenia es incorrecta")
                return admin()
    if a == 0:
        print ("Su ID es incorrecto")
        return admin()

def adminMenu(persona):
    s= input("1.Bloquear Usuario |2.Desbloquear usuario |3.Crear Administrador |4. Eliminar administrador |5.Crear tipo de evento |6. Crear Sensor|7. Reportar evento|8. Salir\nElija su respuesta: ")
    if s == '1':
        #print(TotalUsers.listOfUsers)
        #print(TotalUsers.usuarios_bloqueados)
        name = input("Inserte nombre del usuario: ")
        try:
            TotalUsers.isbanned(name)
            persona.BanCitizen(name)
            return adminMenu(persona)
        except UsuarioBloqueado:
            print(UsuarioBloqueado.msg)
            return adminMenu(persona)

    elif s == '2':
         name = input("Inserte el nombre del usuario: ")
         persona.UnBanCitizen(name)
         return adminMenu(persona)

    elif s == '3':
        nom = input("Inserte nombre del nuevo administrador: ")
        id = input("Inserte ID: ")
        passw = input("Inserte su contraseña: ")
        persona.CreateAdmin (nom, passw, id)
        return adminMenu(persona)
    elif s == '4':
        i = input("Inserte ID: ")
        persona.DeleteAdmin(i)
        return adminMenu(persona)
    elif s == '5':
        nombre = input('Que nombre le quiere asignar a los eventos: ')
        persona.Create_Type_of_Event(nombre)
        return adminMenu(persona)
    elif s == '8':
        return Menu()

    elif s == '6':
        tipo = input('Ingrese tipo de evento: ')
        lugarX = input('Ingrese la ubicacion en x:')
        lugarY = input('Ingrese la ubicacion en y:')
        ubicacion = Ubicacion(lugarX,lugarY)
        persona.addSensor(tipo,ubicacion)
        return adminMenu(persona)

    elif s == "7":
        print(f"Tipos de eventos: {EventAdministrator.tipos_de_eventos}")
        tipo = input('Ingrese tipo de evento: ')
        lugarX = input('Ingrese la ubicacion en x:')
        lugarY = input('Ingrese la ubicacion en y:')
        ubicacion = Ubicacion(lugarX,lugarY)
        nivel = input("ingrese el nivel del evento: ")
        persona.reportEvent(tipo,ubicacion,int(nivel))
        return adminMenu(persona)

    else:
        return adminMenu(persona)


def Usuario():
    a = input('1.Registrarse|2.iniciar sesion\nIngrese una rta: ')
    if a == '1':
        return Registrarse()
    elif a == '2':
        return  IniciarSesion()
    else:
        print("Elija un valor válido")
        return Menu()


def userMenu(person):
    a = input ("1. Enviar solicitud de amistad|2. Rechazar solicitud de amistad|3. Aceptar solicitud de amistad|4. Notificar amigo de un evento|5. Ver solicitudes de amistad|6. Reportar evento|7.ver eventidos compartidos|8. Salir\nElija su respuesta: ")
    if a == '1':
        s = input('Ingresar nombre del amigo que desea agregar: ')
        try:
            r = TotalUsers.userByName(s)
            person.sendRequest(r, person)
            return userMenu(person)

        except NoExisteLaPersona:
            print(NoExisteLaPersona.msg)
            return userMenu(person)

    elif a =='2':
        s = input('Ingresar nombre del amigo para rechazar su solicitud: ')
        try:
            r = TotalUsers.userByName(s)
            noti = Notificacion_amistad(r)
            person.denyRequest(noti)
            return userMenu(person)

        except NoExisteLaPersona:
            print(NoExisteLaPersona.msg)
            return userMenu(person)
        except NoExisteElsolicitador:
            print(NoExisteElsolicitador.msg)
            return userMenu(person)

    elif a == '3':
        s = input('Ingresar nombre del amigo para aceptar su solicitud: ')
        try:
            r = TotalUsers.userByName(s)
            noti = Notificacion_amistad(r)
            person.acceptRequest(noti)
            return userMenu(person)

        except NoExisteLaPersona:
            print(NoExisteLaPersona.msg)
            return userMenu(person)

    elif a == '4':
        try:
            s = input('Ingresar nombre del amigo al que desea notificar un evento: ')
            e = input(f'Ingresar el nombre del evento que desea compartir con {s}: ')
            r = TotalUsers.userByName(s)
            t = EventAdministrator.findEvent(e)
            person.notifyFriend(r, t)
            print('Evento compartido con exito!')
            return userMenu(person)
        except NoTenesAmigos:
            print(NoTenesAmigos.msg)
            return userMenu(person)
        except EventoNoEncontrado:
            print(EventoNoEncontrado.msg)
            return userMenu(person)
        except NoExisteLaPersona:
            print(NoExisteLaPersona.msg)
            return userMenu(person)

    elif a == '5':
        print(person.getNotifications())
        return userMenu(person)

    elif a == "6":
        print(f"Tipos de eventos: {EventAdministrator.tipos_de_eventos}")
        tipo = input('Ingrese tipo de evento: ')
        lugarX = input('Ingrese la ubicacion en x:')
        lugarY = input('Ingrese la ubicacion en y:')
        ubicacion = Ubicacion(lugarX,lugarY)
        nivel = input("ingrese el nivel del evento: ")
        person.reportEvent(tipo,ubicacion,nivel)
        return userMenu(person)

    elif a == "7":
        print(person.getInvitations())
        return userMenu(person)

    elif a == '8':
        return Menu()

    else:
        print("El valor ingresado no corresponde a ninguna accion. Intente denuevo.")
        return userMenu(person)

def Registrarse():
    c = input(("Inserte Cuil: "))
    nombre = input('Inserte su nombre: ')
    if Anses.existPerson(c):
        a = 0
        for person in TotalUsers.listOfUsers:
            if person.cuil == c:
                a = 1
                print('El usuario ya existe')
                return Registrarse()
            elif person.name == nombre:
                a = 1
                print('Ese nombre no esta disponible')
                return Registrarse()
        if a == 0:
            contra = input('Inserte la contraseña: ')
            try:
                tel = int(input('Inserte su numero de telefono: '))
            except ValueError:
                print('El numero ingresado no es valido, vuelva a completar los datos.')
                return Registrarse()
            User = Citizen(nombre, tel, c, contra)
            TotalUsers.addUser(User)
            print('Se ha registrado correctamente')
            return userMenu(User)
    else:
        print('Su cuil no existe')
        return Registrarse()

def IniciarSesion():
    n = input('Ingrese su nombre: ')
    contra = input('Ingrese su contraseña: ')
    a = 0
    for person in TotalUsers.listOfUsers:
        if person.name == n:
            if person.password == contra and person.isBanned == False:
                a = 1
                print('Se ha inciado sesion correctamente')
                return userMenu(person)
            elif person.isBanned == False:
                a =1
                print('Contraseña incorrecta')
                return Menu()
            elif person.password == contra:
                a = 1
                print('Este usuario esta baneado')
                return Menu()
    if a == 0:
        print('Su usuario es incorrecto')
        return Menu()

def ingresarComoSensor():
    for sensor in TotalSensors.ActiveSensors:
        print(sensor)
    x = input("ingrese la coordenada en x:")
    y = input("ingrese la coordenada en y:")
    try:
        float(x)
        float(y)
        if TotalSensors.existActiveSensor(x,y) != None:
            print("ingresando como sensor...")
            sensor = TotalSensors.existActiveSensor(x,y)
            print(sensor)
            b = True
            while b:
                try:
                    nivel_de_evento = int(input("ingrese el nivel del evento que desea reportar"))
                    if 1 <= nivel_de_evento <= 5:
                        sensor.reportEvent(nivel_de_evento)
                        print("evento reportado")
                        print("volviendo al menu...")
                        b = False
                    else:
                        raise NivelInvalido
                except ValueError:
                    print("debe ingresar un número")
                    b = True
                except NivelInvalido:
                    print(NivelInvalido.msg)
                    b = True
        else:
            raise Exception
    except Exception:
        print("las coordenadas ingresadas no corresponden a ningún sensor")
    return Menu()


administrador = Admin("Ernesto", "godeto",'18')
santi = Citizen('santi','1234', '2','santi')
pepe = Citizen('pepe','1234','1','pepe')
TotalUsers.addUser(santi)
TotalUsers.addUser(pepe)
TotalUsers.addadmin(administrador)
u = Ubicacion(0.8,1.9)
a = Ubicacion(1.3,1)
b = Ubicacion(-1,0.9)
c = Ubicacion(0,1)
uu = Ubicacion(-0.5,1.4)
uuu= Ubicacion(0,1)
xxx = Ubicacion(-0.2,-0.5)
xxxx = Ubicacion(-0.3,-0.8)
xxxxx = Ubicacion(1.1,0.3)
xxxxxx = Ubicacion(1.5,-1)
concierto = Event("concierto", xxx, 1)
baile = Event("baile", xxxx, 2)
balada = Event("balada", xxxxx, 3)
duko = Event("duko", xxxxxx, 4)
uuuu = Ubicacion(-0.8,0)
choque = Event("choque",u,4)
ncendio = Event("incendio",uu,2)
recital = Event("recital",uuu,4)
cabalgata = Event("cabalgata",a,4)
toreda = Event("toreada",b,3)
partido = Event("partido",c,2)
show = Event("a",uuuu,3)
l = Ubicacion(0.3, 0.3)
ll = Ubicacion(-0.4, -0.2)
lll = Ubicacion(1, -0.5)
llll = Ubicacion(1.3, 0.2)
lllll = Ubicacion(1.7, -0.8)
llllll = Ubicacion(-1, 0)

fiesta = Event('fiesta', l, 1)
festival = Event('festival', ll, 2)
after = Event('after', lll, 3)
previa = Event('previa', llll, 4)
asado = Event('asado', lllll, 5)
beers = Event('beers', llllll, 6)
EventAdministrator.addEvent(fiesta)
EventAdministrator.addEvent(festival)
EventAdministrator.addEvent(after)
EventAdministrator.addEvent(previa)
EventAdministrator.addEvent(asado)
EventAdministrator.addEvent(beers)
EventAdministrator.addEvent(choque)
EventAdministrator.addEvent(recital)
EventAdministrator.addEvent(cabalgata)
EventAdministrator.addEvent(toreda)
EventAdministrator.addEvent(partido)
EventAdministrator.addEvent(show)
EventAdministrator.addEvent(concierto)
EventAdministrator.addEvent(baile)
EventAdministrator.addEvent(balada)
EventAdministrator.addEvent(duko)
tipo = Type("choque")
tipo1 = Type("incendio")
tipo2 = Type("cabalgata")
EventAdministrator.addTipoDeEvento(tipo)
EventAdministrator.addTipoDeEvento(tipo1)
EventAdministrator.addTipoDeEvento(tipo2)
z = Ubicacion(1,1)
x = Ubicacion(1.5,0.5)
v = Ubicacion(-1,-1)
s = Sensor("choque",z)
ss = Sensor("incendio",x)
sss = Sensor("recital",v)
TotalSensors.addSensor(s)
TotalSensors.addSensor(ss)
TotalSensors.addSensor(sss)

Menu()
