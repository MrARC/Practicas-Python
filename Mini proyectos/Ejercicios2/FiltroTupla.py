"""
Ejercicio 7
Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

tupla_edades = (21, 32, 25, 13, 17, 21, 22, 14, 12, 7, 42, 32, 10, 15, 16, 14, 12, 18)

edades_filtradas = filter(lambda edad: edad > 20, tupla_edades)

print(list(edades_filtradas))