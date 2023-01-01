# generator
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# Generate a new dictionary with stockprice over 100
prices2 = {key: value for key, value in prices.items() if value >100}
print(prices2)

# multilevel list
names = ['Alice', 'Bob', 'Cindy', 'David', 'Eddy']
courses = ['French', 'Math', 'English']
# input 3 courses result for 5 students
# WRONG: scores = [[None]*len(courses]*len(names)
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'Please input {name}\'s {course} result: '))
        print(scores)

# heap sort
import heapq
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

# itertools module
import itertools
# Generate all the permutations of ABCD
itertools.permutations('ABCD')
# Generate C 5 3 of ABCDE
itertools.combinations('ABCDE', 3)
# Generate Cartesian product of ABCD and 123
itertools.product('ABCD', '123')
# generate unlimited loop of ABC
itertools.cycle(('A', 'B', 'C'))

# collections
from collections import namedtuple, deque, Counter, OrderedDict, defaultdict
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y= 22)
p[0]+p[1]
p.x + p.y

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))

d = OrderedDict.fromkeys('abcde')
d.move_to_end('b')
''.join(d)
d.move_to_end('b', last=False)
''.join(d)

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())


