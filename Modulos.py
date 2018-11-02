"""
Modulos
"""

import math

# raíz cuadrada
print(math.sqrt(16))  # => 4.0
print(math.pow(3, 3))  # 3 elevado a la 3 => 27

"""
Podemos importar ciertos modulos unicamente con "from 'lib' import 'functions'"
"""

from math import sqrt, ceil, floor

# retornar el num más cercano a su prox entero
print(ceil(2.7))  # debería ser 3
print(floor(2.7))  # debería ser

# Podemos hacer los nombres de los modulos más cortos
import math as m

m.sqrt(16) == math.sqrt(16)  # True

# Con la función dir podemos ver que atributos y funciones están definidos en un modulo
print(dir(math))

# Los modulos son archivos python ordinarios, podemos importar uno escribiendo el nombre del archivo
import ModuloEjemplo as mEjemplo

suma = mEjemplo.sumar(5, 3) # => 8
print(f'Suma: {suma}')