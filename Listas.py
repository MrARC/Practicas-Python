"""
Las listas almacenan secuencias
"""

lista = [1, 2, 3, 4]

# También puede iniciar vacia
lista2 = []

print("Valores iniciales:")
print(f"Lista 1: {lista}")
print(f"Lista 2: {lista2}")

# es lista2 none?
# debería evaluar a False
print(lista2 is None)

# Podemos hacer un append a la ultima posición de la lista
lista.append(5)  # => lista1 = [1,2,3,4,5]
lista2.append(1)
lista2.append(3)
lista2.append(5)  # => lista2 = [1, 3, 5]

print(f"Lista 1: {lista}")
print(f"Lista 2: {lista2}")

# Quitamos el ultimo valor de la lista con pop()
lista.pop()  # valor ahora [1, 2, 3, 4]
lista2.pop()  # valor ahora = [1, 3]

print("Nuevos valores después de pop()")
print(f"Lista 1: {lista}")
print(f"Lista 2: {lista2}")

# Obtener ultimos elementos de las listas
print("Ultimos elementos de las listas")
print(f"Ultimo Lista 1: {lista[-1]}")
print(f"Ultimo Lista 2: {lista2[-1]}")

# Rangos con :
print(f"Rango de 0 a 3 Lista 1: {lista[0:3]}")
print(f"Rango de 0 a 1 Lista 2: {lista2[0:1]}")

# Omitir el principio, debe imrpimir 3, 4
print(f"Omitir el principio Lista 1: {lista[2:]}")
# Omitir el final, debe imprimir 1, 2, 3
print(f"Omitir el final Lista 1: {lista[:3]}")

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Lista 3: {lista3}")
# Imprimir cada segunda entrada
print(f"Imprimir cada 2da entrada: {lista3[::2]}")

lista3R = lista3[::-1]
# Reverse a una lista
print(f"Lista 3 reversed: {lista3R}")

# Primeros 3 elementos de lista reversed
print(f"Lista 3 primeros 3 elementos reversed: {lista3R[0:3]}")

# 1 layer copy
print(f"Lista 2 = {lista2}")
print(f"Lista 3 = {lista3}")
layer = lista3 = lista2[:]
print(f"1 layer copy (lista3 = lista2): {layer}")

# Remover elementos de forma arbirtraria con del
# vamos a eliminar el primer elemento de la lista1
print(f"Lista 1 sin alterar = {lista}")
del lista[0]
print(f"Lista 1 con 1er elemento eliminado = {lista}")

# Borrar primer ocurrencia con el numero 3 de lista 1
lista.remove(3)
print(f"Lista 1 con el primer 3 eliminado: {lista}")

# Añadir un elemento en un index especificado
lista.insert(0, 100)
# el primer elemento será 100
print(f"Lista 1 con 100 añadido en el index 0: {lista}")
print(f"Lista 1 + Lista 2 = {lista+lista2}")

# concatenar lista 1 con extend y sumarle lista2
print(f"Lista 2: {lista2}")
lista.extend(lista2)
print(f"Lista 1 después de concatenarle lista 2: {lista}")

# checar la existencia de 100 en la lista 1
hay100 = "Sí" if 100 in lista else "No"
print(f"Hay algún 100 en la lista? {hay100}!")

print(f"Tamaño de lista 1: {len(lista)}")