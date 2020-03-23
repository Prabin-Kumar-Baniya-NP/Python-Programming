"""
Python Operators
1. Arithmetic Operator
2. Relational Operator
3. Assignment operator
4. Logical Operator
5. Bitwise Operator
6. Membership Operator
7. Identity Operator
"""
# **********************************************************************************************************************
"""
1. Arithmetic Operator: Addition, Subtraction, Multiplication, Division, Floor Division, Modulus and Exponential
"""
# Addition
print(2+3)
# Subtraction
print(4-5)
# Multiplication
print(3*4)
# Division
print(9/2)  # Prints 4.5
# Floor Division
print(9//2)  # Prints 4
# Modulus: Gives the remainder
print(9 % 2)
# Exponential
print(3**4)  # It is equivalent to 3 ^ 4

# **********************************************************************************************************************
"""
Relational operator: Less than, Greater than, equal to, not equal to, greater or equal to, less or equal to
"""
# less than
print(3 < 4)  # Prints True
# Greater than
print(4 > 3)  # Prints True
# Less than or equal to
print(7 <= 7)  # Prints True
# Greater than or equal to
print(0 >= 0)  # Prints True
# Equal to
print(3 == 3)  # Prints True
# Not Equal to
print(3 != 4)  # Prints True
# **********************************************************************************************************************
"""
Assignment Operator: assign, add and assign, multiply and assign, subtract and assign, divide and assign,
                     floor divide and assign, modulus and assign, exponential and assign                     
"""
# Assign
a=5
b=6
c=7
# Add and assign
a += 2
print(a)  # Prints 7
# Subtract and assign
b -= 2
print(b)  # Prints 4
# Multiply and assign
c *= 2
print(c)  # Prints 14
# Divide and assign
a /= 2
# Floor divide and assign
b //= 2
# Modulus and assign
c %= 3
# Exponential and assign
c **= 2
# **********************************************************************************************************************
"""
Python Logical Operator: and, or, not
"""
# and
print(2 > 3 and 5 > 3)  # Prints False
# or
print(2 > 3 or 5 > 3)   # Prints True
# not
print(not(2 > 3 and 5 > 3))  # Prints True
# **********************************************************************************************************************
"""
Python Membership Operator: in, not in
"""
l1 = [1,2,3,4,5]
l2 = ['a','b','c']
print(2 in l1)    # Prints True
print('a' in l2)  # Prints True
print(3 in l2)    # Prints False
print('b' in l1)  # Prints False
# **********************************************************************************************************************
"""
Python identity Operator: is, is not
"""
print(2 is 2)       # Prints True
print(3 is not 2)   # Prints True
