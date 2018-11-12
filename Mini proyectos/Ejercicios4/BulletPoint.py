"""
Este programa copia el portapapeles y añade un "*" a cada linea de texto para
usarlo en una wiki
https://automatetheboringstuff.com/chapter6/
"""

# librería pyperclip para obtener el copiapapeles del sistema
import pyperclip
import sys

texto = pyperclip.paste()
if texto is None:
    print('Debe haber algo en el portapapeles!')
    sys.exit() # salir del interprete
# separar frases por salto de linea
lineas = texto.split('\n')
for i in range(len(lineas)):
    # añadir el bullet al inicio de cada palabra
    lineas[i] = "* " + lineas[i]
texto = '\n'.join(lineas)
pyperclip.copy(texto)
print('Listo!')