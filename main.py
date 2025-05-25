from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
def animal_sound(animal):
    print(animal.make_sound())

d= Dog()
c= Cat()
animal_sound(d)
animal_sound(c)