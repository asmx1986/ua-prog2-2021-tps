from EventIT.MapsSist.ZonaClass import Zona
from typing import List

class Map:
    def __init__(self, zonas: List[Zona]):
        self.__Zonas = zonas

    def __repr__(self):
        return f"{self.__Zonas}"

    def getListaDeZonas(self):
        return self.__Zonas.copy()

    def search_ubicacion(self, latitud, longitud):
        for zona in self.__Zonas:
            ubicaciones = zona.Get_Ubicaciones()
            for ubicacion in ubicaciones:
                latubi, lonubi = ubicacion.Get_Coordinates()
                if latubi == latitud and lonubi == longitud:
                    return ubicacion
        return False
