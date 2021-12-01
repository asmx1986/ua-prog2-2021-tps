import datetime

from Anses.Anses import leerCuilsDelAnses, leerCiudadano, leerDataEspecificaDeCiudadano, escribirCiudadano, \
    leerDataEspecificaDeAdmin, escribirAdministrador, leerTiposDeEvento, escribirEvento, modificarEstadoDeBloqueo, \
    leerDataEspecificaEvento, checkerCaducidadDeEventos, escribirSolicitud, constructorDeEventoEnRuntime, \
    checkerCaducidadDeInvitacion, leerDataEspecificaSolicitudes, leerSolicitudes, modificarEventoEnPersistencia, \
    generadorDeCitizenEnRuntime, reescribirCitizenModificado, borrarsolicitud, leerEvento
from GestionUsuarios.Ciudadano import Ciudadano
from GestionUsuarios.Administrador import Administrador
from GestionUsuarios.ABM import crearAdministrador, eliminarAdministrador, modificarUsernameAdministrador, modificarContrasenaDeAdmin
from Mapa.Mapa import mapa


def login():
    print("1- Registrarse")
    print("2- Iniciar sesion como administrador")
    print("3- Iniciar sesion como usuario")
    print("4-Ver menu de rankings")
    print("5- Salir del programa")
    try:
        z=int(input("seleccione la opción: "))
        if z==1:
            ContieneCuilEnAnses()
        elif z==2:
            EstaElUsernameAdmin()
        elif z==3:
            EstaElUsernameCiudadano()
        elif z==4:
            menuRankings()
        elif z==5:
            print("Gracias por usar el programa")
        else:
            print("opción invalida, seleccione otra vez")
            login()
    except ValueError:
        print("valor incorrecto, vuelva a elegir el numero")
        login()

def ContieneCuilEnAnses():
    cuil = str(input("Ingrese su numero de CUIL sin guion(debe ser de 11 digitos, EJ: 23440529259), en caso de querer volver atras ingrese el numero 0: "))
    if cuil == "0":
        login()
    else:
        listaCUILsDelAnses = []
        leerCuilsDelAnses(listaCUILsDelAnses)
        posicionListaCuilsDelAnses = 0
        existeEnAnses = False
        while posicionListaCuilsDelAnses < len(listaCUILsDelAnses):
            if cuil == listaCUILsDelAnses[posicionListaCuilsDelAnses]:
                existeEnAnses = True
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + len(listaCUILsDelAnses)
            else:
                posicionListaCuilsDelAnses = posicionListaCuilsDelAnses + 1
        if existeEnAnses == True:
            yaExisteElUsuario(cuil)
        else:
            print("Su numero de Cuil no se encuentra en la lista del Anses, vuelva a escribirlo. En caso de seguir teniendo este problema comuniquese con el Anses.")
            ContieneCuilEnAnses()
def yaExisteElUsuario(cuil):
    listaCUILsDeUsersCreados = []
    leerDataEspecificaDeCiudadano(listaCUILsDeUsersCreados,0)
    estaDuplicado = False
    posicionListaCuilDeUsersCreados = 0
    while posicionListaCuilDeUsersCreados < len(listaCUILsDeUsersCreados):
        if cuil == listaCUILsDeUsersCreados[posicionListaCuilDeUsersCreados]:
            estaDuplicado = True
            posicionListaCuilDeUsersCreados = posicionListaCuilDeUsersCreados + len(listaCUILsDeUsersCreados)
        else:
            posicionListaCuilDeUsersCreados= posicionListaCuilDeUsersCreados + 1
    if estaDuplicado == True:
        print("El CUIL que ingresó es de un usuario ya creado. Si es el suyo vaya a login para iniciar sesión,sino escriba un nuevo cuil.")
        ContieneCuilEnAnses()
    else:
        EstaRepetidoElCelular(cuil)
def EstaRepetidoElCelular(cuil):
    celular = str(input("Ingrese su numero de telefono sin su codigo de país(debe tener 10 digitos en total, EJ: 1154885993), en caso de querer volver atras ingrese el numero 0: "))
    if celular == "0":
        login()
    elif len(celular) == 10:
        listaCelularesDeUsersCreados = []
        leerDataEspecificaDeCiudadano(listaCelularesDeUsersCreados,1)
        estaDuplicado = False
        posicionListaCelularesDeUsersCreados = 0
        while posicionListaCelularesDeUsersCreados < len(listaCelularesDeUsersCreados):
            if celular == listaCelularesDeUsersCreados[posicionListaCelularesDeUsersCreados]:
                estaDuplicado = True
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + len(listaCelularesDeUsersCreados)
            else:
                posicionListaCelularesDeUsersCreados = posicionListaCelularesDeUsersCreados + 1
        if estaDuplicado == True:
            print("El numero de telefono que ingresó se encuentra en uso por otro usuario, ingrese uno nuevo.")
            EstaRepetidoElCelular(cuil)
        else:
            creadorDelUsuario(cuil,celular)
    else:
        print("el numero ingresado no tiene 10 digitos,ingreselo otra vez.")
        EstaRepetidoElCelular(cuil)
def creadorDelUsuario(cuil,celular):
    intCUIL = int(cuil)
    intCelular = int(celular)
    CiudadanoACrear = Ciudadano(intCUIL,intCelular,0,False)
    escribirCiudadano(CiudadanoACrear)
    print("Se ha creado el usuario.")
    login()

def EstaElUsernameAdmin():
    username=str(input("Ingrese su nombre de usuario, en caso de querer volver atras ingrese el numero 0: "))
    if username == "0":
        login()
    else:
        ListaNombresDeAdmins=[]
        leerDataEspecificaDeAdmin(ListaNombresDeAdmins,0)
        existeElUsuario=False
        indiceDeLista = 0
        posicionDelNombre = -1
        while indiceDeLista < len(ListaNombresDeAdmins):
            if username == ListaNombresDeAdmins[indiceDeLista]:
                existeElUsuario = True
                posicionDelNombre = indiceDeLista
                indiceDeLista= indiceDeLista + len(ListaNombresDeAdmins)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            EstaLaContrasenaAdmin(username,posicionDelNombre)
        else:
            print("Este username no existe, escriba otro.")
            EstaElUsernameAdmin()
def EstaLaContrasenaAdmin(username,posicionDelNombre):
    contrasena = str(input("Ingrese su contraseña, en caso de querer volver atras ingrese el numero 0: "))
    if contrasena == "0":
        login()
    else:
        ListaContrasenasAdmins=[]
        leerDataEspecificaDeAdmin(ListaContrasenasAdmins,1)
        if contrasena == ListaContrasenasAdmins[posicionDelNombre]:
            crearObjetoAdminEnRuntime(username,contrasena,posicionDelNombre)
        else:
            print("contraseña incorrecta, escribala de nuevo")
            EstaLaContrasenaAdmin(username,posicionDelNombre)
def crearObjetoAdminEnRuntime(username,contrasena,posicionDelNombre):
    ListaPosicionDelABM= []
    leerDataEspecificaDeAdmin(ListaPosicionDelABM,2)
    booleanABM = int(ListaPosicionDelABM[posicionDelNombre])
    ABM = False
    if booleanABM == 1:
        ABM = True
    else:
        ABM = False
    AdminEnRuntime = Administrador(username,contrasena,ABM)
    menuAdmin(AdminEnRuntime)
def menuAdmin(AdminEnRuntime):
    print("¿Que desea hacer?")
    print("1-Agregar tipo de evento")
    print("2-Bloquear usuario")
    print("3-Desbloquear usuario")
    print("4-Crear administrador")
    print("5-Modificar administrador")
    print("6-Eliminar administrador")
    print("7-Cerrar la sesión")
    try:
        x=int(input("seleccione la opción: "))
        if x == 1:
            AdminEnRuntime.crearTipoDeEvento()
            menuAdmin(AdminEnRuntime)
        elif x == 2:
            citizenAModificarEstado = generadorDeCitizenParaBloqueoODesbloqueo(AdminEnRuntime)
            AdminEnRuntime.bloquearCiudadano(citizenAModificarEstado)
            modificarEstadoDeBloqueo(citizenAModificarEstado)
            menuAdmin(AdminEnRuntime)

        elif x == 3:
            citizenAModificarEstado = generadorDeCitizenParaBloqueoODesbloqueo(AdminEnRuntime)
            AdminEnRuntime.desbloquearCiudadano(citizenAModificarEstado)
            modificarEstadoDeBloqueo(citizenAModificarEstado)
            menuAdmin(AdminEnRuntime)
        elif x == 4:
            if AdminEnRuntime.accesoAABM == True:
                usuario = checkerInexistenciaDelUsername(AdminEnRuntime)
                newcontrasena = creadorDeContrasena(AdminEnRuntime)
                ABM = selectorDeABM(AdminEnRuntime)
                AdminACrear = crearAdministrador(usuario,newcontrasena,ABM)
                escribirAdministrador(AdminACrear)
                print("se ha creado el administrador nuevo")
                menuAdmin(AdminEnRuntime)
            else:
                print("No se encuentra autorizado para hacer esa operación")
                menuAdmin(AdminEnRuntime)
        elif x == 5:
            menuDeModificacion(AdminEnRuntime)
        elif x == 6:
            if AdminEnRuntime.accesoAABM == True:
                usuarioAEliminar = checkAdminName(AdminEnRuntime)
                eliminarAdministrador(usuarioAEliminar)
                menuAdmin(AdminEnRuntime)
            else:
                print("No se encuentra autorizado para hacer esa operación")
                menuAdmin(AdminEnRuntime)
        elif x == 7:
            print("Se ha cerrado la sesión correctamente.")
            login()
        else:
            print("opción invalida, seleccione otra vez")
            menuAdmin(AdminEnRuntime)
    except ValueError:
        print("valor incorrecto, vuelva a elegir el numero")
        menuAdmin(AdminEnRuntime)
def checkerInexistenciaDelUsername(AdminEnRuntime):
    username = str(input("Ingrese el nombre de usuario, escriba 0 si desea volver atras: "))
    if username == "0":
        menuAdmin(AdminEnRuntime)
    else:
        ListaNombresDeAdmins = []
        leerDataEspecificaDeAdmin(ListaNombresDeAdmins, 0)
        existeElUsuario = False
        indiceDeLista = 0
        while indiceDeLista < len(ListaNombresDeAdmins):
            if username == ListaNombresDeAdmins[indiceDeLista]:
                existeElUsuario = True
                indiceDeLista = indiceDeLista + len(ListaNombresDeAdmins)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            print("Ya existe un admin con ese nombre")
            menuAdmin(AdminEnRuntime)
        else:
            return username
def creadorDeContrasena(AdminEnRuntime):
    contrasena = str(input("ingrese la contraseña del nuevo administrador, escriba 0 si desea volver atras: "))
    if contrasena == "0":
        menuAdmin(AdminEnRuntime)
    else:
        return contrasena
def selectorDeABM(AdminEnRuntime):
    x= str(input("escriba 1 si desea que este admin tenga acceso a los metodos ABM, 0 si desea volver atras, y cualquier otro valor en caso de que no desea que tenga acceso a los metodos ABM:"))
    if x == "0":
        menuAdmin(AdminEnRuntime)
    elif x == "1":
        return True
    else:
        return False
def checkAdminName(AdminEnRuntime):
    username = str(input("escriba el nombre de usuario del Admin: "))
    listaNombre = []
    leerDataEspecificaDeAdmin(listaNombre,0)
    indiceLista = 0
    existeElUser = False
    while indiceLista < len(listaNombre):
        if username == listaNombre[indiceLista]:
            existeElUser = True
            indiceLista = indiceLista + len(listaNombre)
        else:
            indiceLista = indiceLista + 1
    if existeElUser == True:
        return username
    else:
        print("No existe este username de administrador")
        menuAdmin(AdminEnRuntime)
def checkAdminNametoModify(AdminEnRuntime):
    username = str(input("escriba el nombre de usuario del Admin: "))
    if username == AdminEnRuntime.usuario:
        listaNombre = []
        leerDataEspecificaDeAdmin(listaNombre,0)
        indiceLista = 0
        existeElUser = False
        while indiceLista < len(listaNombre):
            if username == listaNombre[indiceLista]:
                existeElUser = True
                indiceLista = indiceLista + len(listaNombre)
            else:
                indiceLista = indiceLista + 1
        if existeElUser == True:
            return username
        else:
            print("No existe este username de administrador")
            menuAdmin(AdminEnRuntime)
    else:
        print("ese no es tu username")
        menuDeModificacion(AdminEnRuntime)
def checkAdminPassword(AdminEnRuntime):
    contrasena=str(input("escriba su contraseña: "))
    if contrasena == AdminEnRuntime.contrasena:
        listaContrasena = []
        leerDataEspecificaDeAdmin(listaContrasena,1)
        indiceLista = 0
        existeLaContra = False
        while indiceLista < len(listaContrasena):
            if contrasena == listaContrasena[indiceLista]:
                existeLaContra = True
                indiceLista = indiceLista + len(listaContrasena)
            else:
                indiceLista = indiceLista + 1
        if existeLaContra == True:
            return contrasena
        else:
            print("no existe esa contrasena")
            menuAdmin(AdminEnRuntime)
    else:
        print("no escribiste tu contraseña")
        menuDeModificacion(AdminEnRuntime)
def menuDeModificacion(AdminEnRuntime):
    print("1-Modificar el username.")
    print("2-Modificar la contraseña.")
    y = str(input("seleccione la opción,seleccione 0 para volver atrás: "))
    if y == "0":
        menuAdmin(AdminEnRuntime)
    elif y == "1":
        UsernameViejo = checkAdminNametoModify(AdminEnRuntime)
        modificarUsernameAdministrador(UsernameViejo)
        menuAdmin(AdminEnRuntime)
    elif y == "2":
        contrasena = checkAdminPassword(AdminEnRuntime)
        modificarContrasenaDeAdmin(contrasena)
        menuAdmin(AdminEnRuntime)
    else:
        print("opción invalida, vuelva a escribirlo.")
        menuDeModificacion(AdminEnRuntime)
def generadorDeCitizenParaBloqueoODesbloqueo(AdminEnRuntime):
    cuilUser=str(input("Escriba el cuil del usuario: "))
    listaUsernames=[]
    leerDataEspecificaDeCiudadano(listaUsernames, 0)
    indiceLista=0
    valorABuscar =-1
    existeElUsername = False
    while indiceLista < len(listaUsernames):
        if cuilUser == listaUsernames[indiceLista]:
            valorABuscar = indiceLista
            existeElUsername = True
            indiceLista = indiceLista + len(listaUsernames)
        else:
            indiceLista = indiceLista + 1
    if existeElUsername == True:
        cuilUserINT = int(cuilUser)
        listaTelefonos = []
        leerDataEspecificaDeCiudadano(listaTelefonos,1)
        telefono = int(listaTelefonos[valorABuscar])
        listaSoliRechazada = []
        leerDataEspecificaDeCiudadano(listaSoliRechazada,2)
        soliRechazada = int(listaSoliRechazada[valorABuscar])
        listaBoolNumerico = []
        leerDataEspecificaDeCiudadano(listaBoolNumerico,3)
        boolNumerico = int(listaBoolNumerico[valorABuscar])
        if boolNumerico == 1:
            boolean = True
        else:
            boolean = False
        return Ciudadano(cuilUserINT,telefono,soliRechazada,boolean)
    else:
        print("el usuario a modificar no existe.")
        menuAdmin(AdminEnRuntime)

def EstaElUsernameCiudadano():
    cuilCiudadano=str(input("Ingrese su CUIL correspondiente(EJ:42382331653), en caso de querer volver atras ingrese el numero 0: "))
    if cuilCiudadano == "0":
        login()
    else:
        ListaNombresDeCiudadano=[]
        leerDataEspecificaDeCiudadano(ListaNombresDeCiudadano,0)
        existeElUsuario=False
        indiceDeLista = 0
        posicionDelCuil = -1
        while indiceDeLista < len(ListaNombresDeCiudadano):
            if cuilCiudadano == ListaNombresDeCiudadano[indiceDeLista]:
                existeElUsuario = True
                posicionDelCuil = indiceDeLista
                indiceDeLista= indiceDeLista + len(ListaNombresDeCiudadano)
            else:
                indiceDeLista = indiceDeLista + 1
        if existeElUsuario == True:
            checkearCelular(cuilCiudadano,posicionDelCuil)
        else:
            print("Este CUIL no pertenece a ningún usuario, escriba otro.")
            EstaElUsernameCiudadano()
def checkearCelular(cuil,posicionDelCuil):
    celular = str(input("ingrese su numero de telefono, sin su cogigo de país(EJ:1154885993), en caso de querer volver atras introduzca el numero 0: "))
    if celular == "0":
        login()
    else:
        listaTelefonosCiudadanos = []
        leerDataEspecificaDeCiudadano(listaTelefonosCiudadanos, 1)
        if celular == listaTelefonosCiudadanos[posicionDelCuil]:
            crearCiudadanoEnRuntime(cuil,celular,posicionDelCuil)
        else:
            print("el numero de telefono es incorrecto, escribalo otra vez")
            checkearCelular(cuil, posicionDelCuil)
def crearCiudadanoEnRuntime(cuil,celular,posicionDelCuil):
    listaSolicitudesRechazadas = []
    leerDataEspecificaDeCiudadano(listaSolicitudesRechazadas,2)
    solicitudesR = int(listaSolicitudesRechazadas[posicionDelCuil])
    listaBloqueo = []
    leerDataEspecificaDeCiudadano(listaBloqueo,3)
    bloqueoINT= int(listaBloqueo[posicionDelCuil])
    if bloqueoINT == 1:
        bloqueoBOOLEAN = True
    else:
        bloqueoBOOLEAN = False
    ciudadanoEnRuntime = Ciudadano(cuil,celular,solicitudesR,bloqueoBOOLEAN)
    menuCitizen(ciudadanoEnRuntime)
def menuCitizen(ciudadanoEnRuntime):
    checkerCaducidadDeEventos()
    print("1-Crear Evento")
    print("2-Ver invitaciones")
    print("3-Enviar invitación")
    print("4-Ver mapa")
    print("5-Cerrar la sesión")
    try:
        r = int(input("Seleccione la opción: "))
        if r == 1:
            if ciudadanoEnRuntime.estaBloqueado == True:
                print("Actualmente se encuentra bloqueado, comuniquese con un administrador.")
                menuCitizen(ciudadanoEnRuntime)
            else:
                try:
                    nombre = str(input("Escriba el nombre del evento: "))
                    chequerNombreYaUsado(nombre,ciudadanoEnRuntime)
                    ano = int(input("Escriba el año del evento de forma numerica(EJ 2021): "))
                    chequerValidezAno(ano,ciudadanoEnRuntime)
                    mes = int(input("Escriba el mes de forma numerica(EJ 12): "))
                    chequerValidezmes(mes,ciudadanoEnRuntime)
                    dia = int(input("Escriba el dia de forma numerica(EJ 26): "))
                    chequerValidezdia(ano, mes, dia, ciudadanoEnRuntime)
                    hora = int(input("Escriba la hora de forma numerica(23): "))
                    chequerValidezHora(hora, ciudadanoEnRuntime)
                    minuto = int(input("Escriba el minuto de foma numerica(37): "))
                    chequerValidezFecha(ano, mes, dia, hora, minuto, ciudadanoEnRuntime)
                    tipoDeEvento = chequertipoEvento()
                    cantidadMaximaDePersonas = chequerCantidadMaximaDePersonas()
                    coordenadaEnx = float(input("Escriba la coordenada en el eje X: "))
                    coordenadaEny = float(input("Escriba la coordenada en el eje Y: "))
                    newEvento = ciudadanoEnRuntime.crearEvento(nombre,ano,mes,dia,hora,minuto,tipoDeEvento,cantidadMaximaDePersonas,coordenadaEnx,coordenadaEny)
                    escribirEvento(newEvento)
                    print("se añadio el evento " + nombre + " a la lista de eventos.")
                    menuCitizen(ciudadanoEnRuntime)
                except ValueError:
                    print("Ingresaste un valor invalido,cargue la información de nuevo")
                    menuCitizen(ciudadanoEnRuntime)
        elif r == 2:
            menuInvitaciones(ciudadanoEnRuntime)
        elif r == 3:
            if ciudadanoEnRuntime.estaBloqueado == True:
                print("Actualmente se encuentra bloqueado, comuniquese con un administrador.")
                menuCitizen(ciudadanoEnRuntime)
            else:
                checkerCaducidadDeEventos()
                UsernameAEnviar = chequerValidezUsernameAEnviar(ciudadanoEnRuntime)
                eventoDeLaSolicitud = selectorDeEvento(ciudadanoEnRuntime)
                evento = constructorDeEventoEnRuntime(eventoDeLaSolicitud)
                solicitud = ciudadanoEnRuntime.enviarSolicitud(ciudadanoEnRuntime,UsernameAEnviar,evento)
                if solicitud == False:
                    menuCitizen(ciudadanoEnRuntime)
                else:
                    escribirSolicitud(solicitud)
                    print("se ha enviado la invitación")
                    menuCitizen(ciudadanoEnRuntime)
        elif r == 4:
            checkerCaducidadDeEventos()
            mapa()
            menuCitizen(ciudadanoEnRuntime)
        elif r == 5:
            print("Se ha cerrado la sesión correctamente.")
            login()
        else:
            raise ValueError
    except ValueError:
        print("valor incorrecto, vuelva a elegir el numero")
        menuCitizen(ciudadanoEnRuntime)
def chequertipoEvento():
    listaTiposDeEvento =  []
    leerTiposDeEvento(listaTiposDeEvento)
    for x in listaTiposDeEvento:
        print(x)
    tipoDeEventoABuscar = str(input("Ingrese el tipo de evento: "))
    indiceLista = 0
    estaEnLosTipos=False
    while indiceLista < len(listaTiposDeEvento):
        if tipoDeEventoABuscar == listaTiposDeEvento[indiceLista]:
            estaEnLosTipos=True
            indiceLista = indiceLista + len(listaTiposDeEvento)
        else:
            indiceLista = indiceLista + 1
    if estaEnLosTipos == True:
        return tipoDeEventoABuscar
    else:
        print("Este tipo de evento no existe,escriba otro")
        chequertipoEvento()
def chequerCantidadMaximaDePersonas():
    x=int(input("Escriba la cantidad maxima de personas para asistir al evento: "))
    if x >= 1:
        return x
    else:
        print("Cargaste un valor invalido, vuelva a cargarlo.")
        chequerCantidadMaximaDePersonas()
def chequerNombreYaUsado(nombre,ciudadanoEnRuntime):
    listaNombresDeEventos = []
    leerDataEspecificaEvento(listaNombresDeEventos,0)
    estaRepetidoElNombre = False
    indice = 0
    while indice < len(listaNombresDeEventos):
        if nombre == listaNombresDeEventos[indice]:
            estaRepetidoElNombre = True
            indice = len(listaNombresDeEventos)
        else:
            indice = indice + 1
    if estaRepetidoElNombre == True:
        print("Ya existe un evento con este nombre")
        menuCitizen(ciudadanoEnRuntime)
    else:
        pass
def chequerValidezAno(ano,ciudadanoEnRuntime):
    try:
        if ano < datetime.datetime.now().year:
            raise ValueError
        else:
            pass
    except ValueError:
        print("El año ingresado ya pasó")
        menuCitizen(ciudadanoEnRuntime)
def chequerValidezmes(mes,ciudadanoEnRuntime):
    try:
        if mes>0:
            if mes <= 12:
                pass
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("El mes ingresado es invalido")
        menuCitizen(ciudadanoEnRuntime)
def chequerValidezdia(ano,mes,dia,ciudadanoEnRuntime):
    try:
        if dia > 0:
            if mes == 1:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            elif mes == 2:
                if ano % 400 == 0:
                    if ano % 100 != 0 and ano % 4 == 0:
                        if dia > 29:
                            raise ValueError
                        else:
                            pass
                    else:
                        if dia > 28:
                            raise ValueError
                        else:
                            pass
            elif mes == 3:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            elif mes == 4:
                if dia > 30:
                    raise ValueError
                else:
                    pass
            elif mes == 5:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            elif mes == 6:
                if dia > 30:
                    raise ValueError
                else:
                    pass
            elif mes == 7:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            elif mes == 8:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            elif mes == 9:
                if dia > 30:
                    raise ValueError
                else:
                    pass
            elif mes == 10:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            elif mes == 11:
                if dia > 30:
                    raise ValueError
                else:
                    pass
            elif mes == 12:
                if dia > 31:
                    raise ValueError
                else:
                    pass
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("La fecha es invalida")
        menuCitizen(ciudadanoEnRuntime)
def chequerValidezHora(hora,ciudadanoEnRuntime):
    try:
        if hora >= 0:
            if hora <24:
                pass
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("ingreso una hora invalida")
        menuCitizen(ciudadanoEnRuntime)
def chequerValidezMinuto(minuto,ciudadanoEnRuntime):
    try:
        if minuto >= 0:
            if minuto <60:
                pass
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("ingreso un minuto invalido")
        menuCitizen(ciudadanoEnRuntime)
def chequerValidezFecha(ano,mes,dia,hora,minuto,ciudadanoEnRuntime):
    fecha = datetime.datetime(ano,mes,dia,hora,minuto)
    if fecha <= datetime.datetime.now():
        print("la fecha introducida ya pasó")
        menuCitizen(ciudadanoEnRuntime)
    else:
        pass
def chequerValidezUsernameAEnviar(ciudadanoEnRuntime):
    try:
        listaCUILS = []
        leerDataEspecificaDeCiudadano(listaCUILS,0)
        listaCUILS.remove(str(ciudadanoEnRuntime.getCUIL()))
        indice = 0
        while indice < len(listaCUILS):
            print(listaCUILS[indice])
            indice = indice + 1
        nombre = int(input("ingrese el CUIL de la persona a la que desea enviarle la solicitud. Para volver atras ingrese 0: "))
        if nombre == 0:
            menuCitizen(ciudadanoEnRuntime)
        else:
            indice2 = 0
            existe = False
            while indice2 < len(listaCUILS):
                if nombre == int(listaCUILS[indice2]):
                    existe = True
                    indice2 = len(listaCUILS)
                else:
                    indice2 = indice2 + 1
            if existe == True:
                return nombre
            else:
                raise ValueError
    except ValueError:
        print("Ingresaste un valor invalido")
        chequerValidezUsernameAEnviar(ciudadanoEnRuntime)
def selectorDeEvento(ciudadanoEnRuntime):
    checkerCaducidadDeEventos()
    listaNombres = []
    leerDataEspecificaEvento(listaNombres,0)
    indice1 = 0
    while indice1 < len(listaNombres):
        print(listaNombres[indice1])
        indice1 = indice1 + 1
    try:
        nombreEvento = str(input("ingrese el nombre del evento al que desea invitar. Para volver al menu ingrese 0: "))
        if nombreEvento == "0":
            menuCitizen(ciudadanoEnRuntime)
        else:
            indice2 = 0
            existeElEvento = False
            while indice2 < len(listaNombres):
                if nombreEvento == listaNombres[indice2]:
                    existeElEvento = True
                    indice2 = len(listaNombres)
                else:
                    indice2 = indice2 + 1
            if existeElEvento == True:
                return nombreEvento
            else:
                raise ValueError
    except ValueError:
        print("ingreso un nombre invalido")
        selectorDeEvento(ciudadanoEnRuntime)
def menuInvitaciones(ciudadanoEnRuntime):
    checkerCaducidadDeEventos()
    checkerCaducidadDeInvitacion()
    posicionesDeInvitaciones = checkerHayInvitaciones(ciudadanoEnRuntime)
    aceptaOrechaza = mostradorDeInvitacion(ciudadanoEnRuntime, posicionesDeInvitaciones)
    if aceptaOrechaza == 0:
        menuCitizen(ciudadanoEnRuntime)
    elif aceptaOrechaza == 1:
        NombreEvento = getterNombreEventoDeSolicitud(posicionesDeInvitaciones)
        Evento = constructorDeEventoEnRuntime(NombreEvento)
        ciudadanoEnRuntime.aceptarSolicitud(Evento)
        modificarEventoEnPersistencia(Evento)
        borrarsolicitud(posicionesDeInvitaciones)
        if len(posicionesDeInvitaciones) >= 1:
            print("Se aceptó la invitación")
            menuInvitaciones(ciudadanoEnRuntime)
        else:
            print("Se aceptó la invitación, no tiene mas invitaciones para responder")
            menuCitizen(ciudadanoEnRuntime)
    elif aceptaOrechaza == -1:
        CUIL = getterCUILEnvianteDeSolicitud(posicionesDeInvitaciones)
        User = generadorDeCitizenEnRuntime(CUIL)
        ciudadanoEnRuntime.rechazarSolicitud(User)
        reescribirCitizenModificado(User)
        borrarsolicitud(posicionesDeInvitaciones)
        if len(posicionesDeInvitaciones) >= 1:
            print("Se rechazo la invitacion")
            menuInvitaciones(ciudadanoEnRuntime)
        else:
            print("Se rechazo la invitación, no tiene mas invitaciones para responder")
            menuCitizen(ciudadanoEnRuntime)
def checkerHayInvitaciones(ciudadanoEnRuntime):
    listaCUILSRecievers = []
    leerDataEspecificaSolicitudes(listaCUILSRecievers,1)
    listaPosiciones = []
    indice = 0
    while indice < len(listaCUILSRecievers):
        if int(ciudadanoEnRuntime.getCUIL()) == int(listaCUILSRecievers[indice]):
            listaPosiciones.append(indice)
            indice = indice + 1
        else:
            indice = indice + 1
    if len(listaPosiciones) == 0:
        print("No tiene solicitudes en estos momentos")
        menuCitizen(ciudadanoEnRuntime)
    else:
        print("Tiene " + str(len(listaPosiciones)) + " solicitudes en estos momentos.")
        return listaPosiciones
def mostradorDeInvitacion(ciudadanoEnRuntime,listaPosiciones):
    try:
        listaInvitacionesGlobal = []
        leerSolicitudes(listaInvitacionesGlobal)
        invitacion = listaInvitacionesGlobal[listaPosiciones[0]]
        ListaNombresEventos = []
        leerDataEspecificaEvento(ListaNombresEventos,0)
        indice = 0
        posicionDeCoord = -1
        while indice < len(ListaNombresEventos):
            if invitacion[2] == ListaNombresEventos[indice]:
                posicionDeCoord = indice
                indice = len(ListaNombresEventos)
            else:
                indice = indice + 1
        ListaCoordEjeX = []
        leerDataEspecificaEvento(ListaCoordEjeX, 6)
        ListaCoordEjeY = []
        leerDataEspecificaEvento(ListaCoordEjeY, 7)
        coordX = float(ListaCoordEjeX[posicionDeCoord])
        coordY = float(ListaCoordEjeY[posicionDeCoord])
        zona = " "
        if coordX >= 0 and coordY >= 0:
            zona = "zona noreste"
        elif coordX < 0 and coordY >= 0:
            zona = "zona noroeste"
        elif coordX < 0 and coordY < 0:
            zona = "zona suroeste"
        elif coordX >= 0 and coordY < 0:
            zona = "zona sureste"
        print("Esta invitacion fue enviada a las " + invitacion[3] + " por el usuario con el CUIL " + invitacion[0] + " para invitarle al evento " + invitacion[2] + ".Este se encuentra en la " + zona + " de la ciudad, en la coordenadas " + str(coordX) + " en el eje X y " + str(coordY) + " en el eje Y.")
        try:
            k = int(input("ingrese 1 para aceptar la solicitud, 0 para volver atras o -1 para rechazar la solicitud: "))
            if k == 1:
                return k
            elif k == 0:
                return k
            elif k == -1:
                return k
            else:
                raise ValueError
        except ValueError:
            print("ingreso un valor invalido.")
            mostradorDeInvitacion(ciudadanoEnRuntime,listaPosiciones)
    except TypeError:
        pass #esto lo hago porque cuando se acepta o rechaza una invitación al salir salta un typeError
def getterNombreEventoDeSolicitud(listaPosiciones):
    listaNombresEventos = []
    leerDataEspecificaSolicitudes(listaNombresEventos,2)
    return listaNombresEventos[listaPosiciones[0]]
def getterCUILEnvianteDeSolicitud(listaPosiciones):
    listaCUILSolicitud = []
    leerDataEspecificaSolicitudes(listaCUILSolicitud, 0)
    return int(listaCUILSolicitud[listaPosiciones[0]])

def menuRankings():
    checkerCaducidadDeEventos()
    try:
        print("1-Ver Top de eventos con mas inscripciones")
        print("2-Ver Top 3 de eventos en la zona noreste")
        print("3-Ver Top 3 de eventos en la zona noroeste")
        print("4-Ver Top 3 de eventos en la zona sureste")
        print("5-Ver Top 3 de eventos en la zona suroeste")
        print("6-Ver mapa de eventos")
        print("7-Salir del menu de los rankings")
        L = int(input("Seleccione la opcion: "))
        lista = []
        leerEvento(lista)
        if L == 1:
            rankingGlobal()
            menuRankings()
        elif L == 2:
            listaNoreste = generateList(1,1,lista)
            rankingPorZona(listaNoreste)
            menuRankings()
        elif L == 3:
            listaNoroeste = generateList(-1, 1, lista)
            rankingPorZona(listaNoroeste)
            menuRankings()
        elif L == 4:
            listaSureste = generateList(1, -1, lista)
            rankingPorZona(listaSureste)
            menuRankings()
        elif L == 5:
            listaSuroeste = generateList(-1, -1, lista)
            rankingPorZona(listaSuroeste)
            menuRankings()
        elif L == 6:
            checkerCaducidadDeEventos()
            mapa()
            menuRankings()
        elif L == 7:
            print("Se ha cerrado el menu")
            login()
        else:
            raise ValueError
    except ValueError:
        print("valor invalido, vuelva a escribirlo")
        menuRankings()
def rankingGlobal():
    lista = []
    leerEvento(lista)
    print(lista)
    if len(lista) == 0:
        print("No hay eventos creados en estos instantes.")
    elif len(lista) >= 1:
        sorter(lista)
        print("Posicion - Nombre - zona - Personas inscriptas")
        indice = 0
        zona = " "
        while indice < len(lista):
            coordX = float(lista[indice][6])
            coordY = float(lista[indice][7])
            if coordX >= 0 and coordY >= 0:
                zona = "zona noreste"
            elif coordX >= 0 and coordY < 0:
                zona = "zona sureste"
            elif coordX < 0 and coordY < 0:
                zona = "zona suroeste"
            elif coordX < 0 and coordY >= 0:
                zona = "zona noroeste"
            indicePrinteable = indice + 1
            print(str(indicePrinteable) + " - " + lista[indice][0] + " - " + zona + " - " + lista[indice][3])
            indice = indice + 1
def rankingPorZona(lista):
    if len(lista) == 0:
        print("No hay eventos en esta zona")
    elif len(lista) == 1:
        sorter(lista)
        print("Solo hay 1 evento en estos momentos.")
        print("Posicion - Nombre - Personas inscriptas")
        indice = 0
        while indice < len(lista):
            indicePrinteable = indice + 1
            print(str(indicePrinteable) + " - " + lista[indice][0] + " - " + lista[indice][3])
            indice = indice + 1
    elif len(lista) == 2:
        sorter(lista)
        print("Solo hay 2 evento en estos momentos.")
        print("Posicion - Nombre - Personas inscriptas")
        indice = 0
        while indice < len(lista):
            indicePrinteable = indice + 1
            print(str(indicePrinteable) + " - " + lista[indice][0] + " - " + lista[indice][3])
            indice = indice + 1
    elif len(lista) >= 3:
        sorter(lista)
        print("Posicion - Nombre - Personas inscriptas")
        indice = 0
        while indice < len(lista):
            indicePrinteable = indice + 1
            print(str(indicePrinteable) + " - " + lista[indice][0] + " - " + lista[indice][3])
            indice = indice + 1
def sorter(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(lista[j][3]) < int(lista[j + 1][3]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
def generateList(x,y,list):
    toReturn = []
    for i in range(len(list)):
        if float(list[i][6])/int(x) > 0 and float(list[i][7])/int(y) > 0:
            toReturn.append(list[i])
    return toReturn