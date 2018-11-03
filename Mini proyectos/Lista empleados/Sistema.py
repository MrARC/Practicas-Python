import time
import sys
import csv
from Empleado import Empleado

class Sistema:

    # Constructor de instancia de clase
    def __init__(self):
        print("Iniciando sistema empleados")
        loading = True
        nDots = 0
        while loading:
            # ya que la salida se guarda en el buffer la información que se va a 
            # escribir se almacena antes de ser escrita a la terminal, con el parametro
            # flush podemos escribir todo lo del buffer a la terminal sin esperar
            nDots += 1
            print('.', end='', flush=True)
            time.sleep(0.02)
            if nDots >= 30:
                loading = False

    @classmethod
    def obtenerElementosMenu(self) -> list:
        return [
            "SISTEMA DE EMPLEADOS AURA 0.1",
            "/h",
            "1 - Añadir empleado",
            "2 - Listar empleados",
            "3 - Modificar empleado",
            "4 - Ver empleado",
            "0 - Salir",
            "/h",
        ]
    # Imprime el menu del sistema:
    @classmethod
    def imprimirMenu(self):
        print('\n')
        for elemento in self.obtenerElementosMenu():
            if elemento == "/h":
                print("------------------------------")
            else:
                print(f"{elemento}")
        self.getInput("Introduce la opción que deseas seleccionar: ")

    # Captura la entrada del teclado
    @classmethod
    def getInput(self, msg):
        opcion = input(msg)
        if opcion is not '':
            self.handleInput(int(opcion))

    @classmethod
    def obtenerEmpleados(self):
        with open("empleados.csv") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            next(csvReader) # saltar el header
            print('Nombre'.ljust(15), end='')
            print('Apellido'.ljust(20), end='')
            print('Puesto'.ljust(25), end='')
            print('\n')
            for row in csvReader:
                print(row[0].ljust(15) + row[1].ljust(20) + row[2].ljust(25))
                print('\n')

    @classmethod
    def añadirEmpleado(self):
        print("\nHas seleccionado añadir empleado")
        time.sleep(1)
        print("- Ahora introduce los datos del empleado -")
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        puesto = input('Puesto de trabajo: ')
        empleado = Empleado(nombre, apellido)
        print(empleado.nombre)

    @classmethod
    def handleInput(self, opcion: int):
        if opcion == 1:
            self.añadirEmpleado()
        if opcion == 2:
            self.obtenerEmpleados()
        if opcion == 0:
            exit()

# Se executa si el código es el archivo principal
if __name__ == "__main__":
    sistema = Sistema()
    menuActivo = True
    while menuActivo:
        sistema.imprimirMenu()
