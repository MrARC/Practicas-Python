"""
Creamos strings con "" o ''
"""

print("Hola esto es una string")

print("Yo soy otra string")

# Podemos concatenar strings usando el operador "+" o simplemente uniendolas
# con comillas dobles
print("String" + " concatenada")
print("String " "concatenada sin el +")

# Una cadena es una lista de caracteres
# Debería imprimir una H
print("Hola"[0])
print("----------------------")
msg = "Hola mundo"
# Ciclar cada letra e imprimirla
for letra in msg:
    print(letra)
print("----------------------")
# Podemos sacar la longitud de una cadena de texto con len()
print('Longitud de msg:', len(msg))

# Podemos hacer interpolación de cadenas con .format()
print('Mi nombre es {} y tengo {} años'.format('Alfonso', 20))

# Podemos repetir los argumentos para ahorrarnos escribir
print('{0} es grande, {0} es guapo, {0} es inteligente y {1} es feo'.format('Daniel', 'Aldo'))

# Podemos interpolar cadenas basandonos en keywords si es que no
# queremos contar la posición de las variables a reemplazar
print('Mi hobby favorito es {hobby1} y hoy es el día {dia}'.format(dia= 'Lunes', hobby1= 'jugar ajedrez'))

# Otra forma de interpolar (vieja, para python 2.5)
msg2 = "Mi nombre es %s y tengo %s años" % ("Alfonso", "20")
print(msg2)

nombre = "Alfonso"
print(f"Dijo que su nombre era {nombre}")
print(f"Su nombre tiene {len(nombre)} caracteres de largo")