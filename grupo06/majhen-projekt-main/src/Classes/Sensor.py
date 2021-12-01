from abc import ABC, abstractclassmethod
from Import_index import generate_id

class Sensors (ABC):
    def __init__(self, event) -> None:
        super().__init__()
        self._id = generate_id()
        self.event = event
        self.concurrency = event.get_concurrency()

    def get_id(self):
        return self._id

    def get_actual_concurrency(self):
        return self.concurrency
    
    def update_concurrency(self, number_to_sum):
        self.concurrency += number_to_sum

    def get_event_description(self):
        return self.event.get_description()

    def get_event(self):
        return self.event

class Sensor (Sensors):
    def __init__(self, event) -> None:
        super().__init__(event)

class Sensor_load:
    def __init__(self, _id, event, concurrency) -> None:
        self._id = _id
        self.event = event
        self.concurrency = concurrency

    def get_id(self):
        return self._id

    def get_actual_concurrency(self):
        return self.concurrency
    
    def update_concurrency(self, number_to_sum):
        self.concurrency += number_to_sum

    def get_event_description(self):
        return self.event.get_description()

    def get_event(self):
        return self.event