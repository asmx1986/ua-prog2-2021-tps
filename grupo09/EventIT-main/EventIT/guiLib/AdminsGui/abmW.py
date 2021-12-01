import tkinter as tk
from tkinter import messagebox

from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UserManagementLib.CreateProfileClass import CreateProfile

class AbmW(tk.Tk):
    def __init__(self, reg_de_usuarios: RegDeUsuarios, admin: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"450x400+{550}+{150}")
        self.wm_resizable(1, 1)
        self.regdeusuarios = reg_de_usuarios
        self.admin = admin
        self.Create_Widgets()

    def Create_Widgets(self):
        #Creacion de widgets
        self.keynameentry = tk.Entry(self)
        self.nameentry = tk.Entry(self)
        self.phoneentry = tk.Entry(self)
        self.cuilentry = tk.Entry(self)

        self.phone_btn = tk.Button(self, text= "chanege phone", command= lambda: self.modify_profile("phone"))
        self.cuil_btn = tk.Button(self, text= "change cuil", command= lambda: self.modify_profile("cuil"))
        self.name_btn = tk.Button(self, text= "change ame", command= lambda: self.modify_profile("name"))

        self.daralta_btn = tk.Button(self, text= "register user", command= self.register)
        self.darbaja_btn = tk.Button(self, text= "unsubscribe", command= self.dardebaja)

        self.text = tk.Label(self, text= "register use all parameters\nunsubscribe and \ndes/bloq use only keyname")

        self.bloq_btn = tk.Button(self, text= "Bloq", command= lambda: self.bloqueo(True))
        self.desbloq_btn = tk.Button(self, text= "unlock", command= lambda: self.bloqueo(False))




        #Impresion de widgets
        self.keynameentry.insert(0, "keyname user")
        self.keynameentry.grid(row= 0, column=0)
        self.nameentry.insert(0, "new name")
        self.nameentry.grid(row= 1, column= 0)
        self.phoneentry.insert(0, "new phone")
        self.phoneentry.grid(row= 1, column= 1)
        self.cuilentry.insert(0, "new cuil")
        self.cuilentry.grid(row= 1, column= 2)

        self.phone_btn.grid(row= 2, column= 1)
        self.cuil_btn.grid(row= 2, column= 2)
        self.name_btn.grid(row = 2, column= 0)

        self.daralta_btn.grid(row= 3, column= 0)
        self.darbaja_btn.grid(row= 3, column= 1)

        self.text.grid(row= 4, column= 0)

        self.bloq_btn.grid(row= 5, column= 1)
        self.desbloq_btn.grid(row= 5, column= 2)


    def modify_profile(self, parameter):
        try:
            previouscuil = self.regdeusuarios.Get_Ciudadanos()[self.keynameentry.get()][0].Get_Cuil()
            user = self.regdeusuarios.searchCitizen(cuil= previouscuil)
            if parameter == "phone":
                phone = self.phoneentry.get()
                int(phone)#lanza un error para prevenir que se lance algo que no sea un numero
                user.Mod_Telefono(phone)
            if parameter == "cuil":
                cuil = self.cuilentry.get()
                int(cuil)#lanza un error para asegurar que sea un numero
                user.Mod_CUIL(cuil)
            if parameter == "name":
                name = self.nameentry.get()
                user.Mod_Name(name)
        except ValueError:
            messagebox.showwarning(title= "Use numbers", message= "Remember to use only numbers in when chainging phone or cuil")
        except KeyError:
            messagebox.showwarning(title= "User not found", message= "The user with that key name couldnt be found")


    def register(self):
        key_name = self.keynameentry.get()
        phone = self.phoneentry.get()
        cuil = self.cuilentry.get()
        if (self.regdeusuarios.searchCitizen(int(phone)) != None) or (self.regdeusuarios.searchCitizen(cuil= int(cuil)) != None):
            messagebox.showwarning(title= "Existing account", message= "An acount with this data already exist")
        else:
            if CreateProfile.Create_Profile("user", key_name, phone, cuil, self.regdeusuarios, self.dataanses):
                self.user = self.regdeusuarios.Get_Ciudadanos()[key_name][0]

    def dardebaja(self):
        key_name = self.keynameentry.get()
        if key_name in self.regdeusuarios.Get_Ciudadanos():
            cuilciudadano = self.regdeusuarios.Get_Ciudadanos()[key_name][0].Get_Cuil()
            ciudadano = self.regdeusuarios.searchCitizen(cuil= cuilciudadano)
            self.regdeusuarios.Manage_Ciudadanos(ciudadano, False, key_name)
        else:
            messagebox.showwarning(title= "User not found", message= "A user with that keyname couldnt be found")

    def bloqueo(self, bool):
        keyname = self.keynameentry.get()
        if keyname in self.regdeusuarios.Get_Ciudadanos():
            self.regdeusuarios.estado_de_bloqueo(bool, keyname)
        else:
            messagebox.showwarning(title= "User not found", message= "A user with this key name couldnt be found")







