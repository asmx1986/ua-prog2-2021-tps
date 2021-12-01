import csv
import pandas as pd


class Anses:
    # Diferenciamos si es ciudadano o admin con la variable type
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

    def confirmation(self, data, num):
        user = self.type.lower()
        with open(f"../Database/DB_{user}.csv", "r") as file:
            database = csv.reader(file, delimiter=",")
            for line in database:
                if data == line[num]:
                    return True
            return False

    def confirmName(self, name):
        return self.confirmation(name, 0)

    def confirmCuil(self, cuil):
        return self.confirmation(cuil, 1)

    def confirmTelephone(self, telephone):
        return self.confirmation(telephone, 2)

    def confirmation2(self, login_type, login, check_type, check):
        df = pd.read_csv(f"../Database/DB_{self.type}.csv")
        return df.loc[df[login_type] == login, check_type].item() == check

    def confirmPassword(self, login_type, login, password):
        return self.confirmation2(login_type, login, "Password", password)

    @staticmethod
    def checkCuilAnses(cuil):
        with open(f"../Database/DB_anses.csv", "r") as file:
            database = csv.reader(file, delimiter=",")
            for line in database:
                if str(cuil) == line[0]:
                    return True
            return False

    @staticmethod
    def addCuil(cuil):
        if not Anses("ciudadano").checkCuilAnses(cuil):
            f = open("../Database/DB_anses.csv", "a", newline="")
            writer = csv.writer(f)
            writer.writerow([cuil])



