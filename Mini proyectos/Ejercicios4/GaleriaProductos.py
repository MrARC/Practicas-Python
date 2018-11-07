"""
Ejercicio 2
De la galería de productos, el usuario introducirá el código y el número de unidades del producto
que desea comprar. El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de 
seguir ingresando diferentes códigos de productos con sus respectivas cantidades,
y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. 
"""

productos = {
    1: ["camisa", "$300"],
    2: ["cinturón", "$120"],
    3: ["zapatos", "$800"],
    4: ["pantalón", "$500"],
    5: ["calcetines", "$80"],
    6: ["faldas", "$90"],
    7: ["gorras", "$120"],
    8: ["sueter", "$600"],
    9: ["corbata", "$150"],
    10: ["chaqueta", "$600"]
}

def obtener_precio(codigo: int):
    return int(productos.get(codigo, '$0')[1].replace('$', ''))

def obtener_producto(codigo: int):
    return productos.get(codigo, ['-', '$0'])

def listar_productos():
    print('🧦👖   Tienda de Ropa "El caballo elegante"   👔👕')
    print('Elije el producto deseado')
    print('Producto'.rjust(25), end='')
    print('Código'.rjust(15))
    for producto in productos:
        id_producto = producto
        producto = obtener_producto(producto)
        nombre = producto[0].capitalize()
        # precio = producto[1]
        print(nombre.ljust(25, '.').rjust(40), end='')
        print(str(id_producto))
while True:
    while True:
        try:
            listar_productos()
            codigo = int(input('Introduce el código del producto: '))
            precio = obtener_precio(codigo)
            print(f'💲  El precio es de: ${precio}')
            cantidad = int(input('Introduce el numero de unidades: '))
            total = cantidad * precio
            print(f'💲  El total a pagar es de: ${total}')
            break
        except ValueError:
            print('Debes introducir un numero valido')
    desicion = input('Si deseas salir presiona 1, de lo contrario presiona otro num: ')
    if desicion == '1':
        print('👋   ¡Adiós!')
        break