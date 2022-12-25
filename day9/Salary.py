"""
There are three types of employees in a company: manager, programmer and salesman.
We need to design a salary management system to calculate the monthly salary based on employee's information.
"""
from abc import ABCMeta, abstractmethod

class Employee(object, metaclass=ABCMeta):
    """Employee"""
    def __init__(self, name):
        """
        Initialization
        :param name: Name
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        :return: monthly salary
        """
        pass

class Manager(Employee):
    """Departmental manager"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    """Programmer"""
    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour

class Salesman(Employee):
    """Salesman"""
    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05

def main():
    emps = [
        Manager('A'), Programmer('B'),
        Manager('C'), Salesman('D'),
        Salesman('E'), Programmer('F'),
        Programmer('G')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input(('Please input the monthly working hours:')))
        elif isinstance(emp , Salesman):
            emp.sales = float(input('Please input this month sales amount of %s.' % emp.name))
        # get_salary implies poly-morphism
        print('%s\'s salary this month is $%s' %(emp.name, emp.get_salary()))

if __name__ == '__main__':
    main()