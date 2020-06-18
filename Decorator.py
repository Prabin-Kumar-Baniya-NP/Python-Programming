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