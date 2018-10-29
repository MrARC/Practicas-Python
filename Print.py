"""
Ejemplos print()
"""

print("Hola hola")

print("Hello, World", end="!")  # => Hello, World!

# Obtener input de la consola
print("")
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}!")
print("Hola {nombre}!".format(nombre=nombre))
print("Hola {0}!".format(nombre))

# Equivalente ternario
mi_dinero = 1000
# esto va a imprimir que es rico
print("Soy rico" if mi_dinero > 10000 else "Soy pobre")

