def main():
    try:
        with open('sonnet18.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('The file specified cannot be opened!')
    except LookupError:
        print('The index or key is not in the file!')
    except UnicodeDecodeError:
        print('The decode method is wrong!')

if __name__ == '__main__':
    main()