"""
Ejercicio 4
Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
Muestra por pantalla en cuanto se habrá convertido el capital inicial 
transcurridos esos años si cada año se aplica la tasa de interés introducida.

Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en
C * (1 + x/100)elevado a n (años).

Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se
convierte en 24117.14 dolares al cabo de 20 años.
"""

def calcular_interes(dolares: int, tasa: int, años: int) -> int:
    interes = dolares * pow(1 + tasa/100, años)
    return interes

dolares = int(input('💵  Introduce cuantos dolarés quieres calcular: $ '))
tasa = float(input('💹  Introduce la tasa de interés: % '))
años = int(input('📅  Introduce la cantidad de años a aplicar tasa de interés: '))
print('-'*30)
print(f'💰  Dolarés con interes: {calcular_interes(dolares, tasa, años)}')