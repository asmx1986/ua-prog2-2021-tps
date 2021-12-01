import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd


class Mapa:
    __x = []
    __y = []
    __participantes = []
    tipo =[]

    @classmethod
    def __deColumnaaLista(cls):
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\gestiondeeventos\dataEventos\eventosReportados.csv","r+") as archivo:
            header = next(archivo)
            column_names=["tipo","x","y", "participantes"]
            df = pd.read_csv(archivo,names=column_names)
            cls.__x=df.x.tolist()
            cls.__y =df.y.tolist()
            cls.__participantes = df.participantes.tolist()
            cls.__tipo = df.tipo.tolist()

    @classmethod
    def dibujarMapaCiudad(cls):
        Mapa.__deColumnaaLista()
        x = cls.__x
        y = cls.__y
        tamano = cls.__sizer()
        colores = cls.__colorer()

        #Graficar coordenadas
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.scatter(x=x,y=y,s= tamano,color=colores)
        #Graficar mapa (Rectangulo)
        ax.add_patch(
            patches.Rectangle(
                xy=(0,0),
                width=6,
                height=6,
                linewidth=1,
                color='red',
                fill=False))
        ax.set_title("Coordenadas de evento")

        #Guardar grafico
        filename = r"C:\Users\Francisco\Desktop\Prog 2\EventIt\monitoreo\plot1.png"
        plt.savefig(filename)
        #Mostrar grafico
        plt.show()

    @classmethod
    def __sizer(cls):

        size=[]
        for i in cls.__participantes:
            if i == 1:
                size.append(200)
            if i > 1 and i <= 3:
                size.append(500)
            if i > 3:
                size.append(1500)
        return size

    @classmethod
    def __colorer(cls):
        color=[]
        for i in cls.__participantes:
            if i == 1:
                color.append('lightcoral')
            if i > 1 and i <= 3:
                color.append('indianred')
            if i > 3:
                color.append('darkred')
        return color
