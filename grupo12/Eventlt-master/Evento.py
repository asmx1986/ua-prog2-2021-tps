class EventType:
    def __init__(self, titulo, description, location):
        self.titulo = titulo
        self.description = description
        self.location = location
        self.peopleQuantity = 0
        self.listOfPeople = []

    def getPeople(self):
        return self.peopleQuantity
        
    def __repr__(self):
        return self.titulo