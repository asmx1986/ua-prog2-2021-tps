from Monitoreo.M_Anses import Anses
from Monitoreo.M_ABM import ABM
from Monitoreo.Manipulacion_csv import writeRow, getRow, writeRow2


class Login:
    @staticmethod
    def checkLogin(login, login_type):
        a = Login()
        if a.checkName(login, login_type):
            return login
        elif a.checkCuil(login, login_type):
            return login
        elif a.checkTelephone(login, login_type):
            return login

    @staticmethod
    def checkName(name, user_type):
        name = str(name)
        return Anses(user_type).confirmName(name)

    @staticmethod
    def getName(user_type, login_type, login):
        login = str(login)
        return Anses(user_type).getName(login_type, login)

    @staticmethod
    def checkCuil(cuil, user_type):
        cuil = str(cuil)
        return Anses(user_type).confirmCuil(cuil)

    @staticmethod
    def checkTelephone(telephone, user_type):
        telephone = str(telephone)
        return Anses(user_type).confirmTelephone(telephone)

    @staticmethod
    def getInfo(user_type, login_type):
        info = getRow(user_type, login_type)
        del info[3]

    @staticmethod
    def register(user_type, name, cuil, telephone, password):
        a = Login().checkName(name, user_type)
        b = Login().checkCuil(cuil, user_type)
        c = Login().checkTelephone(telephone, user_type)
        d = Anses(user_type).checkCuilAnses(cuil)
        if d:
            if not a and not b and not c:
                if Login().addUser(user_type, name, cuil, telephone, password):
                    return True
                else:
                    print("\nDatos ya usados, intentelo de nuevo")
            else:
                print("\nDatos ya usados por otro ciudadano")
        else:
            print("\nCuil no encontrado en Anses")

    @staticmethod
    def loginAdmin(login_type, login_data, password):
        return Login().login("admin", login_type, login_data, password)

    @staticmethod
    def loginCiudadano(login_type, login_data, password):
        return Login().login("ciudadano", login_type, login_data, password)

    @staticmethod
    def login(user_type, login_type, login_data, password):
        check = Login().checkLogin(login_data, user_type)
        if check:
            confirm_password = Anses(user_type).confirmPassword(login_type, login_data, password)
            if login_type == "Name" or "Cuil" or "Telephone":
                if not ABM().getBlock(user_type, login_type, login_data):
                    if confirm_password:
                        return True
                    else:
                        print("\nContraseña incorrecta")
                else:
                    print("\nUsuario bloqueado")
            else:
                print("\nEl tipo de ingreso es incorrecto")
        else:
            print("\nLogin incorecto")

    @staticmethod
    def addUser(user_type, name, cuil, telephone, password):
        writeRow(user_type, name, cuil, telephone, password, 0, "No")
        if user_type != "admin":
            writeRow2('Camigos', name, ['Nada que encontrar...'])
            writeRow2('Csolicitudes', name, ['Nada que encontrar...'])
        return True
