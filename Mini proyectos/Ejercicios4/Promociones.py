"""
Ejercicio 1
1) Este programa pide primeramente la cantidad total de compras de una persona.
Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción.
Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, 
el programa genera de forma aleatoria un número entero del cero al cinco.
Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar
el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco,
no hay descuento, pero si es uno de los otros cuatro colores,
sí se aplicará un descuento determinado según la tabla que  aparecerá,
y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario,
de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.
"""

import random

total_compras = 0
while True:
    try:
        total_compras = int(input('💵  Introduce el total de la cantidad total de compras: $ '))
        break
    except ValueError:
        print('❌  Debes introducir un numero')

if (total_compras < 100):
    print('❌  No aplica promoción')
else:
    num_aleatorio = random.randint(0, 4)
    bolas = ['Blanca', 'Azul', 'Verde', 'Negra', 'Roja']
    recompensa = ['No tiene', '.10', '.20', '.25', '.50']
    print('Tu gasto iguala o supera los $100 por lo tanto participa en la promoción')
    print('COLOR'.rjust(30), end='')
    print('DESCUENTO'.rjust(30))
    cont = 0
    for bola in bolas:
        print(f'Bola {bola}'.rjust(30), end='')
        valDesc = ''
        if bola == 'Blanca':
            valDesc = 'No tiene'
        else:
            valDesc = f"% {recompensa[cont].replace('.', '')}"
        print(valDesc.rjust(30))
        cont += 1
    # imprimir tabla de descuentos
    print(f'🔮  Te has sacado la bola: {bolas[num_aleatorio]}')
    if bolas[num_aleatorio] == 'Blanca':
        print('❌  No aplica promoción')
    else:
        descuento = (float(recompensa[num_aleatorio]) * total_compras)
        total_conDescuento = total_compras - descuento
        print(f'💲  Descuento a aplicar: ${descuento}')
        print(f'💲  Precio final: ${total_conDescuento}')
