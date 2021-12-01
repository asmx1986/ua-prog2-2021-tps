from Monitoreo.Manipulacion_csv import write


class Admin:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def setAlta(event_type):
        write('DB_evento', 'Type', 'State', event_type, "Alta")

    @staticmethod
    def setBaja(event_type):
        write('DB_evento', 'Type', 'State', event_type, "Baja")

    @staticmethod
    def unblock(name):
        write('DB_ciudadano', 'Name', 'Blocked', name, "No")

    @staticmethod
    def block(name):
        write('DB_ciudadano', 'Name', 'Blocked', name, "Yes")
