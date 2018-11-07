"""
Ejercicio 3
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman
"""

def riman(palabra1: str, palabra2: str) -> bool:
    if len(palabra1) < 3 or len(palabra2) < 3:
        print('Palabra muy corta')
    else:
        if palabra1[-3:] == palabra2[-3:]:
            print('Si riman')
        elif palabra1[-2:] == palabra2[-2:]:
            print('Riman un poco')
        else:
            print('No riman')

palabra1 = input('Introduce la palabra 1: ')
palabra2 = input('Introduce la palabra 2: ')
riman(palabra1, palabra2)