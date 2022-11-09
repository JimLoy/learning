class Pet:
    
    def eat(self,name='Pet'):
        print(f'{name} is eating...')

    
    def sleep(self):
        print('ZZzz.')


class Canino:
    def ladrar(self):
        print('Guau Guau')

class Dog(Pet,Canino):# Hereda de Pet y Canino (herencia multiple)
    def __init__(self, name):
        self.name = name
        print(f'{self.name}')
    
    def eat(self):
        super().eat(self.name) # Super() es para llamar a los metodos de los sempais


korone = Dog('Korone')
korone.ladrar()
korone.eat()
korone.sleep()