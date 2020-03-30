"""
While loop and for loop
"""
# While loop
# First Program
a = 10
while a <= 20:
    print(a)
    a += 1
else:
    print("Reached 20")
"""
Output:
10
11
12
13
14
15
16
17
18
19
20
Reached 20
"""
# Second Program
a = 10
while a <= 20:
    print(a)
    a += 1
    if a == 21: break
else:
    print("Reached 20")
"""
Output:
10
11
12
13
14
15
16
17
18
19
20
"""
# Single Statement while
b = 10
while b <= 20: print('b'); b += 1;
# **********************************************************************************************************************
"""
For Loop
"""
for i in range(3):        # Prints 0 to 2
    print(i)
for j in range(0,5):      # Prints 0 to 4
    print(j)
for k in range(0,20,5):   # Prints 0,5,10,15
    print(k)
for l in range(20,0,-5):  # prints 20,15,10,5
    print(l)
# Else in for loop
# First Program
for i in range(5):
    print(i)
else:
    print("Reached 4")
# Second Program
for j in range(5):
    print(j)
    if j==4: break
else:
    print("This is not executed")
