from decimal import *
import math  # for the latest example

# numbers can be integer, float and complex
x = 1  # integer
y = 1.1  # float
z = 1+2j  # complex number

# the problem of float numbers
print(0.1+0.1+0.1)  # this should be 0, but it is not

# solution: use a decimal library
a = Decimal("0.1")
print(a+a+a)

# aritmetic operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # float result
print(10 // 3)  # integer result
print(10 % 3)  # modulus or remainder
print(10 ** 3)

# augmented assignment operator
x = 1
x *= 3  # can be any of the above operators
print(x)

# useful functions for numbers
print(round(8.9))
print(abs(-2.9))

# use the math library

print(math.acos(0.45))
