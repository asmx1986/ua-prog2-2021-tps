from .Requests import Request

class Friend_request(Request):
    def __init__(self, sender, recipient):
        super().__init__(sender, recipient)
        
    def execute(self):
        if self.recipient.exists_citizen_blocked(self.sender.get_cuil()):
            # Presenter ?  ¿Va acá o va en citizen?
            print("Usted no puede mandar la solicitud de amistad ya que actualmente se encuentra bloqueado para el usuario: " + self.recipient.name + " " + self.recipient.last_name)
            #
            return "citizen_blocked" 
            
        if self.recipient.exists_friend(self.sender.get_cuil()):
            # Presenter ? ¿Va acá o va en citizen?
            print("Usted ya es amigo del usuario " + self.recipient.name + " " + self.recipient.last_name)
            #

            return "are_already_friends"

        if self.recipient.get_cuil() == self.sender.get_cuil():
            print("No puede enviarse solicitudes de amistad a usted mismo")

            return "same_user_error"
        else:
            return self.recipient.receive_friend_request(self.sender) 