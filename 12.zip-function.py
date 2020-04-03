"""
zip function in python
zip() is a built-in Python function that gives us an iterator of tuples
"""
# Example 1
z=zip([1,2,3],['a','b','c','d'],['!','#','$','%'])
a,b,c=zip(*z)
print(a)  # Prints (1, 2, 3)
print(b)  # Prints ('a', 'b', 'c')
print(c)  # Prints ('!', '#', '$')
# Example 2
for i in zip([11,22,33],['aa','bb','cc']):
    print(i)
# Prints
# (11, 'aa')
# (22, 'bb')
# (33, 'cc')
