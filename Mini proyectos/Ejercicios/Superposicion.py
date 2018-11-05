def superposicion(lista1: iter, lista2: iter) -> bool:
    nComun = False
    for x in lista1:
        for y in lista2:
            if x == y:
                nComun = True
    return nComun

hayComun = "Sí" if superposicion([2, 5, 1, 5, 7], [6, 34, 89, 32, 6]) else "No"
print(f'Hay uno en comun? {hayComun}') 