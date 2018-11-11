"""
Ejercicio 2
Escribe un programa que te permita jugar a una versión simplificada del juego Master Mind.
El juego consistirá en adivinar una cadena de números distintos.
Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras).
Después el programa debe ir pidiendo que intentes adivinar la cadena de números.
En cada intento, el programa informará de cuántos números han sido acertados 
(el programa considerará que se ha acertado un número si coincide el valor y la posición).
"""
# lib random
import random

def randomDigits(digits):
    lower = 10 ** (digits - 1)
    upper = 10 ** digits - 1
    return random.randint(lower, upper)

def iniciarJuego(longitud: int):
    nRandom = randomDigits(longitud)
    # definir intentos y bucle de intentos
    maxIntentos = longitud * 20
    intentos = 0 # cuantas veces se ha equivocado
    # rellenar clave maestra en vector
    claveMaestra = []
    for l in str(nRandom):
        claveMaestra.append(l)
    # llave secreta
    print(f"SECRET KEY: {nRandom}")
    print('-'*50)
    print(
        f"🧠  MASTERMIND | Vamos a iniciar un juego, es muy fácil,\ntú trataras de adivinar un numero de  🎰  {longitud} cifras."
        f"\nSi fallas {maxIntentos} veces pierdes :) te estaré dando pistas cuando te acerques al resultado."
        "\nBuena suerte 🍀"
    )
    print('-'*50)
    # ciclo de juego
    while intentos < maxIntentos:
        tryN = ""
        while True:
            try:
                tryN = int(input(f'Introduce un num ({longitud} cifras): '))
            except ValueError:
                print(f'Solo puedes introducir numeros!')
            if len(str(tryN)) < longitud or len(str(tryN)) > longitud:
                print(f'Tu respuesta debe ser de {longitud} cifras!')
            else:
                break
        tryN = str(tryN)
        adivinados = 0
        pos = 0
        for valorIntento in tryN:
            if valorIntento == claveMaestra[pos]:
                adivinados+=1
            pos+=1
        if(adivinados == longitud):
            print('\n')
            print('-'*30)
            print(f'🏆 🎉   ¡FELICIDADES!   👍  ✅')
            print(f'Has adivinado el numero correcto ({nRandom})')
            print(f'Te ha tomado {intentos} intentos!')
            print('-'*30)
            print('\n')
            break
        simbolo = '✅' if adivinados >= 1 else '🚫'
        print(f'\n{simbolo}   Has acertado {adivinados} cifras de {len(str(nRandom))}', end='')
        intentos += 1
        print(f' | 🔮   Tienes {maxIntentos-intentos} intentos\n')
    if intentos > 24:
        print('🚨\t¡HAS PERDIDO!\t💀')
while True:
    longitud = int(
        input("Introduce la longitud de la cadena a adivinar (2 a 9 cifras): ")
    )
    if longitud >= 2 and longitud <= 9:
        iniciarJuego(longitud)
        break
    else:
        print("Introduce una longitud correcta")