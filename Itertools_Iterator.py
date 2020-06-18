from itertools import count, cycle, repeat
# Iterable
# Checking whether list is iterable or not
list1 = [1,2,3,4,5,6,7]
print(dir(list1))  # Prints many magic methods in which there is __iter__
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
# Creating our own Iterator
class My_range:
    def __init__(self,start,end):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        else:
            current = self.value
            self.value += 1
            return current

obj1 = My_range(5,15)
print(next(obj1))  # 5
print(next(obj1))  # 6
print(next(obj1))  # 7
print(next(obj1))  # 8