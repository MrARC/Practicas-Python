"""
Los ciclos foor iteran listas
"""

equipo = ["Alfonso Reyes", "Aldo Daniel", "Daniel Tejeda", "Maria Andrea", "Manuel"]


# estructura: for {variableCiclo} in {list}
for integrante in equipo:
    print(f'{integrante} trabaja en AURA')
print('---------------------')

# también podemos trabajar rangos
for i in range(21):
    # esto imprime del 0 al 20
    print(i, end=' ')

# esto imprime del 0 al 10
# range(start, stop)
print('\n')
for i in range(0, 11):
    print(i, end=' ')

print('\n')
print('2 en 2:')
# en los rangos podemos usar steps, el equivalente a usar el i+2 en lugar de i++
for i in range(2, 11, 2): #imprime de 2 en 2 iniciando desde el 2
    print(i, end=' ')


"""
Ciclos while de una vez, estos se ejecutan hasta que se cumpla una condicion
"""

condicion = 0
print('\nDel 1 al 10 con while')
while condicion < 10:
    condicion += 1
    print(condicion, end=' ')

condicion = 0
print('\nDel 1 al 10 con while pero de 2 en 2')
while condicion < 10:
    condicion += 2
    print(condicion, end=' ')
# ciclando lista con while y for
lista = [5, 2, 1, 5, 3]
size = len(lista)
index = 0
print(f'\nCiclar una lista: {lista} con while')
while index < size:
    print(f'{lista[index]}', end=' ')
    index += 1
# con for ahora:
print(f'\nCiclar una lista: {lista} con for')
for i in lista:
    print(f'{i}', end=' ')