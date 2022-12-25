class Person(object):
    """Person"""
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
        print('%s is playing happily.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s is watching av.' % self._name)
        else:
            print('%s is only allowed to watch cartoon.' % self._name)

class Student(Person):
    """Student"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        return self._grade

    def study(self, course):
        print('%s in %s is studying %s' % (self._name, self._grade, course))

class Teacher(Person):
    """Teacher"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s %s is teaching %s.' % (self._title, self._name, course))

def main():
    stu = Student('Sean', 15, 'G10')
    stu.study('math')
    stu.watch_av()
    t = Teacher('Luo Hao', 38, 'Mr.')
    t.teach('python programming design')
    t.watch_av()

if __name__ == '__main__':
    main()