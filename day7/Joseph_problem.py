def josephus_problem(n=30, m=9, k=15):
    if n == 1:
        return [1]
    total = list(range(1,n+1))
    count = 1
    pointer = 0
    while len(total) > k:
        if count != m:
            count += 1
            pointer += 1
            if pointer >= len(total):
                pointer = pointer - len(total)
        else:
            print("remove", total.pop(pointer))
            count = 1
    print(total)
    return total


def main():
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('基' if person else '非', end='')

if __name__ == '__main__':
    josephus_problem()
    main()