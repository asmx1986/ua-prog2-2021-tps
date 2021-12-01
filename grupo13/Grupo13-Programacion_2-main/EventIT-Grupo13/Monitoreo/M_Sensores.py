from Monitoreo.Manipulacion_csv import writeRow, writelist, getList, getDatabase, sortDatabase, compareFirst3Row
from Monitoreo.M_Anses import Anses


class Sensor:
    @staticmethod
    def addEvent(event_type, x, y, description):
        if 0 <= x <= 10 and 0 <= y <= 10:
            writeRow("evento", event_type, x, y, "Baja", description, ['Nada que encontrar...'])
        else:
            return True

    @staticmethod
    def getParticipants(event_type):
        return getList('DB_evento', 'Type', 'Participants', event_type)

    @staticmethod
    def getEvents():
        return getDatabase('DB_evento')

    @staticmethod
    def getApprovedEvents():
        dfn = getDatabase('DB_evento')
        only_alta = dfn[(dfn["State"] == "Alta")]
        return only_alta

    @staticmethod
    def reportEvent(event_type, names_list):
        participants_list = Sensor().getParticipants(event_type)
        ranking = sortDatabase('DB_evento')
        for participant in participants_list:
            for name in names_list:
                if participant == name:
                    print("\nCiudadano que ya participa del evento, se procederá a ignorarlo")
                    if isinstance(names_list, list):
                        names_list.remove(name)
                    else:
                        names_list = ['Nada que encontrar...']
                elif not Anses('ciudadano').confirmName(name):
                    print("\nNombre no encontrado en el sistema, se procederá a ignorarlo")
                    if isinstance(names_list, list):
                        names_list.remove(name)
                    else:
                        names_list = ['Nada que encontrar...']
        if participants_list == ['Nada que encontrar...']:
            if len(names_list) == 1:
                writelist('DB_evento', 'Type', 'Participants', event_type, names_list, ['Nada que encontrar...'])
            else:
                writelist('DB_evento', 'Type', 'Participants', event_type, names_list, ['Nada que encontrar...'])
        elif not names_list:
            pass
        else:
            for name in names_list:
                writelist('DB_evento', 'Type', 'Participants', event_type, name, ['Nada que encontrar...'])
        new_database = sortDatabase('DB_evento')
        if not compareFirst3Row(ranking, new_database, 'Type'):
            print("\n=-==-==-==-= NUEVO evento en el top 3 ranking =-==-==-==-=")

    def delreportEvent(self, event_type, name):
        if len(self.getParticipants(event_type)) == 1:
            self.getParticipants(event_type).remove(name)
            writelist("DB_evento", 'Type', 'Participants', event_type, ['Nada que encontrar...'], self.getParticipants(event_type))
        else:
            new_participants = self.getParticipants(event_type)
            new_participants.remove(name)
            writelist("DB_evento", 'Type', 'Participants', event_type, new_participants, self.getParticipants(event_type))
