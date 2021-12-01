from Monitoreo.Manipulacion_csv import getList, getValue


class Event:
    def __init__(self, event_type):
        self.event_type = event_type
        self.coords_x = self.getcoordsx()
        self.coords_y = self.getcoordsy()
        self.state = "Baja"
        self.participants = self.getparticipants()
        self.numparticipants = self.getnumParticipants()

    def getparticipants(self):
        return getList('DB_evento', 'Type', 'Participants', self.event_type)

    def getcoordsx(self):
        return getValue('DB_evento', 'Type', 'Coords_x', self.event_type)

    def getcoordsy(self):
        return getValue('DB_evento', 'Type', 'Coords_y', self.event_type)

    def getnumParticipants(self):
        return len(self.participants)

    def getype(self):
        return self.event_type
