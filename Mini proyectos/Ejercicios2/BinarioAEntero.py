import math

def convertir_a_entero(binario: int) -> int:
    return int(str(binario), 2)

binario = input('Introduce el num binario a convertir a decimal: ')
print(f'Conversión a decimal: {convertir_a_entero(int(binario))}')