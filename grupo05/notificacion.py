class Notification:

    def __init__(self, sender):
        self.sender = sender

    def getSender(self):
        return self.sender


class Notificacion_amistad(Notification):
    def __init__(self,sender):
        super().__init__(sender)

    def __repr__(self):
        return f"{self.sender.name} quiere ser tu amigo"


class Notificacion_Evento(Notification):
    def __init__(self,sender,event):
        super().__init__(sender)
        self.event = event

    def __repr__(self):
        return f"{self.sender.name} te comparte este evento: {self.event}"

