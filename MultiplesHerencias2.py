# Crear otra definición de clase que adquiere una herencia de Superhero y Bat
from Herencia import Superhero
from MultiplesHerencias import Bat

# Definir clase Batman que adquiere herencia de superhero y Bat
class Batman(Superhero, Bat):
    def __init__(self, *args, **kwargs):
        # Normalmente para heredar los atributos tenemos que llamar super:
        # super(Batman, self).__init__(*args, **kwargs)
        # Pero estamos manejando multiples herencias, y super() solo funciona
        # con la siguiente clase base en la lista MRO (__mro__).
        # Entonces en lugar de llamar de forma explicita __init__ usamos *args y **kwargs
        # el cual nos permite pasar de forma clara los argumentos
        Superhero.__init__(
            self, "anonymous", movie=True, superpowers=["Wealthy"], *args, **kwargs
        )
        # args va primero porque can_fly pertenece a un diccionario
        Bat.__init__(self, *args, can_fly=True, **kwargs)
        # hacer override del atributo name heredado
        self.name = "Ben Affleck"

    def sing(self):
        return "na nanana nana na"


if __name__ == "__main__":
    superhero = Batman()

    # Obtener la resolución de metodos (mro) usada por getattr() y super()
    print(Batman.__mro__)  # =>
    # (<class '__main__.Batman'>,
    # <class 'Herencia.Superhero'>,
    # <class 'Clases.Human'>,
    # <class 'MultiplesHerencias.Bat'>, <class 'object'>)

    # Llamar metodo pero que usa su propio atributo de clase
    print(superhero.get_species())  # => Superman

    # Llamar metodo override de sing
    print(superhero.sing())  # => na nanana na na

    # Llamar metodo de Human, que viene a su vez de la clase Superhero
    superhero.say("Hello")  # => Ben Affleck: Hello

    # Llamar metodo de Superhero
    superhero.boast()  # > I have the powers: Wealthy

    # Llamar metodo que solo existe en la clase Bat
    print(superhero.sonar())  # => ))) ... (((

    # Cambiar atributo heredado
    superhero.age = 50
    print(superhero.age)  # => 50

    can_i_fly = "Yes" if superhero.fly else "No"
    superhero.say(f"Can i fly? {can_i_fly}")  # => Ben Affleck: Can i fly? Yes