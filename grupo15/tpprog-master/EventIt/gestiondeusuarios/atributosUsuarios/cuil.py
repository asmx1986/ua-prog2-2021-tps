class Cuil:
    def __init__(self, number: str):
        if len(str(number)) > 11:
            raise ValueError("EL cuil debe tener 11 digitos")
        else:
            self.number = number

    def __str__(self):
        return str(self.number)
