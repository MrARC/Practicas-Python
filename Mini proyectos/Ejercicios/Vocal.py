def vocal(caracter: str) -> bool:
    caracter = caracter.lower()
    return caracter in ['a', 'e', 'i', 'o', 'u']

letra = input('Checar si es vocal o no: ')
esVocal = 'Si' if vocal(letra) else 'No'
print(f'{esVocal} es vocal')