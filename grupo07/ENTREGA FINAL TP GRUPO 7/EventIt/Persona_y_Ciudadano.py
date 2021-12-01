import csv
from abc import ABC
import InfoBase
from Error import RegisterError
from Usuario_Ciudadano import CiudadanoUsuario


class Persona(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre


class Ciudadano(Persona):
    def __init__(self, nombre, cuil, celular):
        super().__init__(nombre)
        self.__cuil = cuil
        self.__celular = celular

    def registrarse(self, usuario_nombre, clave):
        try:
            with open("datasetAnses.csv") as csv_file:
                archivo = csv.reader(csv_file, delimiter=",")
                header = next(archivo)
                i = 0
                for row in archivo:
                    if self.__cuil == int(row[1]) and self.__celular == int(row[2]):
                        i += 1
                        usuario_ciudadano = CiudadanoUsuario(usuario_nombre, self.__cuil, self.__celular, clave)
                        InfoBase.ciudadanos_usuarios.append(usuario_ciudadano)
                        InfoBase.ciudadanos_usuarios_nombres.append(usuario_nombre)
                        InfoBase.ciudadanos_usuarios_claves.append(clave)
                        InfoBase.ciudadanos_usuarios_celulares.append(self.__celular)
                        InfoBase.ciudadanos_usuarios_CUILs.append(self.__cuil)
                        return usuario_ciudadano
                if i == 0:
                    raise RegisterError()
        except RegisterError as r:
            return r.get_mensaje()


"""Meli = Ciudadano("Melina Juarez", 98765, 742684)
print(Meli.registrarse(Meli, 123))
"""
