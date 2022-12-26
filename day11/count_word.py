corpurus = ['a', 'and', 'a', 'and']

output = {}

for word in corpurus:
    try:
        output[word] +=1
    except:
        output[word]=1