def fib(stop_number):
    if stop_number == 0:
        return 1
    if stop_number == 1:
        return 1
    if stop_number > 1:
        return fib(stop_number - 1) + fib(stop_number - 2)

if __name__ == '__main__':
    for i in range(20):
        print(i, ' ', fib(i))