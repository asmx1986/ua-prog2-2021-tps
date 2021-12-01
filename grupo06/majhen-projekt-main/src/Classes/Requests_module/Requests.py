from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

class Request (Command):
    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient 
    
    @abstractmethod
    def execute(self) -> None:
        pass
