"""
Class inside the class
"""


class Employ:
    def __init__(self, name, address, age, brand, CPU, ram):
        self.name = name
        self.address = address
        self.age = age
        self.lap = self.laptop(brand, CPU, ram)

    def get_info(self):
        print(f"Employ name is {self.name}; Address is {self.address} and age is {self.age}")
        self.lap.get_info()

    class laptop:
        def __init__(self, brand, CPU, ram):
            self.brand = brand
            self.cpu = CPU
            self.ram = ram

        def get_info(self):
            print(f"Laptop is of {self.brand} having CPU {self.cpu} and Ram Storage {self.ram}")


Employ1 = Employ("Prabin", "Butwal", 19, 'HP', "i5", "8-GB")
Employ1.get_info()
