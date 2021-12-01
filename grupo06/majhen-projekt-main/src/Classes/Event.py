from abc import ABC, abstractclassmethod

from Import_index import generate_id

class Events (ABC):
    def __init__(self, zone: str, description: str) -> None:
        self.description = description
        self.zone = zone
        self.friend = False
        self.concurrency = 1
        self._id = generate_id()
        
    @abstractclassmethod
    def get_type_event_str(self) -> str:
        pass

    def add_friend(self, friend):
        self.friend = friend
        self.concurrency = 2

    def get_concurrency(self):
        return self.concurrency

    def get_description(self) -> str:
        return self.description

# Type Events

class Birthday_event (Events):
    def __init__(self, zone, description) -> None:
        super().__init__(zone, description)

    def get_type_event_str(self):
        return "Birthday"

class Concert_event (Events):
    def __init__(self, zone, description) -> None:
        super().__init__(zone, description)

    def get_type_event_str(self):
        return "Concert"

class Party_event (Events):
    def __init__(self, zone, description) -> None:
        super().__init__(zone, description)

    def get_type_event_str(self):
        return "Party"

class Event_load:
    def __init__(self, description, zone, concurrency, _id) -> None:
        self.description = description
        self.zone = zone
        self.concurrency = 1
        self._id = _id
        