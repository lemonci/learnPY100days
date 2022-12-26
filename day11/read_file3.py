import time

def main():
    # read the whole file once
    with open('sonnet18.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # read the file line by line
    with open('sonnet18.txt', mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # read file line by line to a list
    with open('sonnet18.txt', encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()