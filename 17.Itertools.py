"""
Python IterTools
count, cycle and repeat
"""
from itertools import count,cycle,repeat

for i in count(10):
    if i==15: break
    print(i)              # Prints 10,11,12,13,14

lst=[1,2,3,4]
a=0
for i in cycle(lst):
    a+=1
    if a==20: break
    print(i)               # Prints 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 each in new line until a=20


lst1=[1,2,3,4,5]
for i in repeat(lst1,6):   # lst1 as object and 6 is the number of times object is repeated
    print(i)


# ***********************************************************************************************************************
a = iter([1, 2, 3])  # Creating our own iterator
print(next(a))  # Prints 1
print(next(a))  # Prints 2
print(next(a))  # Prints 3
# print(next(a))  # Gives error if written this line
even = iter((2, 4, 6, 8, 10))
print(next(even))  # Prints 2
print(next(even))  # Prints 4
