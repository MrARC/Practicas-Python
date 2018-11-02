"""
Funciones en Python

Usa "def" para crear nuevas funciones
"""


def suma(x, y):
    print(f"X es {x} y Y es {y}")
    return x + y


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


print(keyword_args(nombre="Alfonso", apellido="Reyes"))

# y ambos a la vez
def all_args(*args, **kwargs):
    print(args)
    print(kwargs)


all_args(1, 5, 3, kwarg="1", otro="23")

print("--------------")
print("Unpacking para argumentos:")
# Podemos desempacar variables en funcionesu sando * para tuples y ** para diccionarios o kwargs
tup = (66, 65, 2, 6)
dic = {"nombre": "Alfonso", "apellido": "Reyes"}

all_args(
    *tup, **dic
)  # => equivalente a all_args(66, 65, 2, 6, nombre= 'Alfonso', apellido= 'Reyes')


# retornar varios valores también es posible
def swapa(x, y):
    return y, x


tup1 = (3, 6, 1)
tup2 = (9, 2, 5)
tup1, tup2 = swapa(tup1, tup2)  # swap a las variables
print(f"tup1= {tup1}, tup2= {tup2}")  # tup1 ahora es 9,2,5 y tup2 es 3,6,1

# lo mismo para int por ejemplo
var1 = 9
var2 = 6
var1, var2 = swapa(var1, var2)
print(f"new swap: {var1}{var2}")  # debería dar 69

# scope de las funciones
x = 5


def set_x(num):
    x = num
    print(f"Valor x local scope: {x}")


def set_global_x(num):
    global x
    print(x)  # => x = 5
    x = num
    print(f"Valor nuevo x glob: {x}")


print(f"Pre valor x: {x}")
set_x(42)
set_global_x(15)
print(f"Nuevo valor x: {x}")  # debería ser 15 ahora

# first class functions
def crear_adder(x):
    def adder(y):  # solo podemos colocar uno
        return x + y

    return adder


var_adder_x = 5
print(f"Valor adder x: {var_adder_x}")
# es como crear una herencia
var_adder = crear_adder(var_adder_x)  # adder es igual a 5
# ahora es 5 +10 (x+y)
print(f"Nuevo valor adder (5+10): {var_adder(10)}")

# Tipos en funciones
def myName(nombre) -> str:
    return nombre


# Si tenemos tipos, tenemos acceso a ayuda del IDE
print(myName("Alfonso").upper())


def capitalizar(texto: str) -> str:
    newStr = ""
    for letra in texto:
        newStr += letra.upper()
    return newStr


# capitalizar una palabra:
print(capitalizar("buenas tardes"))


"""
Funciones anonimas (lambdas)
"""

# También podemos crear funciones anonimas
l1 = (lambda x: x > 2)(3)  # Evalua a true

l2 = (lambda nombre: "Hermoso" if nombre == "Daniel" else "No")(
    "Daniel"
)  # Evalua a hermoso

l3 = (lambda x, y: x + y)(4, 10)  # Evalua a 14

print(l1)
print(l2)
print(l3)

"""
Funciones de mayor orden incluidas
"""


def add_1(num: int):
    return num + 1


# add_10(3)   # => 13

print("built-in:")
# Mapeo
# retorna 2, 3, 4, cada elemento del iterable pasa a la función add_1
print(list(map(add_1, [1, 2, 3])))

# Otro ejemplo con mapeo
def capitalizarPalabra(palabra: str) -> str:
    return palabra.capitalize()


print(list(map(capitalizar, ["palabras", "sin capitalizar"])))

# Filter, toma una función como referencia y filtra aquellos parametros del iterable cuya función retorna true
# retorna aquellos que sean mayor a 0
print(list(filter(lambda n: n > 0, range(-5, 5))))

admitidos = ["suavecito", "esponjocito", "cremosito"]
# filtrar aquellos elementos que si están en la lista
# aquí solo pasaría suavecito y cremosito
print(
    list(
        filter(
            lambda elemento: elemento in admitidos,
            ["daniel", "suavecito", "cremosito", "manuel", "maria andrea"],
        )
    )
)

# aquí solo pasarían aquellos que son mayor a 100
print(list(filter(lambda n: n >= 100, [153, 100, 54, 32, 72, 56])))  # output:  153, 100

# map avanzado con adder
def create_adderFunction(x):
    def adder(y):  # solo podemos colocar uno
        return x + y

    return adder


add_1 = create_adderFunction(1)

print(list(map(add_1, [1, 2, 3, 4, 5])))  # retornaría: 2, 3, 4, 5, 6

# Podemos usar list comprehensions para maps y filtros, de esta forma la salida de la lista será dentro de ella misma

# mapeado
print([add_1(i) for i in range(0, 3)])  # => [1, 2, 3]

# filtro
print([x for x in [1, 2, 3, 4, 5] if x >= 3])  # => [3, 4, 5]

# se pueden construir sets y diccionarios también de la misma forma

# para un set:
print({x for x in range(0, 11) if x >= 5})  # => { 5, 6, 7, 8, 9, 10 }
print(
    {s for s in "abdsaqwvadrqerqdasfrcqwejkbsgnafioa" if s in "abc"}
)  # => imprime solo 3 caracteres que sea abc

# para un diccionario
print({x: "value definido" for x in range(5)})
# otro ejemplo diccionario
print({x: x ** 2 for x in range(5)})

