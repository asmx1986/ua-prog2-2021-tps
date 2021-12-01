# Acá van se van a registrar todas las instancias correspondientes y los modificadores de esos estados
# from ..Admin import Admin 
try:
    from ..Admin import Admin
except ImportError:
    import sys
    Admin = sys.modules[__package__ + '.Admin']



class Admins_state:
    def __init__(self) -> None:
        self.admins_list = dict()
    
    def block_admin(self, admin_id):
        if self.validate_admin_exists(admin_id):
            self.admins_list[admin_id].blocked = True

    def add_hardcoded_admin(self, admin_dev):
        self.admins_list.update({ admin_dev.get_id(): admin_dev })

    def add_admin_to_list(self, name_new_admin) -> Admin:
        new_admin = Admin(name_new_admin)
        
        self.admins_list.update({ new_admin.get_id(): new_admin })

        return new_admin
        
    def delete_admin(self, admin_id) -> None:
        self.admins_list.pop(admin_id)

    def validate_admin_exists(self,  admin_id: str):
        return bool(self.admins_list.get(admin_id))

    def login_admin(self, admin_id: str, admin_password: str) -> bool:
        if self.admins_list.get(admin_id) and self.admins_list.get(admin_id).password == admin_password:
            return True
        
        return False

    def get_admin(self, admin_id = None) -> Admin:
        if admin_id == None:
            for admin_id_temp, admin in self.admins_list.items():
                if not admin.blocked:
                    admin_id = admin_id_temp
        
        return self.admins_list.get(str(admin_id))

    def validate_if_admin_is_blocked(self, admin_id):
        if self.admins_list.get(admin_id)["blocked"]:
            return True
        
        return False
