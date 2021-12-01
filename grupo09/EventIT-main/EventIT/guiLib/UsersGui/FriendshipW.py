import tkinter as tk
from tkinter import messagebox

from EventIT.UsersLib.RegDeUsuarios import RegDeUsuarios
from EventIT.UsersLib.CitizenClass import Ciudadano
from EventIT.FrienshipSistem.FrienshipSist import Frienship_System


class FrienshipW(tk.Tk):
    def __init__(self, reg_de_usuarios: RegDeUsuarios, user: Ciudadano):
        super().__init__()
        self.wm_title("EventIT")
        self.wm_geometry("950x400")
        self.wm_resizable(1, 1)
        self.regdeusuarios = reg_de_usuarios
        self.user = user
        self.Create_Widgets()

    def Create_Widgets(self):
        #CANVAS
        self.displayinfo = tk.Canvas(self, width=600, height=400, bg="white")
        self.displayinfo.grid(row=0, column= 3, rowspan = 20)

        self.vsb = tk.Scrollbar(self, orient= "vertical", command= self.displayinfo.yview())
        self.vsb.grid(row=0, column= 4, rowspan= 20, sticky= "ns")

        self.displayinfo.config(yscrollcommand = self.vsb.set)

        self.displayframe = tk.Frame(self.displayinfo, bg="white")
        self.displayinfo.create_window((10, 0), window= self.displayframe, anchor="nw")





        #Creacion de widgets
        self.data = tk.Entry(self)
        self.send_phone_btn = tk.Button(self, text= "send by phone", command = lambda: self.send_friendship("phone"))
        self.send_cuil_btn = tk.Button(self, text= "send by cuil", command = lambda: self.send_friendship("cuil"))
        self.send_keyname_btn = tk.Button(self, text= "send by key name", command = lambda: self.send_friendship("key"))

        self.acept_phone_btn = tk.Button(self, text= "accept by phone", command= lambda:  self.accept_friend("phone"))
        self.accept_cuil_btn = tk.Button(self, text= "accept by cuil", command= lambda:  self.accept_friend("cuil"))
        self.accept_keyname_btn = tk.Button(self, text= "accept by key name", command= lambda:  self.accept_friend("key"))

        self.seefriends_btn = tk.Button(self, text= "see list of friends", command = lambda: self.show_friends())
        self.seerequests_btn = tk.Button(self, text= "see requests", command= self.show_requests)


        #Impresion de widgets
        self.data.grid(row= 1, column= 0)
        self.data.insert(0, "phone/cuil/key name")
        self.send_phone_btn.grid(row= 2, column= 0)
        self.send_cuil_btn.grid(row= 2, column= 1)
        self.send_keyname_btn.grid(row= 2, column= 2)

        self.acept_phone_btn.grid(row= 3, column= 0)
        self.accept_cuil_btn.grid(row= 3, column= 1)
        self.accept_keyname_btn.grid(row= 3, column= 2)



        self.seefriends_btn.grid(row= 4, column=1)
        self.seerequests_btn.grid(row=5, column=1)


    def show_requests(self):
        tk.Label(self.displayframe, text= "---show---requests---").pack()
        for solicitante in self.user.Get_ListaDeSolicitudes():
            tk.Label(self.displayframe, text = f"user name: {solicitante.Get_Name()} user phone: {solicitante.Get_Telefono()}"
                                             f" user cuil {solicitante.Get_Cuil()}").pack()


    def show_friends(self):
        tk.Label(self.displayframe, text= "---show---friends----").pack()
        for friend in self.user.Get_ContactosDeInteres():
            tk.Label(self.displayframe, text = f"user name: {friend.Get_Name()} user phone: {friend.Get_Telefono()}"
                                             f" user cuil {friend.Get_Cuil()}").pack()


    def accept_friend(self, by):
        try:
            if by == "phone":
                phone = int(self.data.get())
                Frienship_System.AceptarSolicitud(self.regdeusuarios, CelSolicitante= phone,
                                                  CelDestinatario= self.user.Get_Telefono())
            if by == "cuil":
                cuil = int(self.data.get())
                Frienship_System.AceptarSolicitud(self.regdeusuarios, CuilSolicitante= cuil,
                                                  CuilDestinatario= self.user.Get_Cuil())
            if by == "key":
                keyname = self.data.get()
                Frienship_System.AceptarSolicitud(self.regdeusuarios, NameSolicitante= keyname,
                                                  NameDestinatario= self.user.Get_Name())


        except ValueError:
            messagebox.showwarning(title= "Value error", message= "if you want to look by phone or cuil, use numbers")


    def send_friendship(self, by):
        try:
            if by == "phone":
                phone = int(self.data.get())
                Frienship_System.EnviarSolicitud(self.regdeusuarios, CelSolicitante= self.user.Get_Telefono(),
                                                 CelDestinatario= phone)
            if by == "cuil":
                cuil = int(self.data.get())
                Frienship_System.EnviarSolicitud(self.regdeusuarios, CuilSolicitante= self.user.Get_Cuil(),
                                                 CuilDestinatario= cuil)
            if by == "keyname":
                keyname = self.data.get()
                Frienship_System.EnviarSolicitud(self.regdeusuarios, NameSolicitante= self.user.Get_Name(),
                                                 NameDestinatario= keyname)

        except ValueError:
            messagebox.showwarning(title= "Value error", message= "if you want to look by phone or cuil, use numbers")







if __name__ == "__main__":
    user1 = Ciudadano("jorge", 1, 1)
    user2 = Ciudadano("Emilio", 2, 2)
    user3 = Ciudadano("Roberto", 3, 3)
    user4 = Ciudadano("mariano", 4, 4)

    regdeususarios = RegDeUsuarios()

    regdeususarios.Manage_Ciudadanos(user1, True, "jorge")
    regdeususarios.Manage_Ciudadanos(user2, True, "emilio")
    regdeususarios.Manage_Ciudadanos(user3, True, "roberto")
    regdeususarios.Manage_Ciudadanos(user4, True, "mariano")



    user1.Mod_ContactosDeInteres(user2, True)
    user1.Mod_ListaDeSolicitudes(user3, True)



    FrienshipW(regdeususarios, user1).mainloop()
