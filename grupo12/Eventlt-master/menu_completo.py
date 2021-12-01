import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
from citizen import ciudadano
# from listaDeEventos import eventos
import new_world
from listadeCuidadanos import etlist
from administrador import administrator
from revisionlist import defualt_revision_list
from registrodezonas import registroDeZonas
from estadisticas import Stats_Board


class MainMenu:
    @staticmethod
    def menu_o():
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        try:
            print('Bienvenido a Eventlt')
            menu_login = int(input('1.Ingresar como Administrador | 2.Ingresar como usuario | 3.Ingresar como sensor | Ingresar cualquier otro número para salir: '))

            if menu_login == 1:
                MainMenu.log_adm()

            elif menu_login == 2:
                MainMenu.menu_login_citizen()

            elif menu_login == 3:
                print('Bienvenido al menu sensor')
                acceso = int(input('1.Acceder a estadísticas | 2.Acceder al mapa: '))
                if acceso == 2:
                    sensor.acces_map()
                elif acceso == 1:
                    acceso_stats = int(input('1.Acceder al historial de valores máximos de concurrencia | 2.Visualizar gráfico de personas por zona: '))
                    if acceso_stats == 1:
                        print(registroDeZonas.listadoZonas(seconddf))
                        acces_max = int(input('Ingrese la zona a la que desea acceder para visualizar los valores máximos por ocurrencia.'))
                        Stats_Board.showMaxZone(acces_max)
                    elif acceso_stats == 2:
                        Stats_Board.show_p_per_zone(Stats_Board)
                    else:
                        print('Número inválido')
                        time.sleep(3)
                        os.system('cls' if os.name == 'nt' else 'clear')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print('Para salir del programa debe presionar un número.')
            time.sleep(3)
            MainMenu.menu_o()

    @staticmethod
    def register():
        anses = pandas.read_csv(os.path.abspath("DatasetAnses.csv"))
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        phone_number = input("Ingrese su número telefónico: (+54) ")
        try:
            int(phone_number)
        except ValueError:
            print("Debe ingresar su número telefónico correctamente")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_login_citizen()
        
        checkIfExist = False
        for a in anses['Telefono']:
            if int(phone_number) == int(a):
                checkIfExist = True
        if checkIfExist == False:
            print('su teléfono no esté en el dataset del anses')
            return MainMenu.menu_o()

                 
        user_cuil = input("Ingrese su CUIL: ")
        try:
            int(user_cuil)
        except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_login_citizen()

        checkIfExist = False
        for a in anses['CUIL']:
            if int(user_cuil) == int(a):
                checkIfExist = True
        if checkIfExist == False:
            print('su CUIL no está en el dataset del anses')
            return MainMenu.menu_o()


        df = pandas.read_csv(os.path.abspath("Database.csv"))
        for numbers in df['Phonenumber']:
            if str(numbers) == str(phone_number):
                print("Ya hay un usuario registrado con este número telefónico")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                MainMenu.menu_login_citizen()
        
        for CUILnumbers in df['CUIL']:
            if str(CUILnumbers) == str(user_cuil):
                print("Ya hay un usuario registrado con este CUIL")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                MainMenu.menu_login_citizen()

        counter = len(str(user_cuil))

        counter2 = len(str(phone_number))

        password = input("Ingrese su contraseña por favor: ")

        password1 = input("Ingrese su contraseña nuevamente: ")

        name = input('Ingrese su nombre: ')

        surname = input('Ingrese su apellido: ')

        try:
            if str(name).isdigit() == True or str(surname).isdigit() == True:
                raise ValueError()
        except ValueError:
            print('Ingresaste números en tu nombre o apellido, inténtelo de nuevo')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.menu_login_citizen()

        try:
            age = input("cual es tu edad: ")
            int(age)
        except ValueError:
            print("Usted ha ingresado un caracter inválido, inténtelo nuevamente")
        print('¿en qué zona está?')
        print(registroDeZonas.listadoZonas(seconddf))
        zona_user = int(input('respuesta: '))
        if zona_user > (len(seconddf['Nombre']) - 1):
            print('este número no es válido')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return MainMenu.menu_o

        if counter == 11 and password == password1 and counter2==11:
            with open(os.path.abspath("Database.csv"),mode="a",newline="") as h:
                writer = csv.writer(h,delimiter=",")
                writer.writerow([user_cuil,password,phone_number,name,surname,age,zona_user])
            ciudadano.create_citizen(name,surname,age, user_cuil,phone_number,zona_user)
            print(etlist.getcl())
            # print("Su clase citizen fue creada exitosamente")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            h.close()
            MainMenu.menu_login_citizen()
        elif counter != 11:
            print("Has ingresado el número incorrecto de un CUIL.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.register()
        elif password != password1:
            print("Contraseña incorrecta, inténtelo de nuevo.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.register()
        elif counter2 != 11:
            print("Cantidad de dígitos de su número telefónico es incorrecta.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.register()

    @staticmethod
    def login ():
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        user_cuil = (input("Ingrese su CUIL: "))
        try:
            int(user_cuil)
        except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.menu_login_citizen()
        user_cuil = int(user_cuil)
        i = 0
        for a in df['CUIL']:
            if str(user_cuil) == str(a):
                break
            i += 1
            if i == len(df["CUIL"]):
                print('Su CUIL no fue encontrado')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                MainMenu.menu_login_citizen()
                return i
        password = input("Ingrese su contraseña: ")
        if str(password) == str(df['Password'][i]):
            print("Bienvenido a Eventlt.\n\n")
            MainMenu.menu_citizen(i) #<---- esto linkea al menu de las acciones del ciudadano
        else:
            print("Contraseña inválida.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            MainMenu.menu_login_citizen()

    @staticmethod
    def menu_login_citizen():
        print("Por favor, seleccione una de las siguentes opciones:")
        try:
            user = int(input("1.Log in | 2. Registrarse | 3.Salir: "))
        except ValueError:
            print('eso no es un número, inténtelo nuevamente')
            MainMenu.menu_login_citizen()
        if user == 1:
            MainMenu.login()
        elif user == 2:
            MainMenu.register()
        elif user == 3:
            MainMenu.menu_o()
        else:
            print("Debes ingresar los números indicados anteriormente.")
            MainMenu.menu_login_citizen()
    @staticmethod
    def menu_citizen(citizenidentifier):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        from listaDeEventos import eventos as ev
        for a in etlist.citizenlist:
            if int(df['CUIL'][citizenidentifier]) == int(a.CUIL):
                ciudadanos = a
        if ciudadanos.citizenBan == True:    # si la cuenta esta baneada no pasa
            print('Su cuenta se encuentra bloqueada, no puede ingresar')
            return MainMenu.menu_o
        try:
            c = int(input(f'{ciudadanos.name}, elija lo que quiere hacer:\n\n1.Asistir a evento | 2.Dejar de asistir a evento | 3.Menu de amigos | 4.Cambiar zona: ')) # SOLO PUEDE SER UN NUMERO
        except ValueError:
            print('Debe ingresar un número')
            time.sleep(3)
            os.system('cls' if os.name== 'nt' else 'clear')
            MainMenu.menu_o()
        if c == 1:
            print(ciudadanos.seeEvents(ciudadanos.zone))
            choice = int(input('¿A qué evento quiere asistir?: '))
            if choice > (ev.howManyEvents(ciudadanos.zone) - 1) or choice < 0:
                print('ese número no es válido')
                return MainMenu.menu_citizen(citizenidentifier)
            print(ciudadanos.asistEvent(ciudadanos.zone, choice))
            return MainMenu.menu_citizen(citizenidentifier)
        elif c == 2:
            if len(ciudadanos.involvedEvents) == 0:
                print('usted no está en ningún evento')
                return MainMenu.menu_citizen(citizenidentifier)
            print(ciudadanos.seeInvolvedEvents())
            choice = int(input('¿A qué evento quiere dejar de asistir?: '))
            if choice > (len(ciudadanos.involvedEvents)-1) or choice < 0:
                print('ese número no es válido')
                return MainMenu.menu_citizen(citizenidentifier)
            print(ciudadanos.unAsistEvent(ciudadanos.zone, choice))
            return MainMenu.menu_citizen(citizenidentifier)
        elif c == 3:
            menu_amigos.friends_menu(citizenidentifier)
        elif c == 4:
            registroDeZonas.listadoZonas(seconddf)
            print(registroDeZonas.listadoZonas(seconddf))
            num = int(input("¿A qué zona desea cambiarse?\n"))
            ciudadanos.change_zone(num)
            print('Su zona se actualizó correctamente')
            MainMenu.menu_citizen(citizenidentifier)
        else:
            return MainMenu.menu_o()
        
    @staticmethod
    def log_adm():
        df = pandas.read_csv(os.path.abspath("Base_Adm.csv")) #va el path csv de administradores
        admin_user = input("Ingrese su nombre de usuario como admnistrador: ")
        admin_serch = 0
        for a in df['Admin_user']:
            if str(admin_user) == str(a):
                break
            admin_serch += 1
        if admin_serch == len(df["Admin_user"]):
            print('Su nombre no está como usuario, volviendo al menu principal.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()
            return admin_serch
        admin_password = input('Ingrese su contraseña: ')
        if str(admin_password) == str(df['Password'][admin_serch]):
            print(f"Usted ingresó como {admin_user}, bienvenido.")
            menu_administrador.Bienvenido()
        else:
            print("Contraseña inválida, volviendo al menu principal.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()


class menu_administrador():
    revisionlist=[]

    @staticmethod
    def Bienvenido():
        choice = int(input("Elija una de las siguientes opciones: 1-Agregar evento| 2-Bannear| 3-Remover Ban| 4-Ver lista de revisión: "))
        if choice == 1:
            return menu_administrador.admin_addEvent()
        elif choice == 2:
            return menu_administrador.BanCitizen()
        elif choice == 3:
            return menu_administrador.UnBanCitizen()
        elif choice == 4:
            defualt_revision_list.update_revision_list()
            return menu_administrador.check_revisionList()
        else:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            MainMenu.menu_o()

    @staticmethod
    def admin_addEvent():
        zona = input('Ingrese la zona del evento: ')
        nombre = input('Título de evento: ')
        descripcion = input('Descripcion del evento: ')
        latitud = input('Latitud: ')
        longitud = input('Longitud: ')
        administrator.addEvent(zona, nombre, descripcion, latitud, longitud )
        print('El evento fue creado exitosamente.')
        return menu_administrador.Bienvenido()

    @staticmethod
    def check_revisionList():
        print(defualt_revision_list.getlist())
        citizenindex = int(input("Seleccione la posición del ciudadano al que quiere revisar (empezando desde el 0): "))
        ban_choice = str(input("¿Quiere remover el ban del citizen? si/no: "))
        chosen_citizen = defualt_revision_list.revision_list[citizenindex]
        if ban_choice =="si":
            administrator.unbanCitizen(chosen_citizen)
            chosen_citizen.quien_me_rechazo = []
            defualt_revision_list.removecitizen(chosen_citizen)
            print("El usuario fue des-banneado y removido de la lista de revisión")
            return menu_administrador.Bienvenido()
        else:
            defualt_revision_list.removecitizen(chosen_citizen)
            chosen_citizen.quien_me_rechazo = []
            print("El ciudadano fue removido de la lista de revisión y automaticamente fue baneado")
            return menu_administrador.Bienvenido()

    @staticmethod
    def BanCitizen():
        usuarioseleccionado = int(input("¿A quien desea bannear? "))
        for usuarios in etlist.citizenlist:
            if usuarios.CUIL == usuarioseleccionado and usuarios.citizenBan == False:
                administrator.banCitizen(usuarios)
                print(f"El usuario con CUIL {usuarioseleccionado} fue banneado")
                return menu_administrador.Bienvenido()
        print("Usuario no encontrado")
        return menu_administrador.Bienvenido()

    @staticmethod
    def UnBanCitizen():
        usuarioseleccionado = int(input("¿A quien desea removerle el ban? CUIL: "))
        for users in etlist.BannedCitizenList:
            if users.CUIL == usuarioseleccionado:
                administrator.unbanCitizen(users)
                print(f"Se removio el ban de la persona con el CUIL: {usuarioseleccionado}")
                return menu_administrador.Bienvenido()
        print("Usuario no encontrado")
        return menu_administrador.Bienvenido()

    @classmethod
    def update_revision_list(cls):
        for citizen in etlist.citizenlist:
            if len(citizen.quien_me_rechazo) == 5:
                cls.revisionlist.append(citizen)
                administrator.banCitizen(citizen)


class menu_amigos:

    @staticmethod
    def friends_menu(user):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        for ciudadanos in etlist.citizenlist:
            if int(df['CUIL'][user]) == int(ciudadanos.CUIL):
                x = ciudadanos
        menu_choice = int(input(f"{x.name}, bienvenido a sus contactos:\n\n1.Ver solicitudes | 2.Enviar solicitud | 3.Ver eventos de contactos | Volver al menú: "))
        if menu_choice == 1:
            print(x.ver_solicitudes())
            acciones_disponibles = int(input('1.Aceptar una solicitud | 2.Rechazar una solicitud: '))
            if acciones_disponibles == 1:
                solicitud_choice = input('Dime el número del que quieres agregar: ')
                print(x.aceptar_solicitud(solicitud_choice))
                return menu_amigos.friends_menu(user)
            elif acciones_disponibles == 2:
                solicitud_choice = input('Dime el número del que quieres rechazar: ')
                print(x.aceptar_solicitud(solicitud_choice))
                return menu_amigos.friends_menu(user)
            else:
                return menu_amigos.friends_menu(user)
        elif menu_choice == 2:
            friend_cuil = int(input("Dime el CUIL de tu amigo: "))
            print(x.enviar_solicitud(friend_cuil))
            return menu_amigos.friends_menu(user)
        elif menu_choice == 3:
            if len(x.friends) == 0:
                print('Usted no tiene amigos.')
                return menu_amigos.friends_menu(user)
            num = 0
            for friend in x.friends:
                print(f"{num} | {friend.name} {friend.lastName} | {friend.CUIL}")
                num += 1
            choice = int(input('¿De cual contacto quiere ver?: '))
            if choice > (len(x.friends)-1) or choice < 0:
                print('Número inválido')
                return menu_amigos.friends_menu(user)
            elif len(x.friends[choice].involvedEvents) == 0:
                print('Su amigo no ha reportado ningún evento')
                return menu_amigos.friends_menu(user)
            for eventos in x.friends[choice].involvedEvents:
                print(eventos)
            return menu_amigos.friends_menu(user)
        else:
            MainMenu.menu_citizen(user)

class sensor:
    @staticmethod
    def acces_map():
        a = pandas.read_csv(os.path.abspath("zona.csv"))
        print('Zonas disponibles: ')
        print(registroDeZonas.listadoZonas(a))
        num = int(input("Elija su zona: "))
        if num <= len(a['Nombre']):
                new_world.Mapa.show_map(a['Latitud'][num],a['Longitud'][num])
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print('Número inválido')
            os.system('cls' if os.name == 'nt' else 'clear') 
