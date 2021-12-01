from GestionUsuarios import Administrador
from Anses.Anses import leerDataEspecificaDeAdmin,leerAdministradores,adminCleaner,adminListPlacerAfterClean,escribirAdministrador

def crearAdministrador(nuevoUsuario, nuevaContrasena, accesoAABM):
    newAdmin = Administrador.Administrador(nuevoUsuario, nuevaContrasena, accesoAABM)
    return newAdmin
def eliminarAdministrador(usuarioAeliminar):
    listaNombres=[]
    leerDataEspecificaDeAdmin(listaNombres,0)
    indiceNombre = 0
    posicionDelNombre = -1
    while indiceNombre < len(listaNombres):
        if usuarioAeliminar == listaNombres[indiceNombre]:
            posicionDelNombre = indiceNombre
            indiceNombre = indiceNombre + len(listaNombres)
        else:
            indiceNombre = indiceNombre + 1
    listaAdmins = []
    leerAdministradores(listaAdmins)
    listaAdmins.pop(posicionDelNombre)
    adminCleaner()
    adminListPlacerAfterClean(listaAdmins)
    print("Se elimino el usuario " + usuarioAeliminar + ".")
# "Se le pasa un usuario de Administrador y se le modifica la contraseña y se guarda en el archivo de texto listaAdministradores"
def modificarUsernameAdministrador(usernameViejo):
    usernameNuevo = str(input("Ingrese su nuevo nombre de usuario, no puede ser 0: "))
    if usernameNuevo == "0":
        print("Escribiste 0, el cual es un username invalido")
        modificarUsernameAdministrador(usernameViejo)
    else:
        listaUsernameNuevo=[usernameNuevo]
        listaNombres = []
        leerDataEspecificaDeAdmin(listaNombres,0)
        indiceNombre = 0
        posicionDelNombre=-1
        while indiceNombre < len(listaNombres):
            if usernameViejo == listaNombres[indiceNombre]:
                posicionDelNombre = indiceNombre
                indiceNombre = indiceNombre + len(listaNombres)
            else:
                indiceNombre = indiceNombre + 1
        listaContrasenas = []
        leerDataEspecificaDeAdmin(listaContrasenas,1)
        listaUsernameNuevo.append(listaContrasenas[posicionDelNombre])
        listaABM = []
        leerDataEspecificaDeAdmin(listaABM,2)
        print(listaABM)
        listaUsernameNuevo.append(listaABM[posicionDelNombre])
        print(listaUsernameNuevo)
        listaAdmins=[]
        leerAdministradores(listaAdmins)
        listaAdmins.pop(posicionDelNombre)
        adminCleaner()
        adminListPlacerAfterClean(listaAdmins)
        if listaUsernameNuevo[2] == "1":
            ABMBoolean = True
        else:
            ABMBoolean = False
        adminModificado = crearAdministrador(listaUsernameNuevo[0],listaUsernameNuevo[1],ABMBoolean)
        escribirAdministrador(adminModificado)
        print("se modifico el username a " + (usernameNuevo))
def modificarContrasenaDeAdmin(contrasenaVieja):
    contrasenaNueva = str(input("Ingrese su nueva contraseña, no puede ser 0: "))
    if contrasenaNueva == "0":
        print("Escribiste 0, el cual es un username invalido")
        modificarUsernameAdministrador(contrasenaVieja)
    else:
        listaNombres = []
        leerDataEspecificaDeAdmin(listaNombres, 0)
        indiceNombre = 0
        posicionDelNombre = -1
        while indiceNombre < len(listaNombres):
            if contrasenaNueva == listaNombres[indiceNombre]:
                posicionDelNombre = indiceNombre
                indiceNombre = indiceNombre + len(listaNombres)
            else:
                indiceNombre = indiceNombre + 1
        listaUsernameNuevo=[listaNombres[posicionDelNombre]]
        listaUsernameNuevo.append(contrasenaNueva)
        listaABM = []
        leerDataEspecificaDeAdmin(listaABM,2)
        listaUsernameNuevo.append(listaABM[posicionDelNombre])
        listaAdmins = []
        leerAdministradores(listaAdmins)
        listaAdmins.pop(posicionDelNombre)
        adminCleaner()
        adminListPlacerAfterClean(listaAdmins)
        if listaUsernameNuevo[2] == "1":
            ABMBoolean = True
        else:
            ABMBoolean = False
        adminModificado = crearAdministrador(listaUsernameNuevo[0], listaUsernameNuevo[1], ABMBoolean)
        escribirAdministrador(adminModificado)
        print("se modifico el username a " + (listaNombres[posicionDelNombre]))










