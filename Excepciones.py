"""
Manejo de excepciones con bloque try/except
"""

try:
    #raise sería el equivalente a throw
    raise IndexError("Error de index")
except IndexError as e:
    print(e)
    pass
    # se pueden manejar varias excepciones si es necesario
except(TypeError, IndexError):
    pass
else: #el else va después de los bloques except
    # se ejecuta unicamente si el código dentro del bloque de try no lanza excepciones
    print("Todo al 100")
finally:
    # se ejecuta bajo todas las circunstancias
    print("Finally")


# prueba con lista e intentando acceder a un index no disponible
lista = [2, 3, 6]
print(f"Intentando obtener index en lista {lista}")
try:
    print(lista[7])
except IndexError as e:
    print('Error IndexError con lista')
    pass
else:
    print("Si se pudo obtener el valor index")
    pass

# aquí si debe funcionar
try:
    print(lista[0])
except IndexError as e:
    print('Error IndexError con lista')
    pass
else:
    print("Si se pudo obtener el valor index")
    pass

print('Try con set...')
# ejemplo en creación de Set con elemento list (no posible, debería salir TypeError)
try:
    miSet = {[2, 5], 5, 1, 'aaa'} # esto no se puede ya que la lista es mutable    
except TypeError as typeError:
    print('Error TypeError con creación set')
    pass
else:
    pass
    print('Si se pudo crear el set')

print('Intentar con otro set...')

# aquí si debería funcionar
try:
    miSet = {6, 5, 1, 'aaa'} # esto no se puede ya que la lista es mutable    
except TypeError as typeError:
    print('Error TypeError con creación set')
    pass
else:
    pass
    print('Si se pudo crear el set')

# sin try/finally para limpiar recursos, se puede usar un statement "with"

with open('hola.txt') as txt:
    print('Imprimiendo contenido hola.txt:')
    for linea in txt:
        print(linea)