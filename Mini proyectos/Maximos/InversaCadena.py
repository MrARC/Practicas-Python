def inversa(cadena: str) -> str:
    newCadena = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        newCadena += cadena[indice]
        indice -= 1
        cont -= 1
    return newCadena
    # return cadena[::-1]

texto = input('Introduce un texto para voltearlo: ')
print(inversa(texto))