"""
Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""

lista_nombres = [
    "Alfonso Reyes Cortés",
    "Armando Valdez",
    "Babo",
    "Carlos",
    "Daniel Tejeda",
    "David"
    "Erick Valdez",
    "Francisco",
    "Gustavo",
    "Hector",
    "Ivan",
    "José",
    "Kevin",
    "Luis",
    "Mario",
    "Nombre",
    "Oscar",
    "Pedro",
    "Quintero",
    "Ricardo",
    "Saul",
    "Tavo",
    "Uriel",
    "Victor",
    "Ward",
    "Ximena",
    "Yvar",
    "Zasdad",
]

def buscar_con_letra(letra: str) -> int:
    n = 0
    for nombre in lista_nombres:
        if nombre[0].lower() == letra.lower():
            n += 1
    return n

letra = input('¿Qué letra quieres buscar?: ')
print(f'Hay {buscar_con_letra(letra)} nombres que empiezan con {letra}')
