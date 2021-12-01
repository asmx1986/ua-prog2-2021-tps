from abc import ABC

class usuario(ABC):
    def __init__(self, name, lastName, age, CUIL):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.CUIL = CUIL
        
    def __str__(self):
        return self.name + " " + self.lastName
        
