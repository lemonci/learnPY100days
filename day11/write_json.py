import json

def main():
    mydict = {
        'name': 'Luo Hao',
        'age': 38,
        'qq': 957658,
        'friends': ['Wang Dachui', 'Bai Yuanfang'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 270},
            {'brand': 'Benz', 'max_speed': 320},
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('Data is saved!')

if __name__ == '__main__':
    main()