def isprime(input_num: int):
    if input_num in [2,3]:
        return True
    is_p = False
    for i in range(2, int(input_num/2)+1):
        if input_num % i == 0:
            is_p = False
#            print(i, is_p)
            break
        else:
            is_p = True
    return is_p

def find_primenumber(input_num: int):
    for i in range(1, input_num):
        if isprime(i) == False:
            print("%d is not a prime number" % i)
            continue
        else:
            print("%d is a prime number" % i)

if __name__ == '__main__':
    find_primenumber(100)