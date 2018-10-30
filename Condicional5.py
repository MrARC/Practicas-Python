"""
Is checa si los tipos pertenecen al mismo tipo de objeto, pero "==" checa si
tienen el mismo valor
"""

# creamos una lista
a = [1, 2, 3, 4]
b = a
c = 4
d = 7

# Debe evaluar a True, ya que a y b pertenecen al mismo tipo
print(a is b)
# False
print(b is c)

# Apuntar B a una nueva lista
b = [1, 2, 3, 4]

# Ahora b no apunta al mismo objeto que a, debe ser False
print(b is a)