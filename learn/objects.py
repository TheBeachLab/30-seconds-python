#!/usr/bin/env python3

# in python everything is an object
# type() and id()

# type() returns the class of object
print(type(7))
print(type(7.1))
print(type(1+2j))
print(type(True))
print(type((1, 2, 3)))
print(type([1, 2, 3]))

# id() returns a unique identifier for an object
print(id(7))
print(id(3434))

# isinstance() to check the type pf object

if isinstance(7, int):
    print("yes, that is an integer")


# define a class of objects


class cars:
    def electric(self):
        print('this is an electric car')

    def petrol(self):
        print('this is a petrol car')


def main():
    lambo = cars()  # lambo is an object of class cars
    lambo.electric()


main()
