import re

def main():
    poem = "By my bedside comes the bright moonlight, It covers the floor like frost. Looking up I see the clear moon, Looking down I miss my dear hometown."
    sentence_list = re.split(r'[,.!;]\s?', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    main()