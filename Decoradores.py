"""
@Decoradores
"""

from functools import wraps

# Los decoradores nos permiten interceptar los parametros y modificarlos

def carnita_asada(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, carnita_asada = target_function(*args, **kwargs)
        if carnita_asada:
            return f'{msg} Si se va a hacer la carnita asada'
        else:
            return f'{msg} No se hará la carnita asada'
        return msg
    return wrapper

@carnita_asada
def say(carnita_asada=False):
    msg = 'Se hará la carnita asada?'
    return msg, carnita_asada

print(say()) # Se hará la carnita asada? No se hará la carnita asada
print(say(carnita_asada=True)) # Se hará la carnita asada? Si se va a hacer la carnita asada