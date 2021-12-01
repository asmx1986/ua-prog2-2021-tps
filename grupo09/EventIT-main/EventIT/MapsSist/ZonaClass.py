from typing import List
from EventIT.MapsSist.UbicacionClass import Ubicacion

class Zona:
    def __init__(self, ubicaciones: List[Ubicacion], numeroDeZona, nombre):
        self.__Ubicaciones = ubicaciones
        self.__NumeroDeZona = numeroDeZona
        self.nombre = nombre

    def __repr__(self):
        return f"{self.nombre}"

    def Get_Ubicaciones(self):
        return self.__Ubicaciones

    def Get_NumeroDeZona(self):
        return self.__NumeroDeZona
