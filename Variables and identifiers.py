# Variables Assignment
a = 5
b = 6
# Multiple Assignment
c, d = 7, 8
# Swapping the variables
a, b = b, a
c, d = d, c
# Deleting the variables
del a, b, c, d
# To check for valid identifier
import keyword
# The function keyword.iskeyword checks whether the given argument is python keyword or not
print(keyword.iskeyword('_var1'))   # Prints false
print(keyword.iskeyword('return'))  # Prints True

