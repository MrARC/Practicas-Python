"""
Ejercicio 1
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números.
Supongamos que tenemos mas de 3 números o no sabemos cuantos números son.
Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""
def max_in_list(lista: iter) -> int:
    highest = 0
    for x in lista:
        if x > highest:
            highest = x
    return highest

lista = ([32, 2, 6, 2465, 23, 62523, 2, 46, 142])
print(f'Mayor num en lista {lista}: {max_in_list(lista)}')
    # return max(lista) => manera corta

