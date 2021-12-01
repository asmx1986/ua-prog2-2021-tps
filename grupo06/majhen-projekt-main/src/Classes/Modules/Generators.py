import string
import datetime
import random
from datetime import datetime
from random import randint

# Aux functions

def get_hex_character(value):
    value = str(value)
    equivalences = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }

    if value in equivalences:
        return equivalences[value]
    else:
        return value

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""

    while decimal > 0:
        residue = decimal % 16
        true_character = get_hex_character(residue)
        hexadecimal = true_character + hexadecimal
        decimal = int(decimal / 16)

    return hexadecimal

# Generators

def generate_id() -> str:
    date = datetime.now()
    date = f"{date.minute}{date.microsecond}"
    date = decimal_to_hexadecimal(int(date))
    
    suffix = str(randint(0, 100000000) + randint(0, 100000000) + randint(0, 100000000))
    parcial_id = date + suffix

    len_parcial_id = len(parcial_id)
    id_ = parcial_id[2] + parcial_id[4] + parcial_id[7] + parcial_id[6] + parcial_id[len_parcial_id - 1] + parcial_id[len_parcial_id - 2]
    
    return id_


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
	
    ## length of password from the user
	length = int(random.randint(5, 9))

	## shuffling the characters
	random.shuffle(characters)
	
	## picking random characters from the list
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	## shuffling the resultant password
	random.shuffle(password)

	return "".join(password)