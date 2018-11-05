"""
Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año bisiesto.
Un año bisiesto es divisible por 4, pero no por 100.
También es divisible por 400
"""
def es_biciesto(año: int) -> bool:
    return año % 4 == 0 and año % 100 != 0 or año % 400 == 0

año = input('Introduce el año que deseas revisar si es biciesto: ')
str_biciesto = "Sí" if es_biciesto(int(año)) else "No"
print(f'{año} {str_biciesto} es un año biciesto')