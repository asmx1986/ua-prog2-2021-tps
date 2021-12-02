from excepciones import CoordenadaInvalida

class Ubicacion:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x} , {self.y}"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def CorrectCoordenates(self):
        if -1 <= float(self.getX()) < 2 and -1 <= float(self.getY()) < 2:
            return True
        else:
            raise CoordenadaInvalida

    def isOk(self):
        try:
            float(self.x)
            float(self.y)
            if not self.CorrectCoordenates():
                raise CoordenadaInvalida
        except ValueError:
            raise ValueError

#pop = Ubicacion("a",1)
#pop.isOk()
