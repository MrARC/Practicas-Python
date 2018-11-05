"""
Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.
"""

cadena = input('Introduce la cadena a evaluar y obtener vocales: ')
cadena = cadena.lower()
vocales = "aeiou"
lista = []

for i in cadena:
    for x in vocales:
        if i == x:
            lista.append(i)

def contar_vocales(l, v):
        print(f"Hay {l.count(v)} '{v}' en la palabra '{cadena}'")

for vocal in vocales:
        contar_vocales(lista, vocal)