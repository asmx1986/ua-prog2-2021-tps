# from EventIT.MapsSist.MapClass import Map

class UsuarioANSES:
    def __init__(self, name, telCell, cuil, ubicacion):
        self.__name = name
        self.__telCell = telCell
        self.__cuil = cuil
        self.__ubicacion = ubicacion

    def __repr__(self):
        return f"Usuario: {self.__name}\nNumero de telefono: {self.__telCell}\nCuil: {self.__cuil}"

    def getName(self):
        return self.__name

    def getTelCell(self):
        return self.__telCell

    def getCuil(self):
        return self.__cuil

    def getUbicacion(self):
        return self.__ubicacion

    def getZona(self, lista_de_zonas):
        for zona in lista_de_zonas:
            if self.__ubicacion.Get_Coordinates() in list(map(lambda x:x.Get_Coordinates(), zona.Get_Ubicaciones())): #la idea es ver si esa ubicacion es parte de la zona PROBAR
                return zona
