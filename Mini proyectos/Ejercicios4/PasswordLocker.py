# pw.py - An insecure password locker program

# importar sys para funciones de sistema
import sys
import pyperclip # libreria para acceder al clipboard del usuario

PASSWORDS = {
    "email": "F7minlBDDuvMJuxESSKHFhTxFtjVB6",
    "blog": "VmALvQyKAxiVH5G8v01if1MLZF3sdt",
    "luggage": "12345",
}

if len(sys.argv) < 2:
    print('Usage: python PasswordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # primer argumento de la linea de comandos
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS.get(account, ''))
    print(f'La contraseña para {account} ha sido copiada en el portapapeles')
else:
    print(f'Cuenta no encontrada')