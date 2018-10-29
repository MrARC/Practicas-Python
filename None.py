"""
None es un objeto, usar "is" para comparar objetos con none en lugar de "=="
"""

# Debe evaluar a True
print(None is None)

# False
print("asd" is None)

# None evalua a False
print(bool(None))
print(bool(""))
print(bool(0))
print(bool([]))  # lista
print(bool({}))  # diccionario
print(bool(()))  # tuple
