import time
import sys
import csv


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
            print(".", end="", flush=True)
            time.sleep(0.02)
            if nDots >= 30:
                loading = False

    # Imprime el menu del sistema:
    @classmethod
    def imprimirMenu(self):
        self.limpiarConsola()
        print("\n")
        for elemento in self.obtenerElementosMenu():
            if elemento == "/h":
                print("-" * 30)
            else:
                print(f"{elemento}")
        self.getInput("Introduce la opción que deseas seleccionar: ")

    @classmethod
    def limpiarConsola(self):
        print("\n" * 100)

    @classmethod
    def obtenerElementosMenu(self) -> list:
        return [
            "SISTEMA DE EMPLEADOS AURA 0.1",
            "/h",
            "1 - Añadir empleado",
            "2 - Listar empleados",
            "3 - Modificar empleado",
            "4 - Eliminar empleado",
            "0 - Salir",
            "/h",
        ]

    # Captura la entrada del teclado
    @classmethod
    def getInput(self, msg):
        opcion = input(msg)
        if opcion is not "":
            try:
                self.handleInput(int(opcion))
            except ValueError:
                print("Opción no valida")
                time.sleep(2)

    @classmethod
    def handleInput(self, opcion: int):
        if opcion == 1:
            self.añadirEmpleado()
        if opcion == 2:
            self.obtenerEmpleados()
        if opcion == 3:
            self.modificarEmpleado()
        if opcion == 4:
            self.eliminarEmpleado()
        if opcion == 0:
            exit()

    @classmethod
    def obtenerEmpleados(self):
        with open("empleados.csv") as csvFile:
            csvReader = csv.reader(csvFile, delimiter=",")
            # paginador
            empleados = []
            for row in csvReader:
                empleados.append((row[0], row[1], row[2], row[3]))
            empleados = sorted(empleados, key=lambda tup: tup[0])

            def header():
                print("\n----------------------------------")
                print("Lista de empleados AURA")
                print(f"Empleados registrados: {len(empleados)}")
                print("----------------------------------")

            if len(empleados) == 0:
                print("No hay empleados añadidos")
                time.sleep(2)
            else:
                # maxima cantidad de empleados por pag = 5
                nPags = len(empleados) // 5
                nPags = 1 if nPags == 0 else nPags
                # fix por si queda algun elemento fuera de la pag
                if (len(empleados) % 5) > 0:
                    nPags += 1
                pagActual = 1

                def lista():
                    header()
                    print("Pagina: {0}/{1}".format(pagActual, nPags))
                    print("ID".ljust(5), end="")
                    print("Nombre".ljust(20), end="")
                    print("Apellido".ljust(25), end="")
                    print("Puesto".ljust(25))
                    print("-" * 30)
                    elementos = pagActual * 5
                    try:
                        for x in range(elementos - 5, elementos):
                            empleado = empleados[x]
                            nombreEmpleado = (
                                empleado[1][:15] + ".."
                                if len(empleado[1]) >= 15
                                else empleado[1]
                            )
                            apellidoEmpleado = (
                                empleado[2][:15] + ".."
                                if len(empleado[2]) >= 15
                                else empleado[2]
                            )
                            print(
                                empleado[0].ljust(5)
                                + nombreEmpleado.ljust(20)
                                + apellidoEmpleado.ljust(25)
                                + empleado[3].ljust(25)
                            )
                    except IndexError:
                        # fix temporal por si se sale del rango de la lista
                        pass
                    print("-" * 30)

                def bottom():
                    texto_indicador = ""
                    if pagActual > 1 and pagActual != nPags:
                        texto_indicador = (
                            "Pag anterior: A | Siguiente pag: S | Salir: 0"
                        )
                    elif pagActual == nPags:
                        texto_indicador = "Pag anterior: A | Salir: 0"
                    else:
                        texto_indicador = "Siguiente pag: S | Salir: 0"
                    print(texto_indicador)

                while True:
                    self.limpiarConsola()
                    lista()
                    bottom()
                    sigOpcion = input("Selecciona una opción: ")
                    if sigOpcion == "A" or sigOpcion == "a":
                        if pagActual >= 2:
                            pagActual -= 1
                        else:
                            print("Opción no permitida")
                            time.sleep(2)
                    elif sigOpcion == "S" or sigOpcion == "s":
                        if pagActual >= 1 and pagActual != nPags:
                            pagActual += 1
                        else:
                            print("Opción no permitida")
                            time.sleep(2)
                    elif sigOpcion == "0":
                        break
                    else:
                        print("Comando desconocido")
                        time.sleep(2)

    @classmethod
    def añadirEmpleado(self):
        print("\nHas seleccionado añadir empleado")
        time.sleep(1)
        print("- Ahora introduce los datos del empleado -")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        puesto = input("Puesto de trabajo: ")
        ids = []
        # obtener ids:
        with open("empleados.csv", "r") as csvFile:
            reader = csv.reader(csvFile, delimiter=",")
            for row in reader:
                ids.append(row[0])
        if len(ids) == 0:
            ids.append(0)
        # last id:
        idNuevoEmpleado = int(ids[-1]) + 1
        # abrir archivo como escribible y hacer append
        with open("empleados.csv", "a") as csvFile:
            writer = csv.writer(csvFile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            writer.writerow([idNuevoEmpleado, nombre, apellido, puesto])
            print("Empleado añadido")
            time.sleep(2)

    @classmethod
    def modificarEmpleado(self):
        print("\nHas seleccionado modificar empleado")
        time.sleep(1)
        nId = False
        while nId == False:
            print("- Ahora introduce el ID del empleado -")
            idModificar = input("ID: ")
            with open("empleados.csv") as csvFile:
                reader = csv.reader(csvFile, delimiter=",")
                listaEmpleados = list(reader)
                for row in listaEmpleados:
                    if row[0] == idModificar:
                        nId = True
                        print("\nDatos empleado a modificar:")
                        print(f"Nombre: {row[1]}")
                        print(f"Apellido: {row[2]}")
                        print(f"Puesto: {row[3]}")
                        print("-" * 30)
                        # Solicitar nuevos datos
                        nuevoNombre = input("Nuevo nombre: ")
                        nuevoApellido = input("Nuevo apellido: ")
                        nuevoPuesto = input("Nuevo puesto: ")
                        # borrar empleado viejo e insertar el nuevo
                        listaEmpleados.remove(row)
                        listaEmpleados.append(
                            [idModificar, nuevoNombre, nuevoApellido, nuevoPuesto]
                        )
                        with open("empleados.csv", "w") as csvWrite:
                            writer = csv.writer(
                                csvWrite, delimiter=",", quoting=csv.QUOTE_MINIMAL
                            )
                            for empleado in listaEmpleados:
                                writer.writerow(
                                    [empleado[0], empleado[1], empleado[2], empleado[3]]
                                )
                            print("Empleado modificado")
                            time.sleep(2)
                            break
                if nId == False:
                    print("Empleado no encontrado")

    @classmethod
    def eliminarEmpleado(self):
        print("\nHas seleccionado eliminar empleado")
        time.sleep(1)
        nId = False
        while nId == False:
            print("- Ahora introduce el ID del empleado -")
            idEliminar = input("ID: ")
            with open("empleados.csv") as csvFile:
                reader = csv.reader(csvFile, delimiter=",")
                listaEmpleados = list(reader)
                for row in listaEmpleados:
                    if row[0] == idEliminar:
                        nId = True
                        listaEmpleados.remove(row)
                if nId:
                    with open("empleados.csv", "w") as csvWrite:
                        writer = csv.writer(
                            csvWrite, delimiter=",", quoting=csv.QUOTE_MINIMAL
                        )
                        for empleado in listaEmpleados:
                            writer.writerow(
                                [empleado[0], empleado[1], empleado[2], empleado[3]]
                            )
                        print("Empleado eliminado")
                        time.sleep(2)
                        break
                else:
                    print("No se encontro este empleado")
                    time.sleep(2)


# Se executa si el código es el archivo principal
if __name__ == "__main__":
    sistema = Sistema()
    while True:
        sistema.imprimirMenu()
