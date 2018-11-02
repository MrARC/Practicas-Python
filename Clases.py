"""
Clases, usamos la declaración "class" para crear una clase
"""


class Human:
    # Atributo de clase, compartido por todas las instancias de esta clase
    species = "H. sapiens"

    # Inicializador básico, se llama cuando la clase es instanciada.
    # Los guiones bajos al inicio y al final de init denotan objetos o
    # atributos que son usados por Python pero que viven en el namespace
    # controlado por el usuario. Metodos (o objetos o atributos) como:
    # __init__, __str__, __repr__, etc. Son llamados metodos especiales
    # o a veces llamados dunder methods, no se recomienda inventar nombres
    # por nosotros mismos
    def __init__(self, name):
        # Asignar el argumento al atributo nombre
        self.name = name
        self._age = 0

    # Un metodo de la instancia, todos los metodos toman "self" como primer argumento
    def say(self, msg):
        print(f"{self.name}: {msg}")

    # Otro metodo
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    # Un metodo de clase se comparte en todas las instancias
    # Se llaman con la clase que lo llama como primer argumento
    @classmethod
    def get_species(cls):
        return cls.species

    # Los metodos estaticos se llaman sin una referencia de clase o instancia
    @staticmethod
    def grunt():
        return "*grunt*"

    # Una propiedad es como un getter, convierte el metodo age() en un atributo de solo lectura
    # No hay necesidad de escribir getters y setters en Python
    @property
    def age(self):
        return self._age

    # Permite establecer una propiedad
    @age.setter
    def age(self, age):
        self._age = age

    # Permite borrar una propiedad
    @age.deleter
    def age(self):
        del self._age


# Cuando el interprete de Python leee el código fuente ejecuta todo su código
# Esta propiedad __name__ se asegura que el bloque de código se ejecute solo cuando este modulo es el programa principal
if __name__ == "__main__":
    # crear instancia de clase
    i = Human(name="Alfonso")
    i.say("Hola")  # Alfonso: Que onda
    j = Human(name="Daniel")
    j.say("Que onda")  # Daniel: Que onda
    # i & j son instancias de Human, en otras palabras son objetos Human

    # Llamar nuestro metodo de clases
    i.say(i.get_species())
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())  # Alfonso: H. neanderthalensis
    j.say(j.get_species())  # Daniel: H. neanderthalensis

    # Llamar metodo estatico:
    print(Human.grunt())  # => *grunt*

    # establecer atributo edad en 42 años
    i.age = 42
    i.say(f"tengo {i.age} años")
    j.say(f"tengo {j.age} años")

    # borrar atributo age de la instancia
    del i.age

    i.say(f"tengo {i.age} años")  # => AttributeError
