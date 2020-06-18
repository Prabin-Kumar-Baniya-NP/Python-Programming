# Generators
def my_range(start,end):
    for i in range(start,end+1):
        yield i

g1 = my_range(10,20)
print(g1)  # <generator object my_range at 0x7f5aa043a350>
print(next(g1)) # 10
print(next(g1)) # 11
for i in my_range(100,110):
    print(i)  # Prints from 100 to 110

# Generator Expression
g_exp = (x for x in range(200,210))
for i in g_exp:
    print(i)  # Prints from 200 to 209

# Examples
# Fibonacci Series
def fib(end):
    f, s = 0, 1
    while f <= end:
        yield f
        f, s = s, f+s
my_fib1 = fib(50)
for i in my_fib1:
    print(i)
# Note :
"""
An iterator does not make use of local variables, all it needs is iterable to iterate on.
A generator may have any number of 'yield' statements.
We can implement your own iterator using a python class; a generator does not need a class in python.
"""