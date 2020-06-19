# Decorator - adding extra functionality to the function
# Example 1
def decorate(fun):
    def inner():
        fun()
        for i in range(10,20):
            print(i)
    return inner
def print_num ():
    for i in range(10):
        print(i)

result = decorate(print_num)
result()

# ************************************************************************************************************
def decorate1(fun):
    def inner_fun():
        fun()
        for i in range(20,40):
            if i % 2 !=0:
                print(i)
    return inner_fun
def even_20():
    for i in range(20):
        if i % 2 == 0:
            print(i)

result1 = decorate1(even_20)
result1()
