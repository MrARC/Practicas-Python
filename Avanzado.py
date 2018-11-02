"""
Generadores
"""

def double_numbers(iterable: iter):
    for i in iterable:
        yield i + i

# Los generadores hacen un uso eficiente de la memoria porque solo cargan los datos
# necesarios para procesar el siguiente valor en el iterable. Esto les permite realizar
# operaciones en valores de rango prohibitivos muy altos

for i in double_numbers(range(0, 900000000000000000000000)): # range es mi generador
    print(i)
    if i >= 30: # cuando llegue a 30, cortar
        break

values = (-x for x in [1, 2, 3, 4 , 5]) # generador (-1, -2, -3, -4, -5)
for x in values:
    print(x, end=' ')
print('\n')


# También podemos  hacer un cast de generador directo a una lista
values = (-x for x in [1, 2, 3, 4 , 5]) 
gen_to_list = list(values)
print(gen_to_list)