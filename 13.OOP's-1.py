"""
Class is the blueprint of object
Object is the instance of class
"""


# Example 1:
class operation:
    def __init__(self):
        print("It contains different mathematical concepts")

    def addition(self, x, y):
        return x + y

    def substraction(self, p, q):
        return p - q


a = 15
b = 20
add = operation()
minus = operation()
print("Sum of a and b is", add.addition(a, b))
print("Difference of a and b is", minus.substraction(a, b))


# **********************************************************************************************************************
# Example 2
class information:
    def __init__(self, name, address, age):
        self.name = name
        self.address = address
        self.age = age

    def get_info(self):
        return (f"Student name is {self.name}; address is {self.address}; and age is {self.age}")


ram = information("Ram", "Delhi", 15)
shyam = information("Shyam", "Kathmandu", 16)
print(ram.get_info())
print(shyam.get_info())


# **********************************************************************************************************************
# Example 3
class Compute:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def operation(self):
        return (self.x + self.y + self.z, self.x - self.y - self.z)


digits = Compute(3, 2, 1)
print(digits.operation())
