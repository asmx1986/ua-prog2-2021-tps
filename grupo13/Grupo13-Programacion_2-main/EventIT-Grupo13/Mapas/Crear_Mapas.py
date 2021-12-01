from Monitoreo.Manipulacion_csv import sortDatabase_coords, sortDatabase
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def resetMap():
    map_participants = ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    dfn = pd.DataFrame(map_participants, columns=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    dfn.to_csv("../Database/DB_mapa.csv", index=False)


def setMapa(state):
    resetMap()
    df_mapa = pd.read_csv("../Database/DB_mapa.csv")
    x = 0
    while x <= 10:
        y = 0
        while y <= 10:
            df = sortDatabase_coords('DB_evento', x, y)
            if state == "Alta":
                df = df[(df["State"] == "Alta")]
            lista = df.values.tolist()
            num = 0
            while len(lista) > num:
                num_part = lista[num][5]
                df_mapa.iloc[y][x] += num_part
                df_mapa.to_csv("../Database/DB_mapa.csv", index=False)
                num += 1
            y += 1
        x += 1
    df_mapa.to_csv("../Database/DB_mapa.csv", index=False)


def createMap(state):
    setMapa(state)
    db_mapa = pd.read_csv("../Database/DB_mapa.csv")
    ax = sns.heatmap(db_mapa, annot=True, fmt="d", linewidths=1.5, square=True, cmap='Blues_r')
    plt.gca().invert_yaxis()
    if state == "Alta":
        ax.set_title('Número de participantes por zona (solo habilitados)', size=10)
    else:
        ax.set_title('Número de participantes por zona', size=10)
    ax.set_xlabel('Coordenada X', size=10)
    ax.set_ylabel('Coordenada Y', size=10)
    plt.show()


def createBar():
    df = sortDatabase("DB_evento")
    sns.set_style('darkgrid')
    sns.set_palette('Set2')
    ax = sns.barplot(x="Type", y="Participants", data=df.iloc[:3], n_boot=3)
    ax.set_title('Número de participantes por evento - Top 3', size=15)
    ax.set_xlabel('Eventos', size=10)
    ax.set_ylabel('Número de participantes', size=10)
    plt.show()


def createBarbyzone(x, y):
    df = sortDatabase_coords("DB_evento", x, y)
    sns.set_style('darkgrid')
    sns.set_palette('Set2')
    ax = sns.barplot(x="Type", y="Participants", data=df.iloc[:3])
    ax.set_title('Número de participantes por evento - Top 3', size=15)
    ax.set_xlabel('Eventos', size=10)
    ax.set_ylabel('Número de participantes', size=10)
    plt.show()
