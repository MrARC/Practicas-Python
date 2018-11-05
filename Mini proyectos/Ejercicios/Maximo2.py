def max(a: int, b: int):
    if a > b:
        print('A es mayor a B')
    if b > a:
        print('B es mayor a A')
    if a == b:
        print('Ambos son iguales')

print('Introduce el num que deseas comparar')
a = input('Valor a: ')
b = input('Valor b: ')
max(a, b)