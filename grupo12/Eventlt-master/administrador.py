from listadeCuidadanos import etlist
from listaDeEventos import eventos

class administrator():

    def __init__(self, user):
        self.user = user

    @classmethod
    def addEvent(cls, location, nombre, descripcion, latitud, longitud):
        return eventos.eventCreator(location, nombre, descripcion, latitud, longitud)

    @staticmethod
    def banCitizen(citizen):
        citizen.citizenBan = True
        etlist.addBannedCitizen(citizen)
        
    @staticmethod
    def unbanCitizen(citizen):
        citizen.citizenBan = False
        etlist.removeBannedCitizen(citizen)
