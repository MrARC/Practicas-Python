"""
Control de flujos e iterables
"""

variable = 10  # declaramos una variable

if variable > 10:
    print("variable es mayor a 10")
elif variable < 10:  # elif sería else if
    print("variable es menor que 10")
else:  # de lo contrario
    print("variable es igual a 10")
nombre = 'Daniel'

if nombre == 'Alfonso':
    print("Tu nombre es Alfonso")
elif nombre == 'Daniel':
    print("Tu nombre es Daniel alias el sua🅱ecito")
else:
    print("No me sé tu nombre jaja salu2")
lista = [1, 4, 6, 3]
if 5 in lista:
    print("Si hay un 5 en la lista")
elif 3 in lista:
    print("Hay un 3 en lista")
else:
    print("No hay ni 5 ni 3 en la lista")