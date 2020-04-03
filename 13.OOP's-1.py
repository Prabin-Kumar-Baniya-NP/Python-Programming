"""
Class is the blueprint of object
Object is the instance of class
"""


# Example 1:
class operation:
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
