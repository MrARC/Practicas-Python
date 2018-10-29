"""
Los tuples son como listas pero inmutables
"""

tup = (1, 2, 3, 4)
# Imprimir tuple
print(f"Tuple: {tup}")
# Debería ser 1
print(f"Primer elemento tuple: {tup[0]}")
# Sacar el tipo de la variable, debería ser class tuple
print(f"Clase: {type(tup)}")
# Debería ser 4
print(f"Longitud del tuple: {len(tup)}")
tup2 = tup + (5, 6, 7, 8)
# Debería ser (1,2,3,4,5,6,7,8)
print(f"Tuple 2: {tup2}")

# Al igual que en las listas, podemos hacer operaciones como concatenar
tup3 = (2, 52, 13)
print(f'Tuple 3: {tup3}')
tup3 = tup3 + tup
print(f'Tuple 3 + Tuple 1: {tup3}')
# imprimir un rango
print(f'Primeros 5 elementos tuple 3+1: {tup3[:5]}')
# ¿hay algún 5 en la lista? 
resp = "Sí" if 5 in tup3 else "Nop"
print(f'¿Hay algún 5 en tup 3+1? {resp}')

# ¿hay algún 2 en la lista? 
resp = "Sip" if 2 in tup3 else "Nop"
print(f'¿Hay algún 2 en tup 3+1? {resp}')

# Podemos desempaquetar tuples en variables
a, b, c = (1, 5, 3) # a = 1, b = 5, c = 3
print(f'{a}, {b}, {c}')

# Podemos hacer extended unpacking poniendo un asterisco al lado de la variable
a, *b, c = (1, 9, 4, 3, 4, 1, 7, 3) # a = 1, b = [5,2,1,8,9], c = 3
print(f'{a}, {b}, {c}')

# Los tuples igual se crean por default si no ponemos parentesis
f, g, h = 5, 2, 1
print(f'f:{f}, g:{g}, h:{h}, clase: {type(f)}')

# Cambiar posiciones de tuple es muy sencillo
f, g = g, f
print(f'f y g swap: {f}, {g}')