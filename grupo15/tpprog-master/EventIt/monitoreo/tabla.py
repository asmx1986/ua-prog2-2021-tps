import csv
from operator import itemgetter
from gestiondeeventos.evento import Evento


class TabladeEstadistica:

    @classmethod
    def mostrarEventosTop(cls):
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataEventos\eventosReportados.csv",newline="") as archivo:
            reader = csv.reader(archivo)
            df = list(reader)
        archivo.close()

        df.pop(0)
        sorted_list = sorted(df, key=itemgetter(3), reverse=True)

        for i in range(0, 3):
            print(sorted_list[i])

    @classmethod
    def __filtrarEventos(cls):
        events=[[],[],[],[]]
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataEventos\eventosReportados.csv",newline="") as archivo:
            header = next(archivo)
            reader = csv.reader(archivo)
            for row in reader:
                if row[3]==1:
                    events[0].append(Evento(row[0],row[1],row[2],row[3]))
                if row[3]==2:
                    events[1].append(Evento(row[0],row[1],row[2],row[3]))
                if row[3]==3:
                    events[2].append(Evento(row[0],row[1],row[2],row[3]))
                if row[3]==4:
                    events.append(Evento(row[0],row[1],row[2],row[3]))
        return events

    @classmethod
    def eventosporZona(cls):
        something = TabladeEstadistica.__filtrarEventos()
        for i in something:
            return f"Zona {something.index(i)} {i}"
