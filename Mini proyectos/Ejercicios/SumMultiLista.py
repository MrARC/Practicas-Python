def sumar(iterator: iter) -> int:
    suma = 0
    for x in iterator:
        suma += x
    return suma

print(sumar([2, 5, 4, 8])) # => 19