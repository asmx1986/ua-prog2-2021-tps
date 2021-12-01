import csv
import datetime
from GestionEventos.Evento import Evento
from GestionUsuarios.Ciudadano import Ciudadano


def escribirCiudadano(ciudadano):
    CiudadanoParaEscribir = ciudadano.ciudadanoAEscribir()
    with open("../Archivos/listaUsuarios.csv","a",newline="") as listaCiudadanos:
        csv_User_writer = csv.writer(listaCiudadanos,delimiter=",")
        csv_User_writer.writerow(CiudadanoParaEscribir)
    listaCiudadanos.close()
def leerCiudadano(listaUsuarios):
    with open("../Archivos/listaUsuarios.csv","r") as listaCiudadanos:
        csv_User_Reader=csv.reader(listaCiudadanos)
        next(listaCiudadanos)
        for line in csv_User_Reader:
            listaUsuarios.append(line)
    listaCiudadanos.close()
def leerDataEspecificaDeCiudadano(listaUsuarios,valorABuscar):
    with open("../Archivos/listaUsuarios.csv","r") as listaCiudadanos:
        csv_User_Reader=csv.reader(listaCiudadanos)
        next(listaCiudadanos)
        for line in csv_User_Reader:
            listaUsuarios.append(line[valorABuscar])
    listaCiudadanos.close()
def citizenCleaner():
    cleaner = open("../Archivos/listaUsuarios.csv", "w")
    cleaner.close()
def citizenListPlacerAfterClean(lista):
    with open("../Archivos/listaUsuarios.csv","a",newline="")as listaCitizen:
        csv_Citizen_writer = csv.writer(listaCitizen,delimiter=",")
        csv_Citizen_writer.writerow(["CUIL","telefono","solicitudes_rechazadas","boolean_de_bloqueo"])
        indice = 0
        while indice < len(lista):
            csv_Citizen_writer.writerow(lista[indice])
            indice = indice + 1
    listaCitizen.close()
def leerCuilsDelAnses(listaCuils):
    with open("../Archivos/CUIL.csv","r") as ansesCUILs:
        csv_CUILs_reader = csv.reader(ansesCUILs)
        next(ansesCUILs)
        for line in csv_CUILs_reader:
            listaCuils.append(line[0])
    ansesCUILs.close()
def modificarEstadoDeBloqueo(ciudadano):
    listaCuils = []
    leerDataEspecificaDeCiudadano(listaCuils,0)
    indiceCuil = 0
    posicionCuil = -1
    while indiceCuil < len(listaCuils):
        if ciudadano.CUIL == int(listaCuils[indiceCuil]):
            posicionCuil = indiceCuil
            indiceCuil = len(listaCuils)
        else:
            indiceCuil = indiceCuil + 1
    listaCitizens = []
    leerCiudadano(listaCitizens)
    listaCitizens.pop(posicionCuil)
    citizenCleaner()
    citizenListPlacerAfterClean(listaCitizens)
    escribirCiudadano(ciudadano)
    print("se modifico el estado de bloqueo del usuario con CUIL " + str(ciudadano.CUIL) + ".")
def generadorDeCitizenEnRuntime(CUIL):
    listaCUILS = []
    leerDataEspecificaDeCiudadano(listaCUILS,0)
    indice = 0
    posicionDelUser = -1
    while indice < len(listaCUILS):
        if CUIL == (listaCUILS[indice]):
            posicionDelUser = indice
            indice = len(listaCUILS)
        else:
            indice = indice + 1
    listaUsers = []
    leerCiudadano(listaUsers)
    citizenACrear = listaUsers[posicionDelUser]
    boolean = False
    if (int(citizenACrear[3])) == 1:
        boolean = False
    else:
        pass
    citizen = Ciudadano(CUIL,int(citizenACrear[1]),int(citizenACrear[2]),boolean)
    return citizen
def reescribirCitizenModificado(citizenModificado):
    listaNombres = []
    leerDataEspecificaDeCiudadano(listaNombres,0)
    indice = 0
    posicionDelNombre = -1
    while indice < len(listaNombres):
        if citizenModificado.CUIL == (int(listaNombres[indice])):
            posicionDelNombre = indice
            indice=len(listaNombres)
        else:
            indice = indice + 1
    listaCiudadanos = []
    leerCiudadano(listaCiudadanos)
    listaCiudadanos.pop(posicionDelNombre)
    citizenCleaner()
    citizenListPlacerAfterClean(listaCiudadanos)
    escribirCiudadano(citizenModificado)

def escribirTipoDeEvento(tipoDeEvento):
    with open("../Archivos/tiposDeEventos.csv","a",newline="") as listaTipos:
        csv_event_tipe_writer = csv.writer(listaTipos,delimiter=",")
        csv_event_tipe_writer.writerow([tipoDeEvento])
    listaTipos.close()
def leerTiposDeEvento(listaTiposEventos):
    with open("../Archivos/tiposDeEventos.csv","r") as tiposDeEventos:
        csv_event_tipe_reader = csv.reader(tiposDeEventos)
        next(tiposDeEventos)
        for line in csv_event_tipe_reader:
            listaTiposEventos.append(line[0])
    tiposDeEventos.close()
def escribirEvento(newEvento):
    EventoParaEscribir = newEvento.eventoAEscribir()
    with open("../Archivos/ListaEventos.csv","a",newline="") as listaEventos:
        csv_Event_writer = csv.writer(listaEventos,delimiter=",")
        csv_Event_writer.writerow(EventoParaEscribir)
    listaEventos.close()
def leerDataEspecificaEventoparaMapa(lista,valorABuscar):
    with open("../Archivos/ListaEventos.csv","r") as listaEventos:
        csv_Event_reader=csv.reader(listaEventos)
        next(listaEventos)
        for line in csv_Event_reader:
            lista.append(float(line[valorABuscar]))
    listaEventos.close()
def leerDataEspecificaEvento(lista,valorABuscar):
    with open("../Archivos/ListaEventos.csv","r") as listaEventos:
        csv_Event_reader=csv.reader(listaEventos)
        next(listaEventos)
        for line in csv_Event_reader:
            lista.append(line[valorABuscar])
    listaEventos.close()
def leerEvento(eventList):
    with open("../Archivos/listaEventos.csv","r") as listaEventos:
        csv_Event_Reader=csv.reader(listaEventos)
        next(listaEventos)
        for line in csv_Event_Reader:
            eventList.append(line)
    listaEventos.close()
def eventCleaner():
    cleaner = open("../Archivos/listaEventos.csv","w")
    cleaner.close()
def eventListPlacerAfterClean(lista):
    with open("../Archivos/listaEventos.csv","a",newline="")as listaEventos:
        csv_Event_writer = csv.writer(listaEventos,delimiter=",")
        csv_Event_writer.writerow(["nombre","fecha","tipoDeEvento","cantidad_de_personas","cantidad_maxima_de_personas","boolean_numerico_esta_lleno","coordenada_en_x","coordenada_en_y"])
        indice = 0
        while indice <len(lista):
            csv_Event_writer.writerow(lista[indice])
            indice = indice + 1
    listaEventos.close()
def checkerCaducidadDeEventos():
    listaFechasSTR = []
    leerDataEspecificaEvento(listaFechasSTR,1)
    listaanosINT = []
    listamesesINT = []
    listaDiasINT = []
    listaHorasINT = []
    listaMinutosINT = []
    indice1 = 0
    while indice1 < len(listaFechasSTR):
        listaSpliteadapaso1 = listaFechasSTR[indice1].split(" ")
        listaSpliteadaFecha = listaSpliteadapaso1[0].split("-")
        listaSpliteadaHora = listaSpliteadapaso1[1].split(":")
        listaanosINT.append(int(listaSpliteadaFecha[0]))
        listamesesINT.append(int(listaSpliteadaFecha[1]))
        listaDiasINT.append(int(listaSpliteadaFecha[2]))
        listaHorasINT.append(int(listaSpliteadaHora[0]))
        listaMinutosINT.append(int(listaSpliteadaHora[1]))
        indice1 = indice1 + 1
    indice2 = 0
    hayQueEliminar = False
    listaPosicionesAEliminar = []
    while indice2 < len(listaFechasSTR):
        fechaDelEvento = datetime.datetime(listaanosINT[indice2],listamesesINT[indice2],listaDiasINT[indice2],listaHorasINT[indice2],listaMinutosINT[indice2],0)
        if fechaDelEvento <= datetime.datetime.now():
            hayQueEliminar = True
            listaPosicionesAEliminar.append(indice2)
            indice2 = indice2 + 1
        else:
            indice2 = indice2 + 1
    if hayQueEliminar == False:
        pass
    else:
        indice3 = 0
        listaEventos = []
        leerEvento(listaEventos)
        while indice3 < len(listaPosicionesAEliminar):
            listaEventos.pop(listaPosicionesAEliminar[indice3])
            indice3 = indice3 + 1
        eventCleaner()
        eventListPlacerAfterClean(listaEventos)
def constructorDeEventoEnRuntime(nombreEvento):
    listaNombres = []
    leerDataEspecificaEvento(listaNombres,0)
    indice1 = 0
    posicionDelEvento = -1
    while indice1 < len(listaNombres):
        if nombreEvento == listaNombres[indice1]:
            posicionDelEvento = indice1
            indice1 = len(listaNombres)
        else:
            indice1 = indice1 + 1
    listaEventos = []
    leerEvento(listaEventos)
    eventoaConstruirEnRuntime = listaEventos[posicionDelEvento]
    listaSpliteadapaso1 = eventoaConstruirEnRuntime[1].split(" ")
    listaSpliteadaFecha = listaSpliteadapaso1[0].split("-")
    listaSpliteadaHora = listaSpliteadapaso1[1].split(":")
    anoINT = int(listaSpliteadaFecha[0])
    mesINT = int(listaSpliteadaFecha[1])
    DiaINT = int(listaSpliteadaFecha[2])
    HoraINT = int(listaSpliteadaHora[0])
    MinutoINT = int(listaSpliteadaHora[1])
    eventoEnRuntime = Evento(eventoaConstruirEnRuntime[0],anoINT,mesINT,DiaINT,HoraINT,MinutoINT,eventoaConstruirEnRuntime[2],int(eventoaConstruirEnRuntime[4]),float(eventoaConstruirEnRuntime[6]),float(eventoaConstruirEnRuntime[7]))
    eventoEnRuntime.setCantidadDePersonas(int(eventoaConstruirEnRuntime[3]))
    booleanEstaLLeno = False
    if int(eventoaConstruirEnRuntime[5]) == 1:
        booleanEstaLLeno = True
    else:
        pass
    eventoEnRuntime.setEstaLleno(booleanEstaLLeno)
    return eventoEnRuntime
def modificarEventoEnPersistencia(evento):
    listaNombresDeEventos = []
    leerDataEspecificaEvento(listaNombresDeEventos,0)
    indice = 0
    posicionDelEvento = -1
    while indice < len(listaNombresDeEventos):
        if evento.nombre == listaNombresDeEventos[indice]:
            posicionDelEvento = indice
            indice = len(listaNombresDeEventos)
        else: indice = indice + 1
    listaEventos = []
    leerEvento(listaEventos)
    listaEventos.pop(posicionDelEvento)
    eventCleaner()
    eventListPlacerAfterClean(listaEventos)
    escribirEvento(evento)

def escribirSolicitud(solicitud):
    try:
        solicitudParaEscribir = solicitud.solicitudAEscrbir()
        with open("../Archivos/solicitudes.csv","a",newline="") as listaSolicitudes:
            csv_Request_writer = csv.writer(listaSolicitudes,delimiter=",")
            csv_Request_writer.writerow(solicitudParaEscribir)
        listaSolicitudes.close()
    except AttributeError:
        pass
def leerSolicitudes(requestList):
    with open("../Archivos/solicitudes.csv","r") as listaSolicitudes:
        csv_Request_reader = csv.reader(listaSolicitudes)
        next(listaSolicitudes)
        for line in csv_Request_reader:
            requestList.append(line)
    listaSolicitudes.close()
def leerDataEspecificaSolicitudes(lista,valorABuscar):
    with open("../Archivos/solicitudes.csv","r") as listaSolicitudes:
        csv_Request_reader = csv.reader(listaSolicitudes)
        next(listaSolicitudes)
        for line in csv_Request_reader:
            lista.append(line[valorABuscar])
    listaSolicitudes.close()
def requestCleaner():
    cleaner = open("../Archivos/solicitudes.csv","w")
    cleaner.close()
def requestListPlacerAfterClean(lista):
    with open("../Archivos/solicitudes.csv","a",newline="") as listaSolicitudes:
        csv_Request_writer = csv.writer(listaSolicitudes,delimiter=",")
        csv_Request_writer.writerow(["CUIL_del_enviador","CUIL_del_invitado","nombre_del_evento","hora_de_envio"])
        indice = 0
        while indice < len(lista):
            csv_Request_writer.writerow(lista[indice])
            indice = indice + 1
    listaSolicitudes.close()
def checkerCaducidadDeInvitacion():
    listaNombresEventos = []
    leerDataEspecificaEvento(listaNombresEventos,0)
    listaNombresEventosSolicitudes = []
    leerDataEspecificaSolicitudes(listaNombresEventosSolicitudes,2)
    indiceSolicitudes = 0
    listaPosicionesSolicitudesSinEventos = []
    while indiceSolicitudes < len(listaNombresEventosSolicitudes):
        indiceNombres = 0
        existeElEvento = False
        while indiceNombres < len(listaNombresEventos):
            if listaNombresEventosSolicitudes[indiceSolicitudes] == listaNombresEventos[indiceNombres]:
                existeElEvento = True
                indiceNombres = len(listaNombresEventos)
            else:
                indiceNombres = indiceNombres + 1
        if existeElEvento == True:
            indiceSolicitudes = indiceSolicitudes + 1
        else:
            listaPosicionesSolicitudesSinEventos.append(indiceSolicitudes)
            indiceSolicitudes = indiceSolicitudes + 1
    if len(listaPosicionesSolicitudesSinEventos) == 0:
        pass
    else:
        listaSolicitudes = []
        leerSolicitudes(listaSolicitudes)
        indiceListaPosiciones = 0
        while indiceListaPosiciones < len(listaPosicionesSolicitudesSinEventos):
            listaSolicitudes.pop(listaPosicionesSolicitudesSinEventos[indiceListaPosiciones])
            indiceListaPosiciones = indiceListaPosiciones + 1
        requestCleaner()
        requestListPlacerAfterClean(listaSolicitudes)
def borrarsolicitud(listaPosiciones):
    listaSolicitudes = []
    leerSolicitudes(listaSolicitudes)
    listaSolicitudes.pop(listaPosiciones[0])
    requestCleaner()
    requestListPlacerAfterClean(listaSolicitudes)

def leerDataEspecificaDeAdmin(listaAdmin,valorABuscar):
    with open("../Archivos/listaAdministradores.csv","r") as listaAdministradores:
        csv_admin_reader=csv.reader(listaAdministradores)
        next(listaAdministradores)
        for line in csv_admin_reader:
            listaAdmin.append(line[valorABuscar])
    listaAdministradores.close()
def leerAdministradores(lista):
    with open("../Archivos/listaAdministradores.csv","r") as listaAdmin:
        csv_Admin_reader = csv.reader(listaAdmin)
        next(listaAdmin)
        for line in csv_Admin_reader:
            lista.append(line)
    listaAdmin.close()
def escribirAdministrador(admin):
    AdminParaEscribir=admin.adminAEscribir()
    with open("../Archivos/listaAdministradores.csv","a",newline="") as listaAdmin:
        csv_Admin_writer = csv.writer(listaAdmin,delimiter=",")
        csv_Admin_writer.writerow(AdminParaEscribir)
    listaAdmin.close()
def adminCleaner():
    cleaner = open("../Archivos/listaAdministradores.csv","w")
    cleaner.close()
def adminListPlacerAfterClean(lista):
    with open("../Archivos/listaAdministradores.csv","a",newline="")as listaAdmin:
        csv_Admin_writer = csv.writer(listaAdmin,delimiter=",")
        csv_Admin_writer.writerow(["username","contraseña","esABM"])
        indice = 0
        while indice < len(lista):
            csv_Admin_writer.writerow(lista[indice])
            indice = indice + 1
    listaAdmin.close()