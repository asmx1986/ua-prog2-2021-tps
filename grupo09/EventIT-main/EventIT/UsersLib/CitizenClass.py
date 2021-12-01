from EventIT.UsersLib.Users import Usuario
import os


class Ciudadano(Usuario):
    def __init__(self, name, telefono, cuil):
        super().__init__(name)
        self.__Telefono = telefono
        self.__CUIL = cuil
        self.__ContactosDeInteres = []
        self.__ListaDeSolicitudes = []
        self.__ListaDeRechazos = []

    def __repr__(self):
        return f"{self.Get_Name()}"

    def Get_Telefono(self):
        return self.__Telefono

    def Get_Cuil(self):
        return self.__CUIL

    def Get_ContactosDeInteres(self):
        return self.__ContactosDeInteres.copy()

    def Get_ListaDeSolicitudes(self):
        return self.__ListaDeSolicitudes.copy()
    
    def Get_ListaDeRechazos(self):
        return self.__ListaDeRechazos.copy()

    def Mod_Telefono(self, telefono: str):
        #Solo la puede llamar el AMB
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
        with open(path,'r') as f:
            replacement = ""
            # using the for loop
            for line in f:
                line = line.strip()
                changes = line.replace(str(self.__Telefono), str(telefono))
                replacement = replacement + changes + "\n"

            f.close()
        # opening the file in write mode
        with open(path,'w') as f:
            f.write(replacement)
            f.close()

        self.__Telefono = telefono


    def Mod_CUIL(self, cuil: str):
        #Solo la puede llamar el AMB
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
        with open(path,'r') as f:
            replacement = ""
            # using the for loop
            for line in f:
                line = line.strip()
                changes = line.replace(str(self.__CUIL), str(cuil))
                replacement = replacement + changes + "\n"

            f.close()
        # opening the file in write mode
        with open(path,'w') as f:
            f.write(replacement)
            f.close()
        self.__CUIL = cuil

    def Mod_ContactosDeInteres(self, ciudadano, add: bool):
        """Permite agregar o eliminar un contacto.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo
            *Solo accedible por FrienshipSistem"""
        if add:
            self.__ContactosDeInteres.append(ciudadano)
        else:
            self.__ContactosDeInteres.remove(ciudadano)

    def Mod_ListaDeSolicitudes(self, ciudadano, add: bool):
        """Permite agregar o eliminar un ciudadano a la lista de solicitudes.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo
            *Solo accedible por FrienshipSistem"""
        if add:
            self.__ListaDeSolicitudes.append(ciudadano)
        else:
            self.__ListaDeSolicitudes.remove(ciudadano)

    def Mod_ListaDeRechazos(self, ciudadano, add: bool):
        """Permite agregar o eliminar un ciudadano a la lista de rechazos.\n
            add = True, para agregarlo.\n
            add = False, para eliminarlo
            *Solo accedible por FrienshipSistem"""
        if add:
            self.__ListaDeRechazos.append(ciudadano)
        else:
            self.__ListaDeRechazos.remove(ciudadano)

        
