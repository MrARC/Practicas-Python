def inversa(cadena: str) -> str:
    cadena = cadena.lower()
    cadena = cadena.replace(' ', '')
    return cadena[::-1]

def esPalindromo(palindromo: str) -> bool:
    palindromo = palindromo.lower()
    palindromo = palindromo.replace(' ', '')
    return inversa(palindromo) == palindromo

palabra = input('Introduce la palabra para ver si es palindromo: ')
if esPalindromo(palabra):
    print('Si es palindromo')
else:
    print('No es palindromo')