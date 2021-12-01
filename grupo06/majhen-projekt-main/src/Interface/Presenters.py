from Import_index import Anses, Citizen, General_state, Admin, General_state, Birthday_event, Concert_event, Party_event, Sensor, Citizens_state, Event_invite_friend

class Presenters:
    def citizen_registration(self) -> Citizen:
        citizen_cuil = input("Por favor ingrese su numero de cuil: ")

        while not Anses.validate_citizen(citizen_cuil):
            citizen_cuil = input("Por favor verifique e ingrese su numero de cuil de nuevo: ")
                
        # Load citizen to the system
        citizen_data = Anses.get_citizen_data(citizen_cuil)
        citizen = Citizen(citizen_data)
        General_state.get_citizens_state().add_citizen_to_list(citizen)
        # 
        
        print("-- ¡Registro exitoso! --")

        return citizen

    def admin_registration(self) -> Admin:
        admins_state = General_state.get_admins_state()

        admin_id = input("Ingrese su 'id' de administrador: ")
        admin_password = input("Ingrese su contraseña de administrador: ")

        while not admins_state.login_admin(admin_id, admin_password):
            print("Datos incorrectos, por favor verifique e ingrese de nuevo los datos.")

            admin_id = input("Ingrese su 'id' de administrador: ")
            admin_password = input("Ingrese su contraseña de administrador: ")
        
        admin = admins_state.get_admin(admin_id) 
        print(f"-- ¡Registro exitoso! Bienvenido administrador {admin.get_name()}--")

        return admin