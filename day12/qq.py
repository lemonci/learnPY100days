"""Verify if the user name and qq is valid and give out the corresponding info
User name: a combination of letters, numbers and underscore, with length in 6-20 symbols
QQ: numbers with 5-12 digit, the first digit cannot be zero
"""
import re

def main():
    username = input('Please input username: ')
    qq = input('Please input QQ number: ')
    # the 1st parameter of the match function is the re string or object needed
    # the 2nd parameter of the match function is the string to be examined
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('Please input a valid username.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('Please input a valid QQ.')
    if m1 and m2:
        print('The input information is valid.')

if __name__ == '__main__':
    main()