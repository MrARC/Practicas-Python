"""
Los sets, pues son sets 🤔
"""

set_vacio = set()

# parece un diccionario solo que carece de los ":" para key/values
un_set = {1, 2, 1, 1, 5, 4}
# imprimir el set
print(f"Set normal: {un_set}")
print(f"Tipo: {type(un_set)}")

# al igual que en un diccionario, los sets deben tener elementos inmutables (no listas)
otro_set = {"aa", 3, 42, ("tuple", "jaja")}

# imprimir el set
print(f"Set con varios elementos {otro_set}")
print(f"Tipo: {type(otro_set)}")

nuevo_set = otro_set
nuevo_set.add(9)  # debería ser ahora ["aa", 3, 42, ('tuple', 'jaja'), 9]
nuevo_set.add(9)  # los sets no tienen elementos duplicados

# intersección con &
inter_set1 = {1, 2, 3, 4, 5, 6}
inter_set2 = {5, 6, 7, 8}
# imprimir intersección, debería ser 5 y 6
print(f"Intersección de set1 y 2: {inter_set1 & inter_set2}")
# hacer unión de sets:
inter_union = inter_set1 | inter_set2
# debería ser: 1, 2, 3, 4, 5, 6, 7, 8
# aquellos elementos repetidos no se añaden 🧐
print(f"Set 1 y 2 unidos: {inter_union}")

# diferencia con "-"
print("diferencia sets {1, 2, 3, 4} - {2, 3, 5}")
print({1, 2, 3, 4} - {2, 3, 5})  # => {1, 4}

# diferencia simetrica con simbolo potencia ^
set_1 = {1, 5, 2, 6}
set_2 = {1, 7, 2, 9}
print("dif simetrica set_1({1, 5, 2, 6}) y set_2({1, 7, 2, 9})")
print(set_1 ^ set_2)  # debería imprimir {5, 6, 7, 9}

# Checar si el set en la izq es un super set de la derecha
print(
    {1, 2} >= {1, 2, 3}
)  # => False (si alteramos el simbolo, si da True ya que {1, 2} se derivan de {1,2,3} y sería un subset)

# Checar si el set en la izq es un super set de la derecha
# aquí ya sería True
print({1, 2, 3, 4} >= {1, 2, 3})  # => True

# Checar si set en la iz es un sub set de la izq
print({1, 3} <= {1, 2, 3})  # => True
print({2, 1} <= {1, 2, 3})  # => True
print({2, 5} <= {1, 2, 3})  # => False

# Borramos elementos del set con remove()
set_del = {1, 22, 3, 64,  6, 32, 15}
print(f'Set_del: {set_del}')
set_del.remove(6)
print(f'Set_del con 6 borrado: {set_del}')

# checar la existencia de un elemento
resp = "Sip" if 33 in set_del else "Nope"
print(f'Hay algún 22 en set_del? ({set_del}): {resp}')
