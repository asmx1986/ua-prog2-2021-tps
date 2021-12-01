from Usuario.U_Login import Login
from Usuario.U_Ciudadano import Ciudadano
from Monitoreo.M_Evento import Event
from Monitoreo.M_ABM import ABM
from Monitoreo.Manipulacion_csv import sortDatabase, sortDatabase_coords, getDatabase
from Mapas.Crear_Mapas import createMap, createBar, createBarbyzone


separator = "=-=" * 20





def menu():
    menugraf = f"""
    {separator}
    EventIT, ¡Mire los eventos de su zona!
    Menu Principal
    (1) Ingresar sesión como ciudadano
    (2) Ingresar sesión como administrador
    (3) Ingresar sesión como sensor
    (4) Registrar nuevo usuario (ciudadano)
    (0) Salir
    {separator}
    """
    print(menugraf)
    option = int(input("Elija una opción : "))
    if option == 1:
        menu1_0()
    elif option == 2:
        menu2_0()
    elif option == 3:
        menu3_0()
    elif option == 4:
        try:
            name = input("""Ingrese nombre: """).strip()
            cuil = int(input("""Ingrese cuil: """))
            telephone = int(input("""Ingrese telefono: """))
            password = input("""Ingrese contraseña: """).strip()
            if Login().register("ciudadano", name, cuil, telephone, password):
                print(f"\nRegistro de {name} completo")
        except (Exception,):
            print(f"\nDatos ingresados no validos")
        menu()
    elif option == 0:
        print("Cerrando el programa...")
        exit(1)
    else:
        print("Opcion inavalida")
        menu()


def menu1_0():
    menu1_0graf = f"""
    {separator}
    (1) Ingresar por Nombre
    (2) Ingresar por Cuil
    (3) Ingresar por Telefono
    (0) Salir
    {separator}
    """
    print(menu1_0graf)
    option = int(input("Elija una opción : "))
    if option == 1:
        name = input("""Ingrese nombre: """).strip()
        password1 = input("""Ingrese contraseña: """).strip()
        if Login().loginCiudadano("Name", name, password1):
            print(f"\nIngreso completo, bienvenido {name}")
            MenuCiudadano(name).menu1_1()
        else:
            menu1_0()
    elif option == 2:
        try:
            cuil = int(input("""Ingrese cuil: """))
            password2 = input("""Ingrese contraseña: """).strip()
            if Login().loginCiudadano("Cuil", cuil, password2):
                name = Login().getName("ciudadano", "Cuil", cuil)
                print(f"Ingreso completo, bienvenido {name}")
                MenuCiudadano(name).menu1_1()
            else:
                menu1_0()
        except (Exception,):
            print(f"Datos no validos")
            menu1_0()
    elif option == 3:
        try:
            telephone = int(input("""Ingrese telefono: """))
            password3 = input("""Ingrese contraseña: """).strip()
            if Login().loginCiudadano("Telephone", telephone, password3):
                name = Login().getName("ciudadano", "Telephone", telephone)
                print(f"Ingreso completo, bienvenido {name}")
                MenuCiudadano(name).menu1_1()
            else:
                menu1_0()
        except (Exception,):
            print(f"Datos no validos")
            menu1_0()
    elif option == 4:
        menu()
    elif option == 0:
        print("Cerrando el programa...")
        exit(1)
    else:
        print("Opcion inavalida")
        menu1_0()


def menu2_0():
    menu2_0graf = f"""
        {separator}
        (1) Ingresar por Nombre
        (2) Ingresar por Cuil
        (3) Ingresar por Telefono
        (0) Salir
        {separator}
        """
    print(menu2_0graf)
    option = int(input("Elija una opción : "))
    if option == 1:
        name = input("""Ingrese nombre: """).strip()
        password1 = input("""Ingrese contraseña: """).strip()
        if Login().loginAdmin("Name", name, password1):
            print(f"Ingreso completo, bienvenido {name}")
            MenuAdmin(name).menu2_1()
        else:
            menu2_0()
    elif option == 2:
        cuil = int(input("""Ingrese cuil: """))
        password2 = input("""Ingrese contraseña: """).strip()
        if Login().loginAdmin("Cuil", cuil, password2):
            name = Login().getName("admin", "Cuil", cuil)
            print(f"Ingreso completo, bienvenido {name}")
            MenuAdmin(name).menu2_1()
        else:
            menu2_0()
    elif option == 3:
        telephone = int(input("""Ingrese telefono: """))
        password3 = input("""Ingrese contraseña: """).strip()
        if Login().loginAdmin("Telephone", telephone, password3):
            name = Login().getName("admin", "Telephone", telephone)
            print(f"Ingreso completo, bienvenido {name}")
            MenuAdmin(name).menu2_1()
        else:
            menu2_0()
    elif option == 4:
        menu()
    elif option == 0:
        print("Cerrando el programa...")
        exit(1)
    else:
        print("Opcion inavalida")
        menu2_0()


def menu3_0():
    menu3_0graf = f"""
    {separator}
    Menu Sensor
    (1) Ver tipos de eventos
    (2) Ver eventos
    (3) Añadir tipo de evento
    (4) Añadir evento
    (5) Reportar un evento
    (0) Salir
    {separator}
    """
    print(menu3_0graf)
    option = int(input("Elija una opción : "))
    if option == 1:
        print(Event().getType().to_markdown())
        menu3_0()
    elif option == 2:
        print(Event().getEvents().to_markdown())
        menu3_0()
    elif option == 3:
        event_type = input("Tipo de evento: ").strip()
        Event().addType(event_type)
        menu3_0()
    elif option == 4:
        try:
            event_name = input("Nombre del evento: ").strip()
            event_type = input("Tipo de evento: ").strip()
            description = input("Descripción: ").strip()
            x = int(input("Coordenada X: "))
            y = int(input("Coordenada Y: "))
            if Event().addEvent(event_name, event_type, x, y, description):
                print("\nCoordenadas invalidas (solo de 0 a 10)")
            else:
                print("\n¡Evento creado!")
        except (ValueError, ):
            print("\nDatos invalidos")
        menu3_0()
    elif option == 5:
        event_name = input("Nombre del evento: ").strip()
        num = int(input("Numero de participantes: "))
        Event().reportEvent(event_name, num)
        menu3_0()
    elif option == 6:
        menu()
    elif option == 0:
        print("Cerrando el programa...")
        exit(1)
    else:
        print("Opcion inavalida")
        menu3_0()


class MenuCiudadano:
    def __init__(self, name):
        self.name = name

    def menu1_1(self):
        menu1_1graf = f"""
        {separator}
        Bienvenido ciudadano
        (1) Entrar a RedSolcial
        (2) Entrar a Eventos
        (0) Salir
        {separator}
        """
        print(menu1_1graf)
        option = int(input("Elija una opción : "))
        if option == 1:
            MenuSolicitudes(self.name).menu1_1_1()
        elif option == 2:
            MenuEventos(self.name).menu1_1_2()
        elif option == 3:
            menu1_0()
        elif option == 0:
            print("Cerrando el programa...")
            exit(1)
        else:
            print("Opcion inavalida")
            self.menu1_1()


class MenuSolicitudes:
    def __init__(self, name):
        self.name = name

    def menu1_1_1(self):
        menu1_1_1graf = f"""
        {separator}
        Bienvenido a RedSocial
        (1) Ver amigos
        (2) Eliminar un amigo
        (3) Ver solicitudes
        (4) Rechazar una solicitud
        (5) Aceptar una solicitud
        (6) Enviar una solicitud
        (7) Ver numero de solicitudes rechazadas
        (0) Salir
        {separator}
        """
        print(menu1_1_1graf)
        option = int(input("Elija una opción : "))
        if option == 1:
            print()
            print(f"Amigos: {Ciudadano(self.name).getfriends()}")
            self.menu1_1_1()
        elif option == 2:
            try:
                name = input("¿Cual es el amigo que desea eliminar?: ").strip()
                Ciudadano(self.name).delFriend(name)
                print(f"\nAmigo {name} eliminado...")
            except (Exception,):
                print(f"\nAmigo invalido...")
            self.menu1_1_1()
        elif option == 3:
            print()
            instance_receiver = Ciudadano(self.name)
            print(f"Solicitudes: {instance_receiver.getfriend_request()}")
            self.menu1_1_1()
        elif option == 4:
            try:
                name = input("¿Cual es la solicitud que desea rechazar?: ").strip()
                Ciudadano(self.name).rejectFriend_Request(name)
                print(f"\nSolicitud {name} rechazada...")
            except (Exception,):
                print(f"\nSolicitud invalida...")
            self.menu1_1_1()
        elif option == 5:
            try:
                name = input("¿Cual es la solicitud que desea aceptar?: ").strip()
                if Login().checkName(name, "ciudadano"):
                    Ciudadano(self.name).acceptFriend_Request(name)
                    print(f"\nSolicitud {name} aceptada...")
                else:
                    print(f"\nUsuario inexistente...")
            except (Exception,):
                print(f"\nSolicitud invalida...")
            self.menu1_1_1()
        elif option == 6:
            try:
                receiver = input("¿Cual es el nombre del remitente?: ").strip()
                ciu2 = Ciudadano(receiver)
                Ciudadano(self.name).sendFriend_Request(ciu2)
            except (Exception,):
                print(f"\nCiudadano invalido...")
            self.menu1_1_1()
        elif option == 7:
            rejected = Ciudadano(self.name).getrejected_requests()
            if rejected == 1:
                print(f"Fue rechazada {rejected} solicitud")
            else:
                print(f"Fueron rechazadas {rejected} solicitudes")
            self.menu1_1_1()
        elif option == 8:
            MenuCiudadano(self.name).menu1_1()
        elif option == 0:
            print("Cerrando el programa...")
            exit(1)
        else:
            print("Opcion inavalida")
            self.menu1_1_1()


class MenuEventos:
    def __init__(self, name):
        self.name = name

    def menu1_1_2(self):
        menu1_1_2graf = f"""
        {separator}
        Bienvenido a Eventos
        (1) Ver amigos
        (2) Ver eventos
        (3) Ver eventos aprobados
        (4) Autoreportarte un evento
        (5) Reportar un evento a amigos
        (6) Entrar a Mapas
        (0) Salir
        {separator}
        """
        print(menu1_1_2graf)
        option = int(input("Elija una opción : "))
        if option == 1:
            print()
            print(f"Amigos: {Ciudadano(self.name).getfriends()}")
            self.menu1_1_2()
        elif option == 2:
            print()
            print(Event().getEvents().to_markdown())
            self.menu1_1_2()
        elif option == 3:
            print()
            print(Event().getApprovedEvents().to_markdown())
            self.menu1_1_2()
        elif option == 4:
            try:
                a = input("Puede reportar a cualquiera pero sin su concentimiento, ¿Procedera? (y/n): ").strip()
                if a == "y":
                    event_type = input("Nombre del evento: ").strip()
                    Event().reportEvent(event_type, self.name)
                    print("\nEvento reportado...")
            except (Exception, ):
                print("\nDatos invalidos")
            self.menu1_1_2()
        elif option == 5:
            try:
                a = input("Tus amigos seran añadidos pero sin su concentimiento, ¿Procedera? (y/n): ").strip()
                if a == "y":
                    event_type = input("Nombre del evento: ").strip()
                    friends = Ciudadano(self.name).getfriends()
                    Event().reportEvent(event_type, friends)
                    print("\nEvento reportado...")
            except (Exception, ):
                print("\nDatos invalidos")
            self.menu1_1_2()
        elif option == 6:
            MenuMapas(self.name).menu1_1_2_7()
        elif option == 7:
            MenuCiudadano(self.name).menu1_1()
        elif option == 0:
            print("Cerrando el programa...")
            exit(1)
        else:
            print("Opcion inavalida")
            self.menu1_1_2()


class MenuMapas:
    def __init__(self, name):
        self.name = name

    def menu1_1_2_7(self):
        menu1_1_2_7graf = f"""
        {separator}
        Bienvenido a Mapas
        (1) Todos los eventos
        (2) Todos los eventos aprovados
        (3) Ver ranking (tabla)
        (4) Ver ranking
        (5) Ver ranking por zona (tabla)
        (6) Ver ranking por zona
        (0) Salir
        {separator}
        """
        print(menu1_1_2_7graf)
        option = int(input("Elija una opción : "))
        if option == 1:
            createMap("Baja")
            self.menu1_1_2_7()
        elif option == 2:
            createMap("Alta")
            self.menu1_1_2_7()
        elif option == 3:
            print(sortDatabase('evento').to_markdown())
            self.menu1_1_2_7()
        elif option == 4:
            createBar()
            self.menu1_1_2_7()
        elif option == 5:
            try:
                x = int(input("Coordenada X: "))
                y = int(input("Coordenada Y: "))
                print(sortDatabase_coords('evento', x, y).to_markdown())
            except (Exception,):
                print('\nCoordenadas invalidas')
            self.menu1_1_2_7()
        elif option == 6:
            try:
                x = int(input("Coordenada X: "))
                y = int(input("Coordenada Y: "))
                createBarbyzone(x, y)
            except (Exception,):
                print('\nCoordenadas invalidas')
            self.menu1_1_2_7()
        elif option == 3:
            print(sortDatabase('evento').to_markdown())
            self.menu1_1_2_7()
        elif option == 7:
            MenuEventos(self.name).menu1_1_2()
        elif option == 0:
            print("Cerrando el programa...")
            exit(1)
        else:
            print("Opcion inavalida")
            self.menu1_1_2_7()


# Parte del admin
class MenuAdmin:
    def __init__(self, name):
        self.name = name

    def menu2_1(self):
        menu2_1graf = f"""
        {separator}
        Administrador, ¿que desea hacer?
        (1) Ver eventos
        (2) Ver ciudadanos
        (3) Dar de alta un evento
        (4) Dar de baja un evento
        (5) Bloquear un ciudadano
        (6) Desbloquear un ciudadano
        (7) Registrar nuevo usuario (administrador)
        (0) Salir
        {separator}
        """
        print(menu2_1graf)
        option = int(input("Elija una opción : "))
        if option == 1:
            print()
            print(Event().getEvents().to_markdown())
            self.menu2_1()
        elif option == 2:
            print()
            print(getDatabase("DB_ciudadano").to_markdown())
            self.menu2_1()
        elif option == 3:
            evento = input("""Ingrese evento: """).strip()
            try:
                ABM().setAlta(evento)
                print(f"\nEvento {evento} dado de Alta")
            except (Exception,):
                print(f"\n¡¡¡Evento no encontrado!!!")
            self.menu2_1()
        elif option == 4:
            evento = input("""Ingrese evento: """).strip()
            try:
                ABM().setBaja(evento)
                print(f"\nEvento {evento} dado de Baja")
            except (Exception,):
                print(f"\n¡¡¡Evento no encontrado!!!")
            self.menu2_1()
        elif option == 5:
            name = input("""Ingrese nombre: """).strip()
            try:
                ABM().block(name)
                print(f"\nCiudadano {name} bloqueado")
            except (Exception,):
                print(f"\nCiudadano no encontrado")
            self.menu2_1()
        elif option == 6:
            name = input("""Ingrese nombre: """).strip()
            try:
                ABM().unblock(name)
                print(f"\nCiudadano {name} desbloqueado")
            except (Exception,):
                print(f"\nCiudadano no encontrado")
            self.menu2_1()
        elif option == 7:
            try:
                name = input("""Ingrese nombre: """).strip()
                cuil = int(input("""Ingrese cuil: """))
                telephone = int(input("""Ingrese telefono: """))
                password = input("""Ingrese contraseña: """).strip()
                Login().register("admin", name, cuil, telephone, password)
            except (Exception,):
                print(f"\nDatos ingresados no validos")
            self.menu2_1()
        elif option == 8:
            menu2_0()
        elif option == 0:
            print("Cerrando el programa...")
            exit(1)
        else:
            print("Opcion inavalida")
            self.menu2_1()
