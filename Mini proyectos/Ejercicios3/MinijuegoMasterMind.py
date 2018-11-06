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
    print(f"SECRET KEY: {nRandom}")
    print('-'*50)
    print(
        f"🧠  MASTERMIND | Vamos a iniciar un juego, es muy fácil,\ntú trataras de adivinar un numero de  🎰  {longitud} cifras."
        "\nSi fallas 25 veces pierdes :) te estaré dando pistas cuando te acerques al resultado."
        "\nBuena suerte 🍀"
    )
    print('-'*50)
    # definir intentos y bucle de intentos
    intentos = 0
    # rellenar clave maestra en vector
    claveMaestra = []
    for l in str(nRandom):
        claveMaestra.append(l)
    # primer intento
    while intentos <= 25:
        tryN = int(input(f'Introduce un num ({longitud} cifras): '))
        tryN = str(tryN)
        adivinados = 0
        pos = 0
        for valorIntento in tryN:
            for valorReal in claveMaestra:
                if valorIntento == valorReal:
                    adivinados+=1
                pos += 1
        print(f'\n✅   Has acertado {adivinados} cifras', end='')
        intentos += 1
        print(f'| 🔮   Tienes {25-intentos} intentos\n')
    if intentos > 25:
        print('🚨 ¡HAS PERDIDO! 💀')
while True:
    longitud = int(
        input("Introduce la longitud de la cadena a adivinar (2 a 9 cifras): ")
    )
    if longitud >= 2 and longitud <= 9:
        iniciarJuego(longitud)
        break
    else:
        print("Introduce una longitud correcta")