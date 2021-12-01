from Monitoreo.Manipulacion_csv import write, getValue


class ABM:
    @staticmethod
    def getBlock(user_type, login_type, login):
        blocked = getValue(f'{user_type}', login_type, 'Blocked', login)
        return blocked == "Yes"

    @staticmethod
    def unblock(name):
        write('ciudadano', "Name", "Blocked", name, "No")

    @staticmethod
    def block(name):
        write('ciudadano', "Name", "Blocked", name, "Yes")

    # Cambiar de alta a baja para el evento
    @staticmethod
    def setAlta(event_name):
        write('evento', "Name", "State", event_name, "Alta")

    @staticmethod
    def setBaja(event_name):
        write('evento', "Name", "State", event_name, "Baja")
