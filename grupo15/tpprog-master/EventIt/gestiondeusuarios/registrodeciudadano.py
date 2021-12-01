from gestiondeusuarios.datapreexistente.ansesdata import AnsesData
from gestiondeusuarios.usuarios.ciudadano import Ciudadano

class GestiondeUsuarios:
    def __init__(self):
        self.__ciudadanos = []

    def registro(self, cuil, telefono, contrasena):
        """Estaria bueno poner que en caso de que se vuelva a registrar que le se salga un error de usuarios
                                                ya registrado """
        try:

            if (AnsesData.compararCuilyTelefono(cuil,telefono)) == True:
                    self.__ciudadanos.append(Ciudadano(telefono, cuil, contrasena))
            else:
                raise ValueError("Su telefono o cuil son incorrectos")
        except ValueError:
            print("Su usuario no esta registrado en el ANSES")

    def logCiudadano(self, cuil, contrasena):
        for ciudadano in self.__ciudadanos:
            if (ciudadano.getCuil() == str(cuil)) and ciudadano.getContrasena() == contrasena:
                return ciudadano

    def buscarusuario(self, data):
        """Solo para enviar y etc de solicitudes"""
        for ciudadano in self.__ciudadanos:
            if (str(data) == ciudadano.getCuil()) or (data == ciudadano.getContrasena()):
                return ciudadano

    def getCiudadanos(self):
        return self.__ciudadanos
