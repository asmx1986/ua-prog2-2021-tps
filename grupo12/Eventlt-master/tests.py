import unittest
import csv
import os
import pandas #se debe descargar esta libreria con pip install pandas en la terminal
import time
from citizen import ciudadano
# from listaDeEventos import eventos
import new_world
import webbrowser
import random
from listadeCuidadanos import etlist
from administrador import administrator
from revisionlist import defualt_revision_list


class FakeMainMenu: #A diferencia de la clase original FakeMainMenu es inicializable para poder realizar instancias de testeo
    def menu_o(self,console):
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        try:
            print('Bienvenido a Eventlt')
            menu_login = int(console.input('1.Ingresar como Admin | 2.Ingresar como usuario | 3.Ingresar como sensor | ingresar cualquier otro numero para salir:'))

            if menu_login == 1:
                self.FakeMainMenu.log_adm(console)

            elif menu_login == 2:
                self.FakeMainMenu.menu_login_citizen(console)

            elif menu_login == 3:
                print('Zonas disponibles: ')
                print(registroDeZonas.listadoZonas(seconddf))
                num = int(console.input("Elija su zona: "))
                if num <= len(seconddf['Nombre']):
                    new_world.Mapa.show_map(seconddf['Latitud'][num], seconddf['Longitud'][num])
                else:
                    print('numero invalido')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.FakeMainMenu.menu_o(console)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print('Para salir del programa debe presionar un numero.')
            time.sleep(3)
            self.FakeMainMenu.menu_o(console)

    def register(self,console):
        phone_number = console.input("Ingrese su numero telefonico: (+54) ")
        try:
            int(phone_number)
        except ValueError:
            print("Debe ingresar su numero telefonico correctamente")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.menu_login_citizen(console)
        user_cuil = console.input("Ingrese su CUIL: ")
        try:
            int(user_cuil)
        except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.FakeMainMenu.menu_login_citizen(console)

        df = pandas.read_csv(os.path.abspath("Database.csv"))
        for numbers in df['Phonenumber']:
            if str(numbers) == str(phone_number):
                print("Ya hay un usuario registrado con este numero telefonico")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                self.FakeMainMenu.menu_login_citizen(console)

        for CUILnumbers in df['CUIL']:
            if str(CUILnumbers) == str(user_cuil):
                print("Ya hay un usuario registrado con este CUIL")
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')

                self.FakeMainMenu.menu_login_citizen(console)

        counter = len(str(user_cuil))

        counter2 = len(str(phone_number))

        password = console.input("Ingrese su contraseña,porfavor: ")

        password1 = console.input("Confirme su contraseña,nuevamente: ")

        name = console.input('Ingrese su nombre: ')

        surname = console.input('Ingrese su apellido: ')

        try:
            if str(name).isdigit() == True or str(surname).isdigit() == True:
                raise ValueError()
        except ValueError:
            print('Ingresaste numeros en tu nombre o apellido, intentelo denuevo')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.menu_login_citizen(console)

        try:
            age = console.input("cual es tu edad: ")
            int(age)
        except ValueError:
            print("Usted ha ingresado un caracter invalido, intentelo nuevamente")

        if counter == 11 and password == password1 and counter2 == 11:
            with open(os.path.abspath("Database.csv"), mode="a", newline="") as h:
                writer = csv.writer(h, delimiter=",")
                writer.writerow([user_cuil, password, phone_number, name, surname, age])
            ciudadano.create_citizen(name, surname, age, user_cuil, phone_number)
            print(etlist.getcl())
            # print("Su clase citizen fue creada exitosamente")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            h.close()
            self.FakeMainMenu.menu_login_citizen(console)
        elif counter != 11:
            print("Has ingresado el numero incorrecto de un CUIL.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.register(console)
        elif password != password1:
            print("Contraseña Incorrecta, intentelo denuevo.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.register(console)
        elif counter2 != 11:
            print("Cantidad de digitos de su numero telefonico es incorrecta.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.register(console)

    def login(self,console):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        user_cuil = (console.input("Ingrese su CUIL: "))
        try:
            int(user_cuil)
        except ValueError:
            print("El CUIL debe ser un número")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.menu_login_citizen(console)
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

                self.FakeMainMenu.menu_login_citizen(console)
                return i
        password = console.input("Ingrese su contraseña: ")
        if str(password) == str(df['Password'][i]):
            print("Bienvenido a Eventlt.\n\n")
            self.FakeMainMenu.menu_citizen(i)  # <---- esto linkea al menu de las acciones del ciudadano
        else:
            print("Contraseña invalida.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

            self.FakeMainMenu.menu_login_citizen(console)

    def menu_login_citizen(self,console):
        print("Porfavor, seleccione una de las siguentes opciones")
        try:
            user = console.int(input("1.Log in | 2. Registrarse | 3.Salir : "))
        except ValueError:
            print('eso no es un numero, intentelo nuevamente')
            self.FakeMainMenu.menu_login_citizen(console)
        if user == 1:
            self.FakeMainMenu.login(console)
        elif user == 2:
            self.FakeMainMenu.register(console)
        elif user == 3:
            self.FakeMainMenu.menu_o(console)
        else:
            print("Debes ingresar los numeros indicados anteriormente.")
            self.FakeMainMenu.menu_login_citizen(console)

    def menu_citizen(self,citizenidentifier,console):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
        for a in etlist.citizenlist:
            if int(df['CUIL'][citizenidentifier]) == int(a.CUIL):
                x = a
        if x.zone == -1:
            b = int(console.input(
                f'bienvenido al menu_citizen por primera vez, {x.name}!\n\nPorfavor, ingrese el numero respectivo a su zona:\n{registroDeZonas.listadoZonas(seconddf)}'))  # SOLO PUEDE SER UN NUMERO
            if b > (len(seconddf['Nombre']) - 1):
                print('este numero no es valido, vuelva a intentarlo')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.FakeMainMenu.menu_citizen(citizenidentifier,console)
            else:
                print('muchas gracias!')
                time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
            x.zone = b
        try:
            c = int(console.input(
                f'{x.name}, elija lo que quiere hacer:\n\n1.asistir a evento | 2.dejar de asistir a evento | 3.menu de amigos | 4.cambiar zona: '))  # SOLO PUEDE SER UN NUMERO
        except ValueError:
            print('Debe ingresar un numero')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.FakeMainMenu.menu_o(console)
        if c == 1:
            pass
        elif c == 2:
            pass
        elif c == 3:
            FakeMenuAmigos.friends_menu(citizenidentifier,console)
        elif c == 4:
            registroDeZonas.listadoZonas(seconddf)
            print(registroDeZonas.listadoZonas(seconddf))
            num = int(console.input("a que zona quiere cambiar?\n"))
            x.change_zone(num)
            print('su zona se actualizo correctamente')
            self.FakeMainMenu.menu_citizen(citizenidentifier,console)

    def log_adm(self,console):
        df = pandas.read_csv(os.path.abspath("Base_Adm.csv"))  # va el path csv de administradores
        admin_user = console.input("Ingrese su nombre de usuario como admnistrador: ")
        admin_serch = 0
        for a in df['Admin_user']:
            if str(admin_user) == str(a):
                break
            admin_serch += 1
        if admin_serch == len(df["Admin_user"]):
            print('su nombre no esta como usuario, volviendo al menu principal.')
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.FakeMainMenu.menu_o(console)
            return admin_serch
        admin_password = console.input('Ingrese su contraseña: ')
        if str(admin_password) == str(df['Password'][admin_serch]):
            print(f"Usted ingreso como {admin_user}, bienvenido.")
            FakemenuAdministrador.Bienvenido(console)
        else:
            print("Contraseña invalida, volviendo al menu principal.")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.FakeMainMenu.menu_o(console)


class FakemenuAdministrador():
    revisionlist = []

    def Bienvenido(self,console):
        choice = int(console.input("Elija una de las siguientes opciones:1-agregar evento| 2-Bannear| 3-remover Ban| 4-Ver lista de revisión: "))
        if choice == 1:
            zona = console.input('dime la zona del evento: ')
            nombre = console.input('titulo de evento: ')
            descripcion = console.input('descripcion del evento: ')
            latitud = console.input('latitud: ')
            longitud = console.input('longitud: ')
            administrator.addEvent(zona, nombre, descripcion, latitud, longitud)
            return FakemenuAdministrador.Bienvenido(console)
        elif choice == 2:
            return FakemenuAdministrador.BanCitizen(console)
        elif choice == 3:
            return FakemenuAdministrador.UnBanCitizen(console)
        elif choice == 4:
            defualt_revision_list.update_revision_list()
            return FakemenuAdministrador.chek_revision_list(console)

        else:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0

    def BanCitizen(self,console):
        usuarioseleccionado = int(console.input("A quien desea bannear? "))
        for usuarios in etlist.citizenlist:
            if usuarios.CUIL == usuarioseleccionado and usuarios.citizenBan == False:
                administrator.banCitizen(usuarios)
                print(f"el usuario con CUIL {usuarioseleccionado} fue banneado")
                return 0 #FakeadminMenu no vuelve a bienvenido
        print("Usuario no encontrado")
        return 0 #FakeadminMenu no vuelve a bienvenido

    def UnBanCitizen(self,console):
        usuarioseleccionado = int(console.input("A quien desea remover el ban? CUIL: "))
        for users in etlist.BannedCitizenList:
            if users.CUIL == usuarioseleccionado:
                administrator.unbanCitizen(users)
                print(f"se removio el ban de la persona con el CUIL: {usuarioseleccionado}")
                return FakemenuAdministrador.Bienvenido(console)
        print("Usuario no encontrado")
        return FakemenuAdministrador.Bienvenido(console)

    def chek_revision_list(self,console):
        print(defualt_revision_list.getlist())
        citizenindex = int(
            console.input("seleccione la posicion del ciudadano al que quiere revisar (empezando desde el 0): "))
        ban_choice = str(console.input("Quiere bannear al citizen? si/no: "))
        chosen_citizen = defualt_revision_list.revision_list[citizenindex]
        if ban_choice == "si":
            administrator.banCitizen(chosen_citizen)
            print("El usuario fue banneado")
            return FakemenuAdministrador.Bienvenido(console)
        else:
            defualt_revision_list.removecitizen(chosen_citizen)
            chosen_citizen.quien_me_rechazo = []
            print("El ciudadano fue removido de la lista de revision")
            return FakemenuAdministrador.Bienvenido(console)

    @classmethod
    def update_revision_list(cls):
        for citizen in etlist.citizenlist:
            if len(citizen.quien_me_rechazo) == 5:
                cls.revisionlist.append(citizen)


class FakeMenuAmigos:

    @staticmethod
    def friends_menu(user,console):
        df = pandas.read_csv(os.path.abspath("Database.csv"))
        for a in etlist.citizenlist:
            if int(df['CUIL'][user]) == int(a.CUIL):
                x = a
        a = int(console.input(
            f"{x.name}, bienvenido a sus contactos:\n\n1.Ver solicitudes | 2.Enviar solicitud | 3.Ver contactos | Volver menu"))
        if a == 1:
            pass
        elif a == 2:
            pass
        elif a == 3:
            pass
        else:
            i = 0
            for a in etlist.citizenlist:
                if user.CUIL == a.CUIL:
                    break
                i += 1
            FakeMainMenu.menu_citizen(user)

class registroDeZonas:

    @staticmethod
    def listadoZonas(eventos):
        zonitas = ''
        i = 0
        for zona in eventos['Nombre']:
            zonitas += f'{i} |' + zona + '\n'
            i += 1
        return zonitas

class Console:
    def input(self,msg):
        return input(msg)
    def print(self,msg):
        print(msg)

class FakeConsole():
    def __init__(self,lineas):
        self.lineas=lineas
    def input(self,msg):
        s = self.lineas.pop()
        return s

# class TestMainMenu(unittest.TestCase):
#     def test_login(self):
#         console=FakeConsole(["2","2","91121616818","11111111112","Valen","Valen","Valen","Di Capua","19"])
#         fake_main_menu_test1=FakeMainMenu()
#         fake_main_menu_test1.menu_o(console)
#         result=len(etlist.citizenlist)
#         print(etlist.citizenlist)

class TestmenuAdministrador(unittest.TestCase):
    def test_ban_citizen(self):

        fake_admin_menu_test1=FakemenuAdministrador()
        console=FakeConsole(["12345678910"])
        fake_admin_menu_test1.BanCitizen(console)
        result=len(etlist.BannedCitizenList)
        self.assertEqual(result,1)


if __name__=="__main__":
    unittest.main()
