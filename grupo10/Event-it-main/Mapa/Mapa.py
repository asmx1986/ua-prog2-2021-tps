from matplotlib import pyplot as plt
from Anses.Anses import leerDataEspecificaEventoparaMapa, leerDataEspecificaEvento


def mapa():
    plt.style.use('seaborn')
    x=[]
    leerDataEspecificaEventoparaMapa(x,6)
    y=[]
    leerDataEspecificaEventoparaMapa(y, 7)
    nombres=[]
    s=[]
    leerDataEspecificaEventoparaMapa(s,3)
    sPrima = []
    indice=0
    while indice < len(s):
        appendeable = int(s[indice]) * 5
        sPrima.append(appendeable)
        indice = indice + 1
    leerDataEspecificaEvento(nombres,0)
    for i, label in enumerate(nombres):
        plt.annotate(label, (x[i], y[i]))
    colores = []
    indiceColores = 0
    while indiceColores < len(s):
        colores.append(indiceColores)
        indiceColores = indiceColores + 1
    plt.scatter(x, y, sPrima, c=colores,cmap = 'Blues', marker='o', edgecolor='black', linewidths=2, alpha=0.55)
    plt.title('EVENT-IT')
    plt.plot([0,0],[-100,100], linewidth=2, color='red')
    plt.plot([-100,100],[0,0], linewidth=2, color='red')
    plt.show()