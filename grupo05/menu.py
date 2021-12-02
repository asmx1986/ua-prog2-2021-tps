import os
import pandas as pd #descargar en la terminal


df = pd.read_csv(os.path.abspath('Anses.csv'))
#print(df)


def findCitizen(cuil):
   with open('Anses.csv', 'r'):
        reader = pd.read_csv(os.path.abspath('Anses.csv'))
        i = 0
        try:
            if cuil == int(cuil):
                for row in reader['Cuil']:
                    if str (row) == str (cuil):
                        nombre = reader['Nombre'][i]
                    else:
                        i +=1
                return nombre
        except Exception:
            return "Ingrese un cuil valido"



#print(findCitizen(324566))


def menu_inicial ():
    print("Bienvenido a EventTLT")
    menu_login = "1.Registrarse | 2.Ingresar como Usuario | 3.Ingresar sensor| 4.Ingresar como admin:\n "
    print(menu_login)
    try:
        eleccion = int(input("ingrese in su elección"))
        if eleccion == 1:
            register()
        elif eleccion == 2:
            login()
        elif eleccion == 3:
            pass
        elif eleccion == 4:
            pass
    except ValueError:
        print( "Ingrese un numero valido del 1 al 4")
#menu_inicial()
def register():
    c = input(("Inserte Cuil: "))
    n = input("Inserte Nombre: ")
    contra = input("Inserte Contrasenia: ")
    edad = input("Cual es su edad: ")
    with open('LogIn.csv', 'r'):
        cuentas = pd.read_csv(os.path.abspath('LogIn.csv'))
        j = 0
        for a in cuentas['Cuil']:
            if a == c:
                return "Esa cuenta ya existe"
            for b in cuentas ['Name']:
                if b == n:
                    return 'Esa cuenta ya existe'

        j +=1
        cuentas.loc[j] = [c, n, contra, edad]
        print(cuentas)
#register()


def login():
    n = input("Inserte Nombre: ")
    c = input(("Inserte Contraseña: "))
    i=0
    cuentas = pd.read_csv(os.path.abspath('LogIn.csv'))
    for a in cuentas ['Nombre']:
        if str (n) == str (a):
            break
        i +=1
    if str (c) == str (df['Password'][i]):
        print ("Bienvenido")



