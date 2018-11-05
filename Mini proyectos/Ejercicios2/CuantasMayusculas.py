"""
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 
"""
def cuantasMayusculas(palabra: str) -> int:
    n = 0
    for m in ['ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'][0]:
        for l in palabra:
            if m == l:
                n += 1
    return n

def cuantasMayusculas2(palabra: str) -> int:
    n = 0
    for letra in palabra:
        if letra.isupper():
            n += 1
    return n

palabra = input('Introduce la palabra para medir mayusculas: ')
mayusculas = cuantasMayusculas2(palabra)
print(f'Hay {mayusculas} mayusculas')