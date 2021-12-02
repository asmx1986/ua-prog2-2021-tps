class NivelInvalido(Exception):
    msg = "El nivel posible de un evento es entre 1 y 5"

class CoordenadaInvalida(Exception):
    msg = "Las coordenadas ingresadas son invalidas"

class TipoInexistente(Exception):
    msg = "El tipo de evento no existe"
class EventoNoEncontrado(Exception):
    msg = "Evento no encontrado"

class NoExisteLaPersona(Exception):
    msg = 'No se ha encontrado ninguna persona con ese nombre'

class NoTenesAmigos(Exception):
    msg = 'Amigo no encontrado'

class ValorInvalido(Exception):
    msg = 'Nivel invalido'

class UsuarioBloqueado(Exception):
    msg = "El usuario ya está bloqueado"

class UsuarioNoBloqueado(Exception):
    msg = "El usuario no esta bloqueado"

class NoExisteElsolicitador(Exception):
    msg = "Esta persona no te envio una solicitud de amistad"
