from random import choice
import string
def generate_code(code_len=4):
    code = ''
    population = list(string.ascii_lowercase)
    population.extend(list(string.ascii_uppercase))
    population.extend(list(string.digits))
    for i in range(code_len):
        code += choice(population)
    return code

if __name__ == '__main__':
    generate_code()