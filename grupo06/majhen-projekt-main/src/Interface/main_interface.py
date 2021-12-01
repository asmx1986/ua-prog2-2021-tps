
from Import_index import General_state, Citizen, Admin, erase_screen
from .Presenters import Presenters
from Map.Zones import Zones
from tabulate import tabulate

#import from general_state General state, and then load sensor???
class Interface:
    def __init__(self) -> None:        
        self.inicialize()

    def inicialize(self):
        print("Bienvenido a Lamac ¿Cómo desea entrar?")
        print("1 - Como ciudadano")
        print("2 - Como administrador")
        print("3 - Como sensor")
        print("4 - Ver mapa")

        user_entry = self.control_data_entry(4)

        presenter = Presenters()

        if user_entry == "1":
            citizen = presenter.citizen_registration()

            self.citizen_interface(citizen)

        elif user_entry == "2":

            admin = presenter.admin_registration()

            # Call the admin interface
            self.admin_interface(admin)
        elif user_entry == "3":
            self.sensor_interface()

        else:
            self.map_interface()
    
    # Specific Interfaces
    def citizen_interface(self, citizen: Citizen):

        def initiate_citizen():
            print('Menu Ciudadano.\n¿Que accion desea realizar?')
            print('1. Crear/reportar un evento')
            print('2. Mandar una solicitud de amistad')
            print('3. Volver al menu principal')
            
            citizen_entry = self.control_data_entry(3)

            if citizen_entry == '1':
                print('-- Crear/reportar un evento fue seleccionado -- ')
                citizen.send_event_report()
                self.citizen_interface(citizen)
                #vuelve al menu citizen
            
            elif citizen_entry == '2':
                print('-- Mandar una solicitud de amistad fue seleccionado --')
                print('Ingresa el cuil de la persona: ', end='')
                cuil_FR = input()       # get a cuil, add to friend list.
                citizen_state = General_state.get_citizens_state()
                recipient = citizen_state.get_citizen(cuil_FR)

                citizen.send_friend_request(recipient)
                self.citizen_interface(citizen)
                # vuelve al menu de citizen.
            
            elif citizen_entry == '3':  #go back to main menu
                self.inicialize() 

        initiate_citizen()

    def admin_interface(self, admin_logged: Admin):
        
        def initiate_Admin():
            print('Menu Administrador. \n¿Que accion desea realizar?')
            print('1. Ver tabla de estadisticas')
            print('2. Ver sensores')
            print('3. Opciones de Administrador')
            print('4. Bloquear Ciudadano')
            print('5. Volver al menu principal.')

            admin_entry = self.control_data_entry(5)

            if admin_entry == '1':      # show staticts table
                print('-- Ver tabla de estadisticas fue seleccionado --')
                print('Ver tabla de estadisticas de la zona:')
                print('1. Zona 1')
                print('2. Zona 2')
                print('3. Zona 3')
                print('4. Zona 4')
                print('5. Volver a menu Administrador.')
                
                states_table_entry = self.control_data_entry(5)

                if states_table_entry == '5':
                    self.admin_interface(admin_logged)

                print(f'-- Mostrando tabla de zona {states_table_entry} --')
                sensors_dict = General_state.get_sensors_formatted_data()
                zones = Zones(states_table_entry, sensors_dict)
                statistics_by_zone = zones.get_statistics(int(states_table_entry))
                
                sensors = General_state.get_sensors()
                
                table_data = self.format_statistics(statistics_by_zone, sensors)
              
                print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))

                self.admin_interface(admin_logged)
              
            elif admin_entry == '2':        # show sensors
                print('-- Ver sensores fue seleccionado -- ')           #maybe not show this
                print('¿Que accion desea realizar?')
                sensors = General_state.get_sensors()

                for sensor_id, sensor in sensors.items():
                    print(sensor_id) 
                    print(f"- Concurrencia: {sensor.get_actual_concurrency()}")
                    print(f"- Tipo de evento: {sensor.event.get_type_event_str()}")
                    print(f"- Descripcion del evento: {sensor.get_event_description()}")

                self.admin_interface(admin_logged)

            elif admin_entry == '3':        # create/ block/ delete admin
                print('-- Opciones de Administrador fue seleccionado -- ')
                print('Que accion quiere realizar?')
                print('1. Crear un administrador')
                print('2. Bloquear un administrador')
                print('3. Eliminar un administrador')
                print('4. Ver ranking de sensores por zona')
                print('5. Volver a menu Administrador')
                
                options_admin_entry = self.control_data_entry(4)

                if options_admin_entry == '1':      # create admin
                    print('-- Crear un administrador fue seleccionado --')
                    new_admin = admin_logged.create_admin()

                    print('Un nuevo administrador fue creado, sus credenciales son: ')
                    print(f'- ID:{new_admin.get_id()}')
                    print(f'- Password: {new_admin.get_password()}')

                    self.admin_interface(admin_logged)
                    
                elif options_admin_entry == '2':        #block admin
                    print('Bloquear un administrador fue seleccionado --')
                    id_admin = input('ID del administrador al que se desea bloquear: ')     
                    print(f'{id_admin}')
                    admin_logged.block_admin(id_admin)
                    print(f'Administrador {id_admin} fue bloqueado.')
                    
                    self.admin_interface(admin_logged)
                
                elif options_admin_entry == '3':        #delete admin
                    print('-- Eliminar un administrador fue seleccionado --')
                    id_admin = input('ID del administrador al que se desea eliminar: ')
                    print(f'{id_admin}')
                    
                    admins_state = General_state.get_admins_state()
                    
                    admins_state.delete_admin(id_admin)

                    print(f'El administrador con el id: {id_admin} fue eliminado.')
                    self.admin_interface(admin_logged)

                elif options_admin_entry == "4": # Show table by zone
                    for zone in range(1, 5):
                        print(f'-- Tabla de zona número {zone} --')
                        sensors_dict = General_state.get_sensors_formatted_data()
                        zones = Zones(zone, sensors_dict)
                        statistics_by_zone = zones.get_statistics(int(zone), True)
                        
                        sensors = General_state.get_sensors_formatted_data()
                        
                        table_data = self.format_statistics(statistics_by_zone, sensors)
                    
                        print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))
                    
                    self.admin_interface(admin_logged)

                elif options_admin_entry == '5':        #go back to admin menu
                    self.admin_interface(admin_logged)
                
            elif admin_entry == '5':        #  block citizen, show random citizen getting blocked
                print('-- Opciones ciudadano seleccionado -- ')
                print('¿Que accion desea realizar?')
                print('1. Bloquear un ciudadano')
                print('2. Volver a menu Administrador')

                citizen_options = self.control_data_entry(2)

                if citizen_options == '1':      #block citizen from admin POV
                    print('-- Bloquear ciudadano fue seleccionado -- ')
                    cuil_citizen = input('Cuil del ciudadano que se desea bloquear: ')

                    citizens_state = General_state.get_citizens_state()

                    while not citizens_state.validate_citizen_exists(cuil_citizen):
                        cuil_citizen = input('Corrobore que el cuil del ciudadano que desea bloquear: ')

                    General_state.block_citizen(cuil_citizen)
                    citizen = citizens_state.get_citizen(cuil_citizen)

                    print(f'-- El ciudadano con el cuil {citizen.name} {citizen.last_name} fue bloqueado -- ')

                    self.admin_interface(admin_logged)

                elif citizen_options == '2':    #exit to admin menu
                    self.admin_interface(admin_logged)

            elif admin_entry == '6':        # go back to main menu
                self.inicialize()

        initiate_Admin()
    
    def sensor_interface(self):
        def initiate_sensor_interface():
            print('Menu Sensores.')
            print('1. Sensores activos.')
            print('2. Volver al menu principal.')

            sensor_entry = self.control_data_entry(2)

            if sensor_entry == '1':     #show all active sensors, according to seba in slack
                print('-- Sensores activos fue seleccionado --')
                print('¿Que accion desea realizar?')
                print('1. Mostrar todos los sensores activos')
                print('2. Volver a menu Sensores')

                sensor_type_entry = self.control_data_entry(2)

                if sensor_type_entry == '1':
                    print('--Monstrando sensores activos--')
                    sensors = General_state.get_sensors()

                    for sensor_id, sensor in sensors.items():
                        print(sensor_id) 
                        print(f"- Concurrencia: {sensor.get_actual_concurrency()}")
                        print(f"- Tipo de evento: {sensor.event.get_type_event_str()}")
                        print(f"- Descripcion del evento: {sensor.get_event_description()}")

                    self.sensor_interface()

                elif sensor_type_entry == '2':
                    self.sensor_interface()
            
            elif sensor_entry == '2':
                self.inicialize()
        
        initiate_sensor_interface()

    def map_interface(self):
        def initiate_map_interface():
            print('-- Ver mapa fue seleccionado --') # TODO
            print('Ver mapa de la zona:')
            print('1. Zona 1')
            print('2. Zona 2')
            print('3. Zona 3')
            print('4. Zona 4')
            print('5. Volver a menu principal')
            
            map_entry = self.control_data_entry(5)

            if map_entry == '5':
                self.inicialize()

            print(f"-- Mostrando mapa de la zona {map_entry} --")

            sensors_dict = General_state.get_sensors_formatted_data()
            zones = Zones([1, 2, 3, 4], sensors_dict)
            statistics_by_zone = zones.get_statistics(int(map_entry), True)
            table_data = self.format_statistics(statistics_by_zone, sensors_dict)

            zones.print_map_zone(int(map_entry))

            print(f"-- Mostrando mapa de la zona {map_entry} --")
            print(tabulate(table_data, headers="keys", tablefmt="fancy_grid"))

            initiate_map_interface()

        initiate_map_interface()

    # Format Methods
    def format_statistics(self, statistics_by_zone, sensors):
        table_data = dict({ "ID": [], "Tipo de evento": [], "Descripcion": [], "Concurrencia": [] })
            
        for i in range(len(statistics_by_zone)):
            real_sensor = sensors.get(statistics_by_zone[i]["id_"])
            
            table_data.get("ID").append(real_sensor["_id"])
            table_data.get("Tipo de evento").append(real_sensor["event"]["type_event"])
            table_data.get("Descripcion").append(real_sensor["event"]["description"])
            table_data.get("Concurrencia").append(real_sensor["concurrency"])
        return table_data
    
    def control_data_entry(self, options_quantity) -> str:
        'Solo puede retornar una opcion valida para el sistema'

        entry = input().strip()

        try:
            for char in entry:
                cast_test = int(char)
        except:
            entry = 1000

        while not (int(entry) > 0 and int(entry) <= options_quantity):
                print(f"Por favor introduzca una opción válida para ingresar al sistema (del 1 al {options_quantity}): ", end='')
                entry = input()    
            
        erase_screen()
        return entry