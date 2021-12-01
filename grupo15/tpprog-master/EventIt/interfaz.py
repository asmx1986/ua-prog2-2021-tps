from gestiondeeventos.sensor import Sensor
from gestiondeusuarios.abm.abm import ABM
from gestiondeusuarios.registrodeciudadano import GestiondeUsuarios
from monitoreo.mapa import Mapa
from monitoreo.tabla import TabladeEstadistica

EventIt = GestiondeUsuarios()
EventIt.registro(123,1234,"contraseña")
EventIt.registro(333,3333,"contraseña")
EventIt.registro(555,5555,"contraseña")

fran =EventIt.logCiudadano(123,"contraseña")
vicky =EventIt.logCiudadano(333,"contraseña")
may = EventIt.logCiudadano(555,"contraseña")
fran.Enviarinvitacion(EventIt.buscarusuario(333))
fran.Enviarinvitacion(EventIt.buscarusuario(555))

may.asistirEvento("lollapaloza",2,3)
fran.asistirEvento("lollapaloza",2,3)
vicky.asistirEvento("lollapaloza",2,3)

vicky.asistirEvento("estudio biometrico",3,5)
fran.asistirEvento("estudio biometrico",3,5)

fran.asistirEvento("colecta",4,1)

vicky.asistirEvento("Feria del libro",1,6)

sensor1=Sensor(2,3)
sensor1.filtrarEventos(EventIt.getCiudadanos())
sensor2=Sensor(3,5)
sensor2.filtrarEventos(EventIt.getCiudadanos())
sensor3=Sensor(4,1)
sensor3.filtrarEventos(EventIt.getCiudadanos())
sensor4=Sensor(1,6)
sensor4.filtrarEventos(EventIt.getCiudadanos())

def menudebloqueo(administrador):
    s = ""
    while (s!="q"):
        print("\t|1| Bloquear ciudadano\n\t|2| Desbloquear ciudadano"+"\n"+linea)
        opcion = input("Ingrese una opcion:")
        if int(opcion) == 1:
            cuil = input("Ingrese cuil:")
            administrador.bloquearCiudadano(EventIt.buscarusuario(cuil))
            s = 'q'
        if int(opcion) == 2:
            cuil = input("Ingrese cuil:")
            administrador.desbloquearCiudadano(EventIt.buscarusuario(cuil))
            s = "q"
        else:
            s="q"

def menudeEstadistica():
    s = ""
    while (s!="q"):
        print("\t|1| Ver ranking\n\t|2| Ver tabla"+"\n"+linea)
        opcion = input("Ingrese una opcion:")
        if int(opcion) == 1:
            print(linea)
            TabladeEstadistica.mostrarEventosTop()
            s='q'
        if int(opcion) == 2:
            s = "q"
        else:
            pass

def menudereporte(ciudadano):
    s = ""
    while (s!="q"):
        print(linea + "¿Desea vincular a otro ciudadano?")
        print("\t|1| SI\n\t|2| NO"+"\n"+linea)
        opcion = input("Ingrese una opcion:")
        if int(opcion) == 1:
            cuil = input("Ingrese el cuil del otro ciudadano")
            x=input('Ingrese valor en x:')
            y=input('Ingrese valor en y:')
            tipo=input('Ingrese el tipo:')
            ciudadano2= EventIt.buscarusuario(cuil)
            ciudadano.asistirEvento(tipo,x,y)
            ciudadano2.asistirEvento(tipo,x,y)
            s = "q"
        if int(opcion) == 2:
            print("Ingrese ubicacion y tipo:")
            x=input('Ingrese valor en x:')
            y=input('Ingrese valor en y:')
            tipo=input('Ingrese el tipo:')
            ciudadano.asistirEvento(tipo,x,y)
            print(ciudadano.getEventos())
            s = "q"
        else:
            pass

def menudesolicitudes(ciudadano):
    s=""
    while (s!="q"):
        print(linea)
        print("Usted puede:")
        print("|1| Aceptar solicitud\n|2| Rechazar solicitud\n|3| Salir de solicitudes")
        print(linea)
        eleccion = input("Ingresa tu opcion:")
        if int(eleccion) == 1:
            dato = input("Ingrese el numero de cuil o telefono del ciudadano a aceptar:")
            ciudadano.aceptarInvitacion(EventIt.buscarusuario(int(dato)))

        if int(eleccion) == 2:
            dato = input("Ingrese el numero de cuil o telefono del ciudadano a rechazar:")
            ciudadano.rechazarInvitacion(EventIt.buscarusuario(int(dato)))

        if int(eleccion)==3:
            s = "q"

        else:
            pass

def menudeciudadano(ciudadano):
    s=""
    while (s!="q"):
        print(linea + "¿Que desea realizar?")
        print("\t|1| Reportar un evento\n\t|2| Enviar solicitud\n\t|3| Ver solicitudes\n\t|4| Ver amigos\n\t|5| Ver mapa de eventos"
                "\n\t|6| Cerrar sesion ")
        eleccion = input(linea+"\nIngresa tu opcion:")
        if int(eleccion) == 1:
            menudereporte(ciudadano)
            print("¡Gracias por reportar el Evento!")

        if int(eleccion) == 2:
            cuil = input("Ingrese el cuil del ciudadano:")
            ciudadano.Enviarinvitacion(EventIt.buscarusuario(int(cuil)))

        if int(eleccion) == 3:
            print(ciudadano.contactos.getRecibidas())
            menudesolicitudes(ciudadano)

        if int(eleccion) == 4:
            print(ciudadano.contactos.getAmigos())

        if int(eleccion) == 5:
            Mapa.dibujarMapaCiudad()


        if int(eleccion) == 6:
            s = "q"
        else:
            pass

def menuAdmin(administrador):
    s=""
    while (s!="q"):
        print(linea + "\n¿Que desea realizar?")
        print("\t|1| Ver ciudadanos\n\t|2| Activar sensor\n\t|3| Ver mapa de eventos"
                "\n\t|4| Ver tabla de estadistica\n\t|5| Cerrar sesion ")
        eleccion = input("Ingresa tu opcion:")
        #En ver ciudadanos hay que poner la opcion de bloquear o desbloquear
        if int(eleccion) == 1:
            print(EventIt.getCiudadanos())
            menudebloqueo(administrador)
        if int(eleccion) == 2:
            x = input("Ingrese coordenada en x:")
            y = input("Ingrese coordenada en y:")
            sensorn=Sensor(x,y)
            sensorn.filtrarEventos(EventIt.getCiudadanos())

        if int(eleccion) == 3:
            Mapa.dibujarMapaCiudad()

        if int(eleccion) == 4:
            menudeEstadistica()

        if int(eleccion) == 5:
            s = 'q'
        else:
            pass

def ingreso(number):
    if int(number) == 1:
        print("Usted ingresara como administrador, completar los datos\n")
        usuario = input("Ingresar usuario:")
        contrasena = input("Ingresar contraseña:")
        admin = ABM.iniciarAdministrador(usuario,contrasena)
        menuAdmin(admin)

    if int(number)== 2:
        print("Usted ingresara como ciudadano, completar los datos\n")
        cuil = input("Ingresar cuil:")
        contrasena = input("Ingresar contraseña:")
        ciudadano = EventIt.logCiudadano(int(cuil),contrasena)
        if ciudadano.getstate():
            menudeciudadano(ciudadano)
        else:
            ciudadano.pedirAuditoria()
            print("Usted es un usuario bloqueado, se le ha pedido una auditoria")


    if int(number)==3:
        print("Para registrarse necesita los siguientes datos:\n")
        cuil = input("Ingrese su cuil:")
        telefono = input("Ingrese su telefono:")
        contrasena= input("Ingrese su contraseña:")
        EventIt.registro(int(cuil),int(telefono),contrasena)
        print(EventIt.getCiudadanos())
        print("¡Gracias por unirte a EventIt!\nAhora puede ingresar como ciudadano")

    else:
        pass


while True:
    linea="---------------------------------------------\n"
    bienvenida = "Bienvenido a EvenIt\n"
    pregunta="¿Que desea realizar?\n"
    print(linea+bienvenida+linea+pregunta)
    print("\t|1| Ingresar como admin\n\t|2| Ingresar como Ciudadano\n\t|3| Registrate como Ciudadano\n")
    eleccion = input("Ingresa tu opcion:")
    print(linea)
    ingreso(eleccion)
