"""
Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 
"""
def filtrarPalabras(palabras: iter, restriccionCaracteres: int) -> iter:
    return filter(lambda x: len(x) >= restriccionCaracteres, palabras)

# filtrar palabras que tengan una longitud mayor a 5
palabras = filtrarPalabras(['Una palabra larga', 'corta', 'hola', 'jej', 'Otra palabra larga'], 5)
print(f'Palabras más largas: {list(palabras)}')