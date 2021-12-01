import csv
import pandas as pd
from Monitoreo.Manipulacion_csv import confirmation


class Anses:
    def __init__(self, user_type):
        self.type = user_type

    def getter(self, login_request, login_type, login):
        df = pd.read_csv(f"../Database/DB_{self.type}.csv")
        request = df.loc[df[login_type] == login, login_request].item()
        return request

    def getName(self, login_type, login):
        return self.getter("Name", login_type, login)

    def getCuil(self, login_type, login):
        return self.getter("Cuil", login_type, login)

    def getTelephone(self, login_type, login):
        return self.getter("Cuil", login_type, login)

    def confirmName(self, name):
        return confirmation(self.type, name, 0)

    def confirmCuil(self, cuil):
        return confirmation(self.type, cuil, 1)

    def checkCuilAnses(self, cuil):
        return confirmation("anses", cuil, 0)

    def confirmTelephone(self, telephone):
        return confirmation(self.type, telephone, 2)

    def confirmPassword(self, login_type, login, password):
        df = pd.read_csv(f"../Database/DB_{self.type}.csv")
        return df.loc[df[login_type] == login, "Password"].item() == password

    @staticmethod
    def addCuil(cuil):
        if not Anses("ciudadano").checkCuilAnses(cuil):
            f = open("../Database/DB_anses.csv", "a", newline="")
            writer = csv.writer(f)
            writer.writerow([cuil])
