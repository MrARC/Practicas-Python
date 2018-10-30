""" Ejemplo operadores booleanos """

hambre = True
if hambre:
    print("Si tengo hambre")
else:
    print("No tengo hambre")

comida = True
apetito = hambre and comida
if apetito:
    print("Y apetito, puedo comer")
else:
    print("No tengo apetito")