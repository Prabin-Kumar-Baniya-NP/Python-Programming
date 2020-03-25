"""
Creating Tuples
"""
a=(1,2,3,4,5,6)       # It is tuple
a1=1,2,3,4,5,6        # It is also tuple
a2=(1)                # It belongs to class 'int'
b=('a','b','c','d')   # It is also tuple
# List inside tuple
c=(1,2,3,[4,5,6],7,8)
# Dictionary inside tuple
d=(11,12,13,{'a':14,'b':15},16,17)
# **********************************************************************************************************************
"""
Accessing The elements of Tuple
"""
print(a)
print(a[1])
print(a[:3])
print(a1[3:])
print(a1[-1])
# **********************************************************************************************************************
"""
Deleting tuples
"""
# Deleting the entire tuple
del a1
# Since Tuples are immutable so we cannot delete its elements
del c[3][0]   # But if any elements in tuple are mutable then we can delete and reassign the elements in it.
# **********************************************************************************************************************
"""
Adding Elements in tuple:
Since Tuples are immutable, so we cannot add elements in tuple
"""
# **********************************************************************************************************************
"""
Reassigning Values in the Tuple
"""
# We cant reassign values in tuple but if tuple contain any mutable object then we can reassign its values
c[3][1] = 2
# **********************************************************************************************************************
"""
Tuple Operations and Built-in Functions
"""
# len()
print(len(a))
# Max()
print(max(a))
# Min()
print(min(a))
# sum()
print(sum(a))
# any(): It returns True if even one item in the Python tuple has a True value.
print(any(('a' in ['a', 'b'], 'b' not in [1, 2, 3])))  # Prints True
print(any(()))  # Returns False for empty tuple
# all(): It returns True if all items in the tuple have a True value
print(all(('a' in ['a', 'b'], 'b' in [1, 2, 3])))  # Prints false
print(all(()))  # Returns True for empty tuple
# index()
print(a.index(2))  # Gives the index number of 2
# count()
print(a.count(2))  # it counts how many times the element is repeated
# Sort
a11 = (3, 2, 1)
print(sorted(a11))  # Print sorted version of a11 i.e prints [1,2,3]
# Tuple
a111=tuple("abcde")
print(a111)  # Prints Tuple having elements ('a', 'b', 'c', 'd', 'e')
# Concatenation
print((1,2,3)+(4,5,6))




