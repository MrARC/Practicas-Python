"""
Herencias

Las herencias nos permiten definir clases hijas que adquieren los metodos y variables de la clase padre
Podemos definir una clase "child" como Superhero, la cual adquiere herencia de la clase Human y con ello
sus variables de clase y así com ometodos como "sing, grunt" de la clase Human. Pero también puede tener
sus propiedades unicas

"""

from Clases import Human


class Superhero(Human):

    # Si la clase hijo va a tomar todas las definiciones de la clase padre sin modificaciones, podemos usar
    # el atributo "pass" y nada más, pero en este caso esta comentado para permitir tener una clase hijo unica

    # pass

    # Atributo de clase
    species = "Superhuman"

    def __init__(
        self, name, movie=False, superpowers=["super strenght", "fly", "x-ray"]
    ):

        # atributos de clase adicionales
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers

        # La función "super" permite acceder a los metodos de la clase padre que son sobreescritos por la clase child
        # en este caso, el metodo __init__.
        # Super en este caso llama el constructor de la clase padre
        super().__init__(name)

    # hacemos override al metodo sing de la clase padre
    def sing(self):
        return "Dun, dun, DUN!"

    # añadimos un metodo adicional
    def boast(self):
        for power in self.superpowers:
            print(f"I have the powers: {power}")


# ejecutar esta clase solo si el programa es el modulo principal
if __name__ == "__main__":
    sup = Superhero(name="Superman")

    # checar si es instancia de humano
    if isinstance(sup, Human):
        print("I'm a human")
        # checar si es del tipo SuperHero
    if type(sup) is Superhero:
        print("I'm a superhero")

    # obtener Method Resolution Seach Order usado por getattr() y super()
    # Este atributo es dinamico y puede ser actualizado
    print(
        Superhero.__mro__
    )  # => (<class '__main__.Superhero'>, <class 'Clases.Human'>, <class 'object'>)

    # llamar metodo de clase padre pero usa su propio atributo clase
    print(sup.get_species()) # => "Superhuman"

    # llamar metodo overriden en nuestra clase superhero
    print(sup.sing()) # => "Dun, dun, DUN!"

    # Llamar metodo de humano
    sup.say('Hello')
    # Llamar metodo que solo existe en superheroe
    sup.boast() #=> saca los poderes

    # atributo heredado de la clase Human
    sup.age = 30
    sup.say(f'My age: {sup.age}') # => 30

    # Atributo que solo existe en la clase superhero
    is_elegible = "Yes" if sup.movie == True else "No"
    print(f'Am I Oscar eligible? {is_elegible}')