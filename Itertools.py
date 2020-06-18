from itertools import count, cycle, repeat
# Iterable
list1 = [1,2,3,4,5,6,7]
numbers = iter(list1)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# Itertools - count(), cycle(), repeat()
# count()
for i in count(7):
    print(i)
    if i > 14:
        break
 
''' Output
7
8
9
10
11
12
13
14
15
'''

for i in count(7,2):    # Starts from 7 and increments with interval of 2
    print(i)
    if i> 16:
        break
"""
Output:
7
9
11
13
15
17
"""

# cycle()
c = 0
for i in cycle(["red","green","yellow"]):
    c += 1
    print(i)
    if c > 10:
        break
"""
Output:
red
green
yellow
red
green
yellow
red
green
yellow
red
green
"""

# repeat()
c = 0
for i in repeat(["apple","banana","mango"]):
    print(i)
    c+=1
    if c > 10: break
"""
Output:
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
['apple', 'banana', 'mango']
"""