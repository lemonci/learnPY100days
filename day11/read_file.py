def main():
    f = None
    try:
        f = open('sonnet18.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('Cannot open the file specified!')
    except LookupError:
        print('The index or key is not in the file!')
    except UnicodeDecodeError:
        print('The decode method is wrong!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()