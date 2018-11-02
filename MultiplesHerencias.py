"""
Multiples herencias en Python, esta clase se usa en MultiplesHerencias2
"""

class Bat:

    species='Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly
    
    def say(self, msg):
        msg = '... ... ...'
        return msg
    
    def sonar(self):
        return '))) ... ((('
    
    # executar solo si es la clase principal
if __name__ == '__main__':
    bat = Bat()
    print(bat.say('Hello'))
    print(bat.fly)