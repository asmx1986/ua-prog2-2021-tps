from Monitoreo.Manipulacion_csv import write, getValue


class ABM:
    @staticmethod
    def getBlock(user_type, login_type, login):
        blocked = getValue(f'DB_{user_type}', login_type, 'Blocked', login)
        return blocked == "Yes"

    @staticmethod
    def unblock(name):
        write('DB_ciudadano', "Name", "Blocked", name, "No")

    @staticmethod
    def block(name):
        write('DB_ciudadano', "Name", "Blocked", name, "Yes")

    # Cambiar de alta a baja para el evento
    @staticmethod
    def setAlta(event_type):
        write('DB_evento', "Type", "State", event_type, "Alta")

    @staticmethod
    def setBaja(event_type):
        write('DB_evento', "Type", "State", event_type, "Baja")
