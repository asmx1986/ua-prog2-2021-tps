import csv


class Sensor:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __registrarEvento(self, lista):
        evento= lista[0]
        participantes = len(lista)
        fila=[evento.getTipo(),self.x,self.y,participantes]
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataEventos\eventosReportados.csv","a",newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(fila)
            archivo.close()



    def filtrarEventos(self,lista):
        """Se puede poner y filtrar por fecha y hora"""
        eventosfiltrados=[]
        for ciudadano in lista:
            eventosdeC= ciudadano.getEventos()
            eventosfiltrados += list(filter(lambda x: (x.getX() == self.x ) and (x.getY() == self.y),eventosdeC))
        self.__registrarEvento(eventosfiltrados)



