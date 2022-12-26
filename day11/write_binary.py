def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('jiduo.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('The specified file cannot be opened.')
    except IOError as e:
        print('Error happened when read and write files.')
    print('Execution finished.')

if __name__ == '__main__':
    main()