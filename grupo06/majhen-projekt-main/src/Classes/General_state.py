from os import stat
from .Admin import Admin_dev
from .Event import Birthday_event, Concert_event, Party_event
from .Requests_module.Event_report import Event_invite_friend
from .Sensor import Sensor, Sensor_load
from . import Citizen

from .Modules.Dataset import dataset
from .States.Admins_state import Admins_state
from .States.Citizens_state import Citizens_state
from .Modules.json_module.json_main import Json

# Static class
class General_state:
    admins_state = Admins_state()
    citizens_state = Citizens_state()
    sensors = dict()

    @staticmethod
    def get_sensors():
        return General_state.sensors
        
    @staticmethod
    def block_citizen(citizen_cuil):
        citizen_state = General_state.get_citizens_state()
        citizen_state.block_citizen(citizen_cuil)

    @staticmethod
    def load_previous_status_of_sensors():
        previous_sensors_state_dict = Json().load_json_from_file()

        for sensor_id, sensor in previous_sensors_state_dict.items():
            if sensor["event"]["type_event"] == "Party":
                event = Party_event(sensor["event"]["zone"], sensor["event"]["description"])
            elif sensor["event"]["type_event"] == "Concert":
                event = Concert_event(sensor["event"]["zone"], sensor["event"]["description"])
            else:
                event = Birthday_event(sensor["event"]["zone"], sensor["event"]["description"])

            General_state.sensors.update({ sensor_id: Sensor_load(sensor_id, event, sensor["concurrency"]) })


    @staticmethod
    def get_sensors():
        return General_state.sensors

    @staticmethod
    def get_sensors_formatted_data():
        sensors_dict = dict()

        for sensor_id, sensor in General_state.get_sensors().items():
            event = sensor.get_event()

            sensors_dict.update({ 
                sensor_id: {
                    "_id" : sensor_id,
                    "concurrency": sensor.get_actual_concurrency(),
                    "event": {
                        "description": event.description,
                        "zone": event.zone,
                        "type_event": event.get_type_event_str()
                    }
                } 
            })

        return sensors_dict
    
    @staticmethod
    def load_instances():
        admins_state = General_state.get_admins_state()
        admins_state.add_hardcoded_admin(Admin_dev("1", "123", "Hardcoded admin")) # dev

        admins_state.add_admin_to_list("Ariel") # dev
        admins_state.add_admin_to_list("Lola") # dev
        admins_state.add_admin_to_list("Camila") # dev
        admins_state.add_admin_to_list("Maximo") # dev

        General_state.citizens_state.add_citizen_to_list(Citizen.Citizen({ "name": "Ariel", "last_name": "Aguilera", "cuil" : "1234", "phone" : "123" }))
        counter = 0
        for _, citizen_data in dataset.items():
            General_state.citizens_state.add_citizen_to_list(Citizen.Citizen(citizen_data))

            if counter == 5:
                break # dev struct

            counter +=1

    @staticmethod
    def get_admins_state():
        return General_state.admins_state

    @staticmethod
    def get_citizens_state():
        return General_state.citizens_state

    @staticmethod
    def load_sensor(sensor):
        General_state.sensors.update({ sensor.get_id() : sensor })

        sensors_formatted = General_state.get_sensors_formatted_data()
        Json().save_json(sensors_formatted) # Persist updating sensors

    @staticmethod
    def block_admin(admin_id):
        admins_state = General_state.get_admins_state()
        admins_state.block_admin(admin_id)

    @staticmethod
    def get_admin(admin_id):
        admins_state = General_state.get_admins_state()
        admin = admins_state.get_admin(admin_id)
        return admin

zones = {
    "buenos Aires": { "latitude": 1, "longitude": 1 },
    "la pampa": { "latitude": 2, "longitude": 2 },
    "jujuy": { "latitude": 3, "longitude": 3 },
    "rio negro": { "latitude": 4, "longitude": 4 },
    "santa cruz": { "latitude": 5, "longitude": 5 },
    "cordoba": { "latitude": 6, "longitude": 6 },
    "la rioja": { "latitude": 7, "longitude": 7 },
    "formosa": { "latitude": 8, "longitude": 8 }
}

def Friend_request_presenter(recipient, sender) -> bool:
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

def Event_invite_presenter(sender, event) -> bool:
    sender_data = sender.get_formatted_data()

    print(f'El usuario { sender_data.get("name") } { sender_data.get("last_name") } te esta invitando al evento {event.get_description()}. ¿Queres aceptar la invitacion? (y/n): ', end = "")
    response = str(input())

    return (True if response.lower() == "y" else False)

def Report_event_presenter(citizen) -> Sensor:
    print("¿Qué tipo de evento quiere reportar?")
    print("1 - Cumpleaños")
    print("2 - Concierto")
    print("3 - Fiesta")

    type_event = int(input())

    while not (type_event <= 3 and type_event >= 1):
        print("La opcion ingresada es invalida. Por favor ingrese una opcion valida.")
        print("1 - Cumpleaños")
        print("2 - Concierto")
        print("3 - Fiesta")

        type_event = input()
    
    event_description = input("Ingrese una descripcion para el evento: ")
    event_location = input("Ingrese el nombre de la provincie donde está ocurriendo el evento: ")

    while not (zones.get(event_location.lower())):
        print("La zona ingresada no forma parte de la cobertura del sistema. Por favor corrobore la zona e intente de nuevo")
        event_location = input()

    event_latitude = zones.get(event_location.lower())["latitude"]
    event_longitude = zones.get(event_location.lower())["longitude"]

    event = Report_event_with_friend_presenter(citizen, event_latitude, event_longitude, event_description, type_event)
    
    return Sensor(event)

def Report_event_with_friend_presenter(
    citizen,
    event_latitude, 
    event_longitude, 
    event_description, 
    type_event
) -> Birthday_event | Concert_event | Party_event:

    print("¿Quiere invitar a un amigo al evento? (y/n)", end="")
    response = input("")
    
    if type_event == 1:
        event = Birthday_event(event_latitude, event_longitude, event_description)
    elif type_event == 2:
        event = Concert_event(event_latitude, event_longitude, event_description)
    else:
        event = Party_event(event_latitude, event_longitude, event_description)

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