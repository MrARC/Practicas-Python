"""
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

año_actual = input('Introduce el año en curso: ')
personas_nombres = []
personas_edades = []
for n in range(0, 3):
    personas_nombres.append(input(f'Introduce el nombre de la persona {n+1}: '))
    personas_edades.append(input(f'Introduce el año de nacimiento de {personas_nombres[n]}: '))

n = 0
for persona in personas_nombres:
    años_cumplidos = int(año_actual) - int(personas_edades[n])
    print(f'{persona} cumplira {años_cumplidos} años este año')
    n += 1