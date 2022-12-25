class Person(object):

    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing Ludo.' % self._name)
        else:
            print('%s is playing poker.' % self._name)

def main():
    person = Person('Amy', 12)
    person.play()
    person._gender = 'Female'
    # person._is_les= True
    person.play()

if __name__ == '__main__':
    main()