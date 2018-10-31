"""
Funciones en Python

Usa "def" para crear nuevas funciones
"""

def suma(x, y):
    print(f'X es {x} y Y es {y}')
    return x+y

# llamar función
print(suma(9, 5))

# también se puede llamar de esta forma con argumentos keywords
# pueden llegar en cualquier orden
print(suma(y=8, x=10))


# Podemos crear funciones que toman un numero variable de argumentos
def varargs(*args):
    return args

print(varargs(1, 2, 3))

# Podemos definir variables que toman un num variable de argumentos keyword
def keyword_args(**kwargs):
    return kwargs

print(keyword_args(nombre= 'Alfonso', apellido='Reyes'))

# y ambos a la vez
def all_args(*args, **kwargs):
    print(args)
    print(kwargs)

all_args(1, 5, 3, kwarg= '1', otro='23')

print('--------------')
print('Unpacking para argumentos:')
# Podemos desempacar variables en funcionesu sando * para tuples y ** para diccionarios o kwargs
tup = (66, 65, 2, 6)
dic = {'nombre': 'Alfonso', 'apellido': 'Reyes'}

all_args(*tup, **dic) # => equivalente a all_args(66, 65, 2, 6, nombre= 'Alfonso', apellido= 'Reyes')


# retornar varios valores también es posible
def swapa(x, y):
    return y,x

tup1= (3, 6, 1)
tup2 = (9, 2, 5)
tup1, tup2 = swapa(tup1, tup2) #swap a las variables
print(f'tup1= {tup1}, tup2= {tup2}') #tup1 ahora es 9,2,5 y tup2 es 3,6,1

# lo mismo para int por ejemplo
var1 = 9
var2 = 6
var1, var2 = swapa(var1, var2)
print(f'new swap: {var1}{var2}') # debería dar 69