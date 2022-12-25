from abc import  ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    """Pet"""
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """vocalization"""
        pass

class Dog(Pet):
    """Dog"""
    def make_voice(self):
        print('%s: arf, arf, arf...' % self._nickname)

class Cat(Pet):
    """Cat"""
    def make_voice(self):
        print('%s: meow..meow..meow...' % self._nickname)

def main():
    pets = [Dog("Munchkin"), Cat("Java"), Dog('Drill')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()