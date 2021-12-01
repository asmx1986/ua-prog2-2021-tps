import pandas as pd
from Monitoreo.Manipulacion_csv import writelist, getValue, getList


class Solicitud:
    def __init__(self, transmitter, receiver):
        self.transmitter = transmitter
        self.receiver = receiver

    #En caso que se envie una solicitud
    def send(self, friend_request):
        vacio = ['Nada que encontrar...']
        name_r = self.receiver.name
        name_t = self.transmitter.name
        if self.find_name("DB_csolicitudes", "Friend_request", name_r, name_t) or self.find_name("DB_camigos", "Friends", name_r, name_t):
            print("\nSolicitud enviada con anterioridad")
        else:
            writelist("DB_Csolicitudes", 'Name', 'Friend_request', name_r, friend_request, vacio)
            print("\nSolicitud enviada")

    @staticmethod
    def find_name(csv_name, column2, name_r, name_t):
        lista = getList(csv_name, "Name", column2, name_r)
        for request in lista:
            if request == name_t:
                return True

#   En caso que se rechace la solicitud
    def sumRejected_requests(self):
        self.receiver.rejected_requests += 1
        Solicitud(self.transmitter, self.receiver).sumRejected_requests_csv()
        Solicitud(self.transmitter, self.receiver).rejectedBlocking_cvs()

    def sumRejected_requests_csv(self):
        name = self.receiver.getname()
        df = pd.read_csv("../Database/DB_ciudadano.csv")
        df.loc[df["Name"] == name, "Rejected_requests"] += 1
        df.to_csv("../Database/DB_ciudadano.csv", index=False)

    def rejectedBlocking_cvs(self):
        name = self.receiver.getname()
        rejected = getValue('DB_ciudadano', 'Name', 'Rejected_requests', name)
        if rejected >= 5:
            df = pd.read_csv("../Database/DB_ciudadano.csv")
            df.loc[df["Name"] == name, "Blocked"] = "Yes"
            df.to_csv("../Database/DB_ciudadano.csv", index=False)


