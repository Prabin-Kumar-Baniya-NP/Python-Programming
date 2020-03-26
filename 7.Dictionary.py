"""
Creating Dictionary
"""
# A simple Dictionary
d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
d2 = {'aa': 11, 12: 'bb', 13: 'cc', 'dd': 14}
# Empty Dictionary
empty_dict = {}
# Dictionary Comprehension
d3 = {x: x * x for x in range(20)}  # Squares of number from 0 to 19  ex: 2:4,3:9,4:16
d4 = {x: x * x * x for x in range(20) if x % 2 == 0}  # Cubes of Even Number from 0 to 19  ex: 2:8, 4:64
# Using dict function
d5 = dict([[1, 2], [3, 4], [5, 6], [7, 8]])  # Creating Dictionary from list
d6 = dict(([1, 1], [2, 4], [3, 9]))  # Creating Dictionary from Tuple
# Nested Dictionary
nested={1:'x',2:'y',3:{'a':1,'e':2,'i':3,'o':4,'u':5},4:'z'}
# **********************************************************************************************************************
"""
Accessing Items of dictionary: Can be done using key value
"""
print(d1)
print(d1[1])
print(d2['aa'])
print(d3.get(4))
print(nested[3]['a'])
# **********************************************************************************************************************
"""
Updating Values of Dictionary
"""
# Reassigning Values in Dictionary: However, if the key doesn’t already exist in the dictionary, then it adds a new one.
d1[1] = 'a1'
d2['aa'] = 111
# Adding extra key-value pairs in Dictionary
d1[5] = 'e'
d1[6] = 'f'
empty_dict[1] = 'aeiou'
# **********************************************************************************************************************
"""
Deleting the items of the dictionary
"""
del empty_dict  # Deleting entire dictionary
del d1[5]  # Deleting the specific item of the dictionary
# **********************************************************************************************************************
"""
In-Built Functions of Dictionary
"""
# len()
print(len(d1))
# any()
print(any({False: False, '': ''}))  # Prints False
print(any({False: False, 'a': 1}))  # Prints True
# all()
print(all({False: False, '': ''}))  # Prints False
print(all({False: False, 'a': 1}))  # Prints False
# Sorted()
d7 = {3: 'a', 2: 'b', 1: 'c'}
d8 = {'c': 3, 'b': 2, 'a': 1}
print(sorted(d7))  # Prints [1,2,3]
print(sorted(d8))  # Prints ['a','b','c']
print(type(sorted(d7)))  # Prints class 'list'
# **********************************************************************************************************************
"""
In-Built methods for Python Dictionary
"""
# Keys()- It returns the keys of the entire dictionary
print(d1.keys())    # Prints dict_keys([1, 2, 3, 4, 6])
# Value()- It returns the values of entire dictionary
print(d1.values())  # Prints dict_values(['a1', 'b', 'c', 'd', 'f'])
# items()- It returns the list of key-value pairs
print(d1.items())   # Prints dict_items([(1, 'a1'), (2, 'b'), (3, 'c'), (4, 'd'), (6, 'f')])
# get()- It takes one to two arguments.
# While the first is the key to search for, the second is the value to return if the key isn’t found.
# The default value for this second argument is None.
print(d1.get(1,0))  # Prints a1
print(d1.get(5,0))  # Returns 0 since there is not any key 5
# clear(): It clears the entire dictionary
d7.clear()
d8.clear()
# copy()- It copies the dictionary
new_dict=d1.copy()
# pop()- This method is used to remove and display an item from the dictionary. It takes one to two arguments.
# The first is the key to be deleted, while the second is the value that’s returned if the key isn’t found.
d7={1:'a',2:'b',3:'c',4:'d'}
d7.pop(1)
d7.pop(2,0)
print(d7.pop(3,0))
# Update()-The update() method takes another dictionary as an argument.
# Then it updates the dictionary to hold values from the other dictionary that it doesn’t already.
dict1 = {1: 1, 2: 2}
dict2 = {2: 2, 3: 3}
dict1.update(dict2)
print(dict1)  # Prints {1: 1, 2: 2, 3: 3}
# **********************************************************************************************************************
"""
Python Dictionary Opeartions
"""
# Membership
print(1 in dict1)  # Prints True
print(3 not in dict1)  # Prints True
