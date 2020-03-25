"""
Creating List
"""
# A simple List
l1 = [1, 2, 3, 4]
l2 = ['a', 'b', 'c']
# List inside list
l3 = ['e', 'f', [1, 2, 3], 'g']
# Tuple inside list
l4 = [5, 6, ('x', 'y', 'z'), 7, 8]
# Dictionary inside List
l5 = ['p', 'q', {'r': 11, 's': 12}, 't']
# **********************************************************************************************************************
"""
Accessing elements of List
"""
print(l1[2])
print(l1[-2])
print(l2[1:])
print(l3[2][1])  # Prints 2
print(l4[2][0])  # Prints x
print(l5[2]['s'])  # Prints 12
# **********************************************************************************************************************
"""
Updating the List: Python List are Mutable
"""
l1[2] = 33  # Replaces 3 with 33
l3[2][1] = 22  # Replaces 2 with 22
# **********************************************************************************************************************
"""
Deleting elements from the list
"""
# Deleting the whole list
del l1
# Deleting only specific elements from the list ----1. Using element 2. Using index number of element
# Using element
l2.remove('a')
# Using Index number
del l3[1]
l3.pop(1)
# **********************************************************************************************************************
"""
Adding extra elements in the list 
"""
# Adding elements at last
l4.append(9)
# Adding elements at specific place using index number
l5.insert(1, 'qq')  # Replaced element will shift to index number 3
print(l5)
# **********************************************************************************************************************
"""
List Operations and Built-in Functions
"""
# Multiplication
print(l4 * 3)  # Prints l4 3 times
# Membership
print(5 in l4)  # Checks whether 5 is in l4 or not return either true or false
# List Comprehension
l6 = [i for i in range(1, 20) if i % 2 == 0]  # Creates list having elements from 1 to 19 that are divisible 2
# Length
print(len(l6))
# Max
print(max(l6))
# Min
print(min(l6))
# Sum: Gives the sum of elements of list
print(sum(l6))
# Sort
l7 = [3, 2, 1]
print(sorted(l7))  # Print sorted version of l7 i.e prints [1,2,3]
# List: Converts any other data type into List
l8 = list("abcde")  # Creates List as ['a', 'b', 'c', 'd', 'e']
# any(): It returns True if even one item in the Python list has a True value.
print(any(['a' in ['a', 'b'], 'b' not in [1, 2, 3]]))  # Prints True
print(any([]))  # Returns False for empty list
# all(): It returns True if all items in the list have a True value
print(all(['a' in ['a', 'b'], 'b' in [1, 2, 3]]))  # Prints false
print(all([]))  # Returns True for empty list
# Clear
l9 = [1, 2, 3, 4, 5]
l9.clear()  # It clears the whole list and makes it empty
# index()
print(l7.index(2))  # Gives the index number of 2 from l7
# count()
print(l7.count(2))  # it counts how many times the element is repeated
# reverse()
print(l7.reverse())  # returns reverse of the list l7
# **********************************************************************************************************************
"""
list map 
"""


def square(x):
    return x * x


l10 = [1, 2, 3, 4, 5, 6, 7, 8]
list_of_squares = list(map(square, l10))
print(list_of_squares)
