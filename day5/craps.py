# This is a sample Python script.

from random import randint

def craps():
    money = 1000
    while money > 0:
        print('your total asset:', money)
        needs_go_on = False
        while True:
            debt = int(input('place a bet: '))
            if 0 < debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('Player got %d point' % first)
        if first == 7 or first == 11:
            print('You win!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('Bank wins!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('Player got %d point' % current)
            if current == 7:
                print('Bank wins!')
                money -= debt
            elif current == first:
                print('You win!')
                money += debt
            else:
                needs_go_on = True
    print('You are broken! Game over!')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    craps()
