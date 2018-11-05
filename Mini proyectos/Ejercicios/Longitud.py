def obtenerLongitud(iterator: iter) -> int:
    n = 0
    for x in iterator:
        n+=1
    return n

cadena = input('Introduce la cadena a medir: ')
print(f'Longitud: {obtenerLongitud(cadena)}')