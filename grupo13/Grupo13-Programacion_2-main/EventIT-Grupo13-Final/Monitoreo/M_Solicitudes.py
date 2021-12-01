from Monitoreo.M_ABM import ABM
from Monitoreo.Manipulacion_csv import writelist, getValue, getList, sumValue


class Solicitud:
    def __init__(self, transmitter, receiver):
        self.transmitter = transmitter
        self.receiver = receiver

    def send(self, friend_request):
        vacio = ['Nada que encontrar...']
        name_r = self.receiver.name
        name_t = self.transmitter.name
        if self.find_name("ciudadano_s", "Friend_request", name_r, name_t) or self.find_name("ciudadano_a", "Friends", name_r, name_t):
            print("\nSolicitud enviada con anterioridad")
        else:
            writelist("ciudadano_s", 'Name', 'Friend_request', name_r, friend_request, vacio)
            print("\nSolicitud enviada")

    @staticmethod
    def find_name(csv_name, column2, name_r, name_t):
        lista = getList(csv_name, "Name", column2, name_r)
        for request in lista:
            if request == name_t:
                return True

#   En caso que se rechace la solicitud
    def sumRejected_requests(self):
        name = self.receiver.getname()
        sumValue("ciudadano", "Name", "Rejected_requests", name, 1)
        rejected = getValue('ciudadano', 'Name', 'Rejected_requests', name)
        if rejected >= 5:
            ABM().block(name)
