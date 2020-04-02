"""
Python Numbers: int, float, complex
"""
# **********************************************************************************************************************
"""
int- type, isinstance, exponential
"""
a = 5
print(a)  # Prints 5
print(type(a))  # Prints <class 'int'>
print(isinstance(a, bool))  # Checks whether belongs to class bool or not - Prints False
print(isinstance(a, int))  # Prints True because a belongs to class int
print(2e9)  # Prints 2000000000.0        i.e 2 x 10^9
# **********************************************************************************************************************
"""
float- type, isinstance, 
"""
b = 3.4
c = 1.1111111111111111119
d = 20 / 2
e = 19 / 3
print(type(b))
print(c)  # A float value is only accurate up to 15 decimal places. After that, it rounds the number off
print(d)  # Prints 10.0
print(e)  # Prints 6.333333333333333
# **********************************************************************************************************************
"""
Complex Numbers
"""
f = 2 + 1j
g = 4 + 5j
print(f + g)
# **********************************************************************************************************************
"""
Writing numbers in binary, octal, and hexadecimal
"""
print(0b111)  # Binary
print(0B111)  # Binary
print(0o10)  # Octal
print(0O10)  # Octal
print(0XFF)  # Hexadecimal
print(0xFE)  # Hexadecimal
# **********************************************************************************************************************
"""
Conversion Functions
"""
print(int(7.7))  # Converts Float into int
print(int(0b10))  # Converts binary into decimal
print(int(0xF))  # Converts hexadecimal into decimal
print(float(7))
print(complex(2))
print(bin(2))
print(oct(8))
print(hex(255))
# Interesting question
print((1.1 + 2.2) == 3.3)  # Prints false because its not 3.3 but its 3.3000000000000003
# **********************************************************************************************************************
"""
Maths Module
"""
import math  # Should be written at the top

print(math.factorial(5))
print(math.exp(4))
