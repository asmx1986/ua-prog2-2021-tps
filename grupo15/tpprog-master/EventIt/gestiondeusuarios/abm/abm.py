import csv
import pandas as pd
from gestiondeusuarios.usuarios.administradores import Administrador


class ABM:
    __usuarios=[]
    __contrasenas=[]

    @classmethod
    def habilitarAdministrador(cls,usuario,contrasena):
        ABM.__columnaaLista()
        if usuario not in ABM.__usuarios:
            ABM.__ingresaradministrador(usuario,contrasena)
        else:
            raise ValueError("Este usuarios ya existe")

    @classmethod
    def __ingresaradministrador(cls, usuario, contrasena):
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\data\administradoresData.csv","a",newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow([usuario,contrasena])
            archivo.close()

    @classmethod
    def inhabilitarAdministrador(cls, usuario):
        """Se puede inhabiltar un administrador despues se ve pues dificil"""
        pass


    @classmethod
    def iniciarAdministrador(cls, usuario, contrasena):
        try:
            ABM.__columnaaLista()
            if cls.__usuarios.index(usuario) == cls.__contrasenas.index(contrasena):
                return Administrador()
        except ValueError:
            print("Usuario o contraseña incorrecta")


    @classmethod
    def __columnaaLista(cls):
        with open(r"C:\Users\Francisco\Desktop\Prog 2\EventIt\data\administradoresData.csv","r+") as archivo:
            header = next(archivo)
            column_names=["usuarios","contrasenas"]
            df = pd.read_csv(archivo,names=column_names)
            cls.__usuarios=df.usuarios.tolist()
            cls.__contrasenas =df.contrasenas.tolist()

