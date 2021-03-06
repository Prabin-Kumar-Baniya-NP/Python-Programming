"""
Functions in Python
"""


# **********************************************************************************************************************
# Example: To store Even numbers from 0 to 20 in list
def even_odd(n):
    if n % 2 == 0:
        return n
    else:
        pass


l1 = [i for i in range(0, 21)]
l2 = []
for i in range(len(l1)):
    l2.append(even_odd(l1[i]))
print(l2)
# **********************************************************************************************************************
"""
Types of Function Arguments
1. Required Argument
2. Keyword Argument
3. Default Argument
4. Variable Length Argument
"""
# **********************************************************************************************************************
"""
Required Argument
"""


def sum(x, y):
    return x + y


def min(p, q):
    if p < q:
        return p
    else:
        return q


a = 5
b = 6
print("Sum =", sum(a, b))
print("Min value =", min(a, b))
# **********************************************************************************************************************
"""
Keyword Argument
"""


def sum(x, y):
    return x + y


def minus(p, q):
    return p - q


print("Sum=", sum(x=4, y=6))
print("Difference=", minus(p=8, q=4))
# **********************************************************************************************************************
"""
Default Argument
"""


def multiply(x=6, y=8):
    return x * y


def divide(p=5, q=20):
    return q / p


print("Multiply=", multiply())
print("Divide", divide())
# **********************************************************************************************************************
""""
Variable Length Argument
"""


def unlimited(*x):
    print(x)


n = int(input("Enter how many digits from 0, you want to print"))
for i in range(n):
    unlimited(i)
# **********************************************************************************************************************
"""
Python Lambda expression: Its same like python function but it consists of only one expression (statement)
"""
sum=lambda a,b: a+b
average=lambda c,d,e: (c+d+e)/3
print("Sum of 2 and 3 is",sum(2,3))
print("Average of 5,6,7 is",average(5,6,7))
# **********************************************************************************************************************
"""
Recursive Function
"""
def factotial(n):
    if n == 1:
        return 1
    return n * factotial(n - 1)

f=factotial(4)
print(f"Factorial of 4 is {f}")
