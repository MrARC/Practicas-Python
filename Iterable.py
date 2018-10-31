"""
Un iterable es un objeto que puede ser tratado como una secuencia.
El objeto retornado por la función rango es un iterable
"""

diccionario = {
    "nombre": "Alfonso",
    "apellido": "Reyes",
    "edad": 20,
    "set": {*range(1, 6)},
}
print(f"Diccionario: {diccionario}")

# obtener keys
iterable = diccionario.keys()  # => dict_keys(["nombre", "apellido"....])

print("Keys del iterable:")
# podemos hacer loop en el iterable
for i in iterable:
    print(i, end=" ")

# comprobemos el tipo primero
print(f"\nTipo de iterable: {type(iterable)}")

# pero no podemos acceder por Index
try:
    print(iterable[0])  # => error
except TypeError as identifier:
    print("Iterable no puede accederse por index")

print("-------------------")
print("Iterador next con for:")
# El iterable es un objeto que sabe como crear un iterador
iterador = iter(iterable)
# el iterable recuerda el status conforme nos movemos en el
# obtenemos el siguiente objeto
# esta función se llama n veces el tamaño de keys, se llama next(iterador) n veces para obtener su valor
for i in range(len(diccionario.keys())):
    print(next(iterador))

print("-------------------")
print("Otra forma de iterador next:")
# otra forma:
iterador2 = iter(iterable)
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))
print(next(iterador2))

# si el iterador ha retornado toda la información, lanza un StopIteration exception
try:
    print(next(iterador2))
except StopIteration as ex:
    print('Llegaste al lim del next()')

# podemos listar los elementos del iterador con list()
print(f'Elementos iterador con list(): {list(diccionario.keys())}')