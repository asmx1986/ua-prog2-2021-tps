import matplotlib.pyplot as plt
from event_administrator import EventAdministrator
import csv
from event import Event
from ubicacion import Ubicacion
from ranking import Ranking
import main
import numpy as np





#print(events)






def mapa():
    events = Ranking.getFinalRanking()
    max_coordenadasx = []
    max_coordenadasy = []
    coordenadasx = []
    coordenadasy = []


    #for event in EventAdministrator.actualEvents:
    for event in events:
            top3_eventos = event[1][0:3]
            notTop3_eventos = event[1][4:]
            #for eventt in event[1]:
            for eventt in top3_eventos:
                x = eventt.location.getX()
                y = eventt.location.getY()
                max_coordenadasx.append(x)
                max_coordenadasy.append(y)
            for eventtt in notTop3_eventos:
                x = eventtt.location.getX()
                y = eventtt.location.getY()
                coordenadasx.append(x)
                coordenadasy.append(y)



    area = 300


    with open("zonas.csv") as csv_file:
        zonas = csv.reader(csv_file, delimiter = ",")
        for row in zonas:
            Xi = int(row[1])
            Xf = int(row[2])
            Yi = int(row[3])
            Yf = int(row[4])
            plt.axvline(Xi)
            plt.axhline(Yi)
            #zonass.append([Xi,Xf,Yi,Yf])
            #for zona in zonass:
             #   plt.axvline(Xi)
              #  plt.axhline(Yi)

    plt.scatter(coordenadasx,coordenadasy, c = "green")
    plt.scatter(max_coordenadasx,max_coordenadasy,  c = "red")
    plt.title("eventos en tiempo real")
    #plt.grid(color = "blue")
    plt.show()

    #guardar grafico
    filename = r"C:\Users\Facundo\PycharmProjects\grafico tp-prog"
    plt.savefig(filename)


    #mostrar grafico

#mapa()
