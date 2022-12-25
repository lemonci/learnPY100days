from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """Fighter"""
    # use __slots__ to attribute the member's variables
    __slots__ = ('_name', '_hp')
    def __init__(self, name, hp):
        """Initialize

        :param name: name
        :param hp: life value
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """Attack
        :param other: the object being attacked
        """
        pass

class Ultraman(Fighter):
    """Ultraman"""
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp, mp):
        """initialization
        :param name: Name
        :param hp: Health Points
        :param mp: Magic Points
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """Certain-kill (reduce at least 50 pts or 3/4 of other's hp)

        :param other:
        :return: if succeed, return True. False otherwise.
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        """Magic attack

        :param others: the group being attacked
        :return: if succeed, return True. False otherwise.
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        """Resume mp"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%s Ultraman~~~\n' % self._name + \
            'HP: %d\n' % self._hp + \
            'MP: %d\n' % self._mp

class Monster(Fighter):
    """Monster"""
    __slots__ = ('_name', '_hp')
    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s Monster~~~\n' % self._name + \
            'HP: %d\n' % self._hp

def is_any_alive(monsters):
    """Judge if there is any living monster"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    """Select a living monster"""
    monsters_len = len(monsters)
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    """Display the information of ultraman and monster"""
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    u = Ultraman('Decker', 1000, 120)
    m1 = Monster('A', 250)
    m2 = Monster('B', 500)
    m3 = Monster('C', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('======Round: %02d ======' % fight_round)
        m = select_alive_one(ms) # select a monster
        skill = randint(1, 10) # use randam number to select which skill
        if skill <= 6: # Probability of 60% to use normal attack
            print('%s used normal attack to hurt %s.' % (u.name, m.name))
            u.attack(m)
            print('%s restore %d mp.' % (u.name, u.resume()))
        elif skill <= 9: # 30% probability to use magic attack (may fail because of low mp)
            if u.magic_attack(ms):
                print('%s used magic attack.' % u.name)
            else:
                print('%s failed to use magic attack. ' % u.name)
        else: # 10% probability to use certain-kill (if mp not enough, normal attack)
            if u.huge_attack(m):
                print('%s use certain-kill to torture %s.' % (u.name, m.name))
            else:
                print('%s used normal attack to hurt %s.' % (u.name, m.name))
                print('%s restored mp by %d.' % (u.name, u.resume()))
        if m.alive > 0: # if the monster doesn't die, it will attack the Ultraman.
            print('%s fighted back %s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms) # display the info of Ultraman and monsters at the end of each round.
        fight_round += 1
    print('\n=======The fight is over!=======\n')
    if u.alive > 0:
        print('%s Ultraman wins!' % u.name)
    else:
        print('Monsters win!')


if __name__ == '__main__':
    main()