from .Requests import Request
from .. import General_state

class Event_invite_friend(Request):
    def __init__(self, sender, _recipient, _event):
        self._sender = sender
        self._recipient = _recipient
        self._event = _event

    def execute(self) -> bool:
        return self._recipient.receive_event_invite(self._sender, self._event)

class Event_report (Request):
    def __init__(self, sensor):
        super().__init__(False, False)
        self._admin = self.get_admin()
        self._sensor = sensor
        
    def get_admin(self):
        return General_state.General_state.get_admins_state().get_admin()

    def execute(self):
        self._admin.load_sensor(self._sensor)