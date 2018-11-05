"""
Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 
"""

def palabraMasLarga(lista: iter) -> str:
    palabraMasLarga = ""
    for palabra in lista:
        if len(palabra) > len(palabraMasLarga):
            palabraMasLarga = palabra
    return palabraMasLarga


palabras = [
    "Una palabrita",
    "Una prueba una moneda",
    "Una palabra muy largaaaaaaaaaaa",
    "Palabra cortita",
    "Otra palabrota",
]
print(f"Palabra más larga: {palabraMasLarga(palabras)}")

