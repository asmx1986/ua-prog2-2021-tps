# AGREGAR AL CODIGO DENTRO DE LOS METODOS
# ORDENA LA LISTA DEPENDIENDO DE LAS PERSONAS EN LA ZONA 
# HAY QUE BUSCAR LA FORMA DE REPRESENTARLO COMO ZONAS
import csv
import pandas
import os
from listaDeEventos import eventos
from matplotlib import pyplot

# df=pd.read_csv("Estadisticas.csv")
# print (df.info())
pyplot.title("Cantidad de personas por zona")
pyplot.xlabel("Zonas",labelpad=6)
pyplot.ylabel("Personas",labelpad=6)
df = pandas.read_csv(os.path.abspath("Database.csv"))
seconddf = pandas.read_csv(os.path.abspath("zona.csv"))
users = open("Database.csv","r") 
file = csv.DictReader(users)
zonas=list(seconddf['Nombre'])
nombres = []
i = 0
for col in file:
    nombres.append(col['Name'])
    i += 1


p_x_zona = [[]]
new=[]
a = 0
for sector in seconddf['Nombre']:
    i = 0
    for zona in df['Zona']:
        if a == zona:
            p_x_zona[a].append(nombres[i])
            i += 1
        else:
            i += 1
    new.append(len(p_x_zona[a]))
    a += 1
    p_x_zona.append([]) 



# for events in eventos.list[2]:
#     print(len(events.listOfPeople))

# print (eventos.list)
# # for event in listaDeEventos.eventos.list[0]:
#     # print(event)

# print (p_x_zona)
# print (listaDeEventos.eventos.list)


pyplot.bar(zonas,new)
pyplot.show()

