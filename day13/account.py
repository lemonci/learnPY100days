from time import sleep
from threading import Thread

class Account(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        # Calculate the balance after saving
        new_balance = self._balance + money
        # Simulate transaction time (0.01 secs)
        sleep(0.01)
        # Change the balance of an account
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    # Create 100 threads to deposit money to the same account
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # Wait for all deposit threads to finish
    for t in threads:
        t.join()
    print('Account balance: $%d' % account.balance)

if __name__ == '__main__':
    main()