#!/usr/bin/env python3
# Understanding functions

# two types of functions
# functions that perform a task
# functions that return something

# a simple function


def say_hello():
    print("Hello.")


say_hello()

# a function with an argument


def print_that(something):
    print(f'I and a function that prints {something}')


print_that(23)
print_that('hello')

# a function with a default argument


def square(number=2):
    print(number**2)


square(3)
square()

# the main() function


def main():
    print('this is inside main')


# if __name__ == '__main__':main() # this calls the main function
# in python3 just calling main() would also work
main()

# return in functions
# all functions unless otherwise stated return None

print(say_hello())

# you can return something. With return you can do more things than just printing


def greet(name):
    return f"Hi, {name}"


message = greet("Fran")  # we have this message variable
print(message)
print(len(message))


def is_prime(n):
    if n <= 1:  # 1 is not considered to be prime
        return False  # not a prime number
    for x in range(2, n):
        if n % x == 0:  # the remainder of n/x is zero (n is divisible by x)
            return False  # not a prime number
    else:
        return True  # is a prime number


print(is_prime(6))

# list prime numbers


def list_primes(n):
    for i in range(n):
        if is_prime(i):
            print(i, end=' ', flush=True)
    print("")


list_primes(10)

# *args variable number of arguments
# if we have to multiply 2 numbers


def multiply(x, y):
    return x*y


print(multiply(2, 3))

# but if we have to multiply a variable (unknown) number of numbers


def multiply_many(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


print(multiply_many(2, 3, 4, 6))

# **args dictionaries


def save_user(**user):
    print(user)


save_user(id=1, name="John", age=23)
