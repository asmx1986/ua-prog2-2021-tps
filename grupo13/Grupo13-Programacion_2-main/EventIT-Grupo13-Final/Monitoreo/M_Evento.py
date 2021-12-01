from Monitoreo.Manipulacion_csv import writeRow, writeRow1, getValue, getDatabase, sortDatabase, compareFirst3Row, sumValue, confirmation


class Event:
    @staticmethod
    def addEvent(event_name, event_type, x, y, description):
        if 0 <= x <= 10 and 0 <= y <= 10:
            if confirmation("evento_tipo", event_type, 0):
                if not confirmation("evento", event_name, 0):
                    writeRow("evento", event_name, event_type, x, y, "Baja", description, 0)
                else:
                    print("\nEvento con mismo nombre, pruebe otro")
            else:
                print("\nTipo de evento no valido, creelo primero")
        else:
            return True

    @staticmethod
    def addType(event_type):
        if not confirmation("evento_tipo", event_type, 0):
            writeRow1("evento_tipo", event_type)
            print("\nTipo de evento creado")
        else:
            print("\nTipo de evento no valido, ya fue creado")

    @staticmethod
    def getParticipants(event_name):
        return getValue('evento', 'Name', 'Participants', event_name)

    @staticmethod
    def getEvents():
        return getDatabase('evento')

    @staticmethod
    def getType():
        return getDatabase('evento_tipo')

    @staticmethod
    def getApprovedEvents():
        dfn = getDatabase('evento')
        only_alta = dfn[(dfn["State"] == "Alta")]
        return only_alta

    @staticmethod
    def reportEvent(event_name, data1):
        if data1 == ['Nada que encontrar...']:
            length = 0
        elif isinstance(data1, list):
            length = len(data1)
        elif isinstance(data1, int):
            length = data1
        else:
            length = 1
        old_database = sortDatabase("evento")
        sumValue("evento", "Name", "Participants", event_name, length)
        new_database = sortDatabase("evento")
        if compareFirst3Row(old_database, new_database):
            print("\n=-==-==-==-= NUEVO evento en el top 3 ranking =-==-==-==-=")
