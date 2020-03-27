"""
Sets
"""
# Creating Sets
a = {1, 2, 3, 4, 5}
b = {5, 4, 3, 2, 1}
print(a)  # Prints {1, 2, 3, 4, 5}
print(b)  # Prints {1, 2, 3, 4, 5}
# No Duplicate Entries can be added to set
c = {3, 3, 2, 1, 0}
print(c)  # Prints {0, 1, 2, 3}
# We cannot add list, tuple or dictionary in Set
d = set()
e = {}
print(type(d))  # Prints <class 'set'>
print(type(e))  # Prints <class 'dictionary'>
# **********************************************************************************************************************
"""
Accessing set
"""
print(a)
# We cannot access dictionary by index number. Because no any item is associated to specific index number
# **********************************************************************************************************************
"""
Deleting set and its elements
"""
del a
b.discard(1)
b.remove(2)
# Difference between discard and remove is: if the element is not found discard don't give error message but remove give
b.pop()  # Removes an arbitrary element
b.clear()
# **********************************************************************************************************************
"""
Updating elements in the set
"""
# add()
b.add(1)
b.add(4)
b.add(3)
b.add(2)
print(b)  # Prints {1, 2, 3, 4}
# update()
c.update([4, 5], {6, 7, 8}, (9, 10))
print(c)  # Prints {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# We cannot add list, tuple and dictionary in set but we can form set from list, tuple and dictionary using this method.
"""
Functions in Set
"""
s1 = {4, 5, 2, 3, 1, 6}
s2 = {"Friday", "Sunday", "Saturday", "Wednesday", "Monday", "Thursday", "Tuesday"}
# len
print(len(s1))
# max
print(max(s1))
print(max(s2))  # Prints Wednesday
# The Python function returned ‘Wednesday’ because W has the highest ASCII value among M, T, W, F, and S.
# min()
print(min(s1))
print(min(s2))  # Prints Friday
# sun()
print(sum(s1))
# any()
print(any({0, '0'}))  # Prints True
# all()
print(all({0, '0'}))  # Prints False
# sorted()
print(sorted(s1))
# **********************************************************************************************************************
"""
Methods in Set
"""

# union()
# First Method:
print(s1 | s2)
# Second Method:
print(s1.union(s2))
# intersection()
# First method:
print(s1 & s2)
# Second Method:
print(s1.intersection(s2))
# difference: The difference() method returns the difference of two or more sets. It returns as a set.
print(s1 - s2)
print(s1.difference(s2))
# symmetric difference: This method returns all the items that are unique to each set.
print(s1.symmetric_difference(s2))
# intersection_update: The result of intersection is updated to given set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.intersection_update(s2)
print(s1)  # Prints {3}
# difference_update: The result of difference is updated to given set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.difference_update(s2)
print(s1)  # Prints {1, 2}
# Symmetric_difference_update: The result of symmetric_difference is updated to given set
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.symmetric_difference_update(s2)
print(s1)  # Prints {1, 2, 4, 5}
# copy
s1 = s2.copy()
# isdisjoint(): This method returns True if two sets have a null intersection. However, it can take only one argument.
print({1, 3, 2}.isdisjoint({4, 5, 6}))
# issubset()
print({1, 2}.issubset({1, 2, 3}))  # Prints True because {1,2} is a proper subset of {1,2,3}
print({1, 2}.issubset({1, 2}))  # Prints True because {1,2} is an improper subset of {1,2}.
# issuperset(): this one returns True if the set contains the set in the argument.
print({1, 3, 4}.issuperset({1, 2}))  # Prints False because {1,2} is not present in {1,3,4}
print({1, 3, 4}.issuperset({1}))  # Prints True because {1} is present in {1,3,4}
# **********************************************************************************************************************
"""
Operations on Set
"""
# Membership:
print('p' in {'a', 'p', 'p', 'l', 'e'})
