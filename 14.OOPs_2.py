"""
Types of Variables in Class:
1.Class(Static) Variable
2.Instance Variable
"""


# Example 1:
class Car:
    wheel = 4  # Class(Static) Variable

    def __init__(self):
        self.company = "BMW"  # Instance Variable
        self.price = "10,00,000"  # Instance Variable


my_car = Car()
my_frnd_car = Car()
my_frnd_car.company = "Farrari"
my_frnd_car.price = "20,00,000"
my_car.extra_info = "Made in America"
my_frnd_car.extra_info = "Made in India"
print(my_car.company, my_car.price, my_car.wheel, my_car.extra_info)
print(my_frnd_car.company, my_frnd_car.price, my_frnd_car.wheel, my_frnd_car.extra_info)
# **********************************************************************************************************************
"""
Types of methods
1.Instance Method- 
                 1.Accessor Method : Used when we only need to access the value
                 2.Mutator Method: Used when we required to set or change the value
2.Class Method
3.Static Method
"""


# Example 2: Instance Method
class value:
    def __init__(self, p):
        self.p = p

    def get(self):  # Instance Method - Accessor Method
        return self.p

    def set(self, set_to):  # Instance Method - Mutator Method
        self.p = set_to


first = value(1)
second = value(2)
print(first.p)
print(second.p)
first.set(11)
second.set(22)
print(first.p)
print(second.p)


# **********************************************************************************************************************
# Example 3: Class method
class Employee:
    dress_code = 'white shirt and black pant'  # Class or Static Variable

    def __init__(self):
        self.employee_id = 0000
        self.employee_address = '0000'

    @classmethod
    def get_dress_code(cls):  # Class method - working with class variable
        return cls.dress_code

    @staticmethod
    def random_operation():
        print("Welcome to this company")


employ1 = Employee()
employ1.employee_id = 23456
employ1.employee_address = 'Delhi'
print(employ1.employee_id)
print(employ1.employee_address)
print(Employee.get_dress_code())  # Calling the class method
Employee.random_operation()  # Calling the static method
