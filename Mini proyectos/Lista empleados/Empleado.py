import datetime
import csv

class Empleado:

    entrada = datetime.datetime.now()

    def __init__(self, nombre, apellido):
            self.nombre = nombre
            self.apellido = apellido