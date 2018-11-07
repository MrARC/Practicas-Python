"""
Ejercicio 3:
Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca
el código de la categoría de la película y posterior a ello pide que el usuario introduzca el número
de días de atraso, y así se muestra al final el total a pagar.
"""

peliculas = {
    1: ["favoritos", "$2.50", "$0.50"],
    2: ["nuevos", "$3.00", "$0.75"],
    3: ["estrenos", "$3.50", "$1.00"],
    4: ["super estrenos", "$4.00", "$1.58"],
}

def obtener_precio(codigo: int):
    return float(peliculas.get(codigo, '$0')[1].replace('$', ''))

def obtener_recargo(codigo: int):
    return float(peliculas.get(codigo, '$0')[2].replace('$', ''))

def obtener_pelicula(codigo: int):
    return peliculas.get(codigo, ['-', '$0', '$0'])

def listar_peliculas():
    print('🎬   Peliculas   🎥'.rjust(40))
    print('Elije el código de categoría deseado para ver el precio a pagar')
    print('Categoria'.rjust(15), end='')
    print('Precio'.rjust(15), end='')
    print('Código'.rjust(15), end='')
    print('Recargo/Día de atraso'.rjust(30))
    for pelicula in peliculas:
        id_pelicula = pelicula
        pelicula = obtener_pelicula(pelicula)
        categoria = pelicula[0].capitalize()
        precio = pelicula[1]
        recargo = pelicula[2]
        print(categoria.rjust(15), end='')
        print(precio.rjust(15), end='')
        print(str(id_pelicula).rjust(15), end='')
        print(recargo.rjust(15))
while True:
    while True:
        try:
            listar_peliculas()
            codigo = int(input('» Introduce el código de la categoría de pelicula: '))
            dias_recargo = int(input('» Introduce el numero de días de atraso en la devolución: '))
            precio = obtener_precio(codigo)
            recargo = obtener_recargo(codigo)
            print(f'💲  El precio sin recargo es de: ${precio}')
            total = precio + (dias_recargo * recargo)
            print(f'💲  El total a pagar es de: ${total}')
            break
        except ValueError:
            print('Debes introducir un numero valido')
    desicion = input('Si deseas salir presiona 1, de lo contrario presiona otro num: ')
    if desicion == '1':
        print('👋   ¡Adiós!')
        break