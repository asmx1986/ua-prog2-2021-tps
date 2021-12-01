import tkinter as tk
from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.AdminClass import Administrator
from EventIT.UserManagementLib.CreateProfileClass import CreateProfile


class New_AdminW(tk.Tk):
    def __init__(self, regdeusuarios: RegDeUsuarios, admin: Administrator):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry(f"350x400+{550}+{150}")
        self.wm_resizable(0,0)
        self.admin = admin
        self.regdeusuarios = regdeusuarios
        self.Create_Widgets()


    def Create_Widgets(self):
        #creacion de widgets
        self.name_admin = tk.Entry(self)
        self.create_btn = tk.Button(self, text= "crete admin", command= self.create_admin)




        #impresion de widgets
        self.name_admin.insert(0, "name")
        self.name_admin.grid(row= 0, column= 0)
        self.create_btn.grid(row= 1, column= 0)

    def create_admin(self):
        name = self.name_admin.get()
        CreateProfile.Create_Profile_Admin(name, self.regdeusuarios)



