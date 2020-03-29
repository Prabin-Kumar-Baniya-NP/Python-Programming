"""
Declaring String
"""
a = "he said something"
b = "to her"
city = "America"
d = "her"
# **********************************************************************************************************************
"""
Accessing String
"""
print(a)
print(a[0])
print(a[2:4])
print(a[-1])
print(a[-3:-1])
print(a + b)  # Concatenation of string
print("He took", d, "to", city, "to spend the summer holidays")
# **********************************************************************************************************************
"""
String Formatter
"""
# f-string
print(f"He took {d} to {city} to spend the summer holidays")
# format
print(
    "He took {0} to {1} to spend the summer holidays. Once again -He took {2} to {3} to spend the summer holidays".format(
        d, city, d, city))
# %-operator
print("He took %s to %s to spend summer holidays" % (d, city))
# **********************************************************************************************************************
"""
Python String Functions
"""
# len
print(len(a))
# str- This function converts any data type into a string.
print(str(2 + 3j))
# lower() and upper()- These methods return the string in lowercase and uppercase, respectively.
print(a.lower())
print(a.upper())
# strip- It removes whitespaces from the beginning and end of the string.
x = "  book"
print(x.strip())
# isdigit()- Returns True if all characters in a string are digits.
print(a.isdigit())
# isalpha()- Returns True if all characters in a string are characters from an alphabet.
print(a.isalpha())
# startswith(): It takes a string as an argument, and returns True is the string it is applied on begins with the string in the argument.
print(a.startswith("h"))  # Prints True
print(a.startswith("H"))  # Prints False
# endswith(): It takes a string as an argument, and returns True if the string it is applied on ends with the string in the argument.
print(a.endswith("g"))  # Prints True
print(a.endswith("G"))  # Prints False
# find(): It takes an argument and searches for it in the string on which it is applied. It then returns the index of the substring.
print(b.find("er"))  # Prints 4
# If the string doesn’t exist in the main string, then the index it returns is 1.
print(a.find("er"))  # Prints -1
# replace()- It takes two arguments. The first is the substring to be replaced. The second is the substring to replace with.
print(b.replace("er", "ER"))  # Prints to hER
# split()-It takes one argument. The string is then split around every occurrence of the argument in the string.
a = a.split(" ")
print(a)  # Prints ['he', 'said', 'something']
print(a[0])  # Prints 'he'
print(type(a))  # Prints class 'list'
b = b.split("e")
print(b)  # Prints ['to h', 'r']
# join()
y = "*".join(['red', 'green', 'blue'])
print(y)  # Prints red*green*blue
# **********************************************************************************************************************
"""
Python String Operations
"""
print('hey' < 'hi')  # Prints True
print('ba' + 'na' * 2)  # Prints ‘banana’
print('na' in 'banana')  # Prints True
print('Hey' is 'Hi')
