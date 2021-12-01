class Password:
    def __init__(self, pasword : str):
        if (len(pasword) < 6) and (len(pasword) > 12):
            raise ValueError("Tu contraseña debe contener entre 6 y 12 caracteres")
        else:
            self.password = pasword

    def __str__(self):
        return self.password