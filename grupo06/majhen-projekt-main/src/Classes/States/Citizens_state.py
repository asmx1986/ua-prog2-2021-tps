from random import randint
# Acá van se van a registrar todas las instancias correspondientes y los modificadores de esos estados
class Citizens_state:
    def __init__(self) -> None:
        self.citizens_list = dict()

    def get_citizen(self, citizen_cuil):
        return self.citizens_list.get(citizen_cuil)

    def add_citizen_to_list(self, citizen) -> None:
        self.citizens_list.update({ citizen.get_cuil(): citizen })

    def delete_citizen(self, citizen_cuil) -> None:
        if self.validate_citizen_exists(citizen_cuil):
            self.citizens_list.pop(citizen_cuil)
        
    def validate_citizen_exists(self, citizen_cuil) -> bool:
        return bool(self.citizens_list.get(citizen_cuil))

    def get_random_citizen(self):
        
        list_temp = []
        for citizen_cuil, _ in self.citizens_list.items():
            list_temp.append(citizen_cuil)

        index = randint(1, len(list_temp) - 1)        
        random_citizen = self.citizens_list.get(list_temp[index])
        
        return random_citizen

    def block_citizen(self, citizen_cuil):
        citizen = self.get_citizen(citizen_cuil)
        citizen.blocked = True

        self.citizens_list.update({ citizen.get_cuil(): citizen })