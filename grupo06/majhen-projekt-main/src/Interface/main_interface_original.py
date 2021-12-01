
from Import_index import Sensor_table, General_state
from .Presenters import Presenters

class Interface:
    def __init__(self) -> None:
        self.role = None
        
        self.inicialize()

    def inicialize(self):
        print("Bienvenido a 'insertar nombre de la plataforma'. ¿Cómo desea entrar?")
        print("1 - Como ciudadano")
        print("2 - Como administrador")
        print("3 - Como sensor")

        user_entry = input().strip()

        while not ( int(user_entry) <= 3 and int(user_entry) >= 1 ):
            print("Por favor introduzca una opción válida para ingresar al sistema")
            print("1 - Como ciudadano")
            print("2 - Como administrador")
            print("3 - Como sensor")
            
            user_entry = input()
        
        presenter = Presenters()

        if user_entry == "1":
            citizen = presenter.citizen_registration()
            
            rand_citizen = General_state.citizens_state.get_random_citizen

            citizen.send_friend_request(rand_citizen())
            citizen.send_friend_request(rand_citizen())
            citizen.send_friend_request(rand_citizen())
            citizen.send_friend_request(rand_citizen())
            citizen.send_friend_request(rand_citizen())

            citizen.send_event_report()
            citizen.send_event_report()
            citizen.send_event_report()
            
            # Call the citizen interface
        elif user_entry == "2":

            admin = presenter.admin_registration()
            # Call the admin interface
        else:
            # development is lacking
            Sensor_table()
            # Call the sensor table
