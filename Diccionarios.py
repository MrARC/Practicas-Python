"""
Los diccionarios son mapas con key-values
"""

# declaramos los diccionarios con {}
dic1 = {}
# podemos tener predefinidos
dic2 = {"nombre": "Alfonso", "apellido": "Reyes", "edad": 20}

# las keys de los diccionarios deben de ser de tipo inmutable (int, float, string, tuples)
# una lista al ser mutable nos va a dar una excepción TypeError
dic3 = {("nombre", "apellido", "edad"): ["Alfonso", "Reyes", 20]}

# imprimir diccionario
print(dic2)
print(dic2["nombre"])
# imprimir diccionario 3
print(dic3)
print(f"Dic 3 obtener value {dic3[('nombre','apellido', 'edad')]}")

# obtener keys y values, debe hacerse un wrap con list() para listarlos
print(list(dic2.keys()))
print(list(dic2.values()))

# checar la existencia de una key en dic 2
resp = "Sip" if "nombre" in dic2 else "Nope"
print(f'Hay una key "nombre" en dic2? {resp}')

# hay que usar dic.get("key") en lugar de acceder como dic["key"]
# para evitar un KeyError
nombre = dic2.get("nombre")
apellido = dic2.get("apellido")
edad = dic2.get("edad")
# también soporta un argumento default si la entrada no esta presente
# si no esta presente la key, nos devuelve un None
altura = dic2.get("altura", "1.83m")
print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y mido {altura}")

# para insertar una key que no esta presente usamos setdefault("key", "value")
dic2.setdefault("altura", "1.83m")
# si volvemos a usar un set default el valor seguirá siendo el mismo al anteriormente
# establecido
dic2.setdefault("altura", "asdadss")
# imprimir nuestro dic2 de nuevo
print(f"Diccionario 2 nuevos valores: {dic2}")

# añadiendo valores al diccionario con update
dic2.update({"hobbys": ["ajedrez", "programación", "comer"]})
# también de la otra forma
dic2[("tuple", "jaja")] = "una value"
# imprimir nuestro dic2 de nuevo
print(f"Diccionaro 2 después de actualizar: {dic2}")

# al igual que en las listas, se remueve una key con del
del dic2[("tuple", "jaja")]
# imprimir nuestro dic2 de nuevo
print(f"Diccionaro 2 después de borrar key tuple: {dic2}")

# unpacking en diccionarios
print({"a": 1, **{"b": 2, "c": 3}})  # a:1, b:2, c:3
print({"a": 1, **{"a": 2}})  # a: 2