import re
def main():
    # create a re object
    # use lookbehind and lookahead to ensure there's no number ahead or behind the mobile number
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    # a better one (?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)
    sentence = '''Repeat the important issue 8130123456789 times, \
                  my mobile number is 13512346789, not 15600998765, neither 110 nor 119.
                  The mobile number of Dick is 15600998765.'''
    # Find all expression matched and save them in a list
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('---------------')
    # use an iterator to get the matched items and corresponding content
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('---------------')
    # use search funcion to specify search position and find all matched position
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

if __name__ == '__main__':
    main()