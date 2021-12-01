from .Requests_module.Friend_requests import Friend_request

from .Event import Birthday_event
from .Event import Concert_event
from .Event import Party_event
from .General_state import General_state
from .Requests_module.Event_report import Event_invite_friend, Event_report
from .Sensor import Sensor

zones = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4
}

class Citizen_State:
    def __init__(self) -> None:
        self.friend_list = dict()
        self.rejections_list = dict()
        self.block_list = list()

    def add_friend(self, friend):
        print(f'----- Añadiendo a {friend.name} {friend.last_name} a la lista de amigos de {self.name} {self.last_name} -----') # dev

        self.friend_list.update({ friend.get_cuil(): friend.get_formatted_data() })
    
    def add_citizen_to_block_list(self, citizen):
        self.block_list.append(citizen.get_cuil())

    def update_rejections_list(self, citizen):
        citizen_cuil = citizen.get_cuil()

        print(f'----- Añadiendo a {citizen.name} {citizen.last_name} a la lista de rejections de {self.name} {self.last_name} -----')  # dev

        if self.rejections_list.get(citizen_cuil):
            new_rejections_counter = self.rejections_list.get(citizen_cuil)["rejections_counter"] + 1

            if new_rejections_counter >= 5:
                # Presenter ?
                citizen_data = citizen.get_formatted_data()
                print(f'Usted fue bloqueado para el usuario {citizen_data["name"]} {citizen_data["last_name"]}. Motivo: 5 solicitudes de amistad rechazadas')
                #

                citizen.add_citizen_to_block_list(self)
        else:
            new_rejections_counter = 1

        self.rejections_list.update({ citizen_cuil: { "cuil": citizen_cuil, "rejections_counter": new_rejections_counter } }) # If the record does not exist then "update" creates it

class Citizen (Citizen_State):
    def __init__(self, citizen_data) -> None:
        super().__init__()

        self.name = citizen_data["name"]
        self.last_name = citizen_data["last_name"]
        self.phone = citizen_data["phone"]
        self.cuil = citizen_data["cuil"]
        self.blocked = False

    def get_formatted_data(self) -> dict:
        formatted_data = dict({
            "name": self.name,
            "last_name": self.last_name,
            "phone": self.phone,
            "cuil": self.cuil,
        })

        return formatted_data

    def exists_citizen_blocked(self, citizen_cuil) -> bool:
        return citizen_cuil in self.block_list

    def get_cuil(self) -> str:
        return self.cuil
    
    def send_friend_request(self, recipient):
        response = Friend_request(self, recipient).execute()

        if not (response == "citizen_blocked" or response == "are_already_friends" or response == "same_user_error"):
            self.add_friend(recipient) if response else self.update_rejections_list(recipient)

    def receive_friend_request(self, sender): # Recipient method
        friend_request_response = Friend_request_presenter(self, sender)

        if friend_request_response: 
            self.add_friend(sender) 

        return friend_request_response

    def exists_citizen_blocked(self, citizen_cuil):
        return citizen_cuil in self.block_list

    def exists_friend(self, citizen_cuil):
        return citizen_cuil in self.friend_list

    def send_event_report(self):
        sensor = Report_event_presenter(self)

        Event_report(sensor).execute()

    def receive_event_invite(self, sender, event) -> bool: # Recipient method
        response = Event_invite_presenter(sender, event)

        return response

# ------------------------------- PRESENTER ---------------

def Friend_request_presenter(recipient: Citizen, sender: Citizen) -> bool:
    sender_data = sender.get_formatted_data()

    print(f'{recipient.name} {recipient.last_name} Te llego una solicitud de amistad de { sender_data.get("name") } { sender_data.get("last_name") }. ¿Queres aceptarla? (y/n): ', end = "")
    friend_request_ricipient_response = input().lower().strip()

    
    while not (friend_request_ricipient_response == "y" or friend_request_ricipient_response == "n"):
        print(friend_request_ricipient_response)
        friend_request_ricipient_response = input("La opción ingresada no es valida. Por favor ingrese 'y' o 'n'")

    if friend_request_ricipient_response == "y":
        return True
    elif friend_request_ricipient_response == "n":
        return False

def Event_invite_presenter(sender: Citizen, event) -> bool:
    sender_data = sender.get_formatted_data()

    print(f'El usuario { sender_data.get("name") } { sender_data.get("last_name") } te esta invitando al evento {event.get_description()}. ¿Queres aceptar la invitacion? (y/n): ', end = "")
    response = str(input())

    return (True if response.lower() == "y" else False)

def Report_event_presenter(citizen: Citizen) -> Sensor:
    print("¿Qué tipo de evento quiere reportar?")
    print("1 - Cumpleaños")
    print("2 - Concierto")
    print("3 - Fiesta")

    type_event = input()

    while not (type_event == "3" or type_event == "2" or type_event == '1'):
        print("La opcion ingresada es invalida. Por favor ingrese una opcion valida.")
        print("1 - Cumpleaños")
        print("2 - Concierto")
        print("3 - Fiesta")

        type_event = input()
    
    event_description = input("Ingrese una descripcion para el evento: ")
    zone = input("Ingrese la zona donde está ocurriendo el evento (1 a 4): ")

    while not (zones.get(zone.lower())):
        print("La zona ingresada no forma parte de la cobertura del sistema. Por favor corrobore la zona e intente de nuevo")
        zone = input()

    event = Report_event_with_friend_presenter(citizen, int(zone), event_description, type_event)
    
    return Sensor(event)

def Report_event_with_friend_presenter(
    citizen,
    zone, 
    event_description, 
    type_event
) -> Birthday_event | Concert_event | Party_event:

    print("¿Quiere invitar a un amigo al evento? (y/n): ", end="")
    response = input("")
    
    if type_event == 1:
        event = Birthday_event(zone, event_description)
    elif type_event == 2:
        event = Concert_event(zone, event_description)
    else:
        event = Party_event(zone, event_description)

    if response.lower() == "y":
        friend_cuil = input("Ingrese el cuil de su amigo: ")

        citizens_state = General_state.get_citizens_state()
        while not citizens_state.validate_citizen_exists(friend_cuil):
            print("El usuario ingresado no esta registrado en el sistema. Por favor corrobore los datos e ingrese el cuil de nuevo")
            friend_cuil = input("Ingrese el cuil de su amigo: ")
        
        friend = citizens_state.get_citizen(friend_cuil)
        friend_response = Event_invite_friend(citizen, friend, event).execute()

        if friend_response:
            event.add_friend(friend)
    
    return event