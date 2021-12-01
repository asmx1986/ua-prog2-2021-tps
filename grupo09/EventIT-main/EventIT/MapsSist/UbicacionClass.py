class Ubicacion:
    def __init__(self, latitud, longitud):
        self.__Latitud = latitud
        self.__Longitud = longitud

    def __repr__(self):
        return f'({self.__Latitud},{self.__Longitud})'

    def Get_Coordinates(self):
        return (self.__Latitud, self.__Longitud)
