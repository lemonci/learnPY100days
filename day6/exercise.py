def gcd(num1: int, num2: int):
    cd = 1
    upperBound = max(num1, num2)
    for i in range(1, upperBound):
        if num1 % i == 0 and num2 % i == 0:
            cd = i
    return cd

def lcm(num1: int, num2: int):
    addition = max(num1, num2)
    lcm = max(num1, num2)
    while lcm % num1 != 0 or lcm % num2 != 0:
        lcm = lcm + addition
    return lcm

def is_palindrome(num):
    numStr = str(num)
    numOfDigit = len(str(num))
    while len(numStr) > 1:
        if numStr[0] != numStr[-1]:
            return False
        else:
            numStr = numStr[1:-1]
    return True

def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)