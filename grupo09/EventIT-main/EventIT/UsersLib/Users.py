from abc import ABC, abstractmethod
import os


class Usuario(ABC):
    @abstractmethod
    def __init__(self, name):
        self.__Name = name

    def Get_Name(self):
        return self.__Name

    def Mod_Name(self, newName: str):
        #Solo la puede llamar el AMB
        path = os.path.dirname(os.path.realpath(__file__)) + r'\registro_de_usuarios.txt'
        with open(path,'r') as f:
            replacement = ""
            # using the for loop
            for line in f:
                line = line.strip()
                changes = line.replace(self.__Name, newName)
                replacement = replacement + changes + "\n"

            f.close()
        # opening the file in write mode
        with open(path,'w') as f:
            f.write(replacement)
            f.close()

        self.__Name = newName

