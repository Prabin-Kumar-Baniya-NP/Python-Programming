"""
Inheritance, Use of Constructor and MRO (Method Resolution Order)
"""


class ten:
    def __init__(self):
        print("This is class ten")

    def get_result_10(self):
        print("You got 3.7 GPA in Grade 10")


class eleven(ten):  # Single level Inheritance
    def __init__(self):
        print("This is class Eleven")

    def get_result_11(self):
        print("You got 3.11 GPA in Grade 11")


class twelve(eleven, ten):  # Multiple Inheritance
    def __init__(self):
        super().__init__()
        print("This is class Twelve")

    def get_result_12(self):
        print("You got 3.27 GPA in Grade 12")


my_result = twelve()
my_result.get_result_10()
my_result.get_result_11()
my_result.get_result_12()
# **********************************************************************************************************************
